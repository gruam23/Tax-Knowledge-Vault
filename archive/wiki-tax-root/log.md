---
type: meta
title: "操作日志"
---

# 操作日志

## [2026-05-09] upgrade | 三层架构与深度阅读指针
- 引入三层渐进式详略架构（summary / 速览 / 正文），更新 `INSTRUCTIONS.md` 和 `_templates/`
- 为 `转移定价方法.md` 做示范改造，加入 summary、速览、带 wikilink 的深度阅读指针
- **TODO**：将 `raw/pdfs/` 下的大文件按章节拆分为独立 md，实现 Obsidian 点击精确跳转到章节级别

## [2026-05-09] maintain | 知识孤岛修复与 lint 升级
- 升级 `lint_wiki.py`：新增第 7-9 项检查（知识孤岛检测、hot 统计准确性、index 日期新鲜度）
- 修复 8 个知识孤岛：在 `增值税(VAT-GST).md` 中补充 [[英国增值税体系]]、[[加拿大GST-HST体系]]、[[印度GST体系]] 链接；在 `独立交易原则.md` 中补充 [[转让定价同期资料]]、[[相互协商程序与对应调整]]、[[业务重组]]、[[成本分摊协议]]、[[金融交易]] 链接
- 更新 `INSTRUCTIONS.md` 操作检查单：新增"同步更新相关 md 文件"和"运行健康检查"两项强制步骤

## [2026-05-09] reorganize | 重组概念词条目录
- 将 `concepts/` 目录下的 25 个概念词条按学科领域划分到 `indirect_tax/` (间接税) 和 `transfer_pricing/` (转让定价) 两个子目录中
- 提升了知识库结构的清晰度，解决领域混杂问题

## [2026-05-07] batch-create | 10 个主要国家/地区 VAT/GST 概念页
- Raw sources: `raw/pdfs/ey-vat-guide-{Germany,France,UK,US,Australia,Japan,China-Mainland,India,Singapore,Canada}.md`
- Pages created: [[德国增值税体系]], [[法国增值税体系]], [[英国增值税体系]], [[美国销售税体系]], [[澳大利亚GST体系]], [[日本消费税体系]], [[中国增值税体系]], [[印度GST体系]], [[新加坡GST体系]], [[加拿大GST-HST体系]]
- Key highlights: 德国Organschaft集团制/GoBD; 法国四档税率+2026-2028强制电子发票; 英国脱欧postponed VAT accounting+Windsor Framework; 美国Wayfair经济关联+~13,000管辖区; 澳大利亚Netflix Tax+GST-free vs Input-taxed; 日本合格发票制度(2023)+指定平台运营商(2025); 中国2026增值税法+留抵退税法定化+代扣代缴; 印度双重GST+发票匹配+180天规则; 新加坡OVR+InvoiceNow; 加拿大GST/HST/QST/PST四层税制

## [2026-05-07] deep-dive | EU 增值税章节深度消化
- Extracted: `raw/pdfs/ey-vat-guide-EU-chapter.md` (15页, PDF pp.685-699)
- Pages created: [[欧盟增值税体系]]
- Key insights: 四种应税交易; B2B目的地原则+反向征收; OSS/IOSS一站式申报; ViDA三大支柱(DRR/平台经济/单一注册, 2028-2035); Quick Fixes四项修正; 链式交易0%税率归属; 平台视为供应商规则; 进项税按比例抵扣(pro rata); EU企业vs非EU企业退税双轨制

## [2026-05-07] ingest | EY Worldwide VAT, GST and Sales Tax Guide 2026
- Source: `raw/pdfs/ey-gl-vat-guide-03-2026.pdf`
- Extracted: 23 batches (`raw/pdfs/ey-vat-guide-extracted-{1-100..2201-2226}.md`)
- Summary: [[2026-05-07-EY-VAT-Guide-2026]]
- Pages created: [[增值税(VAT-GST)]], [[EY]]
- Key insights: 153管辖区的VAT/GST/销售税体系汇编; 匈牙利27%全球最高标准VAT税率; 中国增值税法2026年1月正式实施; EU OSS/ViDA数字化改革; 全球电子发票趋势加速

## [2026-04-28] audit | 知识库合规审计
- 对照 Implementation Plan 执行了完整审计
- 修复：创建 knowledge-graph.md、补全 log.md、更新 overview.md、修复 index.md 统计、写入 wiki-cache.json
- 执行 git commit 提交所有新增内容

## [2026-04-28] ingest | Chapter VII-X 深度消化 (pp.331-658)
- Extracted: `raw/pdfs/2022-OECD-TPG-extracted-331-800.md`
- Pages created: [[集团内服务]], [[成本分摊协议]], [[业务重组]], [[金融交易]]
- Key insights: 低附加值服务5%加成率简化机制; CCA按价值计价原则; 业务重组退出补偿(Exit Charge); 集团内贷款隐性支持(Implicit Support)对利率的影响

## [2026-04-28] ingest | Chapter V-VI 深度消化 (pp.241-330)
- Extracted: `raw/pdfs/2022-OECD-TPG-extracted-241-330.md`
- Pages created: [[转让定价同期资料]], [[无形资产及DEMPE原则]]
- Key insights: BEPS三层文档架构(Master File/Local File/CbCR); DEMPE原则颠覆了"法定所有权=全部回报"的旧逻辑

## [2026-04-28] ingest | Chapter III-IV 深度消化 (pp.151-240)
- Extracted: `raw/pdfs/2022-OECD-TPG-extracted-151-240.md`
- Pages created: [[可比性分析]], [[相互协商程序与对应调整]]
- Pages updated: [[转移定价方法]] (补充CUP大宗商品规则)
- Key insights: 9步可比性分析流程; MAP在双重征税争议中的核心作用

## [2026-04-28] ingest | Chapter I-II 深度消化 (pp.61-150)
- Extracted: `raw/pdfs/2022-OECD-TPG-extracted-61-150.md`
- Pages created: [[全球公式分配法]], [[跨国集团协同效应]]
- Pages updated: [[独立交易原则]], [[转移定价方法]]
- Key insights: OECD明确反对全球公式分配法; 协同效应不属于无形资产

## [2026-04-28] ingest | OECD Transfer Pricing Guidelines 2022 (初始提取)
- Source: `raw/pdfs/2022-OECD TRANSFER PRICING GUIDELINES 2022.pdf`
- Extracted: `raw/pdfs/2022-OECD-TPG-extracted-1-60.md`
- Summary: [[2026-04-28-OECD-TPG-2022]]
- Pages created: [[独立交易原则]], [[转移定价方法]], [[OECD]]
- Key insight: 658页转移定价权威指南，确立了独立交易原则和五种定价方法的国际标准框架

## [2026-04-28] init | 知识库初始化
- 创建知识库：国际税收研究
- 路径：../wiki-tax
- 研究方向：CRS / 转移定价 / 国际税收协定 / BEPS / 计量方法
