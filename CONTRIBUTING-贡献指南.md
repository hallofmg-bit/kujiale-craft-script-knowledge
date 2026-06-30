# 贡献指南

## 放在哪里

`skills/` 目录下按共享人创建文件夹，每人维护自己的 Skill：

```text
skills/
└─ shutiao/                    # hallofmg-bit 的经验
   └─ countertop/              # "设计中-台面"脚本开发与排错
      └─ SKILL.md

share-skills-with-github/      # Git、GitHub 与 Skill 共享（公共，仓库根目录）
└─ SKILL.md
```

- 每位贡献者在 `skills/` 下创建以自己命名的文件夹作为共享人根目录。
- 共享人文件夹下按业务域建子目录，每个子目录是一个独立的 Skill（包含 `SKILL.md`）。
- 子目录名与 frontmatter `name` 一致，只用小写英文、数字和连字符。
- `share-skills-with-github/` 是仓库根目录下的公共 Skill，管理 Git/GitHub 与 Skill 共享流程，不归属个人。
- 不为单个函数或单个案例单独建 Skill；同一业务域的经验统一维护在对应的 Skill 中。

## 新人加入

1. 在 `skills/` 下创建自己的文件夹（如 `skills/zhangsan/`）。
2. 在自己的文件夹下按业务域创建子目录（如 `skills/zhangsan/countertop/`）。
3. 在子目录中创建 `SKILL.md`，填写 frontmatter 和内容。
4. 提交 PR，审核通过后即成为该目录的 Code Owner。

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
### 案例 N：案例标题

> 作者：GitHub用户名 | 验证日期：YYYY-MM | 来源：简述项目或场景

#### 目标与结论
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

通过 Pull Request 提交，并附验证证据和风险说明。只修改自己目录下的文件，不改动他人 Skill。
