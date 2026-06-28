---
type: meta
title: "仪表盘"
summary: "知识库维护状态、seed 页面、缺来源页面和成熟页面的 Dataview 仪表盘"
status: reviewed
created: 2026-06-28
updated: 2026-06-28
---

# 知识库仪表盘

## 最近活动
```dataview
TABLE type AS 类型, status AS 状态, updated AS 更新日期
FROM "wiki"
WHERE type != "meta"
SORT updated DESC
LIMIT 15
```

## 种子页面（需要充实）
```dataview
LIST FROM "wiki"
WHERE status = "seed"
SORT updated ASC
```

## 缺少来源的实体
```dataview
LIST FROM "wiki/entities"
WHERE !sources OR length(sources) = 0
```

## 成熟页面
```dataview
LIST FROM "wiki"
WHERE status = "mature" OR status = "evergreen"
SORT updated DESC
```
