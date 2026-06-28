---
type: meta
title: "知识图谱"
created: 2026-04-28
updated: 2026-05-09
---

# 知识图谱 (Knowledge Graph)

> 以下 Mermaid 图谱展示知识库中核心概念之间的语义关联。
> 箭头方向表示"依赖/引用"关系，虚线表示"对比/互斥"关系。

## 1. 直接税体系 (Transfer Pricing)

```mermaid
graph LR
    %% ===== 核心原则层 =====
    ALP["[[独立交易原则]]<br/>Arm's Length Principle"]
    GFA["[[全球公式分配法]]<br/>Global Formulary Apportionment"]

    ALP -. "OECD 明确反对" .-> GFA

    %% ===== 方法论层 =====
    TPM["[[转移定价方法]]<br/>5 种标准方法"]
    CA["[[可比性分析]]<br/>9 步流程"]

    ALP --> TPM
    ALP --> CA
    TPM --> CA

    %% ===== 交易类型层 =====
    DEMPE["[[无形资产及DEMPE原则]]<br/>Intangibles & DEMPE"]
    IGS["[[集团内服务]]<br/>Intra-Group Services"]
    CCA["[[成本分摊协议]]<br/>CCA"]
    BR["[[业务重组]]<br/>Business Restructurings"]
    FT["[[金融交易]]<br/>Financial Transactions"]

    ALP --> DEMPE
    ALP --> IGS
    ALP --> CCA
    ALP --> BR
    ALP --> FT

    DEMPE --> CCA
    DEMPE --> BR
    CA --> IGS

    %% ===== 集团效应层 =====
    SYN["[[跨国集团协同效应]]<br/>MNE Group Synergies"]

    SYN --> CA
    SYN -. "不属于无形资产" .-> DEMPE

    %% ===== 合规与争端层 =====
    DOC["[[转让定价同期资料]]<br/>三层文档架构"]
    MAP["[[相互协商程序与对应调整]]<br/>MAP"]

    ALP --> DOC
    ALP --> MAP
    BR --> MAP
    FT --> MAP

    %% ===== 实体层 =====
    OECD["[[OECD]]<br/>规则制定者"]

    OECD --> ALP
    OECD --> DOC
    OECD --> MAP

    %% ===== 样式 =====
    classDef principle fill:#4fc1ff,stroke:#333,color:#000
    classDef method fill:#dcdcaa,stroke:#333,color:#000
    classDef transaction fill:#ce9178,stroke:#333,color:#000
    classDef compliance fill:#6a9955,stroke:#333,color:#fff
    classDef entity fill:#c586c0,stroke:#333,color:#000

    class ALP,GFA principle
    class TPM,CA method
    class DEMPE,IGS,CCA,BR,FT,SYN transaction
    class DOC,MAP compliance
    class OECD entity
```

## 2. 间接税体系 (Indirect Tax)

```mermaid
graph LR
    %% ===== 基础层 =====
    VAT["[[增值税(VAT-GST)]]<br/>基本原理"]
    
    %% ===== 区域框架层 =====
    EUVAT["[[欧盟增值税体系]]<br/>EU VAT Directive"]
    EUG["[[欧盟增值税术语词典]]<br/>Glossary"]
    
    VAT --> EUVAT
    EUVAT --> EUG

    %% ===== 欧盟成员国实践 =====
    GER["[[德国增值税体系]]"]
    FRA["[[法国增值税体系]]"]
    UK["[[英国增值税体系]]<br/>脱欧后"]

    EUVAT --> GER
    EUVAT --> FRA
    EUVAT -. "脱欧前曾受限" .-> UK

    %% ===== 全球其他实践 =====
    CN["[[中国增值税体系]]"]
    JP["[[日本消费税体系]]"]
    IN["[[印度GST体系]]"]
    SG["[[新加坡GST体系]]"]
    AU["[[澳大利亚GST体系]]"]
    CA["[[加拿大GST-HST体系]]"]
    US["[[美国销售税体系]]"]

    VAT --> CN
    VAT --> JP
    VAT --> IN
    VAT --> SG
    VAT --> AU
    VAT --> CA
    
    VAT -. "显著差异(终端征收)" .-> US

    %% ===== 实体层 =====
    EY["[[EY]]<br/>VAT Guide 发布者"]

    EY --> VAT
    EY --> EUVAT

    %% ===== 样式 =====
    classDef core fill:#4fc1ff,stroke:#333,color:#000
    classDef region fill:#dcdcaa,stroke:#333,color:#000
    classDef country fill:#ce9178,stroke:#333,color:#000
    classDef us_sales fill:#ce9178,stroke:#333,color:#000,stroke-dasharray: 5 5
    classDef entity fill:#c586c0,stroke:#333,color:#000

    class VAT core
    class EUVAT,EUG region
    class GER,FRA,UK,CN,JP,IN,SG,AU,CA country
    class US us_sales
    class EY entity
```

## 图例

| 颜色 | 类别 | 包含页面 |
|------|------|---------|
| 🔵 蓝色 | 核心原则/基础 | 独立交易原则、增值税原理 |
| 🟡 黄色 | 方法论/区域框架 | 转移定价方法、EU VAT体系 |
| 🟠 橙色 | 交易类型/国家实践 | 业务重组、中国增值税、德国增值税等 |
| 🟢 绿色 | 合规与争端 | 同期资料、MAP |
| 🟣 紫色 | 实体 | OECD、EY |
