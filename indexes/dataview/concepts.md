# 概念索引

```dataview
TABLE field, jurisdictions, status, level, updated
FROM "wiki"
WHERE type = "concept" AND status != "deprecated"
SORT field ASC, file.name ASC
```
