---
title: "Phase 3 完成度报告"
type: meta
summary: "Phase 3 治理实施的目录、校验、来源和未完成内容建设审计"
status: reviewed
created: 2026-07-19
updated: 2026-07-19
---

# Phase 3 完成度报告

## 最终目录树

`wiki/` 的正式导航为 `knowledge/`、`jurisdictions/`、`cases/`、`sources/` 与 `_ops/`，并保留 `index.md`、`hot.md`、`overview.md`、`log.md`。旧 `indexes/mocs/` 是 deprecated 兼容页。

## 新旧路径映射

- `01-china-tax` → `jurisdictions/CN`
- `02-international-tax` → `knowledge/international-tax`
- `03-transfer-pricing` → `knowledge/transfer-pricing`
- `04-us-tax`、`05-uk-tax` → 相应法域目录
- `06-eu-vat-gst` → `knowledge/indirect-tax`、`jurisdictions/EU` 和 `jurisdictions/others/*`
- `07-tax-treaties-and-cases` → `knowledge/international-tax/treaties`、`cases/domestic-cases`
- `meta` → `_ops`；`entities` → `sources/organizations`

## Schema、lint 与 manifest

- schema version：3；新增 `jurisdictions`、authority/binding/legal status、时效、替代关系和精确定位字段。
- `vault_lint.py --strict`：通过。
- `manifest_check.py`：0 errors、0 warnings。
- manifest 记录 raw local-only、公开摘要可用性、许可状态、核验日期及下游页。

## CI 与公开风险

- `.github/workflows/vault-check.yml` 在 push/PR 运行严格 lint、manifest check 与敏感/禁用 raw 路径扫描。
- 完整 OECD/EY 提取文本已停止当前 Git 追踪；本地文件未删除；历史清理由人工决定。

## 来源与内容状态

- source summary：5（OECD TPG、EY VAT Guide、OECD Model Tax Convention、EU VAT Directive、Wayfair）。
- 已升级 reviewed 核心卡：常设机构、Wayfair、EU VAT 体系、独立交易原则、DEMPE。
- 已升级 reviewed 输出：独立交易原则、DEMPE、Wayfair 面试回答；都具有 source summary 证据链。
- 当前统计以 `scripts/rebuild_index.py` 和 lint 报告为准；`mature` 保持 0。

## 未完成的 P6 验收项

“至少 5 个 reviewed 核心卡”已达到；“至少 3 个 mature output”仍待真实使用验证。[[../../../outputs/tax-memos/Phase-3-demo-validation-memo|Demo 验证备忘录]]记录了可复现测试与后续材料清单。受益所有人、中国特别纳税调整、Pillar Two 等仍需按 Stage 1/2 摄入真实的官方或原始来源；不得用现有 EY 指南替代法律原文。

## 合并与回滚建议

- 合并建议：P0–P5 可合并；P6 内容建设继续在本分支补足后再合并。
- 回滚：按提交逆序执行 `git revert <SHA>`；不要改写 main 历史。
