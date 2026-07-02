---
title: 热缓存
type: review
summary: "当前维护重点是收口来源追溯、manifest 台账和迁移页 metadata"
field: maintenance
jurisdiction:
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [CODEX.md]
related: [税务知识库 Review 2026-06-28]
created: 2026-06-28
updated: 2026-07-02
---
# 热缓存

## 当前重点

Phase 2 领域优先结构已收口。2026-07-02 已将旧 `wiki/concepts/`、`wiki/policies/`、`wiki/cases/`、`wiki/synthesis/` 中剩余正式页面迁入领域目录，`type` 改为只承担 metadata 和 Dataview 聚合职责。

## 高优先级下一步

- 新建正式知识卡只放入领域目录，不再使用旧技术分类目录作为主浏览入口。
- 使用 `indexes/dataview/全部概念索引.md`、`全部案例索引.md`、`全部政策索引.md`、`全部source索引.md` 按 `type` 查看。
- 对 `needs-review` 页面补权威来源后再升为 `developing` 或 `reviewed`。
- 每次新增或整理 10-20 个页面后运行一次 lint。
- 保持 `raw/manifest.json` 与 source summary、派生页面同步更新。
