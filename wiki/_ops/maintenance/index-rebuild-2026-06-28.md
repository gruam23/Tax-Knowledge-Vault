---
title: 索引重构记录 2026-06-28
type: review
summary: 重构 wiki/index 和核心 MOC，补全迁移内容入口
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [wiki/index.md, indexes/mocs/转让定价 MOC.md, indexes/mocs/欧盟 VAT-GST MOC.md]
related: [Wiki 索引, 转让定价 MOC, 欧盟 VAT-GST MOC]
created: 2026-06-28
updated: 2026-06-28
---
# 索引重构记录 2026-06-28

## 速览

原 `wiki/index.md` 只覆盖少数示例页和部分迁移页，没有把母库迁移来的转让定价、VAT/GST、source summary、raw 原文和维护记录系统关联起来。本次已重构为可作为知识层首页使用的完整索引。

## 已改内容

- `wiki/index.md`：重写为总入口，补充 MOC、source summary、PDF、raw 抽取文本、国际税、转让定价、VAT/GST、中国税、美国税、英国税和维护记录入口。
- `indexes/mocs/转让定价 MOC.md`：补全 12 个转让定价概念、OECD TPG source 和 raw 页码入口。
- `indexes/mocs/欧盟 VAT-GST MOC.md`：补全 13 个间接税/VAT/GST 页面、EY Guide source 和 raw 入口。
- 新增 `BEPS行动计划`、`预约定价安排`、`无形资产定价` 三个概念页，修复 source summary 中原本指向空页面的关键链接。
- 后续按 archive 索引风格重排 `wiki/index.md` 和根 `index.md`：顶部统计概览、分区列表、紧凑层级，保留所有已补入口。

## 验证

- 重新运行 `python scripts/vault_lint.py --root . --date 2026-06-28`。
- 当前 lint 摘要显示 dead wikilinks 为 0。
