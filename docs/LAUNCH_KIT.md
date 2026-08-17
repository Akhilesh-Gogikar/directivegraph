# Launch kit

This file is a checklist, not permission to publish. Repository visibility and the first release require explicit maintainer approval.

## Positioning

**One line:** DirectiveGraph explains which documented repository instruction files apply to one target path and why, without inventing natural-language semantics.

**Honest proof:** five synthetic nested repositories deterministically show root, nested, documented override, mixed-format, and repository-wide cases in text, JSON, DOT, and HTML.

**Do not claim:** complete agent prompt assembly, semantic conflict detection, undocumented precedence, user/global memory coverage, or support for every instruction format.

## Five-minute demo

```sh
python3 -m pip install .
directivegraph fixtures/03_override/src/main.py \
  --root fixtures/03_override --format text
directivegraph fixtures/05_public_names/deep/src/task.py \
  --root fixtures/05_public_names --format html --output /tmp/directivegraph.html
python3 -m unittest discover -s tests -v
```

Show the explicit override reason, per-format candidate edges, accessible HTML, and conservative limitations—not a private repository.

## Release gate

- [ ] Ownership, trademark, provenance, and security reviews recorded.
- [ ] Every fixture synthetic; no private instructions, secrets, domains, or absolute paths committed.
- [ ] Tests pass on the documented Python/platform CI matrix.
- [ ] Fresh virtual-environment install and console command pass.
- [ ] HTML checked with keyboard, screen reader, zoom, narrow viewport, and contrast tooling.
- [ ] `CHANGELOG.md` and version agree; signed `v0.1.0` tag intentionally created.
- [ ] Security advisories enabled and issue/PR templates reviewed.
- [ ] Maintainer explicitly approves public visibility and release workflow execution.

Suggested announcement: “DirectiveGraph 0.1.0 gives one target file a deterministic, source-linked instruction trace in text, JSON, DOT, or self-contained HTML—without guessing at cross-vendor semantics.”
