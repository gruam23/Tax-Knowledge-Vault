# Needs Review 页面

```dataview
TABLE type, field, jurisdiction, source_quality, updated
FROM "wiki"
WHERE status = "needs-review"
SORT field ASC, file.name ASC
```
