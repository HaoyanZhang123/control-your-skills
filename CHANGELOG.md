# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。
每个版本的记录都是**完整中文段 + 完整英文段**，不逐句对照。

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
