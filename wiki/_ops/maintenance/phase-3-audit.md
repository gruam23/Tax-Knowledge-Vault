---
title: "Phase 3 治理审计"
type: meta
summary: "Phase 3 开始前的目录、导航、公开风险、schema 和 manifest 基线审计"
status: reviewed
created: 2026-07-19
updated: 2026-07-19
---

# Phase 3 治理审计

## 基线

- 分支：`vault-governance-phase-3`（由 `main` 的 `f61ca67` 建立）。
- 保护边界：相邻母库 `../wiki-tax` 保持只读；本次不改写 Git 历史。
- 工作树中已有 `.obsidian/app.json` 与 `.obsidian/appearance.json` 的本地用户修改，Phase 3 不会纳入提交。

## 当前目录树（摘要）

```text
wiki/
├── 01-china-tax … 10-research-writing/    # 旧编号领域导航
├── comparisons/ entities/ industries/ jurisdictions/ methods/ papers/
├── queries/ questions/ reviews/ rules/ topics/          # 通用模板遗留
├── meta/                                      # 维护、lint、迁移记录
├── sources/                                   # source summary
├── index.md hot.md overview.md log.md
└── _ops/                                      # Phase 3 新操作区
```

根目录还同时有 `domains/`、`indexes/mocs/`、`indexes/dataview/`、`outputs/`、`raw/` 与 `templates/`。这证明领域导航和技术型导航并存。

## 重复导航与旧技术目录

- 10 个 `indexes/mocs/` 页面和 10 个旧编号领域 MOC 重复覆盖相同主题。
- `domains/` 又维护了一套学习路线；根 `index.md` 和 `wiki/index.md` 还手工列出大量概念。
- `wiki/` 顶层含 `comparisons`、`entities`、`industries`、`jurisdictions`、`methods`、`papers`、`queries`、`questions`、`reviews`、`rules`、`topics`，不适合用户按税务领域浏览。
- `wiki/00-meta`、`wiki/meta` 和 `wiki/A知识层` 是额外的旧迁移遗留。

## 公开仓库风险

| 等级 | 发现 | 处理 |
| --- | --- | --- |
| High | Git 当前追踪 40 余份 OECD TPG 与 EY VAT Guide 的完整/大段提取文本。 | P0 将停止追踪并保留本地副本。 |
| High | Git 历史也包含同一路径。 | 仅记录人工 `git filter-repo` 建议，不自动重写。 |
| Medium | 本地有 302 MB 中文 OECD PDF、7.8 MB EY PDF 和 4.7 MB 英文 OECD PDF。 | 已忽略；manifest 标记 local-only。 |
| Medium | EY 指南含国家章节中的联系人字段，全文不应公开。 | 停止追踪提取文本，仅保留摘要。 |
| Low | `.gitignore` 有重复 `.smart-env`，且缺少提取文本、密钥与本地材料规则。 | P0 统一规则。 |

未发现 API key、token、邮箱、电话或本机绝对路径的已追踪文本命中；该结论不覆盖被排除的全文提取材料。

## Schema、lint 与 manifest 问题

- `schema.md` 规定 summary 建议不超过 40 个汉字，lint 实际允许 120 个字符；需统一为 80 个 Unicode 字符。
- schema 仅有单数 `jurisdiction`，缺少多法域、法律效力、有效期、替代关系和精确引用定位。
- lint 文档声称检查孤立页/重复主题/过期 MOC，但现有代码尚未实现，且无 `--strict`。
- `manifest.json` 的 `oecd-tpg-2022.derived_pages` 中 `独立交易原则.md` 重复一次；缺少 local-only、公开摘要、许可状态和最后核验字段。
- OECD source summary 错称“仅提取前 60 页”，但 manifest 记录了至第 800 页的提取；EY summary 则记录了全书提取。两者都需要按 local-only 政策改写。

## 待迁移范围

- 45 个旧编号领域页面：按 P1 映射迁入 `knowledge/`、`jurisdictions/` 或 `cases/`。
- `wiki/entities/` 的 2 页迁入 `sources/organizations/`。
- `wiki/meta/` 的运维记录迁入 `_ops/`；`queries/`、`questions/`、`reviews/` 同步迁入。
- `indexes/mocs/` 与 `domains/` 保留为 deprecated 兼容页，不丢弃知识内容。

## 阶段范围

| 阶段 | 预计范围 |
| --- | --- |
| P0 | `.gitignore`、raw 政策、manifest、source summary、风险报告与停止追踪全文。 |
| P1 | `wiki/` 目录迁移、MOC、旧导航兼容页与全库 wikilink 更新。 |
| P2 | schema、模板、页面 metadata 的渐进迁移。 |
| P3 | semantic lint 与独立 manifest check。 |
| P4 | 本地自动索引、总览与校验脚本；GitHub 不运行或部署 Vault。 |
| P5 | Stage 1/Stage 2 ingest 规范、模板与 CODEX。 |
| P6 | 核心主题权威来源、reviewed 卡和成熟输出升级。 |
