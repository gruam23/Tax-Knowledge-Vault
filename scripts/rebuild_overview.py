#!/usr/bin/env python3
"""Refresh overview's generated indicator block."""
from pathlib import Path
root=Path('.').resolve(); pages=list((root/'wiki').rglob('*.md'))
block=f"<!-- AUTO-GENERATED:BEGIN -->\n当前知识页：{len(pages)}。请优先补齐 needs-review 页面对应的权威 source summary，并以最近 lint 报告为准。\n<!-- AUTO-GENERATED:END -->"
for target in (root/'wiki/overview.md',):
    text=target.read_text(encoding='utf-8')
    import re
    text=re.sub(r'<!-- AUTO-GENERATED:BEGIN -->.*?<!-- AUTO-GENERATED:END -->',block,text,flags=re.S) if '<!-- AUTO-GENERATED:BEGIN -->' in text else text+'\n\n'+block+'\n'
    target.write_text(text,encoding='utf-8')
