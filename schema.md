# 元数据规范

## 通用 Frontmatter

```yaml
---
title:
type:
summary:
field:
jurisdiction:
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

`summary` 是一句话定位信息，建议不超过 40 个汉字。AI 扫描全库时优先读取它。

## 三层渐进式详略结构

正式 wiki 页面应按三层组织：

| 层级 | 位置 | 建议长度 | 用途 |
| --- | --- | --- | --- |
| Layer 1 | frontmatter `summary` | ≤40 个汉字 | 扫描和定位 |
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

`type`: concept, rule, policy, case, paper, method, jurisdiction, industry, entity, topic, source, synthesis, question, review, output

`field`: china-tax, international-tax, transfer-pricing, indirect-tax, us-tax, uk-tax, eu-vat-gst, tax-treaties, tax-tech, research-writing, career-roadmap

`status`: seed, draft, reviewed, mature, needs-review

`level`: basic, intermediate, advanced

`confidence`: low, medium, high

`source_quality`: primary, official, professional, academic, mixed, unknown

`career_use`: interview, memo, research, presentation, portfolio, study

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
