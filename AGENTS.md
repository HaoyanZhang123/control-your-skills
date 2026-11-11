# AGENTS.md — control-your-skills

> 给 AI 与人的同一份维护规则，只写在别处看不出来的约定。

## 这是什么

个人自用的 DeepSeek Harness（DSH）skill 集合。`skills/<name>/SKILL.md` 是唯一事实源；
本机 `<DSH_HOME>/skills/<name>` 是指向这里的目录联接，所以**改这里 = 改 DSH**。

## 加一个 skill

1. 新建 `skills/<kebab-case-name>/SKILL.md`，目录名与 frontmatter 的 `name` 必须一致。
2. frontmatter 只写 DSH 认的键：`name`、`description`（必填），必要时 `whenToUse`。
   `description` 是唯一触发面，写清「做什么 + 什么时候用 + 不适用什么」。
3. **不写 `manifest.yaml`、不建 `static/`**：那是工厂仓（skill开发）的重型骨架，本仓只用
   DSH 原生单文件格式，保证任何 agent 运行时都能直接读。
4. 需要附属文件时，只允许 `references/`（按需读）与 `scripts/`（可执行而不必读入）；
   确有产物素材时才加 `assets/`。不做 `.skill` 打包，不做安装脚本。
5. 两份 README 的 skill 表同步加一行；CHANGELOG 记一条；升版 + tag + Release。
6. 安装/更新只用目录联接或复制，不引入包管理器、不写安装脚本。

写法本身见 `skills/skill-creator/`；新增或改动后用
`python skills/skill-creator/scripts/quick_validate.py skills/<name>` 自检形态。

## 发版

- 版本是**仓库级** SemVer（`v0.1.0`）；skill 文件内不写版本号，避免两处漂移。
- 文案：每版**完整中文段在前、完整英文段在后**，不逐句对照（规则见 `git-release-hygiene`）。
- 顺序：改 CHANGELOG → commit → `git tag` → GitHub Release（正文不重复版本大标题）。
- 封面未就位前，README 不写图片标签，也不放占位图。

## 边界

- 不虚构能力、命令、徽章链接或验证记录；没跑过的就写「未验证」。
- 不在两个 README 里写不同的内容；英文为主文件，中文是完整镜像。
