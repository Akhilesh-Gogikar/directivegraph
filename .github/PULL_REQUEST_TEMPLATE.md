## What changes

Describe the user-visible discovery, precedence, parser, renderer, or documentation change.

## Why

Link the issue and public primary documentation for every semantic claim.

## Clean-room and privacy

- [ ] Fixtures are synthetic and contain no private repository instructions, credentials, personal data, or proprietary policy.
- [ ] New sources, fixtures, dependencies, and assets are recorded in `PROVENANCE.md`.

## Validation

- [ ] `python3 -m unittest discover -s tests -v`
- [ ] Relevant text, JSON, DOT, and HTML demos inspected
- [ ] Accessibility impact checked for HTML changes
- [ ] `git diff --check`

## Compatibility

State report-schema, CLI, documented-semantics, cross-format, privacy, and performance effects. Confirm documentation/changelog updates or explain why none are needed.
