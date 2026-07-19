---
title: archive 根文档优化记录 2026-06-28
type: review
summary: 将母库归档规范吸收为新库正式维护规则
field: maintenance
jurisdiction:
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [archive/wiki-tax-root/INSTRUCTIONS.md, archive/wiki-tax-root/.wiki-schema.md, archive/wiki-tax-root/purpose.md, archive/wiki-tax-root/index.md]
related: [维护手册, Wiki 索引]
created: 2026-06-28
updated: 2026-06-28
---
# archive 根文档优化记录 2026-06-28

## 速览

本次没有用 archive 覆盖现行文档，而是提取其中更成熟的维护规则，合并进新主力库的正式规范。

## 吸收内容

- `CODEX.md`：加入操作前读取顺序、ingest 结束前检查单、命名和引用规则。
- `schema.md`：加入 `summary` 字段、三层渐进式详略结构、原文指针规则、别名词表、置信度标注规则。
- `purpose.md`：补充国际税收与反避税研究线索、实证偏好和争议标注偏好。
- `wiki/index.md`：补充母库成熟索引中的核心实体、转让定价、间接税和来源摘要入口。
- `templates/`：为正式模板加入 `summary`、`## 速览` 和来源指针占位。
- `scripts/vault_lint.py`：将 `summary` 和 `## 速览` 纳入后续 lint 检查。

## 保留现行设计

- 保留新库更完整的 `raw/wiki/domains/outputs/templates/indexes` 分层。
- 保留职业输出、面试、memo、PPT、作品集等用途。
- archive 仍作为历史参考，不作为当前规范入口。

