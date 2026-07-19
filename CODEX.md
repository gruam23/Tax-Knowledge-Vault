# Codex 维护规范

> 任何 AI 在操作本知识库前，必须先读本文件。它是本库的飞行检查单。

## 不可变约束

- 不修改 `../wiki-tax`。
- 本库必须保持独立，不与母库共用 `.git`、`.obsidian/plugins` 或缓存。
- 每次大操作都要记录到 `log.md`。
- 每次 wiki 层 ingest、query 或 lint 都要记录到 `wiki/log.md`。
- 正式 wiki 页面至少应引用一个 source 页面或本地 raw 原始资料。证据不足或来源冲突的内容放入 `wiki/_ops/reviews/`。
- 新增或重写正式 wiki 页面时必须使用三层渐进式详略结构：frontmatter `summary`、正文 `## 速览`、正文深度内容。
- 重要知识点必须能回溯到 source summary 或 raw 原文位置，优先使用可点击 wikilink。
- 新建正式知识卡必须按新路由放入 `wiki/knowledge/`、`wiki/jurisdictions/` 或 `wiki/cases/` 的对应子目录。
- `type` 只作为 metadata，用于 Dataview 和 lint，不决定物理目录。
- 不再向旧 `wiki/concepts/`、`wiki/policies/` 技术目录新建页面；案例应放入新的 `wiki/cases/` 对应分类。需要按类型查看时使用 `indexes/dataview/全部概念索引.md`、`全部案例索引.md`、`全部政策索引.md` 和 `全部source索引.md`。
- 本库以本地 Obsidian 为唯一运行环境；GitHub 只做版本备份、历史、远程审查和供 AI 读取，不负责运行、部署或验收。
- raw 原文、PDF 和完整提取文本只存在本地；GitHub 仅保存 source summary、知识卡、模板、脚本和 manifest 元数据。
- 新页面只使用 `jurisdictions`；`jurisdiction` 是 legacy 字段，不得为了通过 lint 补回。

## 每次操作前读取顺序

1. 读 `CODEX.md`。
2. 读 `wiki/hot.md`，了解近期上下文和当前维护重点。
3. 读 `purpose.md`，确认研究方向和范围。
4. 需要定位页面时读 `index.md` 和 `wiki/index.md`。
5. 涉及具体领域时读相关 MOC。

## 工作流

### Ingest

#### Stage 1：结构化分析（不改正式卡）

先在 `wiki/_ops/ingest/<source-id>-analysis.md` 使用 `templates/ingest-stage-1-template.md` 记录哈希、法域、效力、规则、例外、冲突和建议。Stage 1 不创建或升级正式知识卡。

#### Stage 2：确认后生成

人工确认 Stage 1 后，才创建/更新 source summary 和正式卡；同步更新 related、领域 MOC、manifest、hot、log，并运行重建、lint 和 manifest check。哈希未变化的资料跳过摄入；新版本以 `superseded_by` 保留旧规则历史。

1. 将原始资料放入 `raw/sources/` 或 `raw/assets/`。
2. 在 `wiki/sources/` 创建 source summary。
3. 在对应领域目录创建或更新 concept、rule、policy、case、synthesis 等页面。
4. 对每个新页面写入 `summary` 字段和正文 `## 速览`。
5. 在“来源”或“参考素材”中标注文件名、页码、章节或可点击 raw 链接。
6. 补充 related 链接并更新相关 MOC。
7. 更新 `wiki/hot.md`、`wiki/index.md` 或相关索引。
8. 将操作记录到 `wiki/log.md`。

### Ingest 结束前检查单

- [ ] 新增页面已加入相关 MOC 或 `wiki/index.md`。
- [ ] 新增正式知识卡位于 `wiki/knowledge/`、`wiki/jurisdictions/` 或新的 `wiki/cases/`，不位于旧 `wiki/concepts/`、`wiki/policies/`。
- [ ] 页面 frontmatter 包含 `summary`、`sources`、`related`。
- [ ] 正文包含 `## 速览`。
- [ ] 来源能追溯到 `wiki/sources/` 或 `raw/` 的具体文件/章节/页码。
- [ ] 相关旧页面已补充必要反向链接，避免知识断层。
- [ ] `wiki/hot.md` 已更新当前重点和近期变化。
- [ ] `wiki/log.md` 已追加本次操作记录。
- [ ] 已运行 `python scripts/vault_lint.py --root .` 或说明未运行原因。

### Query

1. 先读取 `wiki/hot.md`、`wiki/index.md` 和相关 MOC。
2. 优先使用 reviewed 或 mature 状态的笔记。
3. 对不确定内容明确说明。
4. 如果回答可以沉淀为专业材料，应保存到 `outputs/`。

### Lint

检查缺失 frontmatter、缺失 sources、死链、孤立页面、重复主题、过期 MOC 和输出材料可追溯性问题。

本地运行：

```powershell
python scripts/rebuild_index.py
python scripts/rebuild_overview.py
python scripts/vault_lint.py --root . --strict
python scripts/manifest_check.py --root .
```

报告写入 `wiki/_ops/lint-reports/`，重要修复记录到 `wiki/log.md`。

## 页面命名和引用规则

- 文件名使用中文短标题，避免不必要的日期前缀；source summary 除外。
- source summary 命名格式优先使用 `YYYY-MM-DD-短标题.md`。
- 交叉引用使用 `[[中文页名]]` 或 `[[路径/页面|显示文本]]`。
- 别名、缩写和同义词维护在 `schema.md` 的“别名词表”中。
