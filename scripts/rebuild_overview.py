#!/usr/bin/env python3
"""Refresh only the generated statistics block in wiki/overview.md."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


BEGIN_MARKER = "<!-- AUTO-GENERATED:BEGIN -->"
END_MARKER = "<!-- AUTO-GENERATED:END -->"
FORMAL_AREAS = ("knowledge", "jurisdictions", "cases")
STATUSES = ("reviewed", "mature", "needs-review", "deprecated")


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    """Return parsed frontmatter, skipping files without it and warning on bad YAML."""
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() != "---":
            continue
        raw = "\n".join(lines[1:index])
        try:
            data = yaml.safe_load(raw) or {}
        except yaml.YAMLError as exc:
            print(f"warning: {path.as_posix()}: invalid YAML frontmatter: {exc}")
            return None
        if not isinstance(data, dict):
            print(f"warning: {path.as_posix()}: frontmatter is not a mapping")
            return None
        return data

    print(f"warning: {path.as_posix()}: missing closing frontmatter delimiter")
    return None


def is_status_page(path: Path, wiki_dir: Path) -> bool:
    """Match the live lint scope while excluding reports and migrated snapshots."""
    relative = path.relative_to(wiki_dir).as_posix()
    if relative.startswith("_ops/lint-reports/"):
        return False
    return "migrated-from-wiki-tax-root" not in path.parts


def collect_stats(root: Path) -> dict[str, int]:
    wiki_dir = root / "wiki"
    outputs_dir = root / "outputs"
    wiki_files = sorted(wiki_dir.rglob("*.md"))
    output_files = sorted(outputs_dir.rglob("*.md"))
    metadata = {path: parse_frontmatter(path) for path in wiki_files + output_files}

    area_counts: dict[str, int] = {}
    formal_pages: set[Path] = set()
    for area in FORMAL_AREAS:
        pages = {
            path
            for path in (wiki_dir / area).rglob("*.md")
            if metadata.get(path) is not None
        }
        area_counts[area] = len(pages)
        formal_pages.update(pages)

    status_pages = [
        path
        for path in wiki_files
        if is_status_page(path, wiki_dir) and metadata.get(path) is not None
    ] + [path for path in output_files if metadata.get(path) is not None]

    return {
        "formal": len(formal_pages),
        "knowledge": area_counts["knowledge"],
        "jurisdictions": area_counts["jurisdictions"],
        "cases": area_counts["cases"],
        "sources": sum(
            1
            for path in wiki_files
            if metadata.get(path) is not None
            and str(metadata[path].get("type", "")) == "source"
        ),
        "outputs": sum(1 for path in output_files if metadata.get(path) is not None),
        **{
            status: sum(
                1
                for path in status_pages
                if str(metadata[path].get("status", "")) == status
            )
            for status in STATUSES
        },
    }


def render_block(stats: dict[str, int]) -> str:
    return "\n".join(
        [
            BEGIN_MARKER,
            f"- 正式知识与法域案例页面：{stats['formal']}",
            f"- Knowledge 页面：{stats['knowledge']}",
            f"- Jurisdiction 页面：{stats['jurisdictions']}",
            f"- Case 页面：{stats['cases']}",
            f"- Source summary：{stats['sources']}",
            f"- Outputs：{stats['outputs']}",
            f"- Reviewed：{stats['reviewed']}",
            f"- Mature：{stats['mature']}",
            f"- Needs review：{stats['needs-review']}",
            f"- Deprecated：{stats['deprecated']}",
            END_MARKER,
        ]
    )


def update_overview(target: Path, block: str) -> None:
    text = target.read_text(encoding="utf-8-sig")
    pattern = re.compile(
        rf"{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}",
        flags=re.DOTALL,
    )
    if pattern.search(text):
        updated = pattern.sub(block, text, count=1)
    else:
        updated = f"{text.rstrip()}\n\n{block}\n"
    target.write_text(updated, encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    stats = collect_stats(root)
    update_overview(root / "wiki" / "overview.md", render_block(stats))


if __name__ == "__main__":
    main()
