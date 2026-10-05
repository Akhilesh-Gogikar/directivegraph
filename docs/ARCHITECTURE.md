# Architecture

DirectiveGraph is a dependency-free Python package and local CLI.

## Data flow

1. `directivegraph.__main__` resolves the repository root, target, format, and optional output path.
2. `directivegraph.core.analyze` rejects targets outside the root and builds a root-to-target directory chain.
3. The scanner checks only paths listed in [SEMANTICS.md](SEMANTICS.md).
4. A small structural Markdown reader records non-heading lines outside fenced code as rules; it does not interpret meaning.
5. The graph adds documented same-directory override edges and conservative closer-source candidates within one format. It never orders different vendors.
6. Renderers emit deterministic JSON, text, DOT, or self-contained HTML.

No stage executes instructions, invokes a model, searches outside the selected ancestry, or makes a network request. Symlinked instruction files on that ancestry are followed; see [SEMANTICS.md](SEMANTICS.md).

## Determinism

File and rule IDs use SHA-256 over root-relative paths and source positions. Files and edges are sorted, reports omit timestamps and absolute roots, and renderers preserve that ordering.

## Boundaries

The package exposes `analyze`, `render_dot`, `render_html`, `render_text`, and `to_json`. See [API_STABILITY.md](API_STABILITY.md) before integrating.
