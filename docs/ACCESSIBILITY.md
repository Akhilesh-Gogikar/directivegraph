# Accessibility

DirectiveGraph aims for accessible CLI and report output without requiring a graphical renderer.

## Current baseline

- Text and JSON are first-class outputs; the CLI uses no required color or interactive terminal controls.
- HTML uses landmarks, headings, a skip link, definition-list metrics, labelled articles, and ordered rule lists.
- Applied/shadowed state is written as text and reinforced by borders, never conveyed by color alone.
- Keyboard focus is visible on the skip link and disclosure; report content does not require a pointer.
- Foreground/background pairs were selected for strong contrast and the layout collapses cleanly on narrow screens.
- DOT is available as plain text for alternative rendering workflows.

## Checks before release

Run the HTML regression test, traverse the skip link and disclosure with only a keyboard, inspect at 200% zoom and a narrow viewport, and smoke-test a screen reader's headings, article names, lists, and status text. Color-contrast tools should check applied and shadowed cards.

## Known limits

Large repositories can produce long pages; graph topology is not narrated beyond ordered cards and embedded JSON; no formal WCAG conformance audit has been completed. [Report an accessibility issue](https://github.com/Akhilesh-Gogikar/directivegraph/issues/new?template=bug.yml) and prefix the title with `accessibility:`. Use [SECURITY.md](../SECURITY.md) if disclosure would expose private instructions.
