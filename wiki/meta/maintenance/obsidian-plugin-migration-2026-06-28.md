---
title: Obsidian 插件迁移记录 2026-06-28
type: review
summary: "记录从 wiki-tax 迁移到 Tax-Knowledge-Vault 的 Obsidian 插件和未覆盖项"
field: maintenance
jurisdiction:
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [E:\agent\Knowledge\wiki-tax\.obsidian]
related: [wiki-tax 迁移记录 2026-06-28]
created: 2026-06-28
updated: 2026-06-28
---
# Obsidian 插件迁移记录 2026-06-28

## 范围

按用户要求，将母库 `wiki-tax` 中的 Obsidian 社区插件迁移到新主力库 `Tax-Knowledge-Vault`。

## 已迁移插件

- `dataview`
- `templater-obsidian`
- `githobs`
- `obsidian-git`
- `smart-connections`
- `obsidian-excalidraw-plugin`
- `realclaudian`

## 迁移内容

- `wiki-tax/.obsidian/plugins/*` -> `Tax-Knowledge-Vault/.obsidian/plugins/*`
- `wiki-tax/.obsidian/community-plugins.json` -> `Tax-Knowledge-Vault/.obsidian/community-plugins.json`

## 未覆盖内容

- 未覆盖新库已有的 `.obsidian/app.json`、`workspace.json`、`appearance.json`、`core-plugins.json`。
- 未复制母库 `.git`、缓存或工作区运行状态。
- 未修改母库 `wiki-tax`。
