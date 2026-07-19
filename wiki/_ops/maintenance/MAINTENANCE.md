---
title: 维护手册
type: review
summary: "本地 Obsidian 的每周、每月、批量迁移和质量检查操作清单"
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [CODEX.md, Tax-Knowledge-Vault-Plan.md]
related: [wiki-tax migration 2026-06-28]
created: 2026-06-28
updated: 2026-07-19
---
# 维护手册

## 每周维护

1. 检查 `inbox/`，把有价值资料移动到 `raw/sources/`。
2. ingest 3-5 个高价值资料。
3. 检查生成页面的 `sources`、`related`、`status` 是否合格。
4. 检查新页面是否包含 `summary` 和 `## 速览`。
5. 检查来源是否标注到 source summary、raw 文件、页码或章节。
6. 更新 `indexes/mocs/` 中的相关 MOC 页面。
7. 更新 `wiki/hot.md`，并向 `wiki/log.md` 追加维护记录。

## 每月维护

1. 在本地依次运行四项验收命令。
2. 阅读 `wiki/_ops/lint-reports/` 中的最新报告。
3. 修复高影响的死链和来源可追溯性缺口。
4. 选择 3-5 个主题做深化 synthesis。
5. 在 `outputs/` 下产出至少一篇 memo、面试回答、案例分析或研究短文。
6. 在相关 `wiki/knowledge/` 领域索引中更新职业能力与学习路线。

## 批量迁移后检查

每次批量导入后，立即运行本地四项验收命令，并把迁移记录写入 `wiki/_ops/maintenance/`。

```powershell
python scripts/rebuild_index.py
python scripts/rebuild_overview.py
python scripts/vault_lint.py --root . --strict
python scripts/manifest_check.py --root .
```

## 本地优先与 GitHub 边界

- Obsidian 本地 Vault 是唯一运行环境，本地脚本结果是唯一验收依据。
- GitHub 只用于版本备份、修改历史、远程审查和供 AI 读取，不运行或部署本库。
- `raw/assets/extracted/`、`raw/assets/pdfs/`、`raw/private/`、`raw/local/` 只存在本地，并由 lint 排除。
- GitHub 仅保存 source summary、知识卡、输出、模板、脚本和 manifest 元数据。

## 当前自动任务

- 税务知识库每日 Inbox 轻维护：`tax-knowledge-vault-daily-inbox-triage`
- 税务知识库每周维护：`tax-knowledge-vault-weekly-maintenance`
- 税务知识库每月 Lint 复盘：`tax-knowledge-vault-monthly-lint-review`

## 自动任务维护

自动任务本身也是知识库维护对象。每月至少检查一次，结构性调整后立即检查一次。

检查项：

- 自动任务 ID、名称、频率是否仍符合当前工作流。
- 自动任务 prompt 是否仍引用正确路径：`本仓库根目录`。
- 自动任务 prompt 是否明确禁止修改母库 `../wiki-tax`。
- 自动任务是否覆盖当前质量规则：`summary`、`## 速览`、sources、related、MOC、raw 原文指针。
- 自动任务是否会读取 `CODEX.md`、`schema.md`、`wiki/hot.md`、`wiki/index.md` 和本维护手册。
- 如果新增目录、脚本、MOC、核心 source 或输出流程，应同步更新自动任务 prompt。
- 自动任务变更必须记录到 `wiki/_ops/maintenance/` 和 `wiki/log.md`。

当前维护原则：

- 每日任务只做轻量 inbox triage，不做大规模改写。
- 每周任务负责 inbox/raw/MOC/hot/log 和小规模 ingest 候选整理。
- 每月任务负责 lint、结构质量、输出物建议和自动任务自身复核。

## Obsidian 插件

新库已迁移母库的社区插件目录和启用列表。首次用 Obsidian 打开时，如果提示信任 vault 或启用社区插件，由用户在 Obsidian 内确认。

`.smart-env/` 是 Smart Connections 的本地索引和运行缓存，不作为知识资产维护，已在 `.gitignore` 中忽略。

## 结构质量标准

- 每个正式 wiki 页面必须有 frontmatter `summary`。
- 每个正式 wiki 页面必须有正文 `## 速览`。
- 每个关键知识点应尽量链接到 source summary 和 raw 原文位置。
- 别名和缩写统一维护在 `schema.md` 的“别名词表”。
