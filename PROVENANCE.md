# Provenance log

This repository must remain independently developed from public sources and synthetic fixtures.

## Rules

- Record every specification, dataset, fixture, snippet, dependency, and generated asset before it enters the repository.
- Prefer public primary sources and link the exact version or commit.
- Do not copy from private, partner, customer, or unpublished research repositories.
- Public visibility is not a copyright license; record applicable terms.
- Stop and request ownership review when provenance is uncertain.

## Sources

| Date | Source/version | Purpose | License or terms | Notes |
|---|---|---|---|---|
| 2026-08-16 | Project brief derived from public-landscape research | Initial scope only | Internal planning | No implementation or copied source |
| 2026-08-16 | [OpenAI Codex: AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) | Public `AGENTS.md` discovery and override filename semantics | Public documentation terms | Original implementation; no source copied |
| 2026-08-16 | [Anthropic Claude Code: memory](https://docs.anthropic.com/en/docs/claude-code/memory) | Public project-memory filenames and hierarchy | Public documentation terms | Original conservative subset |
| 2026-08-16 | [Gemini CLI: GEMINI.md](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md) | Public context filename and hierarchical loading | [Apache-2.0](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE) | No upstream code copied |
| 2026-08-16 | [GitHub Copilot: repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) | Public repository instruction path | GitHub documentation terms | Original conservative subset |
| 2026-08-16 | Repository `fixtures/01_root` through `fixtures/05_public_names` | First proof gate and regression tests | Original synthetic data | No real repository instructions or private/partner content |
| 2026-08-17 | [SPDX MIT License text](https://spdx.org/licenses/MIT.html) | Repository license | MIT | Copyright line supplied by repository owner |
| 2026-08-17 | [Python packaging specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/) | `pyproject.toml` metadata and console entry point | Public documentation terms | No third-party package source copied; runtime dependencies remain empty |
| 2026-08-17 | [GitHub Actions documentation](https://docs.github.com/en/actions) | Least-privilege CI and release automation | GitHub documentation terms | Original workflows; release is tag-triggered and does not publish registries |
| 2026-08-17 | Repository community and `docs/*.md` launch materials | Contribution, governance, support, privacy, accessibility, and launch guidance | Original project documentation | No private or partner material |
