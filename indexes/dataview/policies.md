# 政策索引

```dataview
TABLE field, jurisdictions, status, updated
FROM "wiki"
WHERE type = "policy" AND status != "deprecated"
SORT updated DESC
```
