---
title: 热缓存
type: review
summary: "Phase 3 收尾后的真实来源缺口、领域索引和本地质量门禁"
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [CODEX.md]
related: [税务知识库 Review 2026-06-28]
created: 2026-06-28
updated: 2026-07-19
---
# 热缓存

## 当前重点

Phase 3 领域优先结构已收口。主入口使用 `wiki/hot.md`、`wiki/overview.md`、`wiki/log.md`、`wiki/_ops/maintenance/` 和 `wiki/_ops/lint-reports/`。本库以本地 Obsidian 和本地脚本为运行、验收环境；GitHub 仅用于备份与审查。

本轮已清理 Phase 1 重复占位页，统一 `jurisdictions` 枚举，并确认正式主导航由 `knowledge/`、`jurisdictions/`、`cases/`、`sources/` 和 `_ops/` 各目录的 `index.md` 承担；`indexes/mocs/` 仅作 deprecated 兼容层。

## 高优先级下一步

- 优先为 [[knowledge/international-tax/受益所有人]]、[[knowledge/international-tax/常设机构]]、[[cases/domestic-cases/South Dakota v Wayfair]] 补权威 source。
- 摄入并核验中国现行研发费用加计扣除官方规则；完成 Stage 1 前保持 [[jurisdictions/CN/研发费用加计扣除]] 为 `needs-review`。
- 补充中国特别纳税调整与 Pillar Two 的官方来源和结构化知识页。
- 使用 [[../indexes/dataview/待补来源页面]] 跟踪来源缺口。
- 使用 [[../indexes/dataview/适合转成输出的页面]] 选择下一批 memo / 面试输出。
- 每次新增或整理 10-20 个页面后运行本地四项验收命令，strict lint 只由 errors 阻断。
- 保持 `raw/manifest.json` 与 source summary、派生页面同步更新。
