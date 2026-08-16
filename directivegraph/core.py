"""Conservative instruction-file discovery and graph rendering.

DirectiveGraph models documented file discovery and directory ancestry. It does not
claim that two natural-language directives conflict; that would invent semantics.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from pathlib import Path
from typing import Any


SCHEMA = "directivegraph.report.v1"


class DirectiveGraphError(ValueError):
    """Raised for invalid roots or target paths."""


def _relative(path: Path, root: Path) -> str:
    value = path.relative_to(root).as_posix()
    return value or "."


def _id(prefix: str, *parts: object) -> str:
    raw = "\x1f".join(str(part) for part in parts)
    return f"{prefix}-{hashlib.sha256(raw.encode()).hexdigest()[:10]}"


def _ancestors(root: Path, target: Path) -> list[Path]:
    directory = target if target.is_dir() else target.parent
    try:
        relative = directory.relative_to(root)
    except ValueError as exc:
        raise DirectiveGraphError("target must be inside --root") from exc
    chain = [root]
    cursor = root
    for part in relative.parts:
        cursor /= part
        chain.append(cursor)
    return chain


def _parse_rules(path: Path, root: Path, file_status: str, file_reason: str) -> list[dict[str, Any]]:
    rules: list[dict[str, Any]] = []
    section = ""
    in_fence = False
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped or stripped.startswith("<!--"):
            continue
        if stripped.startswith("#"):
            section = stripped.lstrip("#").strip()
            continue
        text = re.sub(r"^(?:[-*+]\s+|\d+[.)]\s+)", "", stripped).strip()
        if not text:
            continue
        status = "shadowed" if file_status == "shadowed" else "applied"
        reason = file_reason if status == "shadowed" else "Instruction text is in an applicable source; no semantic-conflict inference was attempted."
        relative_text = _relative(path, root)
        rules.append(
            {
                "id": _id("rule", relative_text, line_number, text),
                "line": line_number,
                "section": section or None,
                "text": text,
                "status": status,
                "reason": reason,
            }
        )
    return rules


def _file_record(path: Path, root: Path, kind: str, depth: int, status: str, reason: str) -> dict[str, Any]:
    relative = _relative(path, root)
    record = {
        "id": _id("file", relative),
        "path": relative,
        "format": kind,
        "directory_depth": depth,
        "status": status,
        "reason": reason,
    }
    record["rules"] = _parse_rules(path, root, status, reason)
    return record


def analyze(root: Path | str, target: Path | str) -> dict[str, Any]:
    root_path = Path(root).expanduser().resolve()
    if not root_path.is_dir():
        raise DirectiveGraphError("--root must be an existing directory")
    target_input = Path(target).expanduser()
    target_path = (root_path / target_input).resolve() if not target_input.is_absolute() else target_input.resolve()
    chain = _ancestors(root_path, target_path)
    files: list[dict[str, Any]] = []

    # Codex publicly documents same-directory AGENTS.override.md replacement.
    for depth, directory in enumerate(chain):
        normal, override = directory / "AGENTS.md", directory / "AGENTS.override.md"
        if normal.is_file() and override.is_file():
            reason = f"Shadowed by {_relative(override, root_path)} in the same directory (documented Codex override filename)."
            files.append(_file_record(normal, root_path, "codex", depth, "shadowed", reason))
            files.append(_file_record(override, root_path, "codex", depth, "applied", "Selected instead of same-directory AGENTS.md by the documented override rule."))
        elif override.is_file():
            files.append(_file_record(override, root_path, "codex", depth, "applied", "Applicable Codex override source on the target's directory ancestry."))
        elif normal.is_file():
            files.append(_file_record(normal, root_path, "codex", depth, "applied", "Applicable Codex source on the target's directory ancestry."))

    # Other formats are collected conservatively. Cross-vendor ordering is never inferred.
    for depth, directory in enumerate(chain):
        candidates = [
            (directory / "CLAUDE.md", "claude", "Documented Claude project-memory filename on the target's ancestry."),
            (directory / ".claude" / "CLAUDE.md", "claude", "Documented Claude project-memory path on the target's ancestry."),
            (directory / "GEMINI.md", "gemini", "Documented Gemini context filename on the target's ancestry."),
        ]
        for path, kind, reason in candidates:
            if path.is_file():
                files.append(_file_record(path, root_path, kind, depth, "applied", reason))

    copilot = root_path / ".github" / "copilot-instructions.md"
    if copilot.is_file():
        files.append(_file_record(copilot, root_path, "github-copilot", 0, "applied", "Documented repository-wide GitHub Copilot instruction path."))

    files.sort(key=lambda item: (item["format"], item["directory_depth"], item["path"], item["status"]))
    edges: list[dict[str, str]] = []
    by_format: dict[str, list[dict[str, Any]]] = {}
    for record in files:
        by_format.setdefault(record["format"], []).append(record)
    for kind, records in sorted(by_format.items()):
        applied = [record for record in records if record["status"] == "applied"]
        applied.sort(key=lambda item: (item["directory_depth"], item["path"]))
        grouped = {
            depth: [record for record in applied if record["directory_depth"] == depth]
            for depth in sorted({record["directory_depth"] for record in applied})
        }
        depth_pairs = zip(list(grouped), list(grouped)[1:])
        for before_depth, after_depth in depth_pairs:
            for before in grouped[before_depth]:
                for after in grouped[after_depth]:
                    edges.append(
                        {
                            "from": before["id"],
                            "to": after["id"],
                            "relation": "closer_precedence_candidate",
                            "reason": f"{after['path']} is closer to the target within the {kind} format; only documented conflicts are resolved.",
                        }
                    )
        for shadowed in (record for record in records if record["status"] == "shadowed"):
            winner = next((record for record in applied if record["directory_depth"] == shadowed["directory_depth"]), None)
            if winner:
                edges.append({"from": shadowed["id"], "to": winner["id"], "relation": "shadowed_by", "reason": shadowed["reason"]})
    edges.sort(key=lambda item: (item["relation"], item["from"], item["to"]))
    return {
        "schema": SCHEMA,
        "root": ".",
        "target": _relative(target_path, root_path),
        "files": files,
        "edges": edges,
        "summary": {
            "applied_files": sum(item["status"] == "applied" for item in files),
            "shadowed_files": sum(item["status"] == "shadowed" for item in files),
            "applied_rules": sum(rule["status"] == "applied" for item in files for rule in item["rules"]),
            "shadowed_rules": sum(rule["status"] == "shadowed" for item in files for rule in item["rules"]),
        },
        "limitations": [
            "Natural-language rule conflicts are not inferred; closer-source edges are precedence candidates, not claims that whole files are replaced.",
            "Only documented filenames listed in docs/SEMANTICS.md are scanned; imports, hooks, user-level memory, and generated settings are outside this MVP.",
            "Markdown extraction is structural and intentionally ignores fenced code and headings; it is not a Markdown semantics engine.",
            "Cross-vendor precedence is never inferred.",
        ],
    }


def to_json(report: dict[str, Any]) -> str:
    return json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def render_text(report: dict[str, Any]) -> str:
    lines = [f"DirectiveGraph: {report['target']}"]
    if not report["files"]:
        lines.append("  no supported instruction files found")
    for record in report["files"]:
        lines.append(f"  [{record['status'].upper()}] {record['path']} ({record['format']})")
        lines.append(f"    reason: {record['reason']}")
        for rule in record["rules"]:
            lines.append(f"    L{rule['line']} [{rule['status']}] {rule['text']}")
    if report["edges"]:
        paths = {record["id"]: record["path"] for record in report["files"]}
        lines.append("  precedence graph:")
        for edge in report["edges"]:
            lines.append(f"    {paths[edge['from']]} -> {paths[edge['to']]} [{edge['relation']}]")
            lines.append(f"      reason: {edge['reason']}")
    lines.append(
        f"Summary: {report['summary']['applied_files']} applied file(s), "
        f"{report['summary']['shadowed_files']} shadowed file(s)"
    )
    return "\n".join(lines) + "\n"


def _dot_escape(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def render_dot(report: dict[str, Any]) -> str:
    lines = ["digraph directivegraph {", '  rankdir="LR";', '  node [shape="box", fontname="Helvetica"];']
    target_id = "target"
    lines.append(f'  {target_id} [label="target: {_dot_escape(report["target"])}", shape="oval"];')
    for record in report["files"]:
        style = "dashed" if record["status"] == "shadowed" else "solid"
        lines.append(f'  "{record["id"]}" [label="{_dot_escape(record["path"])}\\n{record["format"]} · {record["status"]}", style="{style}"];')
        if record["status"] == "applied":
            lines.append(f'  "{record["id"]}" -> {target_id} [label="applies"];')
    for edge in report["edges"]:
        lines.append(f'  "{edge["from"]}" -> "{edge["to"]}" [label="{_dot_escape(edge["relation"])}"];')
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_html(report: dict[str, Any]) -> str:
    cards = []
    for record in report["files"]:
        rule_rows = "".join(
            f'<li><code>L{rule["line"]}</code> {html.escape(rule["text"])} <small>{html.escape(rule["status"])}</small></li>'
            for rule in record["rules"]
        ) or "<li><em>No instruction text extracted.</em></li>"
        cards.append(
            f'<article class="{record["status"]}"><header><span>{html.escape(record["format"])}</span><b>{html.escape(record["path"])}</b>'
            f'<mark>{html.escape(record["status"])}</mark></header><p>{html.escape(record["reason"])}</p><ol>{rule_rows}</ol></article>'
        )
    embedded = html.escape(to_json(report))
    summary = report["summary"]
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>DirectiveGraph — {html.escape(report["target"])}</title>
<style>
:root{{--bg:#0b1020;--panel:#151d32;--text:#eef3ff;--muted:#9facca;--accent:#7dd3fc;--shadow:#fca5a5}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--text);font:14px system-ui,sans-serif}}main{{max-width:1000px;margin:auto;padding:32px}}h1{{margin-bottom:4px}}.lede,small{{color:var(--muted)}}.metrics{{display:flex;gap:12px;margin:24px 0}}.metric,article,details{{background:var(--panel);border-radius:10px;padding:16px}}.metric b{{display:block;font-size:24px}}article{{margin:12px 0;border-left:5px solid var(--accent)}}article.shadowed{{border-color:var(--shadow);opacity:.75}}header{{display:grid;grid-template-columns:120px 1fr auto;gap:12px;align-items:center}}header span{{color:var(--muted)}}mark{{border-radius:99px;padding:4px 8px}}li{{margin:7px 0}}details{{margin-top:20px}}pre{{overflow:auto;white-space:pre-wrap}}code{{color:#bae6fd}}
</style></head><body><main><h1>DirectiveGraph</h1><p class="lede">Target: {html.escape(report["target"])} · conservative, per-format ancestry trace</p>
<div class="metrics"><div class="metric"><b>{summary["applied_files"]}</b>applied files</div><div class="metric"><b>{summary["shadowed_files"]}</b>shadowed files</div><div class="metric"><b>{summary["applied_rules"]}</b>applied rules</div></div>
{"".join(cards) if cards else '<article><em>No supported instruction files found.</em></article>'}
<details><summary>Deterministic report JSON</summary><pre><code>{embedded}</code></pre></details></main></body></html>\n'''
