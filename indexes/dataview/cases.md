# 案例索引

```dataview
TABLE field, jurisdictions, status, confidence, updated
FROM "wiki"
WHERE type = "case" AND status != "deprecated"
SORT file.name ASC
```
