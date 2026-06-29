---
name: kujiale-rule-check
description: 酷家乐工艺编辑器规则检测脚本知识。用于 ruleCheck、DesignData、ModelRuleResult、RuleLevel、buildModelCheckResult、buildRuleResult、模型告警与错误提示，以及规则检测脚本拆分、触发和日志排错。
---

# 酷家乐规则检测

## 核心流程

1. 明确检测对象、触发时机和提示级别。
2. 使用系统入口 `ruleCheck`，保持固定入参与返回类型。
3. 用 `buildModelCheckResult` 绑定目标模型。
4. 用 `buildRuleResult` 创建 `WARN` 或 `ERROR` 规则。
5. 将规则结果加入模型结果，再加入总结果数组。
6. 分离可复用子脚本，避免所有规则堆在入口中。
7. 同时验证命中和不命中场景。

## 质量要求

- 提示必须说明对象、条件和修复方向。
- 避免笛卡尔积式遍历和重复告警。
- 记录规则检测触发方式和适用工具线。

## 参考资料

读取 [cases-index-案例索引.md](references/cases-index-案例索引.md) 查看案例计划。
