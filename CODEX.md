# Codex 维护规范

> 任何 AI 在操作本知识库前，必须先读本文件。它是本库的飞行检查单。

## 不可变约束

- 不修改 `E:\agent\Knowledge\wiki-tax`。
- 本库必须保持独立，不与母库共用 `.git`、`.obsidian/plugins` 或缓存。
- 每次大操作都要记录到 `log.md`。
- 每次 wiki 层 ingest、query 或 lint 都要记录到 `wiki/log.md`。
- 正式 wiki 页面至少应引用一个 source 页面或 raw 原始资料。证据不足的内容放入 `wiki/reviews/`。
- 新增或重写正式 wiki 页面时必须使用三层渐进式详略结构：frontmatter `summary`、正文 `## 速览`、正文深度内容。
- 重要知识点必须能回溯到 source summary 或 raw 原文位置，优先使用可点击 wikilink。

## 每次操作前读取顺序

1. 读 `CODEX.md`。
2. 读 `wiki/hot.md`，了解近期上下文和当前维护重点。
3. 读 `purpose.md`，确认研究方向和范围。
4. 需要定位页面时读 `index.md` 和 `wiki/index.md`。
5. 涉及具体领域时读相关 MOC。

## 工作流

### Ingest

1. 将原始资料放入 `raw/sources/` 或 `raw/assets/`。
2. 在 `wiki/sources/` 创建 source summary。
3. 创建或更新 concept、rule、policy、case、synthesis 等页面。
4. 对每个新页面写入 `summary` 字段和正文 `## 速览`。
5. 在“来源”或“参考素材”中标注文件名、页码、章节或可点击 raw 链接。
6. 补充 related 链接并更新相关 MOC。
7. 更新 `wiki/hot.md`、`wiki/index.md` 或相关索引。
8. 将操作记录到 `wiki/log.md`。

### Ingest 结束前检查单

- [ ] 新增页面已加入相关 MOC 或 `wiki/index.md`。
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

运行：

```powershell
python scripts/vault_lint.py --root .
```

报告写入 `wiki/meta/lint-reports/`，重要修复记录到 `wiki/log.md`。

## 页面命名和引用规则

- 文件名使用中文短标题，避免不必要的日期前缀；source summary 除外。
- source summary 命名格式优先使用 `YYYY-MM-DD-短标题.md`。
- 交叉引用使用 `[[中文页名]]` 或 `[[路径/页面|显示文本]]`。
- 别名、缩写和同义词维护在 `schema.md` 的“别名词表”中。
