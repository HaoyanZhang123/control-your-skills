#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""quick_validate.py — DSH skill 形态校验（零第三方依赖）

用法：
    python scripts/quick_validate.py <skill-dir>
    python scripts/quick_validate.py --self-test

只查形态，查不出内容好坏。退出码：0 全绿（可含 WARN）；1 有 FAIL。

为什么不依赖 PyYAML：本 skill 需要能在任何装了 python3 的机器上直接跑。
frontmatter 只解析 `key: value` 与 `key: "引号值"` 两种最常见形态，
够覆盖 DSH skill 的 frontmatter，也不会有解析器版本差异。
"""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# DSH 遇到这些驼峰键会抛错并跳过整个 skill（只在日志告警，模型侧看不到）
LEGACY_KEYS = ("disableModelInvocation", "modelInvocable", "userInvocable")
MAX_DESC = 1024
MAX_BODY_LINES = 150
FORBIDDEN_FILES = ("README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md")


def split_frontmatter(text):
    """返回 (dict, body, error)。只认文件开头的 --- ... --- 块。"""
    if not text.startswith("---"):
        return None, "", "文件开头没有 YAML frontmatter（第一行应为 ---）"
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, "", "frontmatter 未闭合（缺少第二行 ---）"
    data = {}
    for raw in lines[1:end]:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            return None, "", f"frontmatter 行不含冒号: {raw!r}"
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
            val = val[1:-1]
        data[key] = val
    body = "\n".join(lines[end + 1:])
    return data, body, None


def validate(skill_dir):
    """返回 (fails, warns)。空的 (fails) 即为通过。"""
    fails, warns = [], []
    p = Path(skill_dir)
    if not p.is_dir():
        return [f"不是目录: {p}"], warns

    skill_md = p / "SKILL.md"
    if not skill_md.is_file():
        return [f"缺少 SKILL.md: {skill_md}"], warns

    text = skill_md.read_text(encoding="utf-8")
    fm, body, err = split_frontmatter(text)
    if err:
        return [err], warns

    for legacy in LEGACY_KEYS:
        if legacy in fm:
            fails.append(
                f'frontmatter 用了驼峰键 "{legacy}"，DSH 会拒绝并跳过整个 skill；'
                "改用 kebab-case 形式 disable-model-invocation / user-invocable"
            )

    name = fm.get("name", "")
    desc = fm.get("description", "")
    if not name:
        fails.append("frontmatter 缺少 name")
    if not desc:
        fails.append("frontmatter 缺少 description（它是唯一的触发面）")

    if name:
        if not NAME_RE.match(name):
            fails.append(f'name 不是小写 kebab-case: "{name}"')
        if name != p.name:
            fails.append(f'name 与目录名不一致: name="{name}" 目录="{p.name}"')
    if desc and len(desc) > MAX_DESC:
        fails.append(f"description 超长: {len(desc)} > {MAX_DESC} 字符")

    body_lines = [l for l in body.splitlines() if l.strip()]
    if len(body_lines) > MAX_BODY_LINES:
        warns.append(
            f"正文 {len(body_lines)} 行 > {MAX_BODY_LINES}，考虑拆到 references/ 并在正文标清何时读"
        )
    if "TODO" in body or "[TODO" in body:
        warns.append("正文仍有 TODO 占位")

    for fname in FORBIDDEN_FILES:
        if (p / fname).is_file():
            fails.append(f"skill 目录里有 {fname}；附属文档属于仓库，不属于 skill")

    for sub in ("references", "scripts", "assets"):
        d = p / sub
        if d.is_dir() and not any(d.iterdir()):
            warns.append(f"{sub}/ 是空目录，删掉或放真东西")

    refs = re.findall(r"`(references/[^`]+)`", body)
    for r in sorted(set(refs)):
        if not (p / r).is_file():
            fails.append(f"正文引用了不存在的文件: {r}")

    return fails, warns


def self_test():
    """正反双向自测：好样本必须绿，坏样本必须红且点名原因。"""
    import tempfile

    good = """---
name: sample-skill
description: 做一件具体的事。Use for 触发词; not for 别的事.
---

# sample-skill

## 正文

1. 一步。
"""
    cases = [
        ("好样本", good, "sample-skill", True, None),
        ("无 frontmatter", "# 只有正文\n", "sample-skill", False, "没有 YAML frontmatter"),
        (
            "驼峰键",
            '---\nname: sample-skill\ndescription: x\ndisableModelInvocation: true\n---\nbody\n',
            "sample-skill",
            False,
            "disableModelInvocation",
        ),
        (
            "name 与目录不一致",
            '---\nname: other-name\ndescription: x\n---\nbody\n',
            "sample-skill",
            False,
            "与目录名不一致",
        ),
        (
            "缺 description",
            "---\nname: sample-skill\n---\nbody\n",
            "sample-skill",
            False,
            "缺少 description",
        ),
        (
            "引用了不存在的参考文件",
            '---\nname: sample-skill\ndescription: x\n---\n见 `references/missing.md`\n',
            "sample-skill",
            False,
            "不存在的文件",
        ),
        (
            "skill 里有 README",
            '---\nname: sample-skill\ndescription: x\n---\nbody\n',
            "sample-skill",
            False,
            "README.md",
        ),
    ]

    ok = 0
    with tempfile.TemporaryDirectory() as tmp:
        for label, content, dirname, should_pass, expect in cases:
            d = Path(tmp) / dirname
            if d.exists():
                import shutil

                shutil.rmtree(d)
            d.mkdir(parents=True)
            (d / "SKILL.md").write_text(content, encoding="utf-8")
            if label == "skill 里有 README":
                (d / "README.md").write_text("x", encoding="utf-8")

            fails, warns = validate(d)
            passed = not fails
            detail = "; ".join(fails) if fails else "无 FAIL"
            hit = (expect is None) or any(expect in f for f in fails)
            verdict = "PASS" if (passed == should_pass and hit) else "FAIL"
            if verdict == "PASS":
                ok += 1
            print(f"[{verdict}] {label}: 期望{'绿' if should_pass else '红'}"
                  f"（{'命中' if hit else '未命中'}{expect or ''}）→ {detail}")

    print(f"\n自测 {ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 1
    if args[0] == "--self-test":
        return self_test()
    total_fail = 0
    for target in args:
        fails, warns = validate(target)
        print(f"=== {target}")
        for w in warns:
            print(f"  WARN  {w}")
        for f in fails:
            print(f"  FAIL  {f}")
        if not fails and not warns:
            print("  OK    形态检查全绿")
        total_fail += len(fails)
    print(f"\nFAIL {total_fail}")
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
