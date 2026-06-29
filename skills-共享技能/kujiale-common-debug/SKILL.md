---
name: kujiale-common-debug
description: 酷家乐工艺编辑器通用语法与排错知识。用于 printSystemLog、Tetris 日志查询、未找到定义、格式错误、自定义代码无效、唯一标识冲突、依赖发布、可用类型/脚本、脚本域选择，以及保存、运行和输出问题诊断。
---

# 酷家乐公共调试

## 排错顺序

1. 确认业务领域、业务模块、系统入口和触发动作。
2. 在“可用类型/脚本”确认 import。
3. 用最小函数验证入参、返回值和类型。
4. 检查自定义对象和子脚本发布顺序。
5. 添加统一前缀与序号的 `printSystemLog`。
6. 查询对应服务日志。
7. 检查最终输出，不只看编辑器保存成功。

## 常见语法限制

- 一条脚本只定义一个普通函数。
- 唯一标识与函数名完全一致。
- 不使用 `try/catch`、传统 `for`、`while`。
- 不使用字符串 `+` 拼接日志。
- `join` 使用双引号。
- 避免重复变量名。
- 非布尔对象显式与 `null` 比较。

## 日志服务

| 场景 | service |
| --- | --- |
| 台面 | `service.dcs-countertop` |
| 设计后处理 | `service.dcs-post-process-task` |
| 输出 JSON | `service.superoutputtask` |
| 订单 | `service.dcs-order-design` |

## 参考资料

读取 [logging-and-errors-日志与错误排查.md](references/logging-and-errors-日志与错误排查.md) 获取详细检查表。
