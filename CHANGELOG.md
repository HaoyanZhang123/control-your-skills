# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。
每个版本的记录都是**完整中文段 + 完整英文段**，不逐句对照。

## [0.6.0] - 2026-11-18

### 中文

**新增**

- `academic-writing-suite`：学术写作的完整工作台，把起草、润色与去 AI 味三件事放在同一份文档里。三者的交付物不同，但共用同一套证据纪律——先建术语台账与证据清单，再判断改动属于哪一级（语义契约 / 证据方法 / 元数据 / 表层），因为改一处要重开哪些章节是由分级决定的，不是凭感觉。
- 起草这一侧写进去两条硬流程：**引言写两遍**——先写一份会被丢弃的 Draft 0，用它约束评测，等证据齐了再从零重写最终引言，只承诺证据支持的事；以及**先写主题句再填段落**，主题句连不成一篇文章就不填。
- 润色这一侧的核心是「诊断先于改写」：先判十二类失败模式，再按 `论文类型 → 章节任务 → 证据摆放 → 段落必要性 → claim/证据/边界 → 句子润色` 的优先级链修。判错失败模式，后面所有修改都白做。
- 去 AI 味这一侧留了四条学术专有禁令：反价值声明、反元评论、反总括—分述模板、反堆砌。同时写清了**不许动的东西**——边界句删掉不会让文字更自然，只会让主张变强。修改阈值是宁缺毋滥，原文已经自然就保留原文并写明检测通过。
- `references/drafting.md`：引言快漏斗六步与缺口写法诊断表、论证脊、章节职责矩阵、重构四动作、段落三形状、Results 三种主线形状、主张升级的四个合法手段、摘要五种骨架与数字准入测试、结论四要素、首次投稿包、拒稿风险自审十问。
- `references/polishing.md`：十二类失败模式、三轴路由、反向提纲、衔接判据、语体护栏、过度断言清单、phrasebook 式的功能家族表、中译英六条修复模式、压缩顺序、全文清扫的问题表格式。
- `references/de-ai.md`：四条禁令的具体改法与反例、不许动的清单、语体尺度表、改写后自检。
- `figure-legend`：图注单独成 skill。总题只放名词短语、结论式动词与数值都不进去；一个面板一句；n、离散度定义、检验、多重比较四件事收在图注里，正文不再重复交代；图注必须脱离正文可读；英文图注描述图中事实用现在时、样本制备用过去时；复用他人图版必须附授权串，没有就标 `[待确认]` 而不是编一个。
- 图注之所以分开，是因为「图里不该有句子」和「图注该怎么写」是两个问题：`paper-figure-audit` 管前者，`figure-legend` 管后者，两者的边界在 description 里互相点名。
- `assets/build_cover.py`：封面从手绘改成了脚本生成。改文案不用再修图，改常量重跑即可。

**变更**

- `assets/cover.png` 重画：从五张技能卡改为 1600×420 的纯品牌图，只留标记、`DSH / DEVELOPER TOOLKIT` 眉题、仓库名与一条下划线。技能列表本来就在 README 的表格里，图上再列一遍是两处维护同一事实。
- 两份 README 的技能表从五行扩到七行，`alt`、简介、使用示例、仓库结构与许可证说明同步；封面 `alt` 简化为仓库名，理由同上。
- `NOTICE` 补记三条上游出处：`academic-writing-suite` 的去 AI 味规则改编自 `kipozannaki/Reduce-AI-Text`（MIT），引言写两遍与机械语体门禁改编自 `snl-ucsb/paper-writing-skill`（MIT），变更影响分级改编自 `WenyuChiou/academic-writing-skills`（MIT）。三者均按 DSH 单文件格式重写并合并，未分发上游文件。选源时排除了 `Imbad0202/academic-research-skills`：它的 CC-BY-NC 许可与本仓库的 MIT 不兼容。
- `AGENTS.md` 补一条：`SKILL.md` 控制在 150 行内，细节进 `references/`，并在正文标清什么条件下读哪一份——不写清楚，拆出去等于丢了。

**移除**

- 本仓库不再包含 `academic-figure`、`academic-review`、`academic-slides`、`academic-polish`、`academic-writing` 这五个此前从插件工厂项目蒸馏的 skill。它们的核心内容并入了上述两个新 skill，重型结构（`manifest.yaml` 四轴路由 + `static/fragments`）按本仓库既有的单文件约定压平。`academic-figure` 的几何判据（字号 5–7pt、面板容差 1.5pt、导出契约）没有并入：`paper-figure-audit` 的定位是不评判字号与导出格式，并进去会与自己的边界声明冲突，因此该能力随之一并移除。

**验证**

- 七个 skill 全量通过 `skills/skill-creator/scripts/quick_validate.py`（`FAIL 0`），含 `--self-test` 的正反样本。
- 封面脚本 `python assets/build_cover.py` 可重复生成同一张图，产物 1600×420。
- **未验证**：`academic-writing-suite` 与 `figure-legend` 尚未在真实论文上跑过完整流程；三轴路由与机械门禁是规则层面的，没有对应的机检脚本；移除 `academic-figure` 后，字号与面板对齐检查需自行使用目标期刊说明或本机图表工具。

### English

**Added**

- `academic-writing-suite`: one workbench for academic writing that holds drafting, polishing and de-AI rewriting in a single document. The three produce different deliverables but share one evidence discipline: build the terminology ledger and the evidence list first, then classify every change (semantic contract, evidence or method, metadata, surface) — because which sections an edit reopens is decided by that class, not by feel.
- Two hard sequences are written into the drafting side. **Write the introduction twice**: a disposable Draft 0 sets the guardrails for the evaluation, and once the evidence exists the final introduction is rewritten from scratch, promising only what the evidence supports. **Write topic sentences before paragraphs**: if the topic sentences do not chain into one argument, do not fill in the paragraphs.
- The polishing side turns on "diagnose before rewriting": identify the failure mode first, then fix along the chain `paper type → section duty → evidence placement → paragraph necessity → claim/evidence/boundary → sentence`. Get the failure mode wrong and every later edit is wasted.
- The de-AI side keeps four rules specific to academic prose: no value declarations, no meta-commentary, no "overview then enumeration" template, no padding. It also states what must not be touched — deleting a boundary sentence does not make the prose more natural, it only makes the claim stronger. The rewriting threshold is "only when needed": prose that is already natural is kept, with an explicit pass note.
- `references/drafting.md`: the six-step introduction funnel with a gap-writing diagnostic table, the argument spine, the section-duty matrix, the four restructuring moves, three paragraph shapes, three shapes for Results, four legitimate ways to escalate a claim, five abstract skeletons with the number-admission test, the four conclusion elements, the first-submission package, and ten pre-submission rejection-risk questions.
- `references/polishing.md`: twelve failure modes, the three-axis routing, reverse outlining, transition criteria, style guardrails, the overclaiming list, a phrase bank organised by function rather than by replacement, six repairs for Chinese-to-English drafts, the compression order, and the problem-table format for a full sweep.
- `references/de-ai.md`: concrete rewrites and counter-examples for the four rules, the do-not-touch list, the register table by genre, and the post-rewrite self-check.
- `figure-legend`: captions get their own skill. The title is a noun phrase — conclusion verbs and numbers stay out; one sentence per panel; n, dispersion definition, test and multiple-comparison handling are collected into the caption and not repeated in the body; the caption must be readable away from the body; English captions use the present tense for what the figure shows and the past tense for sample preparation; reusing a published figure requires a permission string, and if there is none the answer is a `[待确认]` placeholder, not an invented one.
- Captions are separate because "the figure should not contain sentences" and "how a caption should be written" are different questions: `paper-figure-audit` owns the first, `figure-legend` owns the second, and each names the other in its description.
- `assets/build_cover.py`: the cover is now generated from a script instead of drawn by hand. Changing the wording no longer means editing an image.

**Changed**

- `assets/cover.png` redrawn: five skill cards replaced by a 1600×420 brand image carrying only the marker, a `DSH / DEVELOPER TOOLKIT` eyebrow, the repository name and an underline. The skill list already lives in the README table; repeating it in the image maintained one fact in two places.
- Both READMEs go from five skill rows to seven, with the cover `alt`, overview, usage examples, repository layout and licence notes updated to match; the cover `alt` is now just the repository name, for the same reason.
- `NOTICE` records three upstream sources for `academic-writing-suite`: the de-AI rules adapt `kipozannaki/Reduce-AI-Text` (MIT), the introduction-twice sequencing and the mechanical style gate adapt `snl-ucsb/paper-writing-skill` (MIT), and the change-impact classes adapt `WenyuChiou/academic-writing-skills` (MIT). All three were rewritten for the DSH single-file format and merged; no upstream files are redistributed. `Imbad0202/academic-research-skills` was excluded on licence grounds — CC-BY-NC is incompatible with this repository's MIT.
- `AGENTS.md` gains one rule: keep `SKILL.md` within 150 lines, move detail into `references/`, and state in the body when each reference is read — a split without that pointer loses the content.

**Removed**

- The repository no longer carries `academic-figure`, `academic-review`, `academic-slides`, `academic-polish` and `academic-writing`, five skills previously distilled from another project. Their substance was merged into the two new skills and the heavyweight structure (`manifest.yaml` four-axis routing plus `static/fragments`) was flattened to this repository's existing single-file convention. The geometric criteria from `academic-figure` (5–7pt type at final size, 1.5pt panel tolerance, export contract) were not carried over: `paper-figure-audit` is defined as not judging type size or export format, so folding them in would contradict its own boundary statement, and that capability is gone with it.

**Verification**

- All seven skills pass `skills/skill-creator/scripts/quick_validate.py` outright (`FAIL 0`), including its positive and negative self-test samples.
- `python assets/build_cover.py` regenerates the same 1600×420 image.
- **Not verified**: `academic-writing-suite` and `figure-legend` have not been run end to end on a real manuscript; the three-axis routing and the mechanical style gate are rules only, with no checking script behind them; with `academic-figure` removed, type size and panel alignment now depend on the target journal's instructions or a local figure tool.


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
