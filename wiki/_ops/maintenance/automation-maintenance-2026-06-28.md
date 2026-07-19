---
title: 自动任务维护策略 2026-06-28
type: review
summary: 将自动任务本身纳入知识库维护范围
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [wiki/_ops/maintenance/MAINTENANCE.md]
related: [维护手册, 索引重构记录 2026-06-28]
created: 2026-06-28
updated: 2026-06-28
---
# 自动任务维护策略 2026-06-28

## 速览

自动任务不再只是后台运行器，而是本知识库的维护对象。每月 lint 复盘时必须检查自动任务是否仍符合当前库结构、质量规则和路径约束。

## 已纳入维护的任务

- `tax-knowledge-vault-daily-inbox-triage`
- `tax-knowledge-vault-weekly-maintenance`
- `tax-knowledge-vault-monthly-lint-review`

## 本次已同步的 prompt 规则

- 每日任务读取 `CODEX.md`、`schema.md`、`wiki/hot.md`、`wiki/index.md`、`MAINTENANCE.md`，但只做轻量 inbox triage。
- 每周任务检查 `summary`、`## 速览`、sources、related、MOC、raw 原文指针和索引漏挂。
- 每月任务运行 lint，并额外复核 daily/weekly/monthly 三个自动任务的名称、频率、中文 prompt、路径约束和质量规则覆盖情况。

## 维护要求

- prompt 必须是中文。
- prompt 必须指向新主力库 `本仓库根目录`。
- prompt 必须禁止修改母库 `../wiki-tax`。
- prompt 必须随 `CODEX.md`、`schema.md`、`MAINTENANCE.md` 和核心索引变化而更新。
- 自动任务变更必须写入维护记录。
