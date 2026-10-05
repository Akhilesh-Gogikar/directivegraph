# Contributing to DirectiveGraph

DirectiveGraph explains documented instruction-file discovery without guessing at natural-language conflicts. Contributions should strengthen that conservative boundary.

## Before opening a change

1. Check [SUPPORT.md](SUPPORT.md), existing issues, and [docs/SEMANTICS.md](docs/SEMANTICS.md).
2. A new filename or precedence relation requires a public primary source, a synthetic nested fixture, and an explicit limitation.
3. Record new specifications, fixtures, dependencies, or assets in [PROVENANCE.md](PROVENANCE.md). Never copy private repository instructions.
4. Keep runtime dependencies at zero unless the maintainer approves a concrete, measured need.

## Contribution pathways

Choose the smallest path that matches your context:

- **Docs and provenance:** clarify a semantic claim or attach a better public primary source.
- **Synthetic fixtures:** add a minimal ancestry/override case without copying a real repository.
- **Discovery and parsing:** work in `directivegraph/core.py` while keeping filesystem and Markdown behavior conservative.
- **Renderers and accessibility:** improve text, JSON, DOT, or script-free HTML without changing semantic claims.
- **Security and scale:** harden path, symlink, or large-tree behavior with explicit policy and regression tests.

The curated [issue seeds](docs/ISSUE_SEEDS.md) include likely files, acceptance criteria, and scope estimates. Comment on the intended issue before a change likely to exceed one day.

## Local workflow

```sh
python3 -m unittest discover -s tests -v
python3 -m directivegraph fixtures/03_override/src/main.py \
  --root fixtures/03_override --format text
```

Discovery or precedence changes need a deterministic fixture and regression test. HTML must remain self-contained and screen-reader/keyboard friendly. DOT output must remain deterministic and valid text. Run `git diff --check` before submitting.

## Pull requests

Keep a pull request focused. Explain the documented semantic being modeled, source provenance, cross-format implications, tests, and limitations. Maintainers will reject heuristic natural-language conflict resolution or undocumented cross-vendor precedence.

By contributing, you agree that your contribution is licensed under [MIT](LICENSE) and that you have the right to submit it.

## Contributor ladder

The ladder describes increasing responsibility, not status:

1. **Reporter:** provides a synthetic tree, public source, or documentation correction.
2. **Contributor:** lands a focused change with fixtures, tests, and provenance where needed.
3. **Regular contributor:** repeatedly improves a format or renderer, reviews related changes, and helps refine issues.
4. **Reviewer or maintainer:** is invited based on sustained technical judgment, conservative semantic review, and clean-room stewardship; permissions remain least-privilege.

No number of commits automatically grants access. Governance and final decisions remain as described in [GOVERNANCE.md](GOVERNANCE.md).

## Triage and recognition

Maintainers target an initial label or question within five business days and a first review of a ready, focused pull request within seven. These are goals, not service guarantees. `needs-triage` means scope is not confirmed; `good first issue` should be independently finishable; `help wanted` has agreed direction but needs an owner; `needs-design` or `advanced` needs design review before code; `status: ready` has acceptance criteria and can be claimed; `difficulty: *` and `size: *` estimate effort; `mentored` means a maintainer will guide the work.

Merged contributors are credited in the pull request and relevant changelog or release notes. Substantial design, fixture, accessibility, documentation, and review work should be credited alongside code. Contributors may opt out of public recognition.
