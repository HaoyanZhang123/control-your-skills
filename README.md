<p align="center">
  <img src="assets/cover.png" alt="control-your-skills cover" width="100%">
</p>

<h1 align="center">control-your-skills</h1>

<p align="center">Seven DeepSeek Harness skills for work that has to hold up in public — reading what the user actually meant, Git release discipline, repository presentation, figures that only show data, legends that stand on their own, academic prose with no machine tells, and skills written to a standard.</p>

<p align="center"><a href="README.zh.md">中文</a></p>

<p align="center">
  <a href="https://github.com/deepseek-ai/deepseek-harness"><img alt="DeepSeek Harness" src="https://img.shields.io/badge/DeepSeek_Harness-skill-4B6BFB"></a>
  <a href="https://git-scm.com/doc"><img alt="Git" src="https://img.shields.io/badge/Git-workflow-F05032"></a>
  <a href="https://docs.github.com/en/repositories"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-releases-181717"></a>
  <a href="https://www.markdownguide.org/"><img alt="Markdown" src="https://img.shields.io/badge/Markdown-SKILL.md-1F6FEB"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2EA043"></a>
  <a href="https://github.com/HaoyanZhang123/control-your-skills/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/HaoyanZhang123/control-your-skills?color=2EA043"></a>
</p>

## Overview

This repository is the home of the skills I use with [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). Each skill is a single `SKILL.md`: DSH discovers it from a skills directory and loads it when a task matches its description. There is no build step, no package manager and no runtime dependency.

The set starts from the request itself — what the user meant when the words were vague, wrong or half-formed (`intent-alignment`) — then covers getting work out the door and keeping it legible afterwards: changes leave the working tree safely and with readable release text (`git-release-hygiene`); the repository explains itself to a first-time visitor (`github-repository-presentation`); manuscript figures carry no AI tells while the plotting itself stays unconstrained (`paper-figure-audit`); the legend layer is handled separately, because what a caption may say is a different question from how to draw (`figure-legend`); drafting, polishing and de-AI rewriting share one evidence discipline (`academic-writing-suite`); and new skills get built the way DSH actually loads them (`skill-creator`).

## Skills

| Skill | What it does | Use it when |
|---|---|---|
| [`intent-alignment`](skills/intent-alignment/SKILL.md) | Recovers what the user actually meant instead of what the words literally say: reads the context and the project before acting, separates confirmed requirements from its own guesses, and lowers uncertainty by investigating, explaining concepts, comparing options and trying small reversible samples before asking anyone. Asks only where a wrong guess would change the result. | The request is vague, mis-worded or contradictory, the user cannot say what they want yet, or a delivered result came back as "that's not it" without a reason. Not for clear requests — those run straight through. |
| [`git-release-hygiene`](skills/git-release-hygiene/SKILL.md) | Organizes commits, PRs, changelogs, version numbers, tags and releases from the real Git state. Release and changelog text is written as a complete Chinese block followed by a complete English block. | You are about to commit, open a PR, bump a version, cut a tag, or publish a release. |
| [`github-repository-presentation`](skills/github-repository-presentation/SKILL.md) | Applies one bilingual README skeleton, visual system and wording rules to a GitHub repository, keeps description, topics, badges and release notes consistent, and guides the use of real screenshots for features and workflows. | You are writing or rewriting a repository home page, cover, feature screenshots, badges, description or topics. |
| [`paper-figure-audit`](skills/paper-figure-audit/SKILL.md) | Removes the AI tells from a manuscript figure — text that argues or defends inside the plot, decoration, slide-like structure, one template reused everywhere, fabricated detail — and leaves chart choice, statistics and typography alone. | You are drawing, revising or reviewing a paper figure, or self-checking figures before submission. |
| [`figure-legend`](skills/figure-legend/SKILL.md) | Governs the legend layer: a noun-phrase title with no conclusions or numbers, one sentence per panel, the four statistics items collected into the caption, self-sufficiency away from the body text, tense split in English captions, Chinese caption conventions, and the permission string required when reusing a published figure. | You are writing, revising or reviewing a figure caption, or checking display items before submission. |
| [`academic-writing-suite`](skills/academic-writing-suite/SKILL.md) | The full academic writing workbench: drafting sections and argument from supplied evidence, restructuring a whole manuscript, compressing, Chinese-to-English translation and language polishing, de-AI rewriting, terminology and number consistency sweeps, and first-submission materials. Carries the write-the-introduction-twice sequencing, a mechanical style gate that can actually be run, and change-impact classes that say which sections a single edit reopens. | You are drafting or rewriting a manuscript section, polishing a finished draft, removing machine tells from academic prose, or assembling a submission package. |
| [`skill-creator`](skills/skill-creator/SKILL.md) | Decides whether something should be a skill at all, then splits it into `SKILL.md`, `references/`, `scripts/` and `assets/`, writes the description that actually triggers it, sets the right degree of freedom, and validates the result with a zero-dependency script. | You are creating a new skill, refactoring an overgrown `SKILL.md`, adding references or scripts to an existing one, or auditing a skill against the format. |

All seven skills are written for Chinese-speaking work: their trigger descriptions and rule text are Chinese, while the documents they produce (README, release notes, manuscript prose) follow the task's language. No English edition of the skill text is included yet.

## Installation

Requirements: a DSH build that loads filesystem skills, and the directory DSH scans for user skills (`<DSH_HOME>/skills`). Each skill must sit directly under that directory, one folder per skill.

Cloning once and linking each skill keeps a single source of truth: edits, `git pull` and new releases take effect without copying files.

```powershell
# 1) clone once
git clone https://github.com/HaoyanZhang123/control-your-skills.git "$HOME\control-your-skills"

# 2) link every skill into the DSH skills directory
$repo = "$HOME\control-your-skills\skills"
$dsh  = Join-Path $env:DSH_HOME "skills"
Get-ChildItem $repo -Directory | ForEach-Object {
    New-Item -ItemType Junction -Path (Join-Path $dsh $_.Name) -Target $_.FullName
}
```

Windows directory junctions do not require administrator rights. If a real folder with the same name already exists (for example a local editable copy of a skill), move it aside first; the link cannot overwrite it.

If you prefer plain copies, copy `skills\<name>\` into the DSH skills directory instead of linking, and re-copy when you want an update.

After adding or removing a skill, open a new DSH session so the skill catalog is rebuilt; the `/` menu may need a page refresh before the new skill appears there. Editing an already loaded skill takes effect without a restart.

Rollback: delete the junction (`Remove-Item "<DSH_HOME>\skills\<name>"`) and restore the folder you moved aside.

## Usage

DSH loads a skill when the task matches its description; you can also name a skill explicitly.

```text
这轮改动整理成两个 commit，再补 CHANGELOG 和 Release 说明
→ git-release-hygiene

按我的规范把 README 重写成中英两份，再给 Description 和 Topics
→ github-repository-presentation

这张图里的指标框和结论句该不该留，帮我去掉 AI 味
→ paper-figure-audit

这两个面板的图注帮我改一下，总题别写结论
→ figure-legend

把这段引言重写一遍，再顺手按我的机械门禁过一遍
→ academic-writing-suite

这个 SKILL.md 太长了，帮我拆到 references，再写 description
→ skill-creator

我也说不清这版哪里不对，反正就是不像我要的
→ intent-alignment
```

The skills were extracted from daily use, so they encode opinions rather than handle every workflow: they follow an existing project convention when there is one, and only fall back to a proposal when there is none. The figure skill in particular stays deliberately narrow — it removes AI tells and does not police chart type, statistics or typography. The legend lives in its own skill because "what a caption may say" is a different question from "how to draw". Drafting, polishing and de-AI rewriting share one skill because they share one evidence discipline; splitting them would let the three rule sets drift apart.

## Repository layout

```text
control-your-skills/
├─ skills/
│  ├─ intent-alignment/
│  │  ├─ SKILL.md
│  │  └─ references/exploration-methods.md
│  ├─ git-release-hygiene/SKILL.md
│  ├─ github-repository-presentation/
│  │  ├─ SKILL.md
│  │  └─ references/readme-template.md
│  ├─ paper-figure-audit/SKILL.md
│  ├─ figure-legend/SKILL.md
│  ├─ academic-writing-suite/
│  │  ├─ SKILL.md
│  │  └─ references/
│  │     ├─ drafting.md
│  │     ├─ polishing.md
│  │     └─ de-ai.md
│  └─ skill-creator/
│     ├─ SKILL.md
│     ├─ references/workflows.md
│     ├─ references/output-patterns.md
│     ├─ scripts/quick_validate.py
│     └─ LICENSE.txt
├─ assets/               # cover image and its generator (build_cover.py, Pillow)
├─ README.md            # English (this file)
├─ README.zh.md         # 中文镜像
├─ CHANGELOG.md
├─ AGENTS.md            # conventions for adding a skill
├─ NOTICE
└─ LICENSE
```

## Updating

- Linked install: run `git pull` in the cloned repository. The next DSH session reads the new text; no reinstall step.
- Copied install: copy `skills\<name>\` again.
- If a DSH upgrade or a plugin reinstall replaces the junction with a real folder, re-run the linking step. Nothing is lost — the repository still holds the content.

## License

[MIT](LICENSE). The first two skills started as skill documents in another project; see [NOTICE](NOTICE) for that record. `paper-figure-audit`, `figure-legend` and `intent-alignment` were written for this repository. `skill-creator` is adapted from Anthropic's skill-creator (Apache-2.0), rewritten for DSH; its license text ships inside the skill folder. `academic-writing-suite` adapts the de-AI rules, the introduction-twice sequencing and style gate, and the change-impact classes from three MIT projects, all recorded in [NOTICE](NOTICE).
