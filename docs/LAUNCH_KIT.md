# Launch kit

This is prepared copy and an operating checklist—not permission to publish. Repository visibility, tagging, and the first release require explicit maintainer approval.

## Positioning

**One line:** DirectiveGraph answers which documented repository instruction files apply to one target path and why—without inventing natural-language semantics.

**Who it is for:** developers debugging nested instruction behavior, reviewers auditing repository policy, and tool authors who need a deterministic, source-linked explanation.

**Honest proof:** five synthetic repositories cover root, nested, documented override, mixed-format, and repository-wide cases in text, JSON, DOT, and script-free HTML.

**Differentiators:** one-target scope, explicit reasons, per-format precedence isolation, deterministic IDs/order, local operation, and multiple accessible outputs from one analysis.

**Never claim:** complete prompt assembly, semantic conflict detection, undocumented precedence, user/global memory coverage, benchmark results, adoption, or support for every instruction format.

## Two-minute demo script

```sh
python3 -m pip install .
directivegraph fixtures/03_override/src/main.py \
  --root fixtures/03_override --format text
directivegraph fixtures/05_public_names/deep/src/task.py \
  --root fixtures/05_public_names --format html --output /tmp/directivegraph.html
```

1. Say: “Both repositories are synthetic; the CLI makes no network request.”
2. In text, show applied `AGENTS.override.md`, shadowed same-directory `AGENTS.md`, the reason, and the `shadowed_by` edge.
3. Open the HTML report. Use the skip link and headings, then show source format, status text, extracted rules, and embedded deterministic JSON.
4. Mention JSON for integrations and DOT for graph tooling; all derive from the same conservative report.
5. Close with the boundary: “Candidate edges show documented ordering inside a format; the tool does not decide what two sentences mean.”

Do not demo a private repository, real instruction policy, or hand-edited output. A recording should show the synthetic fixture path.

## Copy bank

### Hacker News

**Title:** `Show HN: DirectiveGraph – explain which repo instructions apply to one file`

**Text:**

> I built DirectiveGraph to answer a deceptively hard repository question: for this target file, which nested agent instruction sources apply, which documented override wins, and why?
>
> It scans only documented filenames on the root-to-target path, keeps formats isolated, and refuses to infer natural-language conflicts. Output is deterministic text, JSON, DOT, or self-contained accessible HTML. Runtime is local, dependency-free, and has no model or network call.
>
> Five synthetic repositories exercise root, nested, override, mixed-format, and repository-wide behavior. I would value primary-source corrections, missing edge cases, and feedback on whether the explanation is conservative enough. Please do not post private instruction files.

### Reddit

**Title:** `I made a local CLI that explains nested repo instructions for one target file`

**Text:**

> DirectiveGraph walks a repository root to one target, finds a deliberately small set of documented instruction filenames, and explains applied sources, same-directory overrides, and closer-source candidate edges.
>
> It does not invoke a model or guess what instructions mean. The CLI emits text, deterministic JSON, DOT, and accessible HTML with zero runtime dependencies. The quickstart uses synthetic repositories. I am looking for reproducible filesystem/parser cases and public sources for any proposed semantics—not private repo examples.

### LinkedIn

> Nested repository instructions are easy to accumulate and hard to explain. I built DirectiveGraph to give one target file a deterministic, source-linked instruction trace.
>
> It models documented discovery, keeps formats isolated, and explicitly refuses natural-language conflict guesses. Output is local text, JSON, DOT, or accessible self-contained HTML. Five synthetic cases and contributor-ready issue seeds make the current limits reviewable.

### X

> DirectiveGraph answers: “Which repo instructions reach this file, and why?” Local, zero runtime deps, deterministic text/JSON/DOT/accessible HTML, and no semantic guessing. Five synthetic cases + scoped issues: https://github.com/Akhilesh-Gogikar/directivegraph

## FAQ

### Does it evaluate which instruction is better?

No. It records structural instruction text and documented relationships. It does not score, merge, or interpret natural language.

### Why are parent and child files both applied?

A deeper source can have precedence on conflicts without erasing every parent instruction. DirectiveGraph shows a candidate edge unless a documented rule explicitly shadows a source.

### Does it read my whole repository?

No. It resolves one target and checks supported instruction paths on that root-to-target ancestry, plus a documented repository-wide path. Reports repeat discovered instruction text.

### Does it call a model or service?

No. Analysis is local, deterministic Python with no runtime dependency, model call, telemetry, or network client.

### Which instruction formats are supported?

Only the public filenames and limited semantics listed in [SEMANTICS.md](SEMANTICS.md). Cross-format precedence, imports, user memory, hooks, and most path-glob instructions are outside `0.1.0`.

### Is it production-ready?

It is an alpha launch candidate. Core synthetic cases are tested, but symlink policy, large-tree hardening, and independent accessibility/security review remain open.

### How can I contribute safely?

Use a synthetic repository and a public primary source for semantic claims. Start with [ISSUE_SEEDS.md](ISSUE_SEEDS.md).

## Launch-day checklist

- [ ] Maintainer explicitly approves public visibility, tag, and release execution.
- [ ] Ownership, trademark, provenance, dependency, secret, private-path, and full-history reviews are recorded.
- [ ] Repository description, topics, social preview, issue labels, and private security advisories are reviewed without changing scope.
- [ ] Fresh install, full tests, all four output demos, JSON parse, HTML keyboard/contrast/zoom checks, and link validation pass from the release commit.
- [ ] `CHANGELOG.md`, package version, tag, and release title agree.
- [ ] Five selected issue seeds exist with owners/triage labels; no empty placeholder issue is filed.
- [ ] Publish one canonical launch post first, then adapt it for other channels rather than duplicating blindly.
- [ ] Monitor questions for six hours, correct factual misunderstandings, and never request private instructions.
- [ ] Record only verifiable launch signals: stars, forks, issue quality, completed demo reports, and contributor activity. Do not infer users from page views.

## First 30 days

### Days 1–3

- Reproduce every credible bug in a synthetic tree; label or ask one focused question within the stated triage target.
- Add FAQ clarifications for repeated confusion instead of promising undocumented semantics.
- Correct external summaries that describe the graph as prompt assembly or conflict resolution.

### Week 1

- Publish one technical walkthrough of discovery, shadowing, and candidate edges.
- Select at most two community issues for active work; keep the rest honest about maintainer capacity.
- Thank reporters, source reviewers, and fixture authors in merged pull requests and the changelog.

### Weeks 2–4

- Review which demo or filesystem case fails most often and improve that path before adding formats.
- Compare requested work with [ROADMAP.md](../ROADMAP.md); reject semantic guessing and private-fixture shortcuts.
- Cut a patch release only for shipped, tested changes. Update issue seeds and roadmap based on evidence.
- At day 30, publish a short retrospective with exact shipped changes, open risks, contribution outcomes, and no inflated adoption narrative.

## Release gate

- [ ] Every fixture is synthetic; no private instructions, secrets, domains, absolute paths, or generated reports are committed.
- [ ] CI is green on the documented Python/platform matrix and pinned actions remain reviewed.
- [ ] Fresh virtual-environment install and installed `directivegraph --version`, `--help`, and all renderer demos pass.
- [ ] Accessibility, privacy, and filesystem boundaries have been manually reviewed; known limits remain visible.
- [ ] Security advisory routing and community templates work after visibility changes.
- [ ] The maintainer explicitly authorizes the release workflow. Until then, do not push a version tag.

## Social preview and media

- Upload [the 1280 × 640 PNG](assets/social-preview.png) in **Settings → General → Social preview** immediately before the visibility change; GitHub does not read this repository file automatically.
- Keep the adjacent SVG as the editable source and follow the [asset notes](assets/README.md).
- Capture demos with synthetic inputs only. Remove usernames, home paths, tokens, partner names, and unrelated windows.
- Provide captions, a transcript, and descriptive alt text. Verify the README image, generated HTML, and demo at 200% zoom, by keyboard, and with a real screen reader before posting.
- Do not place download, adoption, company, performance, or compatibility counts on an asset unless the source and date are public and reproducible.

## Ethical cross-promotion

Cross-link only the seven related OSS tools named in ECOSYSTEM.md, and only where a link answers the reader's next technical question. Links stay optional, disclosed, and outside runtime output. Commercial products require exact owner-approved names, URLs, relationship wording, and trademark or partner permission before inclusion.
