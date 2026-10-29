<p align="center">
  <img src="assets/cover.png" alt="control-your-skills 封面：两个 DeepSeek Harness skill —— 发版纪律与仓库呈现" width="100%">
</p>

<h1 align="center">control-your-skills</h1>

<p align="center">两个 DeepSeek Harness skill：把交付做扎实的 Git 发版纪律，和让别人看得懂的仓库呈现。</p>

<p align="center"><a href="README.md">English</a></p>

<p align="center">
  <a href="https://github.com/deepseek-ai/deepseek-harness"><img alt="DeepSeek Harness" src="https://img.shields.io/badge/DeepSeek_Harness-skill-4B6BFB"></a>
  <a href="https://git-scm.com/doc"><img alt="Git" src="https://img.shields.io/badge/Git-workflow-F05032"></a>
  <a href="https://docs.github.com/en/repositories"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-releases-181717"></a>
  <a href="https://www.markdownguide.org/"><img alt="Markdown" src="https://img.shields.io/badge/Markdown-SKILL.md-1F6FEB"></a>
  <a href="LICENSE"><img alt="许可证：MIT" src="https://img.shields.io/badge/license-MIT-2EA043"></a>
  <a href="https://github.com/HaoyanZhang123/control-your-skills/releases"><img alt="最新版本" src="https://img.shields.io/github/v/release/HaoyanZhang123/control-your-skills?color=2EA043"></a>
</p>

## 简介

这个仓库放我日常在用的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（DSH）skill。每个 skill 就是一个 `SKILL.md`：DSH 从技能目录里发现它，任务与它的 description 匹配时加载。没有构建步骤，没有包管理器，也没有运行时依赖。

第一批收的是「交付」这件事的两端：把改动从工作区安全、诚实、可读地送出去（`git-release-hygiene`），以及把仓库首页讲清楚，让第一次来的人知道它是什么（`github-repository-presentation`）。

## 技能

| Skill | 做什么 | 什么时候用 |
|---|---|---|
| [`git-release-hygiene`](skills/git-release-hygiene/SKILL.md) | 依据真实 Git 状态组织 Commit、PR、Changelog、版本号、Tag 与 Release；发布文案写成完整中文段加完整英文段。 | 准备提交、开 PR、升版本、打 Tag、发 Release 时。 |
| [`github-repository-presentation`](skills/github-repository-presentation/SKILL.md) | 用同一套双语 README 骨架、视觉与措辞规则整理仓库首页，并让 Description、Topics、徽章与 Release Notes 保持一致。 | 写或重写仓库首页、封面、徽章、Description、Topics 时。 |

两个 skill 都面向中文工作流：触发描述与规则正文是中文，产出的文档（README、Release 说明）是中英双语。暂未提供英文版正文。

## 安装

前提：一个会从文件系统加载 skill 的 DSH，以及它扫描的用户技能目录（`<DSH_HOME>/skills`）。每个 skill 必须直接位于该目录下一层，一个 skill 一个文件夹。

只克隆一次、再把每个 skill 联接进去，可以保持单一事实源：改文件、`git pull`、发新版本都无需复制。

```powershell
# 1) 克隆一次
git clone https://github.com/HaoyanZhang123/control-your-skills.git "$HOME\control-your-skills"

# 2) 把每个 skill 联接进 DSH 技能目录
$repo = "$HOME\control-your-skills\skills"
$dsh  = Join-Path $env:DSH_HOME "skills"
Get-ChildItem $repo -Directory | ForEach-Object {
    New-Item -ItemType Junction -Path (Join-Path $dsh $_.Name) -Target $_.FullName
}
```

Windows 目录联接不需要管理员权限。如果同名实目录已存在（比如之前建过的可编辑副本），先把它挪走：联接不能覆盖已有目录。

不想用联接也可以直接复制：把 `skills\<name>\` 复制进 DSH 技能目录，需要更新时再复制一次。

新增或删除 skill 后，开一个新的 DSH 会话让技能目录重建；斜杠菜单可能需要刷新页面才会出现新条目。改动已加载 skill 的正文则无需重启。

回滚：删掉联接（`Remove-Item "<DSH_HOME>\skills\<name>"`），再把你挪走的目录放回去。

## 使用

任务与 description 匹配时 DSH 会自动加载 skill，也可以直接点名。

```text
这轮改动整理成两个 commit，再补 CHANGELOG 和 Release 说明
→ git-release-hygiene

按我的规范把 README 重写成中英两份，再给 Description 和 Topics
→ github-repository-presentation
```

这两个 skill 是从日常使用里抽出来的，带明显偏好：项目已有约定就沿用，没有再提建议，不强行套用某一种提交规范或版本策略。

## 仓库结构

```text
control-your-skills/
├─ skills/
│  ├─ git-release-hygiene/SKILL.md
│  └─ github-repository-presentation/SKILL.md
├─ README.md            # 英文主文件
├─ README.zh.md         # 中文（本文件）
├─ CHANGELOG.md
├─ AGENTS.md            # 新增 skill 的约定
├─ NOTICE
└─ LICENSE
```

## 更新

- 联接安装：在克隆下来的仓库里 `git pull`。下一个 DSH 会话读到新正文，不需要重装。
- 复制安装：重新复制 `skills\<name>\`。
- DSH 升级或插件重装把联接换成实目录时，重新跑一次联接步骤即可。内容不会丢——仓库里仍然有原文。

## 许可证

[MIT](LICENSE)。两个 skill 最初是另一个项目里的技能文档，来源记录见 [NOTICE](NOTICE)。
