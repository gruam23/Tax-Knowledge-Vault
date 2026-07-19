#!/usr/bin/env python3
"""Validate raw/manifest.json paths, hashes, dates and duplicate derived pages."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

SHA = re.compile(r"^[0-9A-Fa-f]{64}$")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    data = json.loads((root / "raw/manifest.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    for source_id, source in data.get("sources", {}).items():
        for key in ("source_summary", "raw_path", "sha256", "last_ingested", "last_verified"):
            if not source.get(key): errors.append(f"{source_id}: missing {key}")
        if source.get("sha256") and not SHA.match(str(source["sha256"])): errors.append(f"{source_id}: invalid sha256")
        if source.get("source_summary") and not (root / source["source_summary"]).is_file(): errors.append(f"{source_id}: missing source_summary")
        if source.get("raw_path") and not source.get("local_only") and not (root / source["raw_path"]).exists(): errors.append(f"{source_id}: missing non-local raw_path")
        pages = source.get("derived_pages", [])
        if len(pages) != len(set(pages)): errors.append(f"{source_id}: duplicate derived_pages")
        for page in pages:
            if not (root / page).is_file(): errors.append(f"{source_id}: missing derived page {page}")
        for path in source.get("extracted_files", []):
            if not (root / path).exists() and not source.get("extracted_files_local_only"):
                errors.append(f"{source_id}: missing extracted file {path}")
    for item in warnings: print("WARNING", item)
    for item in errors: print("ERROR", item)
    print(f"Manifest check: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
