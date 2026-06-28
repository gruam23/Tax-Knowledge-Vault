#!/usr/bin/env python3
"""Lint Tax Knowledge Vault and write a Markdown maintenance report."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


BASE_REQUIRED_FIELDS = [
    "title",
    "type",
    "summary",
    "status",
    "created",
    "updated",
]

FORMAL_TYPES = {
    "concept",
    "rule",
    "policy",
    "case",
    "paper",
    "method",
    "jurisdiction",
    "industry",
    "topic",
    "synthesis",
    "question",
    "output",
}

FORMAL_REQUIRED_FIELDS = BASE_REQUIRED_FIELDS + [
    "field",
    "jurisdiction",
    "level",
    "confidence",
    "source_quality",
    "career_use",
    "sources",
    "related",
]

SOURCE_REQUIRED_FIELDS = BASE_REQUIRED_FIELDS + [
    "confidence",
    "related",
    "sources",
]

ENTITY_REQUIRED_FIELDS = BASE_REQUIRED_FIELDS + [
    "related",
    "sources",
]

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if ":" in line and not line.startswith((" ", "\t", "-")):
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip()
        elif current_key and line.lstrip().startswith("-"):
            data[current_key] = "__list__"
    return None


def required_fields_for(fm: dict[str, str]) -> list[str]:
    page_type = fm.get("type", "")
    if page_type in FORMAL_TYPES:
        return FORMAL_REQUIRED_FIELDS
    if page_type == "source":
        return SOURCE_REQUIRED_FIELDS
    if page_type == "entity":
        return ENTITY_REQUIRED_FIELDS
    if page_type in {"meta", "review"}:
        return BASE_REQUIRED_FIELDS
    return BASE_REQUIRED_FIELDS


def should_require_sources(fm: dict[str, str]) -> bool:
    if fm.get("status") in {"seed", "needs-review"}:
        return False
    return fm.get("type") in FORMAL_TYPES | {"source", "entity"}


def should_require_related(fm: dict[str, str]) -> bool:
    if fm.get("type") in {"meta", "review"}:
        return False
    return fm.get("status") not in {"seed", "needs-review"}


def link_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.replace("\\", "/")


def build_page_index(linkable_files: list[Path], root: Path) -> tuple[set[str], set[str]]:
    paths: set[str] = set()
    stems: set[str] = set()
    for path in linkable_files:
        stem = path.stem
        stems.add(stem)
        r = rel(path.with_suffix(""), root)
        paths.add(r)
        paths.add(rel(path, root))
        if r.startswith("wiki/"):
            paths.add(r.removeprefix("wiki/"))
        if r.startswith("indexes/"):
            paths.add(r.removeprefix("indexes/"))
        if r.startswith("raw/assets/extracted/wiki-tax/"):
            paths.add(r.removeprefix("raw/assets/extracted/wiki-tax/"))
        if r.startswith("raw/assets/pdfs/wiki-tax/"):
            paths.add(r.removeprefix("raw/assets/pdfs/wiki-tax/"))
    return paths, stems


def resolves_link(target: str, source: Path, root: Path, paths: set[str], stems: set[str]) -> bool:
    if not target:
        return True
    if target in stems or target in paths:
        return True
    if "/" in target:
        source_dir = source.parent.relative_to(root)
        candidate = (source_dir / target).as_posix()
        normalized = Path(candidate).as_posix()
        normalized = re.sub(r"(^|/)\./", r"\1", normalized)
        while "/../" in normalized:
            normalized = re.sub(r"[^/]+/\.\./", "", normalized, count=1)
        return normalized in paths
    return False


def section(title: str, items: list[str]) -> str:
    body = "\n".join(f"- {item}" for item in items) if items else "- 无"
    return f"## {title}\n\n{body}\n"


def load_manifest_paths(root: Path) -> set[str]:
    manifest_path = root / "raw" / "manifest.json"
    if not manifest_path.exists():
        return set()
    try:
        manifest = json.loads(read_text(manifest_path))
    except json.JSONDecodeError:
        return set()

    paths: set[str] = {"raw/manifest.json"}
    for source in manifest.get("sources", {}).values():
        for key in ("raw_path", "source_summary"):
            value = source.get(key)
            if isinstance(value, str):
                paths.add(value)
        for key in ("extracted_files", "derived_pages"):
            for value in source.get(key, []):
                if isinstance(value, str):
                    paths.add(value)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    root = Path(args.root).resolve()
    wiki_dir = root / "wiki"
    report_dir = wiki_dir / "meta" / "lint-reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    markdown_files = [
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts and "raw" not in p.relative_to(root).parts
    ]
    linkable_files = [
        p
        for p in root.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and ".smart-env" not in p.parts
        and ".obsidian" not in p.parts
    ]
    wiki_files = [p for p in wiki_dir.rglob("*.md")]
    content_wiki_files = [
        p
        for p in wiki_files
        if "lint-reports" not in p.relative_to(root).parts
        and "migrated-from-wiki-tax-root" not in p.relative_to(root).parts
    ]
    link_markdown_files = [
        p for p in markdown_files if "lint-reports" not in p.relative_to(root).parts
    ]
    paths, stems = build_page_index(linkable_files, root)

    missing_frontmatter: list[str] = []
    missing_fields: list[str] = []
    missing_sources: list[str] = []
    missing_related: list[str] = []
    seed_pages: list[str] = []
    missing_quick_view: list[str] = []
    dead_links: list[str] = []

    for path in content_wiki_files:
        text = read_text(path)
        fm = frontmatter(text)
        name = rel(path, root)
        if fm is None:
            missing_frontmatter.append(name)
        else:
            for field in required_fields_for(fm):
                if field not in fm:
                    missing_fields.append(f"{name} 缺少 `{field}`")
            if should_require_sources(fm) and fm.get("sources", "") in {"", "[]"}:
                missing_sources.append(name)
            if should_require_related(fm) and fm.get("related", "") in {"", "[]"}:
                missing_related.append(name)
            if fm.get("status") == "seed":
                seed_pages.append(name)
            if fm.get("type") in FORMAL_TYPES and "\n## 速览" not in text:
                missing_quick_view.append(name)

        for match in WIKILINK_RE.findall(text):
            target = link_target(match)
            if not resolves_link(target, path, root, paths, stems):
                dead_links.append(f"{name} -> [[{match}]]")

    raw_files = [
        p
        for p in (root / "raw").rglob("*")
        if p.is_file() and p.name != ".gitkeep"
    ]
    all_wiki_text = "\n".join(read_text(p) for p in content_wiki_files)
    manifest_paths = load_manifest_paths(root)
    unreferenced_raw = [
        rel(p, root)
        for p in raw_files
        if rel(p, root) not in manifest_paths
        if p.stem not in all_wiki_text and p.name not in all_wiki_text
    ]

    output_traceability: list[str] = []
    for path in (root / "outputs").rglob("*.md"):
        text = read_text(path)
        fm = frontmatter(text)
        if fm is None or fm.get("related", "") in {"", "[]"} or fm.get("sources", "") in {"", "[]"}:
            output_traceability.append(rel(path, root))

    summary = [
        f"Wiki Markdown 文件数：{len(wiki_files)}",
        f"参与链接检查的 Markdown 文件数：{len(link_markdown_files)}",
        f"缺失 frontmatter：{len(missing_frontmatter)}",
        f"缺失必填 frontmatter 字段：{len(missing_fields)}",
        f"死链数量：{len(dead_links)}",
        f"`sources` 为空的 wiki 页面：{len(missing_sources)}",
        f"`related` 为空的 wiki 页面：{len(missing_related)}",
        f"seed 状态页面：{len(seed_pages)}",
        f"缺失 `## 速览` 的正式页面：{len(missing_quick_view)}",
        f"未被 wiki 正文引用的 raw 文件：{len(unreferenced_raw)}",
        f"输出材料可追溯性问题：{len(output_traceability)}",
    ]

    report = "\n".join(
        [
            "---",
            "type: meta",
            f'title: "Lint 报告 {args.date}"',
            f"created: {args.date}",
            f"updated: {args.date}",
            "status: reviewed",
            "---",
            "",
            f"# Lint 报告 {args.date}",
            "",
            section("摘要", summary),
            section("缺失 Frontmatter", missing_frontmatter),
            section("缺失必填字段", missing_fields[:200]),
            section("死链", dead_links[:200]),
            section("缺失来源字段 sources", missing_sources[:200]),
            section("缺失相关链接字段 related", missing_related[:200]),
            section("Seed 页面", seed_pages[:200]),
            section("缺失速览", missing_quick_view[:200]),
            section("Raw 来源可追溯性问题", unreferenced_raw[:200]),
            section("输出材料可追溯性问题", output_traceability[:200]),
            "## 建议修复\n",
            "- 将本报告作为维护队列；在继续大量新增笔记前，优先修复死链和来源可追溯性问题。",
            "- 迁移页面在 sources、related、raw 原文指针完成复核前，应保持 `needs-review` 或 `developing` 状态，不要提前标为 `reviewed`。",
            "- 每次周度 ingest 后重新运行本脚本，并与上一份报告对比指标变化。",
            "",
        ]
    )

    out = report_dir / f"lint-report-{args.date}.md"
    out.write_text(report, encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
