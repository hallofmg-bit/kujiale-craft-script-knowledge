---
name: kujiale-design-postprocess
description: 酷家乐工艺编辑器设计后处理脚本知识。用于 postProcess、PostProcessDesignData、DesignPostProcessResult、ModelPostProcessResult、addChildren、addParameters、VirtualModel、输出 JSON 前修改方案，以及设计后处理日志与依赖排错。
---

# 酷家乐设计后处理

## 核心流程

1. 确认需求发生在生成 JSON/输出阶段，而不是设计中实时生成。
2. 使用设计后处理业务领域和系统入口 `postProcess`。
3. 用 `DesignPostProcessResult` 初始化修改结果。
4. 用 `ModelPostProcessResult` 或组合结果描述变更。
5. 通过 `addChildren` 添加虚拟模型，通过 `addParameters` 添加参数。
6. 先发布自定义对象和子脚本，再发布入口。
7. 查询 `service.dcs-post-process-task` 日志并检查输出 JSON。

## 边界

- 不要把此域的 `VirtualModel/addChildren` 直接搬到台面 `generateFee`。
- 设计后处理通常不会在设计画布中即时展示。
- 一条脚本只定义一个普通函数；复杂逻辑拆成已发布的子脚本。

## 参考资料

读取 [cases-index-案例索引.md](references/cases-index-案例索引.md) 查看已验证案例和待补充方向。
