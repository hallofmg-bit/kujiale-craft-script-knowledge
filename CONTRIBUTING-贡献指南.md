# 贡献指南

## 按领域提交

| 内容 | Skill |
| --- | --- |
| 台面、洞、挡水、工艺费 | `kujiale-countertop` |
| 设计后处理、虚拟模型 | `kujiale-design-postprocess` |
| 规则检测 | `kujiale-rule-check` |
| 订单字段、提审处理 | `kujiale-order-postprocess` |
| 图纸、尺寸、加工数据 | `kujiale-drawing` |
| 语法、日志、发布与通用排错 | `kujiale-common-debug` |

不要按作者创建 Skill。作者信息写入案例元数据。

## 成功案例准入条件

必须同时满足：

1. 明确业务领域、业务模块和系统入口。
2. 脚本已保存并发布。
3. 有真实触发记录。
4. 有 `printSystemLog`、导出 JSON、规则检测结果或订单结果等证据。
5. 已验证正向场景和至少一个反向场景。
6. 已说明适用环境、依赖对象和已知限制。
7. 已完成脱敏。

未完成验证的内容放在 PR 描述中讨论，不放进 `cases-成功案例/`。

## 提交流程

1. 从 `templates-贡献模板/case-template-成功案例模板.md` 创建案例。
2. 将案例放入对应 Skill 的 `references/cases-成功案例/`。
3. 更新该 Skill 的案例索引或 `SKILL.md` 路由。
4. 运行：

   ```text
   python scripts-工具脚本/validate-skills-校验技能.py
   ```

5. 提交 PR，并附验证证据和风险说明。

## 命名规范

案例文件：

```text
english-slug-中文说明.md
```

Skill 目录及 frontmatter `name`：

```text
lowercase-english-hyphen
```

## 修改已有案例

- 行为变化：更新 `updated` 和验证记录。
- 仅文字修正：保留原验证记录。
- 新环境尚未验证：明确标注，不覆盖已验证结论。
- 与已有案例冲突：并列记录环境差异，不直接删除旧结论。
