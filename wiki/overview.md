---
title: Wiki 总览
type: review
summary: "本地 Obsidian 知识层的覆盖范围、维护重点和 GitHub 备份边界"
field: maintenance
jurisdictions: []
status: reviewed
level: basic
confidence: high
source_quality: primary
career_use: [study]
sources: [CODEX.md]
related: [税务知识库 Review 2026-06-28]
created: 2026-06-28
updated: 2026-07-19
---
# Wiki 总览

wiki 层负责把原始税务资料整理成结构化、可追溯的知识笔记。

## 运行边界

- 本库只在本地 Obsidian 中运行，索引、overview、lint 和 manifest 检查均在本地执行。
- raw 原文、PDF 和完整提取文本仅存本地；GitHub 只保存 source summary、知识卡、输出、模板、脚本和 manifest 元数据。
- GitHub 不负责运行、部署或验收本知识库。

## 当前结构

- `knowledge/`：国际税、转让定价、间接税、行业、税务科技和研究写作知识卡。
- `jurisdictions/`：CN、US、UK、EU 及其他国家和地区页面。
- `cases/`：国内案例及其他案例知识页。
- `sources/`：可公开的 source summary、机构和来源入口。
- `_ops/`：摄入、问题、复核、维护与 lint 报告。

正式主导航由这些目录中的 `index.md` 承担；`indexes/mocs/` 仅保留为 deprecated 兼容层。

## 当前知识覆盖

- 国际税与税收协定：已覆盖国际税核心框架、受益所有人、常设机构和 BEPS。
- 转让定价：已覆盖独立交易原则、可比性分析、方法、DEMPE、集团内服务、金融交易等专题。
- 间接税：中国、美国、英国、欧盟 VAT 以及 AU、CA、DE、FR、IN、JP、SG 的 VAT/GST 页面已纳入法域结构。
- 中国税：已有中国增值税和研发费用加计扣除页面；后者仍待官方来源摄入。
- 美国税：已有销售税体系、Wayfair 案及相应面试输出。
- 来源与输出：当前 lint 口径下有 5 个 source summary 和 5 个 interview outputs。

## 当前成熟度

- 参与 lint frontmatter 检查的页面：78。
- `reviewed`：42。
- `mature`：0。
- `needs-review`：5。
- `deprecated`：1（Phase 1 旧占位跳转页）。
- 当前非阻断 warning：1 个 deprecated 页面提示，以及研发费用加计扣除缺少 `last_verified` 的真实来源缺口提示。

## 当前知识缺口

- 摄入并核验受益所有人的中国官方规则。
- 摄入并核验中国现行研发费用加计扣除官方规则。
- 补充中国特别纳税调整规则及与 OECD TPG 的对应关系。
- 建立 Pillar Two 官方来源、规则框架和法域实施跟踪。
- 继续补齐 Economic nexus、marketplace facilitator 及其他页面中的真实来源缺口。


<!-- AUTO-GENERATED:BEGIN -->
- 正式知识与法域案例页面：47
- Knowledge 页面：27
- Jurisdiction 页面：18
- Case 页面：2
- Source summary：5
- Outputs：6
- Reviewed：42
- Mature：0
- Needs review：5
- Deprecated：1
<!-- AUTO-GENERATED:END -->
