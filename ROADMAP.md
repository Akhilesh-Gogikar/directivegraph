# Roadmap

Roadmap items are intentions, not commitments.

## Scope and sequencing

The next release stays inside conservative, local root-to-target analysis:

1. **Safety and fixtures:** prevent output overwrite and add deterministic snapshots for all five synthetic repositories.
2. **Parser and filesystem policy:** improve wrapped-list handling and define symlink behavior without guessing.
3. **Format breadth:** consider path-glob applicability only with a public primary source and explicit cross-format boundaries.

Each item has a contributor-ready brief in [docs/ISSUE_SEEDS.md](docs/ISSUE_SEEDS.md). A milestone is complete only when fixtures, tests, semantics, provenance, and the changelog agree.

## 0.1 — prove conservative instruction tracing

- Expand synthetic coverage for documented filename and ancestry edge cases.
- Publish machine-readable snapshots for renderer compatibility checks.
- Improve keyboard, screen-reader, and narrow-screen review of generated reports.
- Document filesystem and large-repository performance boundaries.

## Later, only with primary sources

- Additional documented repository instruction formats.
- Path-glob instruction files where applicability can be implemented without ambiguity.
- Optional Graphviz image generation if it can remain dependency-free by default.

## Explicitly not planned

Model-based instruction scoring, natural-language conflict arbitration, a prompt marketplace, undocumented cross-vendor precedence, or collection of repository contents.
