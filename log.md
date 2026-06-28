# Vault Log

## 2026-06-28

- Initialized Phase 1 vault scaffold at `E:\agent\Knowledge\Tax-Knowledge-Vault`.
- Created core directories, root files, templates, Dataview indexes, MOCs, and seed notes.
- Parent vault `E:\agent\Knowledge\wiki-tax` treated as read-only.
- Migrated parent vault content into this vault without modifying `wiki-tax`: wiki pages, raw PDF files, Markdown extractions, original templates, and root reference docs.
- Added maintenance playbook and reusable lint script for recurring vault reviews.
- Completed first post-migration review and created daily, weekly, and monthly Codex maintenance automations.
- 按用户要求迁移 `wiki-tax` 的 Obsidian 社区插件目录和 `community-plugins.json` 到新主力库。
- 将 archive/wiki-tax-root 中更成熟的 AI 操作手册、schema 规则、别名词表、三层详略结构和原文指针规则合并进现行规范。
- 重构 `wiki/index.md` 和核心 MOC，将迁移进来的转让定价、VAT/GST、source summary、raw 原文和维护记录系统挂入索引。
- 将自动任务维护纳入正式维护手册，并准备同步更新周/月自动任务 prompt。
- 已同步更新 daily/weekly/monthly 三个自动任务 prompt，使其覆盖当前中文规范、索引/MOC 维护和自动任务自检。
- 按 archive 索引风格重排根 `index.md` 和 `wiki/index.md`，保留完整入口并改为更清晰的统计概览和分区格式。
