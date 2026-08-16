"""Command-line entry point for ``python -m directivegraph``."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import DirectiveGraphError, analyze, render_dot, render_html, render_text, to_json


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="directivegraph",
        description="Explain which nested, documented agent instruction files apply to a target path.",
    )
    p.add_argument("target", type=Path, help="target file or directory")
    p.add_argument("--root", type=Path, default=Path.cwd(), help="repository root (default: current directory)")
    p.add_argument("--format", choices=("text", "json", "html", "dot"), default="text")
    p.add_argument("--output", type=Path, help="write output to a file instead of stdout")
    return p


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        # CLI paths follow normal shell semantics (relative to the current directory).
        report = analyze(args.root.resolve(), args.target.resolve())
        rendered = {
            "text": render_text,
            "json": to_json,
            "html": render_html,
            "dot": render_dot,
        }[args.format](report)
        if args.output:
            args.output.write_text(rendered, encoding="utf-8")
        else:
            sys.stdout.write(rendered)
        return 0
    except (OSError, DirectiveGraphError) as exc:
        print(f"directivegraph: error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
