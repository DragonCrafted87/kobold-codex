#!/usr/bin/env python3
"""Pin Kobold Codex skill text to the spec."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/specs/2026-10-01-kobold-codex-design.md"
SKILL = ROOT / "skills/kobold-codex/SKILL.md"

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


def main():
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
    for path in (SKILL, SPEC):
        text = path.read_text()
        for needle in NEEDLES:
            if needle in text:
                fail(f"{path} contains a machine or home path")


if __name__ == "__main__":
    main()
