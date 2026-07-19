# 税务知识库

这是一个面向税务研究、职业学习和专业输出复用的 Obsidian 知识库。

## Quick Start

1. 用 Obsidian 打开本仓库根目录。
2. 先读 `purpose.md`、`schema.md` 和 `CODEX.md`，确认写作边界、frontmatter 规范和维护规则。
3. 从 `index.md` 进入全库导航，或从 `wiki/index.md` 进入知识层。
4. 新概念优先使用 `templates/concept-template.md`，新输出优先使用 `templates/interview-template.md` 或 `outputs/interview/` 示例。
5. 每次批量移动、扩写、引入新来源后运行 lint：

```bash
python scripts/vault_lint.py --root .
```

## 推荐 Obsidian 插件

- Dataview：用于 `indexes/dataview/` 查询。
- Templater：用于从 `templates/` 快速生成标准页面。
- Linter：用于统一 Markdown 格式。
- Advanced Tables：用于维护规则表、案例表和对比表。
- Omnisearch：用于全库检索概念、案例和来源。
- Obsidian Git：用于提交前查看差异和回滚误改。

## 核心分层

- `inbox/`：临时收件箱，用来快速保存政策、案例、论文、网页和想法。
- `raw/`：原始资料层，是正式知识的 source of truth。
- `wiki/`：结构化知识层，Phase 2 起按领域优先组织。
- `wiki/sources/`：来源摘要页，连接 raw 原文与研究型知识卡。
- `domains/`：学习路线和领域地图。
- `outputs/`：面试回答、税务 memo、研究报告、PPT、作品集材料。
- `templates/`：各类页面模板。
- `indexes/`：Dataview 查询和 MOC 导航页。

## 领域入口

- `wiki/knowledge/`：按国际税、转让定价、间接税、税务科技、研究写作和行业场景浏览。
- `wiki/jurisdictions/`：按 CN、US、UK、EU 和其他法域浏览。
- `wiki/cases/`：按案例类型浏览。
- `wiki/sources/`：按来源类型浏览可公开 source summary。
- `wiki/_ops/`：维护、复核、摄入与 lint 报告。

## 工作流

### 每日

- 把临时材料放入 `inbox/`，不要直接写成结论。
- 为新增材料补一条 source summary 或待处理记录。
- 对当天新增知识卡补齐 `summary`、`sources`、`related` 和 `## 速览`。

### 每周

- 选择 3-5 张 `needs-review` 或 `developing` 卡升级为研究型知识卡。
- 检查 `wiki/index.md`、领域 `index.md` 和 `indexes/mocs/` 是否覆盖新增页面。
- 运行 lint，处理死链、缺字段和 reviewed/mature 无来源问题。

### 每月

- 复核公开仓库风险，清理本地路径、客户信息、私密配置和未授权原文。
- 把成熟页面沉淀成 `outputs/` 中的面试回答、memo 或研究短文。
- 对高频领域更新 MOC，确认领域结构仍比技术分类更适合检索。

## Lint

运行：

```bash
python scripts/vault_lint.py --root .
```

脚本会解析 YAML frontmatter，检查枚举值、日期、summary 长度、sources wikilink、reviewed/mature 来源要求和全库死链，并生成：

```text
wiki/_ops/lint-reports/lint-report-YYYY-MM-DD.md
```

## 隐私与公开仓库注意事项

- 不提交 `.env`、本地配置、缓存、数据库、客户资料、private/confidential 目录。
- 公开文档不得包含本机绝对路径，使用“本仓库根目录”“只读母库”或相对路径表达。
- 未确认授权的 PDF、网页全文、客户底稿和个人信息不得进入公开输出。
- 来源不足的页面保持 `needs-review` 或 `developing`，不得伪造权威来源。

## 当前状态

本库已经作为相邻只读母库 `../wiki-tax` 的独立派生库初始化完成。当前主力库为本仓库根目录。
