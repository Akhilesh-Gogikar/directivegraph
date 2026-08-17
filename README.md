# DirectiveGraph

[![CI](https://github.com/akigogikar/directivegraph/actions/workflows/ci.yml/badge.svg)](https://github.com/akigogikar/directivegraph/actions/workflows/ci.yml)
[![GitHub License](https://img.shields.io/github/license/akigogikar/directivegraph)](LICENSE)

![DirectiveGraph social preview: a hierarchy showing which instructions reach a file](docs/assets/social-preview.png)

**Ask one file which instructions reach it—and why.** DirectiveGraph turns a repository path into a conservative, source-linked precedence trace.

> **Status: 0.1.0 alpha.** Source installation is supported; no package registry publication has occurred. See the evidence and limitations in [docs/LAUNCH_KIT.md](docs/LAUNCH_KIT.md).

## Why

Nested instruction files create path-specific behavior that is difficult to explain. DirectiveGraph shows applicable sources, documented same-directory overrides, closer-source precedence candidates, extracted rules, and reasons—without pretending it understands natural-language conflicts.

## Install from source

Python 3.10–3.14 is supported. There are no runtime dependencies and no network calls at runtime.

```sh
python3 -m pip install .
```

## One-command demo

```sh
directivegraph fixtures/03_override/src/main.py \
  --root fixtures/03_override --format text
```

The synthetic demo reports `AGENTS.override.md` as applied and same-directory `AGENTS.md` as shadowed. Use `python3 -m directivegraph` without installing, or write accessible HTML in one command:

```sh
directivegraph fixtures/05_public_names/deep/src/task.py \
  --root fixtures/05_public_names --format html --output /tmp/directivegraph.html
```

## What makes it different

- **One target, one explanation:** the report is scoped to a specific path instead of dumping every instruction file.
- **Conservative by construction:** documented overrides are explicit; uncertain relationships remain precedence candidates.
- **Cross-format honesty:** each format is ordered independently and no cross-vendor precedence is invented.
- **Easy to inspect:** text, deterministic JSON, DOT, and self-contained HTML come from the same local analysis.

## Input and output

- Conservative root-to-target scanning for the documented filenames in [docs/SEMANTICS.md](docs/SEMANTICS.md).
- Explicit applied/shadowed reasons and per-format precedence-candidate edges.
- Deterministic `directivegraph.report.v1` JSON, readable text, Graphviz DOT, and accessible script-free HTML.
- Five synthetic repositories covering root, nested, override, mixed-format, and repository-wide cases.

## Non-goals and limitations

- Not a generic linter, prompt pack, marketplace, agent harness, or prompt assembler.
- No natural-language conflict inference or model-based scoring.
- No undocumented or cross-vendor precedence claims.
- Imports, user/global memory, hooks, skills, generated settings, and most path-glob instructions are outside `0.1.0`.
- The structural Markdown reader is deliberately not a complete Markdown parser.

## Documentation

- [Architecture](docs/ARCHITECTURE.md) · [semantics](docs/SEMANTICS.md) · [API stability](docs/API_STABILITY.md)
- [Privacy](docs/PRIVACY.md) · [accessibility](docs/ACCESSIBILITY.md) · [troubleshooting](docs/TROUBLESHOOTING.md)
- [Roadmap](ROADMAP.md) · [changelog](CHANGELOG.md) · [launch kit](docs/LAUNCH_KIT.md)
- [Scope](SCOPE.md) · [provenance](PROVENANCE.md) · [ecosystem](ECOSYSTEM.md) · [issue seeds](docs/ISSUE_SEEDS.md)

## A focused contribution is welcome

Start with one of the five code-aware [issue seeds](docs/ISSUE_SEEDS.md), add a synthetic ancestry case, or challenge a precedence claim with a public primary source. The [contribution pathways](CONTRIBUTING.md#contribution-pathways) explain scope, review expectations, and recognition. Please never upload private repository instructions.

## Community and security

Read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), [SUPPORT.md](SUPPORT.md), and [GOVERNANCE.md](GOVERNANCE.md) before participating. Report vulnerabilities through the private advisory route in [SECURITY.md](SECURITY.md), never a public issue.

Run the complete local check with:

```sh
python3 -m unittest discover -s tests -v
```

## License

[MIT](LICENSE) © 2026 Akhilesh Gogikar.
