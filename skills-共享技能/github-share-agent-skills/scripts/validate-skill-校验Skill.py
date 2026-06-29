#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCED_CODE_PATTERN = re.compile(r"```.*?```", re.DOTALL)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md 缺少 YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter 未闭合")

    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"无效 frontmatter 行: {line}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["缺少 SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append("name 必须使用小写英文、数字和连字符")
    if name != skill_dir.name:
        errors.append("frontmatter name 必须与目录名一致")
    if not description:
        errors.append("缺少 description")
    if "TODO" in text:
        errors.append("SKILL.md 仍包含 TODO")

    for markdown in skill_dir.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        prose = FENCED_CODE_PATTERN.sub("", content)
        for target in LINK_PATTERN.findall(prose):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = (markdown.parent / target.split("#", 1)[0]).resolve()
            if not local_target.exists():
                errors.append(f"{markdown.name}: 本地链接不存在: {target}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验开放 Agent Skill")
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    errors = validate(skill_dir)
    if errors:
        print("Skill 校验失败：")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill 校验通过: {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
