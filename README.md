# 酷家乐工艺编辑器 AI 技能库

把经过真实脚本、日志或输出 JSON 验证的经验，做成 Codex、Claude Code、TRAE 等 AI 工具可复用的开放 Agent Skill。

## 仓库结构

```text
skills/
├─ kujiale-craft-editor/       # 工艺编辑器开发、案例与排错
│  └─ SKILL.md
└─ github-share-agent-skills/  # Git、GitHub 与 Skill 共享
   ├─ SKILL.md
   └─ scripts/

CONTRIBUTING-贡献指南.md
validate-skills-校验技能.py
```

只有两个 Skill。需要分享时，直接分享或复制对应的整个 Skill 文件夹。

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

也可以使用安装脚本：

```bash
python skills/github-share-agent-skills/scripts/install-skill-安装Skill.py \
  --source skills/kujiale-craft-editor \
  --tool codex
```

## 贡献

不要再为每个小功能新建 Skill。工艺编辑器经验统一补充到
`skills/kujiale-craft-editor/SKILL.md`；只有形成独立、稳定且经常单独使用的大能力时，才新增 Skill。

提交前运行：

```bash
python validate-skills-校验技能.py
```

具体要求见 [CONTRIBUTING-贡献指南.md](CONTRIBUTING-贡献指南.md)。
