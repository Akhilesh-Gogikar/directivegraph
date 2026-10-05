# Supported discovery semantics

DirectiveGraph v0 is intentionally conservative. It scans only these public, documented repository instruction paths:

| Format | Paths scanned | MVP interpretation |
|---|---|---|
| Codex | `AGENTS.md`, `AGENTS.override.md` | Walk root-to-target ancestry. In one directory, `AGENTS.override.md` replaces `AGENTS.md`. Deeper applied sources get a **closer precedence candidate** edge; parents are not declared wholly shadowed. |
| Claude Code | `CLAUDE.md`, `.claude/CLAUDE.md` | Collect matching files on root-to-target ancestry and show closer-source candidate edges. No relationship between the two spellings in one directory is invented. |
| Gemini CLI | `GEMINI.md` | Collect matching files on root-to-target ancestry and show closer-source candidate edges. |
| GitHub Copilot | `.github/copilot-instructions.md` | Treat the documented root path as repository-wide. |

## What “rule” means

The tiny Markdown reader records each non-empty, non-heading line outside fenced code as instruction text. It retains its section and line number. It does not decide that two natural-language lines are equivalent or contradictory.

For Claude Code and Gemini CLI, a closer-source candidate edge records position only: the cited documentation describes hierarchical loading, not a closer-wins rule.

`applied` therefore means “comes from a discovered applicable source,” not “guaranteed to win every conflict.” `shadowed` is used only for the documented same-directory `AGENTS.override.md` replacement. Cross-vendor files are never ordered against one another.

Imports, user/global instruction stores, hooks, skill files, path-glob front matter, generated settings, and model-specific prompt assembly are outside v0.

Symlinks have no explicit policy yet. A symlinked instruction file on the ancestry is followed and read, including a target outside `--root`; only the target path itself must resolve under the root. Issue [#7](https://github.com/Akhilesh-Gogikar/directivegraph/issues/7) tracks a containment policy.
