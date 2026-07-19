# Raw 原始资料政策

`raw/` 是本库的本地证据层，不是公开全文资料库。原始 PDF、网页全文、电子书和大段提取文本默认仅保留在本地，不应提交到公开仓库。

## 本地放置规则

- 可公开的来源元数据、文件哈希和简短定位信息维护在 `raw/manifest.json`。
- 本地原文放入 `raw/local/`、`raw/private/` 或 `raw/assets/pdfs/`；它们由 `.gitignore` 排除。
- OCR 或全文提取文本放入 `raw/assets/extracted/`；它们同样仅本地保存。
- 需要协作或公开时，创建 `wiki/sources/` 中的 source summary，记录发布者、版本、公开 URL、精确页码/条文定位和可公开的短摘录。

## Manifest 与 source summary

每个已摄入来源在 `raw/manifest.json` 中记录其 `sha256`、本地路径、`local_only`、许可状态、最后核验日期和下游页面。source summary 负责解释资料能支撑什么结论；其 `Raw 原文位置` 应说明本地位置或“原文尚未入库”。

## 公开仓库边界

本库不会发布未获授权的完整出版物、判决数据库全文、四大专业机构指南全文、客户材料或个人联系方式。历史中如曾出现此类文件，只在治理报告中列出清理建议；未经人工确认不改写 Git 历史。
