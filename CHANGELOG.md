# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。
每个版本的记录都是**完整中文段 + 完整英文段**，不逐句对照。

## [0.4.0] - 2026-11-11

### 中文

**新增**

- `skill-creator`：写 DSH skill 的方法。先判断一件事该不该做成 skill，再按 DSH 真实加载方式拆成 `SKILL.md`、`references/`、`scripts/`、`assets/`。核心是三条：简洁优先、信息只住一处、按任务脆弱程度给自由度。
- 其中一条是踩过坑才写进去的：frontmatter 用驼峰 `disableModelInvocation` / `modelInvocable` / `userInvocable` 会让 DSH 直接跳过整个 skill，而且**只在日志告警**——模型侧看起来就是"这个 skill 没装"，很难查。
- `scripts/quick_validate.py`：零第三方依赖的形态校验，查 frontmatter 与目录名是否一致、驼峰键、description 长度、正文体量、空目录、`references/` 引用是否存在、skill 目录里是否混进 README 类附属文档。带 `--self-test`，七条正反样本全部断言。
- 两份按需读的参考：`references/workflows.md`（顺序与分支流程写法）、`references/output-patterns.md`（严格模板与示例对）。

**变更**

- `github-repository-presentation` 瘦身：两段共 60 行的 README 固定结构示意挪到 `references/readme-template.md`，正文只留"真要落笔写 README 时再打开"的指路句。SKILL.md 从 165 行降到 110 行，规则本身一字未删。
- `assets/cover.png` 重画为四张技能卡，与新增的 skill 对应。

**说明**

- `skill-creator` 改编自 Anthropic 的 skill-creator（Apache-2.0）。改写为 DSH 原生形态：去掉 DSH 不存在的 `.skill` 打包步骤、把依赖 PyYAML 的校验器换成零依赖实现、正文按 DSH 的技能发现与调用规则重写。原文许可证随 skill 目录原样分发，来源记进 `NOTICE`。

### English

**Added**

- `skill-creator`: how to write a DSH skill. Decide first whether something should be a skill at all, then split it into `SKILL.md`, `references/`, `scripts/` and `assets/` the way DSH actually loads them. Three principles run through it: stay concise, keep every fact in exactly one place, and match the degree of constraint to how fragile the task is.
- One rule is in there because it bit us: camelCase `disableModelInvocation` / `modelInvocable` / `userInvocable` in the frontmatter makes DSH skip the whole skill, and it only warns **in the log** — from the model's side it just looks like the skill is not installed.
- `scripts/quick_validate.py`: a zero-dependency format check covering frontmatter and directory-name agreement, the camelCase keys, description length, body size, empty directories, dangling `references/` links, and README-style documents inside a skill folder. It ships with `--self-test` and seven positive/negative assertions.
- Two on-demand references: `references/workflows.md` for sequential and branching flows, `references/output-patterns.md` for strict templates and example pairs.

**Changed**

- `github-repository-presentation` slimmed down: the two README skeleton blocks (60 lines together) moved to `references/readme-template.md`, leaving one sentence in the body pointing at them for when you actually sit down to write a README. `SKILL.md` went from 165 to 110 lines; no rule was removed.
- `assets/cover.png` redrawn as four skill cards to match the new skill.

**Notes**

- `skill-creator` is adapted from Anthropic's skill-creator (Apache-2.0) and rewritten for DSH: the `.skill` packaging step DSH does not have is gone, the PyYAML-dependent validator is replaced with a zero-dependency one, and the text follows DSH's own discovery and invocation rules. The original license ships unchanged inside the skill folder, and the provenance is recorded in `NOTICE`.

## [0.3.0] - 2026-11-09

### 中文

**新增**

- `paper-figure-audit`：论文配图的去 AI 味规则。它只处理"图里不该有的东西"——替作者说话的结论句、替作者辩护的免责与方法声明、装饰、幻灯片式结构、一套模板套所有图、以及生成幻觉（图像模型画数据图、编造的点与箭头、数据撑不住的平滑线）。
- 同一条判据贯穿全篇：**加进去的每一处都要能指向数据**。skill 明确不要求极简，图可以复杂、可以彩色、可以有主次面板。
- 边界写死：不判断统计方法与图型选择，不规定字号、尺寸、导出格式与裁切——这些交给目标期刊说明或本机的图表审计工具。
- 一份交图前自检清单，和一份"删的时候别碰什么"的清单（n、单位、轴题、图例、参考线、确实在编码信息的颜色与形状）。

**变更**

- 仓库定位从"发版与仓库呈现"扩为日常 DSH skill 合集；两份 README 的标题、简介、技能表、使用示例、仓库结构与许可证说明同步更新。
- `assets/cover.png` 重画，封面改为三张技能卡。
- `NOTICE` 区分来源：前两个 skill 源自 `dsh-agent-team-presets`，`paper-figure-audit` 为本仓库原创。

### English

**Added**

- `paper-figure-audit`: an anti-AI-tell ruleset for manuscript figures. It only touches what should not be in the plot — conclusion sentences that argue for the author, disclaimers and method statements that defend them, decoration, slide-like structure, one template reused everywhere, and fabrication (image models drawing data figures, invented points and arrows, smoothing lines the data cannot support).
- One judgement runs through the whole skill: **every element added to a figure must point back to the data**. The skill explicitly does not ask for minimalism; figures may be complex, colourful, and have a hero panel.
- Boundaries are fixed in the text: it does not judge statistics or chart choice, and does not set font size, physical dimensions, export format or cropping — those belong to the target journal or a local figure-audit tool.
- A pre-submission self-check list, and a "do not delete these" list (n, units, axis titles, legends, reference lines, colours and shapes that genuinely encode information).

**Changed**

- Repository scope widened from release and presentation to a personal DSH skill collection; titles, intros, the skill table, usage examples, repository layout and licence notices in both READMEs were updated to match.
- `assets/cover.png` redrawn as three skill cards.
- `NOTICE` now separates provenance: the first two skills come from `dsh-agent-team-presets`; `paper-figure-audit` is original to this repository.

## [0.2.0] - 2026-10-30

### 中文

**新增**

- 仓库封面 `assets/cover.png`，两份 README 顶部同步展示。
- `github-repository-presentation` 的真实功能截图规范：按需要在 Usage、Features、Configuration 等章节配图，主 README 默认 0–5 张，复杂流程、多个核心界面或长文档确有需要时才增加。
- 截图取材授权、敏感信息清理、仓库相对路径、窄屏适配、双语 `alt` 与图注，以及对应的完成前核对要求。

### English

**Added**

- Repository cover `assets/cover.png`, shown at the top of both READMEs.
- Real-screenshot guidance for `github-repository-presentation`: add images to Usage, Features, Configuration and other sections only when they improve understanding. The default is 0–5 functional screenshots per main README, with more only for genuinely complex workflows, multiple core interfaces or long documents.
- Rules for source authorization, sensitive-data removal, repository-relative paths, narrow-screen readability, language-specific alt text and captions, plus matching pre-delivery checks.

## [0.1.0] - 2026-10-30

### 中文

初始版本：把两个日常在用的 DSH skill 收进仓库，并给出可复现的安装方式。

**新增**

- `git-release-hygiene`：按真实仓库状态整理 Commit、PR、Changelog、版本号、Tag 与 Release 的纪律，包含中英双语的发布文案规范。
- `github-repository-presentation`：GitHub 仓库首页的统一双语骨架，覆盖封面、徽章、Description、Topics 与 Release Notes 的表达。
- 中英两份 README 与 Windows 目录联接安装说明（含复制备选与回滚步骤）。

### English

Initial release: the two DSH skills I use every day, plus a reproducible install path.

**Added**

- `git-release-hygiene`: discipline for commits, PRs, changelogs, versioning, tags and releases driven by the real repository state, including the bilingual release-text convention.
- `github-repository-presentation`: one bilingual skeleton for the repository home page, covering cover, badges, description, topics and release-note wording.
- English and Chinese READMEs with a Windows junction install guide (copy fallback and rollback included).
