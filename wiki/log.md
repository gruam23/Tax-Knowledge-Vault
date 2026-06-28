---
title: Wiki 日志
type: review
summary: "Tax Knowledge Vault 的 wiki 层 ingest、query、lint 和维护操作时间线"
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
updated: 2026-06-28
---
# Wiki 日志

## 2026-06-28

- 优化质量门：将 `vault_lint.py` 改为按页面类型检查，支持 YAML 块列表，排除归档迁移快照噪音。
- 补全 `raw/manifest.json`，记录 OECD TPG 2022 和 EY VAT Guide 2026 的 PDF hash、抽取文本、source summary 和派生页面。
- 批量规范转让定价、间接税迁移页和实体页 frontmatter，补齐 `field`、`jurisdiction`、`sources`、`related` 等字段。
- 将无权威来源的 seed 示例页调整为 `needs-review`，补 `summary` 和 `## 速览`。
- 重新运行 lint：缺失 frontmatter、必填字段、死链、空 sources、空 related、seed 页面、raw 追溯问题和输出追溯问题均为 0。
- 创建示例 wiki 页面：受益所有人、常设机构、独立交易原则、Wayfair 案、研发费用加计扣除、国际税核心框架。
- 创建 Phase 1 导航所需的 MOC 和 Dataview 索引。
- 将 wiki-tax 的 wiki 页面迁入新库，包括转让定价概念、间接税概念、实体页、来源摘要和母库根级 wiki 文件。
- 运行迁移后 lint，并将维护 review 记录到 `wiki/meta/maintenance/review-2026-06-28.md`。
- 按用户要求迁移 Obsidian 社区插件，并记录到 `wiki/meta/maintenance/obsidian-plugin-migration-2026-06-28.md`。
- 优化现行知识库规范：吸收母库 archive 中的读取顺序、操作后检查单、`summary` 字段、`## 速览` 和原文指针规则。
- 重写 `wiki/index.md`，补全转让定价、间接税、source summary、raw 原文、维护记录入口；同步补强转让定价和 VAT/GST MOC。
- 将自动任务本身纳入维护对象，要求每月复核任务 prompt、频率、路径和质量规则覆盖情况。
- 按 archive 索引格式美化根索引和 `wiki/index.md`，保留 MOC、source、raw、概念和维护入口。
