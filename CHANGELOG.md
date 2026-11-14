# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。
每个版本的记录都是**完整中文段 + 完整英文段**，不逐句对照。

## [0.5.0] - 2026-11-14

### 中文

**新增**

- `intent-alignment`：用户说得含糊、用词不准、前后要求冲突，或自己还没想清时，先还原真实意图再动手。核心是三条：理解优先于字面匹配；用户确认的要求、上下文支持的推断、Agent 自己的猜测分成三档，不把猜测写成需求；能自己查、自己解释、自己比较、自己试的就不要丢回给用户。
- 与常见「追问式澄清」的区别写在正文里：只在**猜错会明显改变结果**处提问，其余情况先自行降低不确定性；目标明确时直接交还执行工作流，不启动澄清仪式。
- 退出条件也写死了：目标足够明确、关键歧义已处理、授权清楚即退出；退出后不再追加确认态问题或提议范围外的新工作。
- `references/exploration-methods.md`：按需读的方法库。12 类不确定性诊断、六种探索方法（上下文意图重建、目标—手段拆分、抽象词翻译成可观察特征、差异方案与反例比较、诊断性反馈、可逆原型）、关键假设核查清单、8 个场景示例。

**变更**

- `assets/cover.png` 重画为五张技能卡，与新增的 skill 对应。
- 两份 README 的封面 `alt`、定位语、简介、技能表、使用示例、仓库结构与许可证说明同步为五个 skill；`NOTICE` 补记 `intent-alignment` 为本仓库原创。

**验证**

- 五个 skill 全量通过 `skills/skill-creator/scripts/quick_validate.py`（`FAIL 0`），含 `--self-test` 7/7 正反样本。
- 该 skill 做过 8 场景 × 有/无 skill 的 A/B 对照（同一小型项目副本、同一模型，各自真实落盘），覆盖术语歧义、指代歧义、抽象需求、事实缺口、规则冲突、主观反馈、明确任务、明确禁止改文件。**未验证**：长期使用中的实际协作收益、非中文场景下的表现、与其他 skill 同时触发时的优先级。

### English

**Added**

- `intent-alignment`: when the request is vague, mis-worded, self-contradictory, or the user has not decided yet, recover the real intent before acting. Three rules carry it: understanding beats literal matching; what the user confirmed, what the context supports and what the agent guessed are kept in three separate tiers, and a guess is never written up as a requirement; anything the agent can look up, explain, compare or try itself does not get handed back to the user.
- The difference from the usual "ask until it is clear" habit is written into the body: ask only where a wrong guess would visibly change the result; otherwise reduce the uncertainty first. When the request is already clear, hand it straight back to the normal workflow — no clarification ceremony.
- Exit conditions are explicit too: stop once the next step is clear, the key ambiguity is settled and authorization is known; after that, no confirmation-only questions and no out-of-scope proposals.
- `references/exploration-methods.md`: an on-demand method library — twelve kinds of uncertainty, six exploration methods (contextual intent reconstruction, goal-versus-means split, translating abstract words into observable features, contrasting options and counter-examples, diagnostic feedback, reversible prototypes), a key-assumption checklist, and eight worked scenarios.

**Changed**

- `assets/cover.png` redrawn as five skill cards to match the new skill.
- Both READMEs updated to five skills across the cover `alt`, tagline, overview, skill table, usage examples, repository layout and licence notes; `NOTICE` now records `intent-alignment` as original to this repository.

**Verification**

- All five skills pass `skills/skill-creator/scripts/quick_validate.py` outright (`FAIL 0`), including its `--self-test` with seven positive and negative samples.
- The skill went through an 8-scenario A/B comparison (with and without it, same small project copy, same model, each run actually writing to disk), covering terminology ambiguity, referential ambiguity, abstract requests, missing facts, rule conflicts, subjective feedback, clear tasks, and an explicit "do not touch files" instruction. **Not verified**: real-world collaboration gains over time, behaviour outside Chinese, and precedence when another skill triggers at the same time.


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
