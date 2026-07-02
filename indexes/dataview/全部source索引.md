# 全部 source 索引

```dataview
TABLE status, confidence, source_quality, updated, related
FROM "wiki"
WHERE type = "source" AND status != "deprecated"
SORT updated DESC, file.name ASC
```
