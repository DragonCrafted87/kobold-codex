#!/usr/bin/env python3
"""Pin Kobold Codex to the spec."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/specs/2026-10-01-kobold-codex-design.md"
SKILL = ROOT / "skills/kobold-codex/SKILL.md"
README = ROOT / "README.md"
PLUGIN = ROOT / ".claude-plugin/plugin.json"
MARKET = ROOT / ".claude-plugin/marketplace.json"

HEADINGS = (
    "Voice",
    "Smallest change",
    "Prove the real artifact",
    "Fix the cause",
    "Re-running converges",
    "Data shape before logic",
    "Redesign instead of bolting on",
    "Remove dead weight first",
    "Build a rerunnable tool",
)

DESCRIPTION = (
    "Use before writing a reply, a diff, a commit message, or a document. "
    "Kobold Codex is the voice and the engineering principles for "
    "DragonCrafted87's agents on Grok and Claude Code."
)

PLUGIN_DESCRIPTION = (
    "Voice and engineering principles for DragonCrafted87's agents on "
    "Grok and Claude Code."
)

INSTALL_LINES = (
    "grok plugin install DragonCrafted87/kobold-codex --trust",
    "grok plugin install . --trust",
    "/plugin marketplace add DragonCrafted87/kobold-codex",
    "/plugin install kobold-codex@kobold-codex",
)

NEEDLES = (
    "rune" + "wyrm",
    "forge" + "wyrm",
    "hearth" + "wyrm",
    "/home/" + "dragon",
    "dot-" + "files",
)


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def sections(text):
    found = {}
    current = None
    buf = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6} (.+)$", line)
        if match:
            if current is not None:
                found[current] = "\n".join(buf).strip()
            current = match.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line.rstrip())
    if current is not None:
        found[current] = "\n".join(buf).strip()
    return found


def check_skill():
    if not SKILL.is_file():
        fail(f"missing {SKILL}")
    raw = SKILL.read_text()
    if not raw.startswith("---\n"):
        fail("SKILL.md is missing frontmatter")
    end = raw.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter does not close")
    front = raw[4:end]
    body = raw[end + 5 :]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if name is None or name.group(1).strip() != "kobold-codex":
        fail("frontmatter name must be kobold-codex")
    if desc is None or desc.group(1).strip() != DESCRIPTION:
        fail("frontmatter description does not match the spec")
    skill_sections = sections(body)
    spec_sections = sections(SPEC.read_text())
    for heading in HEADINGS:
        if heading not in skill_sections:
            fail(f"SKILL.md missing heading {heading}")
        if heading not in spec_sections:
            fail(f"spec missing heading {heading}")
        if skill_sections[heading] != spec_sections[heading]:
            fail(f"section {heading!r} does not match the spec")
        if skill_sections[heading] in README.read_text():
            fail(f"README restates {heading}")


def check_manifests():
    plugin = json.loads(PLUGIN.read_text())
    market = json.loads(MARKET.read_text())
    if plugin["name"] != "kobold-codex":
        fail("plugin name")
    if plugin["version"] != "0.1.0":
        fail("plugin version")
    if plugin["description"] != PLUGIN_DESCRIPTION:
        fail("plugin description")
    if plugin["license"] != "MIT":
        fail("plugin license")
    if plugin["repository"] != "https://github.com/DragonCrafted87/kobold-codex":
        fail("plugin repository")
    if plugin["author"]["name"] != "Scott Gudeman":
        fail("plugin author")
    if market["name"] != "kobold-codex":
        fail("marketplace name")
    if market["description"] != PLUGIN_DESCRIPTION:
        fail("marketplace description")
    listed = market["plugins"]
    if len(listed) != 1:
        fail("marketplace must list one plugin")
    entry = listed[0]
    if entry["name"] != plugin["name"]:
        fail("marketplace plugin name disagrees with plugin.json")
    if entry["version"] != plugin["version"]:
        fail("marketplace version disagrees with plugin.json")
    if entry["description"] != plugin["description"]:
        fail("marketplace description disagrees with plugin.json")
    if entry["source"] != "./":
        fail("marketplace source must be ./")
    if entry["license"] != "MIT":
        fail("marketplace license")
    readme = README.read_text()
    for line in INSTALL_LINES:
        if line not in readme:
            fail(f"README missing install line: {line}")
    if (ROOT / "hooks").exists() or any(ROOT.rglob("hooks.json")):
        fail("hooks are out of scope")


def check_public_text():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(errors="replace")
        for needle in NEEDLES:
            if needle in text:
                fail(f"{path.relative_to(ROOT)} contains a machine or home path")


def main():
    check_skill()
    check_manifests()
    check_public_text()


if __name__ == "__main__":
    main()
