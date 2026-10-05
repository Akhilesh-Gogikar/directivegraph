# Privacy

DirectiveGraph is local-only by design.

- It reads supported instruction files on the selected root-to-target ancestry and writes only an explicitly selected output path or standard output.
- It has no telemetry, analytics, cookies, remote fonts, remote scripts, model calls, or network client.
- Reports repeat instruction text, paths relative to the root, line numbers, and inferred structural relationships. They are not redacted.
- Symlinked instruction files are followed, so a link can pull text from outside the root into a report.
- Errors may include local paths.

Use synthetic repositories in issues and pull requests. Review JSON, text, DOT, and HTML before sharing them. A root-relative path can still reveal repository structure.

The project does not promise sandboxing or protection from another process with access to the same files. See [SECURITY.md](../SECURITY.md) for vulnerability reporting.
