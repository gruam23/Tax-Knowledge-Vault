#!/usr/bin/env python3
"""Refresh the generated statistics block in root and wiki indexes."""
from pathlib import Path
import re
root = Path('.').resolve()
pages = list((root/'wiki').rglob('*.md'))
status = {s: 0 for s in ('reviewed','mature','needs-review')}
for p in pages:
    t=p.read_text(encoding='utf-8',errors='ignore')
    for s in status:
        if re.search(rf'^status:\s*{s}\s*$',t,re.M): status[s]+=1
block = f"<!-- AUTO-GENERATED:BEGIN -->\nWiki 页面：{len(pages)}；reviewed：{status['reviewed']}；mature：{status['mature']}；needs-review：{status['needs-review']}。\n<!-- AUTO-GENERATED:END -->"
for target in (root/'index.md',root/'wiki/index.md'):
    text=target.read_text(encoding='utf-8')
    if '<!-- AUTO-GENERATED:BEGIN -->' in text: text=re.sub(r'<!-- AUTO-GENERATED:BEGIN -->.*?<!-- AUTO-GENERATED:END -->',block,text,flags=re.S)
    else: text += '\n\n'+block+'\n'
    target.write_text(text,encoding='utf-8')
