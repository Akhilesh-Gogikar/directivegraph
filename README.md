# DirectiveGraph

> **Private incubation repository. Do not publish or announce yet.**

Path-specific execution traces for nested agent instruction files.

## Problem

Nested AGENTS.md, CLAUDE.md, skills, hooks, and vendor rules create file-specific precedence that developers cannot explain.

## MVP

- Scans root-to-target ancestry for documented Codex, Claude Code, Gemini CLI, and GitHub Copilot repository instruction filenames.
- Reports applied files/rules, documented same-directory Codex overrides, closer-source precedence candidates, and explicit reasons.
- Emits deterministic JSON, readable text, self-contained HTML, or Graphviz DOT without hosted services or dependencies.

## Quickstart

Python 3.10+ is the only requirement.

```sh
python3 -m directivegraph fixtures/03_override/src/main.py \
  --root fixtures/03_override --format text
python3 -m directivegraph fixtures/05_public_names/deep/src/task.py \
  --root fixtures/05_public_names --format html --output /tmp/directivegraph.html
python3 -m unittest discover -s tests -v
```

Five independent synthetic repositories under `fixtures/` exercise root-only, nested, override, mixed-vendor, and additional public-filename cases. See [docs/SEMANTICS.md](docs/SEMANTICS.md) for the exact claims this MVP does and does not make.

## Non-goals

- Another generic linter, prompt pack, skill marketplace, or agent harness.
- Model-based scoring of writing quality.
- Inventing undocumented vendor semantics.

## Limitations

- DirectiveGraph does not infer conflicts between natural-language instructions. A precedence edge is a candidate ordering, not a claim that a whole parent file disappears.
- The Markdown reader extracts lines; it is not a complete Markdown parser.
- Imports, user/global memory, hooks, skills, path-glob front matter, and generated settings are outside the MVP.
- Cross-vendor precedence is intentionally never inferred.

- Scope and exclusions: [SCOPE.md](SCOPE.md)
- Source/provenance log: [PROVENANCE.md](PROVENANCE.md)
- Initial execution plan: [docs/PLAN.md](docs/PLAN.md)

## Licensing

No public license is granted while this repository is private. Select an OSS license only after ownership and third-party provenance review.
