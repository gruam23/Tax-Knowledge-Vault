# Vault Log

## 2026-07-02

- Phase 2 收口：迁移旧 `wiki/concepts/`、`wiki/policies/`、`wiki/cases/`、`wiki/synthesis/` 剩余正式页到领域目录，旧技术分类目录不再作为主浏览入口。
- 新增 `indexes/dataview/全部概念索引.md`、`全部案例索引.md`、`全部政策索引.md`、`全部source索引.md`，按 `type` 提供横向查看能力。
- 更新 `CODEX.md`，明确正式知识卡必须放入领域目录，`type` 只作为 metadata，不决定物理目录。
- 运行 `python scripts/vault_lint.py --root .`，生成 `wiki/meta/lint-reports/lint-report-2026-07-02.md`，核心检查项均为 0。

## 2026-06-28

- Phase 2 重构：在 `wiki/` 下建立 `00-meta` 到 `10-research-writing` 及 `sources` 的领域优先结构，每个目录补 `index.md` 作为 MOC。
- 将受益所有人、常设机构、国际税核心框架、BEPS、转让定价核心专题、主要 VAT/Sales Tax 页面和 Wayfair 案迁入领域目录。
- 升级 `schema.md`、`README.md`、`.gitignore`、`templates/concept-template.md` 和 `scripts/vault_lint.py`，新增 PyYAML frontmatter lint、枚举校验、日期校验、summary 长度校验和 sources wikilink 校验。
- 扩写 `受益所有人` 与 `常设机构` 为研究型知识卡；因尚未补权威来源，均保留 `status: needs-review` 与 `sources: []`。
- 新增 `outputs/interview/` 下 5 个面试回答模板，并重新生成 `wiki/meta/lint-reports/lint-report-2026-06-28.md`，新版 lint 摘要为 0 个 frontmatter、枚举、日期、summary、死链、sources 和输出追溯问题。
- Initialized Phase 1 vault scaffold at `本仓库根目录`.
- Created core directories, root files, templates, Dataview indexes, MOCs, and seed notes.
- Parent vault `../wiki-tax` treated as read-only.
- Migrated parent vault content into this vault without modifying `wiki-tax`: wiki pages, raw PDF files, Markdown extractions, original templates, and root reference docs.
- Added maintenance playbook and reusable lint script for recurring vault reviews.
- Completed first post-migration review and created daily, weekly, and monthly Codex maintenance automations.
- 按用户要求迁移 `wiki-tax` 的 Obsidian 社区插件目录和 `community-plugins.json` 到新主力库。
- 将 archive/wiki-tax-root 中更成熟的 AI 操作手册、schema 规则、别名词表、三层详略结构和原文指针规则合并进现行规范。
- 重构 `wiki/index.md` 和核心 MOC，将迁移进来的转让定价、VAT/GST、source summary、raw 原文和维护记录系统挂入索引。
- 将自动任务维护纳入正式维护手册，并准备同步更新周/月自动任务 prompt。
- 已同步更新 daily/weekly/monthly 三个自动任务 prompt，使其覆盖当前中文规范、索引/MOC 维护和自动任务自检。
- 按 archive 索引风格重排根 `index.md` 和 `wiki/index.md`，保留完整入口并改为更清晰的统计概览和分区格式。
