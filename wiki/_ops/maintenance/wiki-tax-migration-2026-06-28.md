---
title: wiki-tax 迁移记录 2026-06-28
type: review
summary: "记录母库 wiki-tax 到派生库 Tax-Knowledge-Vault 的路径映射和只读约束"
field: maintenance
jurisdiction:
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [../wiki-tax]
related: []
created: 2026-06-28
updated: 2026-06-28
---
# wiki-tax 迁移记录 2026-06-28

## 范围

将母库 `../wiki-tax` 的内容迁移到独立派生库 `本仓库根目录`。

## 路径映射

- `wiki-tax/wiki/concepts/` -> `wiki/concepts/`
- `wiki-tax/wiki/entities/` -> `wiki/entities/`
- `wiki-tax/wiki/sources/` -> `wiki/sources/`
- `wiki-tax/wiki/meta/` -> `wiki/meta/`
- `wiki-tax/wiki/*.md` -> `wiki/meta/migrated-from-wiki-tax-root/`
- `wiki-tax/raw/**/*.pdf` -> `raw/assets/pdfs/wiki-tax/`
- `wiki-tax/raw/**/*.md` -> `raw/assets/extracted/wiki-tax/`
- `wiki-tax/_templates/` -> `templates/wiki-tax-original/`
- 选定的 `wiki-tax` 根目录文档和配置 -> `archive/wiki-tax-root/`

## 未迁移内容和约束

- 未复制 `.git`、`.obsidian/plugins`、`.smart-env`、缓存或插件运行时文件。
- 未覆盖新库 Phase 1 根文件。
- 未在 `wiki-tax` 内编辑、移动、重命名、删除或格式化文件。
