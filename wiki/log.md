---
title: Wiki 日志
type: review
summary: "Tax Knowledge Vault 的 wiki 层 ingest、query、lint 和维护操作时间线"
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
# Wiki 日志

## 2026-07-19 — Phase 3 收尾清理

- 清除“独立交易原则”重复标题：正式知识页不变，Phase 1 占位页改为 deprecated 最小跳转页。
- 将 `global`、`treaty` 和国家英文全称规范为统一 `jurisdictions` 枚举；协定属性改用 `authority_type: treaty`。
- 更新 schema、模板、lint、README、CODEX、overview 和 hot，正式主导航统一为领域目录 `index.md`。
- 研发费用加计扣除页继续保持 `status: needs-review`、`confidence: low`、`source_quality: unknown`、`sources: []` 和空 `last_verified`，并新增 Stage 1 来源缺口警告。
- 本地重建、strict lint 和 manifest check 全部通过；errors 为 0，重复标题 warning 为 0，保留 1 个 deprecated 页面提示和 1 个真实税法时效 warning。

## 2026-07-19 — 本地优先治理

- GitHub Actions 已停用，Vault 的运行和验收全部回到本地 Obsidian 与四项本地脚本。
- 所有正式页面和模板完成 `jurisdiction` → `jurisdictions` 迁移；local-only raw 目录不参与 lint 内容扫描。
- 修复 `_ops/reviews`、`_ops/maintenance`、`_ops/lint-reports` 和 `wiki/cases` 的现行路由说明。

## 2026-07-19 — P1

- 将旧编号领域目录迁入 `knowledge/`、`jurisdictions/` 和 `cases/`，来源机构页归入 `sources/organizations/`，原 `meta/` 归入 `_ops/`。
- 新建五区索引；旧 `indexes/mocs/` 只保留 deprecated 兼容链接。

## 2026-07-19

- Phase 3 P0：生成公开仓库风险审查和基线审计；完整原文与提取文本改为 local-only。
- 更新 OECD TPG、EY VAT Guide source summary 的公开定位和 local-only 说明，修复 OECD 提取范围描述与 manifest 的矛盾。
- 运行 lint，报告位于 `wiki/meta/lint-reports/lint-report-2026-07-19.md`；结构性问题留待 P1–P3 一并治理。

## 2026-07-02

- 统一 meta 入口策略：`wiki/00-meta/index.md` 改为兼容页，主入口回到 `wiki/hot.md`、`wiki/overview.md`、`wiki/log.md`、`wiki/meta/maintenance/` 和 `wiki/meta/lint-reports/`。
- 加厚国际税、转让定价、VAT/GST 三个领域 MOC，新增领域定位、学习路径、核心知识卡、关键 source、输出入口、当前待补和页面成熟度说明。
- 升级 `wiki/sources/index.md` 为来源中心，按 OECD/国际组织、中国官方、IRS/美国、HMRC/英国、EY/四大资料、判例、论文、网页剪藏分类；同步升级 `templates/source-template.md`。
- 为受益所有人、常设机构、South Dakota v Wayfair、无形资产及 DEMPE、独立交易原则补“待补 Source 队列”。
- 加厚 `outputs/interview/` 下 5 个面试资产，补 30 秒版、1 分钟版、3 分钟版、专业展开框架、可引用规则/案例、英文表达、可能追问、回答风险和 Sources。
- 新增 Dataview 维护面板：Needs Review 页面、Developing 页面、Mature 知识资产、待补来源页面、适合转成输出的页面、最近30天更新。
- 运行 lint 并更新 `lint-report-2026-07-02.md`：frontmatter、必填字段、枚举、日期、summary、死链、sources wikilink、reviewed/mature 空 sources、输出追溯问题均为 0。
- Phase 2 收口：将 `wiki/concepts/` 中剩余的无形资产定价、全球公式分配法、跨国集团协同效应和主要 indirect_tax 页面迁入 `03-transfer-pricing/`、`06-eu-vat-gst/`；将 `wiki/policies/研发费用加计扣除.md` 迁入 `01-china-tax/`。
- 清空旧 `wiki/concepts/`、`wiki/policies/`、`wiki/cases/`、`wiki/synthesis/` 正式页面目录；主导航和领域 MOC 不再引用旧 concepts 路径。
- 新增按 `type` 聚合的 Dataview 索引：`全部概念索引.md`、`全部案例索引.md`、`全部政策索引.md`、`全部source索引.md`。
- 更新 `CODEX.md` 和 `wiki/hot.md`，明确 `type` 只作为 metadata，正式知识卡必须放入领域目录。
- 运行 lint 并生成 `lint-report-2026-07-02.md`：frontmatter、必填字段、枚举、日期、summary、死链、sources wikilink、reviewed/mature 空 sources、输出追溯问题均为 0。

## 2026-06-28

- Phase 2：将 wiki 主结构从技术分类迁移为领域优先结构，新增 `00-meta/`、`01-china-tax/`、`02-international-tax/`、`03-transfer-pricing/`、`04-us-tax/`、`05-uk-tax/`、`06-eu-vat-gst/`、`07-tax-treaties-and-cases/`、`08-industries/`、`09-tax-tech/`、`10-research-writing/` 和 `sources/index.md`。
- 迁移优先页面：受益所有人、常设机构、国际税核心框架、BEPS行动计划、独立交易原则、可比性分析、转移定价方法、无形资产及DEMPE原则、集团内服务、金融交易、成本分摊协议、业务重组、转让定价同期资料、相互协商程序与对应调整、预约定价安排、欧盟/中国/英国增值税体系、美国销售税体系、South Dakota v Wayfair。
- 同步更新根索引、`wiki/index.md` 和 `indexes/mocs/`，将核心入口指向新领域目录；Phase 1 的独立交易原则薄卡保留在 `00-meta/migrated-duplicates/`。
- 将 `templates/concept-template.md` 升级为研究型知识卡模板，覆盖速览、核心问题、定义、规则来源、判断标准、分析步骤、争议、正反观点、案例、关系、实务用途、面试表达、英文表达、原文摘录、来源和待补充。
- 扩写 `受益所有人` 与 `常设机构`，补规则来源、判断标准、分析步骤、实务证据、面试表达和待补充；二者因 `sources: []` 保持 `needs-review`。
- 新增 `outputs/interview/` 下 5 个输出模板页，覆盖独立交易原则、DEMPE、受益所有人、常设机构和 Wayfair 案。
- 升级 `scripts/vault_lint.py` 为 PyYAML 解析 frontmatter，并校验 status、field、confidence、source_quality、career_use、summary、created/updated、sources wikilink 和 reviewed/mature 来源要求；重新运行 lint，报告所有核心问题为 0。
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
