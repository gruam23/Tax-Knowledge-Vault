---
type: meta
title: "Lint 报告 2026-07-19"
created: 2026-07-19
updated: 2026-07-19
status: reviewed
---

# Lint 报告 2026-07-19

## 摘要

- 参与 frontmatter 检查的 Markdown 文件数：79
- 参与链接检查的 Markdown 文件数：141
- frontmatter 解析错误：0
- 缺失必填字段：0
- 枚举值错误：0
- 日期格式错误：0
- summary 长度错误：0
- 正文死链：0
- `sources` wikilink 错误：0
- `reviewed/mature` 但 sources 为空：0
- `related` 为空的正式页面：0
- seed 页面：0
- 缺失 `## 速览` 的正式页面：0
- 未被 wiki 正文引用的 raw 文件：0
- 输出材料可追溯性问题：0
- 语义迁移/重复警告：0
- deprecated 页面：1
- source 结构警告：0
- 税法时效警告：1

## Errors

### Frontmatter 解析错误

- 无

### 缺失必填字段

- 无

### 枚举值错误

- 无

### 日期格式错误

- 无

### Summary 长度错误

- 无

### 正文死链

- 无

### Sources Wikilink 错误

- 无

## Warnings

### Reviewed/Mature 缺少 sources

- 无

### 缺失 related

- 无

### Seed 页面

- 无

### 缺失速览

- 无

### Raw 来源可追溯性问题

- 无

### 输出材料可追溯性问题

- 无

### 语义迁移与重复主题警告

- 无

### Deprecated 页面

- wiki/_ops/maintenance/migrated-duplicates/独立交易原则-Phase1占位.md 为 deprecated 页面

### Source 页面完整性警告

- 无

### 税法时效警告

- wiki/jurisdictions/CN/研发费用加计扣除.md 缺少 `last_verified`

## 建议修复

- reviewed/mature 页面必须至少保留一个可解析来源；来源不足时降为 needs-review 或 developing。
- 迁移或新增页面后，同步更新对应领域目录中的 `index.md`。
- `indexes/mocs/` 仅作为旧兼容页，不再作为主导航维护。
- sources 中的 wikilink 应指向 source summary 或 raw 原文，避免只写不可追踪的文字来源。
