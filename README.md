# 酷家乐工艺编辑器 AI 脚本知识库

面向酷家乐技术人员的 Agent Skills 共享仓库，用于沉淀经过真实方案、日志和输出结果验证的工艺编辑器脚本经验，并在 Codex、Claude Code、TRAE 等 AI 工具中复用。

## 设计原则

1. 按业务领域维护 Skill，不按人员维护。
2. 每条成功经验必须包含触发入口、业务模块、依赖对象、完整脚本、验证记录和限制。
3. 核心知识只维护一份，使用开放 Agent Skills 格式。
4. 先记录运行证据，再总结规律；推断不能标记为成功案例。
5. 公开仓库禁止提交客户数据、账号、凭证、完整内部日志和企业专属商品 ID。

## 仓库结构

```text
skills-共享技能/
├─ kujiale-countertop/
├─ kujiale-design-postprocess/
├─ kujiale-rule-check/
├─ kujiale-order-postprocess/
├─ kujiale-drawing/
└─ kujiale-common-debug/

platform-guides-AI工具接入/
├─ codex-Codex接入.md
├─ claude-code-ClaudeCode接入.md
└─ trae-TRAE接入.md

templates-贡献模板/
├─ case-template-成功案例模板.md
└─ skill-template-Skill模板.md

scripts-工具脚本/
└─ validate-skills-校验技能.py
```

## 文件命名

一般文件采用：

```text
english-slug-中文说明.md
```

机器约定文件必须保留固定名称：

```text
SKILL.md
README.md
AGENTS.md
CLAUDE.md
agents/openai.yaml
```

Skill 目录保持小写英文和连字符，确保不同 AI 工具能稳定识别；中文说明写入 Skill 的标题、描述和参考文件名。

## 使用

从 `skills-共享技能/` 选择需要的 Skill，按对应平台接入说明安装。Claude Code 和 TRAE 均支持开放 Agent Skills；Codex 使用相同的 `SKILL.md` 核心格式，并可读取 `agents/openai.yaml` 扩展元数据。

## 贡献

先阅读 [CONTRIBUTING-贡献指南.md](CONTRIBUTING-贡献指南.md) 和 [SECURITY-安全与脱敏规范.md](SECURITY-安全与脱敏规范.md)，再使用成功案例模板提交 PR。

## 当前首个已验证案例

[台下盆按台面厚度生成虚拟五金](skills-共享技能/kujiale-countertop/references/cases-成功案例/sink-bottom-virtual-hardware-台下盆按厚度生成虚拟五金.md)
