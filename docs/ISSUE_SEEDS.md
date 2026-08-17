# Issue seeds

These are launch-ready drafts, not proof that an issue has been filed. Maintainers should confirm scope, create only the issues they intend to triage, and keep one owner per issue.

## 1. Protect instruction files from accidental output overwrite

**Proposed title:** `Protect instruction files from accidental --output overwrite`

**Labels:** `good first issue`, `bug`, `safety`, `needs-triage`

**Rationale:** analysis completes before output is written, but a user can point `--output` at an applicable instruction file and destroy source data. The CLI should fail closed.

**Acceptance criteria**

- Resolve the output path before writing and reject it when it aliases the target or any discovered instruction source.
- Cover direct paths, normalized `..` paths, and symlink aliases supported by the chosen platform policy.
- Exit with code `2`, name the conflicting root-relative path when safe, and leave the file byte-for-byte unchanged.
- Normal output behavior remains unchanged.

**Test plan:** temporary synthetic repository tests for target/source collision and one normal write; verify original hashes after failures.

**Skills:** Python paths, CLI validation, data-loss prevention. **Estimated scope:** 3–5 hours.

**Likely files:** `directivegraph/__main__.py`, `directivegraph/core.py`, `tests/test_directivegraph.py`, `docs/TROUBLESHOOTING.md`.

## 2. Add deterministic JSON snapshots for all five synthetic repositories

**Proposed title:** `Add deterministic JSON snapshots for all five synthetic repositories`

**Labels:** `good first issue`, `testing`, `fixtures`, `needs-triage`

**Rationale:** current tests assert important fields, but reviewed snapshots would make unintended schema, reason-text, ordering, and ID changes obvious.

**Acceptance criteria**

- Check in one expected JSON report per existing fixture case; no machine paths or timestamps.
- Add a stdlib-only regeneration command that writes to a temporary location by default and requires an explicit flag to replace snapshots.
- Tests compare exact bytes and print a useful diff on failure.
- Document the review rule: snapshot changes require semantic justification, not blind regeneration.

**Test plan:** clean comparison, intentional temporary mismatch, repeat regeneration twice and compare hashes.

**Skills:** Python `unittest`, JSON fixtures, deterministic testing. **Estimated scope:** 4–6 hours.

**Likely files:** `fixtures/`, `tests/test_directivegraph.py`, `docs/SEMANTICS.md`, optionally `tools/regenerate_snapshots.py`.

## 3. Group wrapped Markdown list continuations into one extracted rule

**Proposed title:** `Group wrapped Markdown list continuations into one extracted rule`

**Labels:** `help wanted`, `parser`, `compatibility`, `needs-design`

**Rationale:** `_parse_rules` treats each non-empty line as a rule. A visually wrapped list item therefore becomes multiple rules, which weakens line attribution and report readability.

**Acceptance criteria**

- Write the minimal structural grammar before implementation: list markers, indented continuations, blank lines, headings, and fenced code.
- Join only unambiguous continuation lines; do not become a full Markdown semantics engine.
- Preserve the first source line and expose the covered line range additively if approved.
- Existing single-line fixtures remain unchanged.

**Test plan:** bullets, numbered items, nested indentation, paragraph boundaries, headings, and fenced-code cases; exact rule order and text assertions.

**Skills:** text parsing, compatibility design, Python. **Estimated scope:** 1–2 days.

**Likely files:** `directivegraph/core.py`, `tests/test_directivegraph.py`, `fixtures/`, `docs/SEMANTICS.md`, `docs/API_STABILITY.md`.

## 4. Define and implement a symlink policy for instruction sources

**Proposed title:** `Define and implement a symlink policy for instruction sources`

**Labels:** `help wanted`, `security`, `filesystem`, `needs-design`

**Rationale:** target containment is resolved, but symlinked instruction files have not received an explicit trust-boundary policy. Reports must not unexpectedly read outside the selected root.

**Acceptance criteria**

- Document behavior for target symlinks, instruction-file symlinks inside the root, links escaping the root, broken links, and loops.
- Reject or skip out-of-root sources with an explicit deterministic reason; never read their content.
- Preserve root-relative paths and avoid machine-specific real paths in reports.
- Update the security boundary and limitations.

**Test plan:** temporary-directory cases for internal, external, broken, and cyclic links; platform-conditional skips with reasons; verify no external sentinel content appears.

**Skills:** filesystem security, cross-platform Python, threat modeling. **Estimated scope:** 2–3 days.

**Likely files:** `directivegraph/core.py`, `tests/test_directivegraph.py`, `SECURITY.md`, `docs/PRIVACY.md`, `docs/SEMANTICS.md`.

## 5. Add documented path-glob instruction applicability

**Proposed title:** `Add documented path-glob instruction applicability`

**Labels:** `advanced`, `semantics`, `import-format`, `provenance-required`

**Rationale:** some public instruction formats scope files with documented path patterns. Supporting one could answer more target-specific questions, but only if matching and precedence are modeled without cross-format invention.

**Acceptance criteria**

- Select exactly one publicly documented format and record the specification/version and terms in `PROVENANCE.md`.
- Publish a design covering pattern syntax, base directory, include/exclude behavior, invalid patterns, precedence, and cross-format isolation.
- Implement matching with the standard library, or stop for dependency/design review.
- Add at least five synthetic cases: match, non-match, nested match, invalid pattern, and interaction with an ancestry source.
- Reports explain applicability or exclusion in JSON, text, DOT, and HTML.

**Test plan:** table-driven pattern fixtures, deterministic renderer checks, path-separator coverage, invalid-input diagnostics, full existing-suite regression.

**Skills:** specification reading, glob semantics, cross-platform paths, graph/report design. **Estimated scope:** 4–7 days after design approval.

**Likely files:** `directivegraph/core.py`, `directivegraph/__main__.py`, `tests/test_directivegraph.py`, `fixtures/`, `docs/SEMANTICS.md`, `docs/API_STABILITY.md`, `PROVENANCE.md`.
