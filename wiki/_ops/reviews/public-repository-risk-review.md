---
title: "公开仓库风险审查"
type: review
summary: "Phase 3 对版权、隐私、本地路径和大文件的公开仓库风险审查"
status: reviewed
created: 2026-07-19
updated: 2026-07-19
---

# 公开仓库风险审查

## Critical

- 未发现已追踪的密钥、客户资料、个人隐私或访问 token。扫描不将“专有技术/商业秘密”这类一般概念误报为密钥。

## High

- `raw/assets/extracted/wiki-tax/` 当前追踪了 OECD TPG 与 EY VAT Guide 的完整或大段提取文本。该目录包含 40 余文件，EY 指南还可能包含联系人信息。P0 将目录设为 local-only，并从当前 Git 索引移除；本地文件不删除。
- Git 历史保留这些路径。建议人工批准后在独立备份与维护窗口运行：`git filter-repo --path raw/assets/extracted/ --invert-paths`，随后通知克隆者重新克隆；本次不执行。

## Medium

- 本地 `raw/assets/pdfs/wiki-tax/` 有约 315 MB 的 PDF。该目录已被忽略，但由 manifest 明确 local-only。
- source summary 以前直接链接本地 PDF；P0 改为说明本地材料和公开 URL，避免让公开仓库依赖不存在的二进制文件。

## Low

- 发现重复 `.smart-env` 忽略规则和不完整的本地运行时排除规则，已归并。
- 未发现已追踪文本中的本机绝对路径、邮箱或电话命中。

## 结论

当前分支的公开表面将只保留 manifest、来源元数据、哈希、定位信息和短摘要。历史清理需要仓库所有者单独确认。
