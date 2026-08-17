# API stability

DirectiveGraph `0.1.x` is alpha software. Compatibility promises are intentionally narrow.

## Intended stable surface within `0.1.x`

- The console command name `directivegraph` and `python -m directivegraph`.
- Existing CLI option names, formats (`text`, `json`, `html`, `dot`), and exit code `0` for success or `2` for user/filesystem errors.
- Report schema identifier `directivegraph.report.v1` and existing field meanings.
- Deterministic output for the same root-relative tree and target.

Additive JSON fields, newly documented filenames, prose, CSS, and HTML/DOT layout may change in a minor release. Consumers should ignore unknown JSON fields and avoid scraping text or HTML.

## Python API

Imports re-exported from `directivegraph.__init__` are available for experimentation but remain provisional until `1.0`. Private helpers and intermediate dictionaries are not APIs.

Breaking changes require a changelog entry and version change. Security or correctness fixes may change previously incorrect output.
