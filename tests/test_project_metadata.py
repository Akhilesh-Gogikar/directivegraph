from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import directivegraph


class ProjectMetadataTest(unittest.TestCase):
    def test_required_community_and_documentation_files(self):
        required = {
            "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md",
            "GOVERNANCE.md", "ROADMAP.md", "CHANGELOG.md", "ECOSYSTEM.md", "pyproject.toml",
            "docs/ARCHITECTURE.md", "docs/TROUBLESHOOTING.md", "docs/API_STABILITY.md",
            "docs/PRIVACY.md", "docs/ACCESSIBILITY.md", "docs/LAUNCH_KIT.md", "docs/ISSUE_SEEDS.md",
            ".github/ISSUE_TEMPLATE/bug.yml", ".github/ISSUE_TEMPLATE/feature.yml",
            ".github/PULL_REQUEST_TEMPLATE.md", ".github/CODEOWNERS", ".github/dependabot.yml",
            ".github/workflows/ci.yml", ".github/workflows/release.yml",
        }
        self.assertEqual([], sorted(name for name in required if not (ROOT / name).is_file()))

    def test_package_and_workflow_contract(self):
        project = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        self.assertIn('version = "0.1.0"', project)
        self.assertIn('dependencies = []', project)
        self.assertIn('license = "MIT"', project)
        self.assertIn('license-files = ["LICENSE"]', project)
        self.assertIn('directivegraph = "directivegraph.__main__:main"', project)
        self.assertEqual("0.1.0", directivegraph.__version__)
        ci = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        release = (ROOT / ".github/workflows/release.yml").read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", ci)
        self.assertIn("ubuntu-latest", ci)
        self.assertIn("macos-latest", ci)
        self.assertIn("windows-latest", ci)
        for version in ("3.10", "3.11", "3.12", "3.13", "3.14"):
            self.assertIn(f'"{version}"', ci)
        self.assertIn("needs: test", release)
        self.assertIn("gh release create", release)
        self.assertIn("contents: write", release)
        self.assertNotIn("pull_request_target", ci + release)
        actions = [line.strip() for line in (ci + release).splitlines() if "uses:" in line]
        self.assertTrue(actions)
        self.assertTrue(all(re.search(r"@[0-9a-f]{40}(?:\s|$)", line) for line in actions))

    def test_local_markdown_links_and_launch_hygiene(self):
        link = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
        broken = []
        text = []
        for markdown in ROOT.rglob("*.md"):
            if any(part in {".git", ".codesight"} for part in markdown.parts):
                continue
            content = markdown.read_text(encoding="utf-8")
            text.append(content)
            for raw in link.findall(content):
                target = raw.strip().split(maxsplit=1)[0].strip("<>").split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (markdown.parent / unquote(target)).exists():
                    broken.append(f"{markdown.relative_to(ROOT)} -> {raw}")
        self.assertEqual([], broken)
        joined = "\n".join(text)
        self.assertNotIn("/" + "Users" + "/", joined)
        self.assertNotIn("One" + "New", joined)
        ecosystem = (ROOT / "ECOSYSTEM.md").read_text(encoding="utf-8")
        self.assertEqual(7, len(set(re.findall(r"github\.com/akigogikar/([a-z0-9-]+)", ecosystem))))
        self.assertIn("optional and informational", ecosystem)

    def test_launch_materials_are_complete_and_scoped(self):
        seeds = (ROOT / "docs/ISSUE_SEEDS.md").read_text(encoding="utf-8")
        self.assertEqual(5, len(re.findall(r"^## \d+\. ", seeds, re.MULTILINE)))
        for field in ("**Proposed title:**", "**Labels:**", "**Rationale:**", "**Acceptance criteria**", "**Test plan:**", "**Skills:**", "**Estimated scope:**", "**Likely files:**"):
            self.assertEqual(5, seeds.count(field), field)
        launch = (ROOT / "docs/LAUNCH_KIT.md").read_text(encoding="utf-8")
        for section in ("### Hacker News", "### Reddit", "### LinkedIn", "### X", "## FAQ", "## Launch-day checklist", "## First 30 days"):
            self.assertIn(section, launch)
        self.assertIn("Never claim", launch)


if __name__ == "__main__":
    unittest.main()
