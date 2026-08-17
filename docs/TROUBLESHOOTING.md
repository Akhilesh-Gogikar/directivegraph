# Troubleshooting

## `target must be inside --root`

Use paths that resolve beneath the selected root. From the repository root, either pass both as relative shell paths or use absolute paths for both.

## No instruction files found

Check the exact supported paths in [SEMANTICS.md](SEMANTICS.md). Imports, user-level memory, hooks, arbitrary filenames, and path-glob instruction files are not scanned in this MVP.

## A parent file is still `applied`

DirectiveGraph does not claim that a deeper file replaces an entire parent file. It emits a `closer_precedence_candidate` edge and leaves natural-language conflict resolution to the documented agent behavior.

## Expected rules are missing

Headings and fenced code are deliberately excluded. Other non-empty Markdown lines are structural rule records; this is not a full Markdown parser.

## DOT does not render as an image

The CLI writes DOT text and does not bundle Graphviz. Inspect the file directly or install a renderer separately. JSON, text, and HTML require no external tool.

## Installation or CLI problem

```sh
python3 --version
python3 -m pip install .
directivegraph --help
python3 -m unittest discover -s tests -v
```

Python 3.10 through 3.14 is supported. Include a synthetic repository tree and exact error when filing an issue.
