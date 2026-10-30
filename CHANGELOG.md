# Changelog

格式参考 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/lang/zh-CN/)。
每个版本的记录都是**完整中文段 + 完整英文段**，不逐句对照。

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
