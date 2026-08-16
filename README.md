# DirectiveGraph

> **Private incubation repository. Do not publish or announce yet.**

Path-specific execution traces for nested agent instruction files.

## Problem

Nested AGENTS.md, CLAUDE.md, skills, hooks, and vendor rules create file-specific precedence that developers cannot explain.

## Planned v0

- Parse documented instruction scopes for selected public agent formats.
- Answer which rule applies to a target file, which rule shadows it, and why.
- Render a source and precedence graph with cross-vendor differences.

## Non-goals

- Another generic linter, prompt pack, skill marketplace, or agent harness.
- Model-based scoring of writing quality.
- Inventing undocumented vendor semantics.

## Repository state

This repository contains only the clean-room project brief and planning scaffold. No implementation has started.

- Scope and exclusions: [SCOPE.md](SCOPE.md)
- Source/provenance log: [PROVENANCE.md](PROVENANCE.md)
- Initial execution plan: [docs/PLAN.md](docs/PLAN.md)

## Licensing

No public license is granted while this repository is private. Select an OSS license only after ownership and third-party provenance review.
