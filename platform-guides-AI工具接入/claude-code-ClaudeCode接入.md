# Claude Code 接入

Claude Code 支持开放 Agent Skills，项目 Skill 路径为：

```text
.claude/skills/<skill-name>/SKILL.md
```

## 安装到项目

```powershell
Copy-Item `
  -Path ".\skills-共享技能\kujiale-countertop" `
  -Destination ".\.claude\skills\kujiale-countertop" `
  -Recurse -Force
```

个人 Skill 可放入：

```text
~/.claude/skills/<skill-name>/SKILL.md
```

调用示例：

```text
/kujiale-countertop
```

Claude Code 也会根据 `description` 自动加载相关 Skill。

官方说明：

```text
https://code.claude.com/docs/en/slash-commands
```
