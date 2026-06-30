# 酷家乐工艺编辑器 AI 技能库

把经过真实脚本、日志或输出 JSON 验证的经验，做成 Codex、Claude Code、TRAE 等 AI 工具可复用的开放 Agent Skill。

## 仓库结构

`skills/` 目录下按共享人创建文件夹，每人维护自己的 Skill：

```text
skills/
├─ shutiao/                    # hallofmg-bit 的经验
│  └─ countertop/              # "设计中-台面"脚本开发与排错
│     └─ SKILL.md
├─ zhangsan/                   # 张三的经验（示例）
│  └─ SKILL.md
└─ share-skills-with-github/   # Git、GitHub 与 Skill 共享（公共）
   └─ SKILL.md

CONTRIBUTING-贡献指南.md
validate-skills-校验技能.py
```

需要分享时，直接分享或复制对应的整个 Skill 文件夹。

## 使用

克隆仓库：

```bash
git clone https://github.com/hallofmg-bit/kujiale-craft-script-knowledge.git
```

安装位置：

| 工具 | 位置或方式 |
| --- | --- |
| Codex | `~/.codex/skills/<skill-name>/` |
| Claude Code | `~/.claude/skills/<skill-name>/` 或项目 `.claude/skills/` |
| TRAE | `Settings -> Rule & Skills -> Skills -> Create` |
| 其他工具 | 导入包含 `SKILL.md` 的整个目录 |

安装时直接复制包含 `SKILL.md` 的整个 Skill 文件夹；所需自动化脚本源码已经收录在
`share-skills-with-github/SKILL.md` 中。

## 贡献

在 `skills/` 下创建以自己命名的文件夹（小写英文、数字和连字符），放入 `SKILL.md`，提交 PR。审核通过后即成为该目录的 Code Owner。

提交前运行：

```bash
python validate-skills-校验技能.py
```

具体要求见 [CONTRIBUTING-贡献指南.md](CONTRIBUTING-贡献指南.md)。
