---
title: 本地新旧目录混合清理审计 2026-07-19
type: review
summary: "Phase 3 正式结构与本地 Phase 1/2 空壳目录的全量文件系统审计和清理决策"
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: ["[[../../../CODEX]]", "[[phase-3-audit]]", "[[phase-3-completion-report]]"]
related: ["[[MAINTENANCE]]", "[[../../overview]]"]
created: 2026-07-19
updated: 2026-07-19
---

# 本地新旧目录混合清理审计 2026-07-19

## 速览

本次审计直接读取本地文件系统，并同时核对 Git 已跟踪、未跟踪、ignored、隐藏和特殊文件。结论是：Phase 1/2 旧目录中没有待迁移的真实内容，67 个暴露结构用目录都只含 `.gitkeep`；44 个 ignored 文件全部属于必须保留的 local-only raw 层。

## 审计口径与总量

- 审计范围：`attachments/`、`domains/`、`inbox/`、`indexes/`、`outputs/`、`raw/`、`templates/`、`wiki/`。
- 清理前目录：118。
- 本地文件：245；其中 Git 已跟踪 201、未跟踪 0、ignored 44。
- 隐藏项目：68，主要为 `.gitkeep` 及 raw local-only 占位文件。
- 0 字节文件：0。
- 符号链接或其他特殊文件：0。
- 只有 `.gitkeep`、没有其他真实项目的目录：67。
- 低内容 Markdown 命中：31；均经保护规则和用途复核，不自动删除。

## 目录决策

| 原路径 | 文件数量 | 忽略文件数量 | 状态 | 建议动作 | 新路径 | 风险 |
| --- | ---: | ---: | --- | --- | --- | --- |
| `attachments/` | 1 | 0 | KEEP | 删除 `.gitkeep`，保留本地空根目录 | 原路径 | 低；Obsidian 后续自动写入 |
| `domains/` 下 11 个旧路线目录 | 11 | 0 | DELETE_EMPTY | 删除 `.gitkeep`、子目录和空 `domains/` | Phase 3 正式领域索引 | 低；无真实文件 |
| `domains/A领域路线…/` | 1 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |
| `inbox/` 根目录与 `temporary-ideas.md` | 1 | 0 | KEEP | 保留实际收件箱 | 原路径 | 低 |
| `inbox/` 下 5 个预建分类目录 | 5 | 0 | DELETE_EMPTY | 删除空分类，未来按需创建 | `inbox/` | 低；无真实材料 |
| `inbox/A临时收件箱…/` | 1 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |
| `indexes/dataview/`、`indexes/mocs/` | 26 | 0 | KEEP | 保留查询和 deprecated 兼容入口 | 原路径 | 中；含有效 wikilink |
| `indexes/A索引层/` | 1 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |
| `outputs/interview/`、`outputs/tax-memos/` | 6 | 0 | KEEP | 保留正式输出 | 原路径 | 低 |
| `outputs/` 下 6 个旧空分类 | 6 | 0 | DELETE_EMPTY | 删除 `.gitkeep` 和空目录 | 正式输出目录 | 低；无真实内容 |
| `outputs/A输出层…/` | 1 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |
| `raw/assets/pdfs/`、`raw/assets/extracted/` | 44 | 44 | KEEP | 原样保留，不移动、不提交 | 原路径 | 高；版权及 local-only 内容 |
| `raw/assets/images/` | 1 | 0 | DELETE_EMPTY | 删除 `.gitkeep` 和空目录 | 按需重建 | 低 |
| `raw/sources/` 下 11 个空分类 | 11 | 0 | DELETE_EMPTY | 删除空子目录，保留 raw 主层 | `raw/` | 低；无真实文件 |
| `raw/manifest.json`、`raw/README.md` | 2 | 0 | KEEP | 保留 manifest 元数据与边界说明 | 原路径 | 低 |
| `templates/` 正式模板 | 18 | 0 | KEEP | 全部保留 | 原路径 | 低；受保护模板 |
| `templates/A中文模板/` | 1 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |
| `wiki/00-meta/` 至 `wiki/10-research-writing/` | 11 | 0 | DELETE_EMPTY | 删除编号式空壳目录 | Phase 3 五区结构 | 低；仅 `.gitkeep` |
| `wiki/knowledge/`、`jurisdictions/`、`cases/`、`sources/`、`_ops/` | 68 | 0 | KEEP | 保留 Phase 3 正式结构 | 原路径 | 低 |
| `wiki/comparisons/`、`entities/`、`industries/`、`methods/`、`papers/`、`queries/`、`questions/`、`reviews/`、`rules/`、`topics/` | 10 | 0 | DELETE_EMPTY | 删除技术分类空壳 | Phase 3 五区结构 | 低；仅 `.gitkeep` |
| `wiki/meta/` 及其 5 个空子目录 | 5 | 0 | DELETE_EMPTY | 删除旧 meta 空壳 | `wiki/_ops/` | 低；仅 `.gitkeep` |
| `wiki/A知识层/`、`wiki/meta/A维护记录…/` | 2 | 0 | DELETE_EMPTY | 删除说明文字目录 | 无 | 低；误建目录 |

## 低内容 Markdown 复核

以下页面虽少于 80 个有效字符，但具有明确用途，予以保留：

- `templates/**`：正式模板和原始兼容模板，受保护。
- `**/index.md`：正式领域导航，受保护。
- `indexes/mocs/*.md`：deprecated 兼容跳转页，仍包含有效 wikilink。
- `indexes/dataview/papers.md`：有效 Dataview 查询，更新旧查询路径后保留。
- `wiki/_ops/maintenance/migrated-duplicates/独立交易原则-Phase1占位.md`：正式 deprecated 跳转页。

因此，本轮删除空 Markdown 0 个，合并重复页面 0 个。

## 迁移与冲突结论

- 需要迁移的真实文件：0。
- 重名文件冲突：0。
- manifest 中需要改写的 derived page 或 source summary 路径：0。
- 无法自动判断并移入 `structure-cleanup-pending/` 的文件：0。
- 清理动作只删除经本地全量核验的 `.gitkeep` 和空目录，不删除任何 raw、PDF、提取文本、客户或个人资料。

## 当前路径修正

当前有效文件中需要更新的旧路径只有：

- `indexes/dataview/interview-answers.md`：`outputs/interview-answers` → `outputs/interview`。
- `indexes/dataview/*.md`：现行查询字段 `jurisdiction` → `jurisdictions`。
- `indexes/dataview/papers.md`：从旧 `wiki/papers` 目录查询改为按 `type: paper` 全库查询。
- `README.md`：删除仍可能保留 `domains/` 的现状描述。
- `wiki/_ops/maintenance/MAINTENANCE.md`：职业路线维护入口改为 Phase 3 正式结构。

历史日志、Phase 3 审计、完成报告和迁移记录中的旧路径是事实记录，保持不变。

## 清理目标

- Phase 3 正式五区结构保持不变，本次不是 Phase 4 重构。
- 67 个由 `da9bafb` 引入的 tracked `.gitkeep` 全部移除。
- local-only `raw/assets/extracted/.gitkeep` 同时移除，但其同目录真实提取文本全部保留。
- 清理完成后原则上不保留 `.gitkeep`。

## 清理结果

- 清理后审计范围内目录：49（清理前 118，删除空目录 69）。
- 真实文件迁移：0；重复页面合并：0；待人工判断：0；空 Markdown 删除：0。
- tracked `.gitkeep`：67 → 0；本地 `.gitkeep` 总数：68 → 0。
- 七个说明文字目录、十一个旧编号 wiki 目录及旧技术分类空壳均已删除。
- `attachments/` 与 `raw/sources/` 本地根目录保留；raw PDF、完整提取文本及其他 local-only 文件均未移动、删除或纳入 Git。
- `.obsidian/app.json` 和 `.obsidian/appearance.json` 未修改。
- 最终验收以清理分支及合并后 `main` 上的四项本地脚本结果为准。
