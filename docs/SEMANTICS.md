# Supported discovery semantics

DirectiveGraph v0 is intentionally conservative. It scans only these public, documented repository instruction paths:

| Format | Paths scanned | MVP interpretation |
|---|---|---|
| Codex | `AGENTS.md`, `AGENTS.override.md` | Walk root-to-target ancestry. In one directory, `AGENTS.override.md` replaces `AGENTS.md`. Deeper applied sources get a **closer precedence candidate** edge; parents are not declared wholly shadowed. |
| Claude Code | `CLAUDE.md`, `.claude/CLAUDE.md` | Collect matching files on root-to-target ancestry. No relationship between the two spellings is invented. |
| Gemini CLI | `GEMINI.md` | Collect matching files on root-to-target ancestry and show closer-source candidate edges. |
| GitHub Copilot | `.github/copilot-instructions.md` | Treat the documented root path as repository-wide. |

## What “rule” means

The tiny Markdown reader records each non-empty, non-heading line outside fenced code as instruction text. It retains its section and line number. It does not decide that two natural-language lines are equivalent or contradictory.

`applied` therefore means “comes from a discovered applicable source,” not “guaranteed to win every conflict.” `shadowed` is used only for the documented same-directory `AGENTS.override.md` replacement. Cross-vendor files are never ordered against one another.

Imports, user/global instruction stores, hooks, skill files, path-glob front matter, generated settings, symlink traversal, and model-specific prompt assembly are outside v0.
