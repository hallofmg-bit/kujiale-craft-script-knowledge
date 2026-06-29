#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCED_CODE_PATTERN = re.compile(r"```.*?```", re.DOTALL)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: 缺少 YAML frontmatter")

    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"{path}: frontmatter 未闭合")

    result: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip():
            continue
        if ":" not in raw_line:
            raise ValueError(f"{path}: 无效 frontmatter 行: {raw_line}")
        key, value = raw_line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def validate_links(text: str, path: Path) -> list[str]:
    errors: list[str] = []
    prose = FENCED_CODE_PATTERN.sub("", text)
    for target in LINK_PATTERN.findall(prose):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            errors.append(f"{path}: 本地链接不存在: {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: 缺少 SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    try:
        frontmatter = parse_frontmatter(text, skill_md)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{skill_md}: name 必须为小写英文、数字和连字符")
    if name != skill_dir.name:
        errors.append(f"{skill_md}: name 与目录名不一致")
    if not description:
        errors.append(f"{skill_md}: 缺少 description")
    if "TODO" in text:
        errors.append(f"{skill_md}: 仍包含 TODO")

    for markdown in skill_dir.rglob("*.md"):
        content = markdown.read_text(encoding="utf-8")
        errors.extend(validate_links(content, markdown))
    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"未找到 Skill 目录: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill 校验失败：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Skill 校验通过，共 {len(skill_dirs)} 个。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
