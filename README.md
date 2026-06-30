# 酷家乐工艺编辑器 AI 技能库

把经过真实脚本、日志或输出 JSON 验证的经验，做成 Codex、Claude Code、TRAE 等 AI 工具可复用的开放 Agent Skill。

## 仓库结构

```text
skills/
├─ shutiao/                    # 工艺编辑器"设计中"脚本开发与排错
│  └─ SKILL.md
└─ share-skills-with-github/   # 使用 GitHub 共享与复用 Skill
   └─ SKILL.md

CONTRIBUTING-贡献指南.md
validate-skills-校验技能.py
```

只有两个 Skill。需要分享时，直接分享或复制对应的整个 Skill 文件夹。

培训视频与 CF 综合知识见
[REFERENCE-工艺编辑器培训与CF参考资料.md](REFERENCE-工艺编辑器培训与CF参考资料.md)。该文件仅作为参考资料，不参与 Skill 自动触发。

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

不要再为每个小功能新建 Skill。工艺编辑器经验统一补充到
`skills/shutiao/SKILL.md`；只有形成独立、稳定且经常单独使用的大能力时，才新增 Skill。

提交前运行：

```bash
python validate-skills-校验技能.py
```

具体要求见 [CONTRIBUTING-贡献指南.md](CONTRIBUTING-贡献指南.md)。
