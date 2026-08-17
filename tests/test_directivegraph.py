from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from directivegraph.core import DirectiveGraphError, analyze, render_dot, render_html, render_text, to_json


class DirectiveGraphTest(unittest.TestCase):
    def case(self, name: str, target: str):
        root = ROOT / "fixtures" / name
        return analyze(root, root / target)

    def test_case_01_root_instruction(self):
        report = self.case("01_root", "src/main.py")
        self.assertEqual(report["summary"]["applied_files"], 1)
        self.assertEqual(report["files"][0]["path"], "AGENTS.md")
        self.assertEqual(report["summary"]["applied_rules"], 2)

    def test_case_02_nested_sources_remain_applied_with_precedence_edge(self):
        report = self.case("02_nested", "pkg/module.py")
        self.assertEqual(report["summary"]["applied_files"], 2)
        self.assertEqual(report["summary"]["shadowed_files"], 0)
        self.assertEqual(report["edges"][0]["relation"], "closer_precedence_candidate")

    def test_case_03_override_has_explicit_shadow_reason(self):
        report = self.case("03_override", "src/main.py")
        shadowed = next(item for item in report["files"] if item["status"] == "shadowed")
        self.assertEqual(shadowed["path"], "AGENTS.md")
        self.assertIn("AGENTS.override.md", shadowed["reason"])
        self.assertTrue(all(rule["status"] == "shadowed" for rule in shadowed["rules"]))

    def test_case_04_does_not_invent_cross_vendor_edges(self):
        report = self.case("04_mixed", "app/page.py")
        self.assertEqual({item["format"] for item in report["files"]}, {"codex", "claude"})
        self.assertTrue(all("codex" not in edge["reason"] or "claude" not in edge["reason"] for edge in report["edges"]))
        self.assertFalse(any(edge for edge in report["edges"] if edge["relation"] == "shadowed_by"))

    def test_case_05_all_renderers_are_deterministic_and_self_contained(self):
        report = self.case("05_public_names", "deep/src/task.py")
        self.assertEqual(report["summary"]["applied_files"], 4)
        self.assertEqual(to_json(report), to_json(self.case("05_public_names", "deep/src/task.py")))
        self.assertIn("digraph directivegraph", render_dot(report))
        self.assertIn("DirectiveGraph:", render_text(report))
        page = render_html(report)
        self.assertIn("<!doctype html>", page)
        self.assertIn('href="#report">Skip to report', page)
        self.assertIn("aria-labelledby=", page)
        self.assertIn("<h2", page)
        self.assertNotIn("<script src=", page)
        self.assertNotIn("<link rel=", page)

    def test_target_outside_root_fails(self):
        with self.assertRaises(DirectiveGraphError):
            analyze(ROOT / "fixtures" / "01_root", ROOT / "README.md")

    def test_top_level_version_does_not_require_target(self):
        result = subprocess.run(
            [sys.executable, "-m", "directivegraph", "--version"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "directivegraph 0.1.0\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
