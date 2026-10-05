# Changelog

All notable changes are recorded here. The project follows semantic versioning for its documented CLI and report contracts after the stability boundaries in [docs/API_STABILITY.md](docs/API_STABILITY.md).

## [Unreleased]

## [0.1.1] — 2026-10-05

No CLI or report-format changes; the `directivegraph.report.v1` contract is unchanged.

### Changed

- Added community, security, packaging, CI, release, privacy, and accessibility documentation for public contributors.
- Moved the repository to `Akhilesh-Gogikar`, kept maintainer launch planning out of the repository, and listed related tools only after they are public.
- Refreshed the social preview for 0.1.1.
- Updated pinned CI actions (`actions/checkout` 7.0.1, `actions/setup-python` 7.0.0).

### Fixed

- Documented that symlinked instruction files are currently followed, including targets outside `--root` (tracked in #7), in the semantics, security, privacy, and architecture docs.
- Documented that Claude Code sources also receive closer-source candidate edges, and that Claude Code and Gemini CLI edges record position rather than a documented closer-wins rule.

## [0.1.0] — 2026-08-17

### Added

- Conservative discovery for documented repository instruction filenames.
- Applied/shadowed explanations with per-format precedence-candidate edges.
- Deterministic JSON, text, DOT, and self-contained HTML reports.
- Five synthetic nested repositories and stdlib tests.

[Unreleased]: https://github.com/Akhilesh-Gogikar/directivegraph/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/Akhilesh-Gogikar/directivegraph/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Akhilesh-Gogikar/directivegraph/releases/tag/v0.1.0
