# 在 AI 工具中套用 Skill

## Codex

个人 Skill：

```text
~/.codex/skills/<skill-name>/SKILL.md
```

安装整个目录，保留 `references/`、`scripts/` 和 `assets/`。

显式调用通常使用：

```text
$skill-name
```

## Claude Code

项目 Skill：

```text
.claude/skills/<skill-name>/SKILL.md
```

个人 Skill：

```text
~/.claude/skills/<skill-name>/SKILL.md
```

可通过：

```text
/skill-name
```

显式调用，也可由 `description` 自动触发。

## TRAE

进入：

```text
Settings -> Rule & Skills -> Skills -> Create
```

导入 Skill 目录中的 `SKILL.md`，并保留支持文件。TRAE 支持开放 Agent Skills，不需要把完整 Skill 改写成长驻 Rules。

## 其他工具

若支持开放 Agent Skills，直接导入整个 Skill 目录。

若仅支持项目规则：

1. 不复制全部参考资料到长驻规则；
2. 在规则中指向仓库的 `SKILL.md`；
3. 指示 AI 按需读取 `references/`；
4. 保留标准 Skill 作为唯一知识源。

## 更新

1. 在知识仓库执行 `git pull --ff-only`；
2. 对比本地已安装版本；
3. 重新安装整个 Skill 目录；
4. 验证目标工具能发现 Skill；
5. 不覆盖用户在目标目录中的未同步修改。
