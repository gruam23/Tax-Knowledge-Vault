# 元数据规范

## 通用 Frontmatter

```yaml
---
title:
type:
summary:
field:
jurisdictions: []
status: seed
level: basic
confidence: medium
source_quality: mixed
career_use:
sources: []
related: []
created:
updated:
---
```

`summary` 是一句话定位信息，最多 80 个 Unicode 字符。AI 扫描全库时优先读取它。

## 三层渐进式详略结构

正式 wiki 页面应按三层组织：

| 层级 | 位置 | 建议长度 | 用途 |
| --- | --- | --- | --- |
| Layer 1 | frontmatter `summary` | ≤80 个 Unicode 字符 | 扫描和定位 |
| Layer 2 | 正文 `## 速览` | ≤150 个汉字 | 快速理解 |
| Layer 3 | 正文其余部分 | 不限 | 深度研究、面试准备、memo 写作 |

## 原文指针规则

每个正式页面的“来源”或“参考素材”应尽量标注：

- source summary 页面
- raw 原文文件
- 页码、章节或段落范围
- 可点击 wikilink

示例：

```markdown
## 来源
- [[2026-04-28-OECD-TPG-2022]] — Chapter II (pp.93-147)
  - CUP 方法：[[2022-OECD-TPG-extracted-61-150|原文 pp.97-101]]
```

## 枚举值

`type`: concept, rule, policy, case, paper, method, jurisdiction, industry, entity, topic, source, synthesis, question, review, output, meta

`field`: china-tax, international-tax, transfer-pricing, indirect-tax, us-tax, uk-tax, eu-vat-gst, tax-treaties, tax-treaties-and-cases, industries, tax-tech, research-writing, career-roadmap, maintenance

`status`: seed, draft, developing, reviewed, mature, needs-review, deprecated

`level`: basic, intermediate, advanced

`confidence`: low, medium, high

`source_quality`: primary, official, professional, academic, mixed, unknown

`career_use`: interview, memo, research, presentation, portfolio, study

## 可选字段与迁移规则

### 税法效力与时间字段

新页面必须使用 `jurisdictions`（例如 `[CN, OECD]`）。单数 `jurisdiction` 仅用于识别尚未迁移的旧页面，lint 只给 warning；不得为了通过 lint 在新页面中补回该字段。

- `authority_type`: treaty, statute, regulation, notice, administrative-guidance, case, professional, academic, internal-analysis。
- `binding_status`: binding, persuasive, nonbinding, unknown；它与 `source_quality`（资料可靠程度）不同。
- `legal_status`: current, amended, repealed, draft, historical, unknown。
- `effective_from`、`effective_to`、`last_verified`：日期；概念页不应为凑字段而填写。
- `supersedes`、`superseded_by`：替代关系的 wikilink 列表。
- `citation_locator`：精确条文、段落或页码，例如 `Article 5`、`Chapter VI, para. 6.32`。

### 证据标记

`confidence` 表示整页综合可信度；具体结论统一使用：

`<!-- evidence: extracted; source: Source ID; locator: Article 5 -->`

`evidence_status` 仅允许 `extracted`、`inferred`、`ambiguous`、`unverified`。

`aliases`：用于记录中英文别名、缩写和常见译名，便于 Obsidian 搜索和 AI 检索。例如 PE、Permanent Establishment、常设机构。

`tags`：用于轻量主题标记，不替代 `field`。适合记录 `OECD`、`VAT`、`case-law` 等跨领域标签。

`domain`：旧字段，仅用于迁移兼容。新页面不得使用 `domain` 表示领域，统一用 `field`。

`complexity`：旧字段，仅用于迁移兼容。新页面不得使用 `complexity` 表示难度，统一用 `level`。

迁移旧页面时：

- 如果同时存在 `domain` 和 `field`，以 `field` 为准。
- 如果同时存在 `complexity` 和 `level`，以 `level` 为准。
- 迁移后可暂留旧字段作为兼容信息，但不得依赖旧字段做索引。
- 新建页面必须只使用 `field` 和 `level`。

## 状态规则

- `seed`：占位或刚建立的薄卡。
- `draft`：已有基本内容，但结构和来源仍不稳定。
- `developing`：正在扩写或迁移，允许保留待补来源。
- `needs-review`：来源不足、需要复核或不得作为确定结论使用。
- `reviewed`：已经按来源核对，至少有一个有效来源。
- `mature`：可复用于输出、培训或作品集，至少有一个有效来源。
- `deprecated`：被新页面替代或不再推荐使用，应指向替代页面。

## 别名词表

- CRS = 共同申报准则 = Common Reporting Standard
- BEPS = 税基侵蚀和利润转移 = Base Erosion and Profit Shifting
- 转移定价 = Transfer Pricing = TP
- DID = 双重差分 = Difference-in-Differences
- OECD = 经济合作与发展组织
- ETR = 有效税率 = Effective Tax Rate
- BTD = 会税差异 = Book-Tax Difference
- AEOI = 自动交换信息 = Automatic Exchange of Information
- PE = 常设机构 = Permanent Establishment
- VAT = 增值税 = Value-Added Tax
- GST = 商品及服务税 = Goods and Services Tax
- OSS = One-Stop Shop（EU 增值税一站式申报门户）
- ViDA = VAT in the Digital Age（EU 增值税数字化改革）
- TOGC = Transfer of a Going Concern（持续经营转让）
- EY = Ernst & Young = 安永

## 置信度标注规则

- EXTRACTED：信息直接出现在原文里。
- INFERRED：从多处原文推断出来。
- AMBIGUOUS：原文说法不清楚或有歧义。
- UNVERIFIED：来自 AI 背景知识，原文没有证据。
