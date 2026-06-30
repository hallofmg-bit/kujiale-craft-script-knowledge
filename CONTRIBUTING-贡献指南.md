# 贡献指南

## 放在哪里

- 工艺编辑器脚本、入口、对象、日志、案例和排错：更新 `skills/shutiao/SKILL.md`。
- Git、GitHub、Skill 制作、安装和跨工具复用：更新 `skills/share-skills-with-github/`。
- 不按作者建目录，不为单个函数或单个案例创建 Skill。

## 成功经验格式

在对应 `SKILL.md` 中增加一个小节，至少写清：

1. 业务目标、业务模块和系统入口；
2. 依赖对象及发布顺序；
3. 完整脱敏脚本；
4. 正向、反向场景和真实验证证据；
5. 失败过程、修正原因和已知限制；
6. 作者或来源摘要、验证日期。

每个案例标题下方用引用块标注署名：

```markdown
## 已验证案例：案例标题

> 作者：GitHub用户名 | 验证日期：YYYY-MM | 来源：简述项目或场景

### 目标与结论
...
```

尚未真实验证的内容必须标为"待验证"，不能写成成功结论。

## 安全与脱敏

禁止提交：

- Token、密码、Cookie、Access Key 和内部认证配置；
- 客户姓名、电话、地址、订单号和原始设计方案 JSON；
- 未脱敏的用户 ID、任务 ID、账号 ID 和完整内部日志；
- 未获公开授权的企业专属商品 ID、价格或供应链映射；
- 内部源代码、受限文档全文、未经授权的 CF 截图和附件。

使用 `BG_ID_FOR_20MM`、`TASK_ID_REDACTED` 等占位符。若误提交凭证，停止推送，清理 Git 历史并立即轮换凭证。

## 提交流程

```bash
git switch -c skill/short-topic
python validate-skills-校验技能.py
git diff --check
git add <明确文件>
git diff --cached
git commit -m "Update shared skill for <topic>"
git push -u origin skill/short-topic
```

通过 Pull Request 提交，并附验证证据和风险说明。
