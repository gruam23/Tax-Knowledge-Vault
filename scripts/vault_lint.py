#!/usr/bin/env python3
"""Lint Tax Knowledge Vault and write a Markdown maintenance report."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import posixpath
import re
from pathlib import Path
from typing import Any

import yaml


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
    "jurisdictions",
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

ALLOWED_STATUS = {"seed", "draft", "developing", "reviewed", "mature", "needs-review", "deprecated"}
ALLOWED_FIELDS = {
    "china-tax",
    "international-tax",
    "transfer-pricing",
    "indirect-tax",
    "us-tax",
    "uk-tax",
    "eu-vat-gst",
    "tax-treaties",
    "tax-treaties-and-cases",
    "industries",
    "tax-tech",
    "research-writing",
    "career-roadmap",
    "maintenance",
}
ALLOWED_CONFIDENCE = {"low", "medium", "high"}
ALLOWED_SOURCE_QUALITY = {"primary", "official", "professional", "academic", "mixed", "unknown"}
ALLOWED_CAREER_USE = {"interview", "memo", "research", "presentation", "portfolio", "study"}
ALLOWED_AUTHORITY_TYPE = {"treaty", "statute", "regulation", "notice", "administrative-guidance", "case", "professional", "academic", "internal-analysis"}
ALLOWED_BINDING_STATUS = {"binding", "persuasive", "nonbinding", "unknown"}
ALLOWED_LEGAL_STATUS = {"current", "amended", "repealed", "draft", "historical", "unknown"}
SUMMARY_MAX_CHARS = 80
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def parse_frontmatter(text: str) -> tuple[dict[str, Any] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing frontmatter delimiter"
    for idx, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            raw = "\n".join(lines[1:idx])
            try:
                data = yaml.safe_load(raw) or {}
            except yaml.YAMLError as exc:
                return None, f"invalid YAML: {exc}"
            if not isinstance(data, dict):
                return None, "frontmatter is not a mapping"
            return data, None
    return None, "missing closing frontmatter delimiter"


def required_fields_for(fm: dict[str, Any]) -> list[str]:
    page_type = str(fm.get("type", ""))
    if page_type in FORMAL_TYPES:
        return FORMAL_REQUIRED_FIELDS
    if page_type == "source":
        return SOURCE_REQUIRED_FIELDS
    if page_type == "entity":
        return ENTITY_REQUIRED_FIELDS
    if page_type in {"meta", "review"}:
        return BASE_REQUIRED_FIELDS
    return BASE_REQUIRED_FIELDS


def has_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def should_require_sources(fm: dict[str, Any]) -> bool:
    page_type = str(fm.get("type", ""))
    return str(fm.get("status", "")) in {"reviewed", "mature"} and page_type in FORMAL_TYPES | {"source", "entity"}


def should_require_related(fm: dict[str, Any]) -> bool:
    page_type = str(fm.get("type", ""))
    status = str(fm.get("status", ""))
    return page_type not in {"meta", "review"} and status not in {"seed", "needs-review", "deprecated"}


def link_target(raw: str) -> str:
    target = raw.split("|", 1)[0].split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    return target.replace("\\", "/")


def build_page_index(linkable_files: list[Path], root: Path) -> tuple[set[str], set[str]]:
    paths: set[str] = set()
    stems: set[str] = set()
    for path in linkable_files:
        r_file = rel(path, root)
        r_no_suffix = rel(path.with_suffix(""), root)
        stems.add(path.stem)
        for value in {r_file, r_no_suffix}:
            paths.add(value)
            if value.startswith("wiki/"):
                paths.add(value.removeprefix("wiki/"))
            if value.startswith("indexes/"):
                paths.add(value.removeprefix("indexes/"))
            if value.startswith("raw/assets/extracted/wiki-tax/"):
                paths.add(value.removeprefix("raw/assets/extracted/wiki-tax/"))
            if value.startswith("raw/assets/pdfs/wiki-tax/"):
                paths.add(value.removeprefix("raw/assets/pdfs/wiki-tax/"))
    return paths, stems


def resolves_link(target: str, source: Path, root: Path, paths: set[str], stems: set[str]) -> bool:
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return True
    if target in stems or target in paths:
        return True
    source_dir = rel(source.parent, root)
    candidates = [target]
    if "/" in target:
        candidates.append(posixpath.normpath(posixpath.join(source_dir, target)))
    for candidate in candidates:
        if candidate in paths:
            return True
        if candidate.endswith(".md") and candidate[:-3] in paths:
            return True
    return False


def validate_date(value: Any) -> bool:
    if isinstance(value, dt.date):
        return True
    if not isinstance(value, str) or not DATE_RE.match(value):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_enum(name: str, value: Any, allowed: set[str]) -> list[str]:
    if not has_value(value):
        return []
    values = as_list(value) if name == "career_use" else [value]
    bad = [str(v) for v in values if str(v) not in allowed]
    return bad


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


def is_ignored_path(path: Path, root: Path) -> bool:
    relative = path.relative_to(root).as_posix()
    if relative.startswith((
        "raw/assets/extracted/",
        "raw/assets/pdfs/",
        "raw/private/",
        "raw/local/",
    )):
        return True
    parts = set(path.relative_to(root).parts)
    return bool({".git", ".smart-env", ".obsidian", ".cache", ".llm-wiki"} & parts)


def is_local_only_raw(path: Path, root: Path) -> bool:
    relative = path.relative_to(root).as_posix()
    return relative.startswith((
        "raw/assets/extracted/",
        "raw/assets/pdfs/",
        "raw/private/",
        "raw/local/",
    ))


def should_check_frontmatter(path: Path, root: Path) -> bool:
    relative = path.relative_to(root).parts
    if not relative:
        return False
    if relative[0] == "wiki" and "lint-reports" not in relative and "migrated-from-wiki-tax-root" not in relative:
        return True
    if relative[0] == "outputs":
        return True
    return False


def should_check_links(path: Path, root: Path) -> bool:
    relative = path.relative_to(root).parts
    if not relative:
        return False
    if relative[0] in {"archive", "templates"}:
        return False
    if path.name in {"CODEX.md"}:
        return False
    return "lint-reports" not in relative


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--date", default=dt.date.today().isoformat())
    parser.add_argument("--strict", action="store_true", help="Return non-zero when errors are found.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    wiki_dir = root / "wiki"
    report_dir = wiki_dir / "_ops" / "lint-reports"
    report_dir.mkdir(parents=True, exist_ok=True)

    markdown_files = [
        p
        for p in root.rglob("*.md")
        if not is_ignored_path(p, root) and "raw" not in p.relative_to(root).parts
    ]
    linkable_files = [
        p
        for p in root.rglob("*")
        if p.is_file() and (not is_ignored_path(p, root) or is_local_only_raw(p, root))
    ]
    frontmatter_files = [p for p in markdown_files if should_check_frontmatter(p, root)]
    link_markdown_files = [
        p for p in markdown_files if "lint-reports" not in p.relative_to(root).parts
    ]
    paths, stems = build_page_index(linkable_files, root)

    frontmatter_errors: list[str] = []
    missing_fields: list[str] = []
    enum_errors: list[str] = []
    date_errors: list[str] = []
    summary_errors: list[str] = []
    missing_sources: list[str] = []
    missing_related: list[str] = []
    source_link_errors: list[str] = []
    dead_links: list[str] = []
    seed_pages: list[str] = []
    missing_quick_view: list[str] = []
    semantic_warnings: list[str] = []
    source_structure_warnings: list[str] = []
    stale_law_warnings: list[str] = []
    titles: dict[str, list[str]] = {}

    for path in frontmatter_files:
        text = read_text(path)
        name = rel(path, root)
        fm, error = parse_frontmatter(text)
        if fm is None:
            frontmatter_errors.append(f"{name}: {error}")
            continue
        if has_value(fm.get("title")):
            titles.setdefault(str(fm["title"]).strip(), []).append(name)

        for field in required_fields_for(fm):
            if field not in fm:
                missing_fields.append(f"{name} 缺少 `{field}`")
            elif field in {"sources", "related"}:
                continue
            elif not has_value(fm.get(field)):
                missing_fields.append(f"{name} 缺少 `{field}`")

        for field, allowed in [
            ("status", ALLOWED_STATUS),
            ("field", ALLOWED_FIELDS),
            ("confidence", ALLOWED_CONFIDENCE),
            ("source_quality", ALLOWED_SOURCE_QUALITY),
            ("career_use", ALLOWED_CAREER_USE),
            ("authority_type", ALLOWED_AUTHORITY_TYPE),
            ("binding_status", ALLOWED_BINDING_STATUS),
            ("legal_status", ALLOWED_LEGAL_STATUS),
        ]:
            for bad in validate_enum(field, fm.get(field), allowed):
                enum_errors.append(f"{name} `{field}` 非法值：{bad}")

        for field in ("created", "updated"):
            if has_value(fm.get(field)) and not validate_date(fm.get(field)):
                date_errors.append(f"{name} `{field}` 日期格式应为 YYYY-MM-DD")
        if has_value(fm.get("jurisdiction")) and not has_value(fm.get("jurisdictions")):
            semantic_warnings.append(f"{name} 仍使用 legacy `jurisdiction`，编辑时迁移至 `jurisdictions`")
        if str(fm.get("type")) == "source":
            required_sections = ["资料定位", "基本信息", "权威等级", "资料结构", "核心贡献", "已生成页面", "待继续整理", "Raw 原文位置"]
            missing_sections = [s for s in required_sections if f"## {s}" not in text]
            if missing_sections:
                source_structure_warnings.append(f"{name} 缺少 source 章节：{', '.join(missing_sections)}")
        if str(fm.get("type")) in {"rule", "policy", "case", "jurisdiction"}:
            if not has_value(fm.get("jurisdictions")):
                stale_law_warnings.append(f"{name} 缺少 `jurisdictions`")
            if not has_value(fm.get("last_verified")):
                stale_law_warnings.append(f"{name} 缺少 `last_verified`")
            if str(fm.get("status")) in {"reviewed", "mature"} and has_value(fm.get("last_verified")):
                try:
                    if (dt.date.today() - dt.date.fromisoformat(str(fm["last_verified"]))).days > 180:
                        stale_law_warnings.append(f"{name} 已超过 180 天未核验")
                except ValueError:
                    stale_law_warnings.append(f"{name} `last_verified` 日期无效")

        summary = fm.get("summary")
        if isinstance(summary, str) and len(summary) > SUMMARY_MAX_CHARS:
            summary_errors.append(f"{name} `summary` 过长：{len(summary)} > {SUMMARY_MAX_CHARS}")

        if should_require_sources(fm) and not has_value(fm.get("sources")):
            missing_sources.append(name)
        if should_require_related(fm) and not has_value(fm.get("related")):
            missing_related.append(name)
        if str(fm.get("status", "")) == "seed":
            seed_pages.append(name)
        if str(fm.get("type", "")) in FORMAL_TYPES and "\n## 速览" not in text:
            missing_quick_view.append(name)

        for item in as_list(fm.get("sources")):
            for match in WIKILINK_RE.findall(str(item)):
                target = link_target(match)
                if not resolves_link(target, path, root, paths, stems):
                    source_link_errors.append(f"{name} sources -> [[{match}]]")

    for path in [p for p in link_markdown_files if should_check_links(p, root)]:
        text = read_text(path)
        name = rel(path, root)
        for match in WIKILINK_RE.findall(text):
            target = link_target(match)
            if not resolves_link(target, path, root, paths, stems):
                dead_links.append(f"{name} -> [[{match}]]")

    raw_files = [
        p
        for p in (root / "raw").rglob("*")
        if p.is_file() and p.name != ".gitkeep" and not is_ignored_path(p, root)
    ]
    all_wiki_text = "\n".join(read_text(p) for p in frontmatter_files if p.exists())
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
        fm, _ = parse_frontmatter(text)
        if fm is None or not has_value(fm.get("related")) or not has_value(fm.get("sources")):
            output_traceability.append(rel(path, root))

    duplicate_titles = [f"title 重复：{title} -> {', '.join(paths)}" for title, paths in titles.items() if title and len(paths) > 1]

    summary = [
        f"参与 frontmatter 检查的 Markdown 文件数：{len(frontmatter_files)}",
        f"参与链接检查的 Markdown 文件数：{len(link_markdown_files)}",
        f"frontmatter 解析错误：{len(frontmatter_errors)}",
        f"缺失必填字段：{len(missing_fields)}",
        f"枚举值错误：{len(enum_errors)}",
        f"日期格式错误：{len(date_errors)}",
        f"summary 长度错误：{len(summary_errors)}",
        f"正文死链：{len(dead_links)}",
        f"`sources` wikilink 错误：{len(source_link_errors)}",
        f"`reviewed/mature` 但 sources 为空：{len(missing_sources)}",
        f"`related` 为空的正式页面：{len(missing_related)}",
        f"seed 页面：{len(seed_pages)}",
        f"缺失 `## 速览` 的正式页面：{len(missing_quick_view)}",
        f"未被 wiki 正文引用的 raw 文件：{len(unreferenced_raw)}",
        f"输出材料可追溯性问题：{len(output_traceability)}",
        f"语义迁移/重复警告：{len(semantic_warnings) + len(duplicate_titles)}",
        f"source 结构警告：{len(source_structure_warnings)}",
        f"税法时效警告：{len(stale_law_warnings)}",
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
            section("Frontmatter 解析错误", frontmatter_errors),
            section("缺失必填字段", missing_fields[:200]),
            section("枚举值错误", enum_errors[:200]),
            section("日期格式错误", date_errors[:200]),
            section("Summary 长度错误", summary_errors[:200]),
            section("正文死链", dead_links[:200]),
            section("Sources Wikilink 错误", source_link_errors[:200]),
            section("Reviewed/Mature 缺少 sources", missing_sources[:200]),
            section("缺失 related", missing_related[:200]),
            section("Seed 页面", seed_pages[:200]),
            section("缺失速览", missing_quick_view[:200]),
            section("Raw 来源可追溯性问题", unreferenced_raw[:200]),
            section("输出材料可追溯性问题", output_traceability[:200]),
            section("语义迁移与重复主题警告", (semantic_warnings + duplicate_titles)[:200]),
            section("Source 页面完整性警告", source_structure_warnings[:200]),
            section("税法时效警告", stale_law_warnings[:200]),
            "## 建议修复\n",
            "- reviewed/mature 页面必须至少保留一个可解析来源；来源不足时降为 needs-review 或 developing。",
            "- 迁移页面后同步更新 `wiki/index.md`、领域 `index.md` 和 `indexes/mocs/`。",
            "- sources 中的 wikilink 应指向 source summary 或 raw 原文，避免只写不可追踪的文字来源。",
            "",
        ]
    )

    out = report_dir / f"lint-report-{args.date}.md"
    out.write_text(report, encoding="utf-8")
    print(out)
    errors = frontmatter_errors + missing_fields + enum_errors + date_errors + summary_errors + dead_links + source_link_errors
    if args.strict and errors:
        print(f"strict lint failed: {len(errors)} error(s)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
