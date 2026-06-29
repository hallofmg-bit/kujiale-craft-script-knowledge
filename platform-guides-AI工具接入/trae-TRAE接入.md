# TRAE 接入

TRAE 已支持开放 Agent Skills。每个 Skill 是包含 `SKILL.md` 的目录，可从 GitHub 下载后导入。

## 导入

1. 打开 TRAE。
2. 进入 `Settings -> Rule & Skills -> Skills -> Create`。
3. 选择本仓库某个 Skill 的 `SKILL.md`。
4. 保留同目录下的 `references/`，确保按需读取案例和排错资料。

推荐先导入：

```text
skills-共享技能/kujiale-countertop/SKILL.md
skills-共享技能/kujiale-common-debug/SKILL.md
```

官方说明：

```text
https://www.trae.ai/blog/trae_tutorial_0115
```

不要把整份知识库复制进长期 Rules。Skills 按需加载，更适合案例、流程和排错知识；Rules 只保留始终生效的团队约束。
