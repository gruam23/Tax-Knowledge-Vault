# Vault Log

## 2026-07-19 — 新旧目录混合清理

- 按本地真实文件系统审计 tracked、untracked、ignored、隐藏、零字节和特殊文件；Phase 1/2 旧目录中没有需要迁移的真实内容。
- 删除 69 个经核验的空目录和 67 个 tracked `.gitkeep`；另移除 1 个 local-only raw 占位 `.gitkeep`，未删除任何原文、PDF、提取文本、客户资料或个人资料。
- 修正现行 Dataview、README 和维护手册中的旧路径；历史日志、审计和迁移记录保持原样。
- Phase 3 五区结构不变，本次不是 Phase 4 重构。

## 2026-07-19 — GitHub 完整安全快照

- 为 67 个可公开空目录加入 `.gitkeep`，使知识库框架能够由 Git 完整还原。
- 同步当前可公开的 Obsidian Vault 配置和全部已跟踪知识库文件到 `main`。
- 继续排除 raw PDF、完整提取文本、private/local 资料、插件、AI 缓存和运行时文件；GitHub 仍不作为运行或验收环境。
- 本地重建、strict lint 与 manifest check 通过后再推送。

## 2026-07-19 — Phase 3 最终小型修正

- 增强 `rebuild_overview.py`：使用 PyYAML 统计正式页面、五类内容与四类成熟度状态，并仅更新 overview 自动生成区块。
- 清理研发费用加计扣除页的旧 MOC 关系和 Phase 1 英文来源占位说明，改为正式 CN 领域索引与 Stage 1 待核验说明。
- 继续保留该页的官方来源缺口、空 `last_verified` 和 `needs-review` 状态，未补写未经核验的政策结论。
- 治理分支本地四项验收通过，overview 重复运行结果稳定；准备合并到 `main`。

## 2026-07-19 — Phase 3 收尾清理

- 将 Phase 1 “独立交易原则”重复页缩减为 deprecated 跳转页，正式页面与标题保持不变。
- 建立 `jurisdictions` 统一枚举并规范 37 个文件；lint 新增列表类型、允许值和 legacy 字段检查。
- 清理 README、CODEX、overview 的 Phase 2/MOC 主导航旧描述，明确领域目录 `index.md` 为正式导航。
- 保留研发费用加计扣除的官方来源缺口、空 `last_verified` 和 `needs-review` 状态，未伪造政策依据。
- 本地四项验收通过：strict lint 的 errors 全部为 0，manifest check 为 0 errors / 0 warnings；仅保留 deprecated 跳转页和研发费用来源缺口两项非阻断 warning。

## 2026-07-19 — 本地优先治理

- 停用 GitHub Actions，明确 GitHub 只用于版本备份、修改历史、远程审查和供 AI 读取。
- 批量迁移 legacy `jurisdiction` 到 `jurisdictions`，新页面和 lint 不再要求单数字段。
- lint 排除本地 raw 原文目录的内容检查，同时允许解析本地 raw 链接。
- 更新 README、CODEX、overview、维护手册和 Dataview 路径；本地四项验收全部通过。

## 2026-07-19 — P1

- 完成 Phase 3 领域/法域/案例/来源/运维五区重构；移动 61 个 wiki 页面，所有迁移使用 `git mv`。
- `indexes/mocs/` 的 10 个旧 MOC 改为 deprecated 兼容页；`domains/` 无 Markdown 内容，无需迁移。
- 更新主入口、输出页和 manifest 的新路径；不再把技术型目录作为 `wiki/` 顶层导航。

## 2026-07-19

- Phase 3 P0：完成公开仓库风险审计，新增 raw local-only 政策与风险审查报告。
- 停止追踪 `raw/assets/extracted/` 的完整 OECD/EY 提取文本；本地文件保留，Git 历史未改写。
- 更新 manifest 的 local-only、许可状态、公开摘要与最后核验字段，删除重复派生页。
- 运行 lint 和 manifest 路径/重复检查；后者通过，lint 报告作为后续 P1–P3 的修复基线。

## 2026-07-02

- 统一 meta 入口策略：保留 `wiki/hot.md`、`wiki/overview.md`、`wiki/log.md`、`wiki/meta/maintenance/`、`wiki/meta/lint-reports/` 为主入口，`wiki/00-meta/index.md` 改为兼容页。
- 加厚 `wiki/02-international-tax/index.md`、`wiki/03-transfer-pricing/index.md`、`wiki/06-eu-vat-gst/index.md`，补领域定位、学习路径、核心知识卡、关键 source、输出入口、待补队列和成熟度说明。
- 升级 `wiki/sources/index.md` 与 `templates/source-template.md`，将 source 体系改为按机构和资料类型组织。
- 为受益所有人、常设机构、Wayfair、DEMPE、独立交易原则补“待补 Source 队列”，未补权威来源的页面仍保持 `needs-review` 或 `developing`。
- 加厚 `outputs/interview/` 5 个面试页面，补 30 秒、1 分钟、3 分钟、专业展开框架、英文表达、追问、风险和 Sources。
- 新增 6 个 Dataview 维护面板：Needs Review、Developing、Mature、待补来源、适合转输出、最近 30 天更新。
- 运行 `python scripts/vault_lint.py --root .`，更新 `wiki/meta/lint-reports/lint-report-2026-07-02.md`，核心检查项均为 0。
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
