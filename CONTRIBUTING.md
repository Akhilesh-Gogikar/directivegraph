# Contributing to DirectiveGraph

DirectiveGraph explains documented instruction-file discovery without guessing at natural-language conflicts. Contributions should strengthen that conservative boundary.

## Before opening a change

1. Check [SUPPORT.md](SUPPORT.md), existing issues, and [docs/SEMANTICS.md](docs/SEMANTICS.md).
2. A new filename or precedence relation requires a public primary source, a synthetic nested fixture, and an explicit limitation.
3. Record new specifications, fixtures, dependencies, or assets in [PROVENANCE.md](PROVENANCE.md). Never copy private repository instructions.
4. Keep runtime dependencies at zero unless the maintainer approves a concrete, measured need.

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
