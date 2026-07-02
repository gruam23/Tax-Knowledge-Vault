---
title: 热缓存
type: review
summary: "当前维护重点是 source 体系、领域 MOC、面试输出和维护面板"
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

Phase 2 领域优先结构已收口。2026-07-02 进一步统一 meta 策略：主入口使用 `wiki/hot.md`、`wiki/overview.md`、`wiki/log.md`、`wiki/meta/maintenance/` 和 `wiki/meta/lint-reports/`；`wiki/00-meta/index.md` 改为兼容页。

本轮已加厚国际税、转让定价、VAT/GST 三个领域 MOC，升级 sources 中心和 source 模板，给核心主题补 source 队列，并把 `outputs/interview/` 页面升级为完整面试资产。

## 高优先级下一步

- 优先为 [[02-international-tax/受益所有人]]、[[02-international-tax/常设机构]]、[[07-tax-treaties-and-cases/South Dakota v Wayfair]] 补权威 source。
- 使用 [[../indexes/dataview/待补来源页面]] 跟踪来源缺口。
- 使用 [[../indexes/dataview/适合转成输出的页面]] 选择下一批 memo / 面试输出。
- 每次新增或整理 10-20 个页面后运行 `python scripts/vault_lint.py --root .`。
- 保持 `raw/manifest.json` 与 source summary、派生页面同步更新。
