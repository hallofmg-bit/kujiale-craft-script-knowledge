# Codex 接入

## 项目内使用

将需要的 Skill 目录复制到项目或个人 Codex Skills 目录。个人目录通常为：

```text
~/.codex/skills/<skill-name>/SKILL.md
```

Windows 示例：

```powershell
Copy-Item `
  -Path ".\skills-共享技能\kujiale-countertop" `
  -Destination "$HOME\.codex\skills\kujiale-countertop" `
  -Recurse -Force
```

安装后可显式调用：

```text
$kujiale-countertop
```

也可以用业务问题触发，例如：

```text
台面有台下盆水槽孔时，按厚度生成工艺费虚拟模型。
```

## 注意

- Codex 使用 `SKILL.md` frontmatter 的 `name` 和 `description` 判断触发。
- `agents/openai.yaml` 提供 UI 展示信息，不承载核心知识。
- 修改 Skill 后运行仓库校验脚本。
