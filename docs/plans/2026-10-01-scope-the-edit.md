# Scope the Edit Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `scope-the-edit` in the existing plugin, with the skill text pinned to `docs/specs/2026-10-01-scope-the-edit-design.md`, and bump the plugin to `0.2.0`.

**Architecture:** The new spec is the only copy of the five section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The creed skill and the 2026-10-01 creed spec stay untouched. The same check still pins them to each other. The README points at both skills and does not restate a section body.

**Tech Stack:** Markdown skill, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Spec:** `docs/specs/2026-10-01-scope-the-edit-design.md`

This plan and that spec are already in the worktree. Do not rewrite the five section bodies while implementing. If a pasted paragraph in this plan disagrees with the spec, the spec wins.

## Global Constraints

- Skill name is `scope-the-edit`. Plugin name and marketplace name stay `kobold-codex`.
- Skill description is one physical line: `Use before changing a file or making a commit. Name the scope of the edit, then add only the plan and the proof that scope calls for.`
- Plugin and marketplace description becomes: `Voice, engineering principles, and edit scoping for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.2.0` in both manifests. License, author, repository, and marketplace `source` stay as they are.
- The five section bodies in `skills/scope-the-edit/SKILL.md` use the heading names in the spec, and each section body equals that heading's body in the spec.
- `skills/kobold-codex/SKILL.md` and `docs/specs/2026-10-01-kobold-codex-design.md` are not edited.
- The skill names no Grok tool and no Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, links both skills and both specs, and does not restate a section body from either skill.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.
- Do not commit onto `feat/initial-plugin` while that branch is the open first-plugin review. Branch from the commit that contains the creed plugin. Today that commit is `8c12679` on `feat/initial-plugin`. If `main` already contains it, branch from `main`.

## Review Focus

- A section body in the new skill is a paraphrase of the spec. The section compare must fail.
- The README repeats a section body from either skill. The README compare must fail.
- `plugin.json` stays at `0.1.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts the new description on more than one line. The frontmatter compare must fail.
- The creed skill or the creed spec changes. The creed section compare must fail.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Add the skill, bump the plugin, and pin the check

**Files:**

- Create: `skills/scope-the-edit/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `README.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: heading bodies under `Name the scope`, `Small`, `Intermediate`, `Architectural`, and `Real code` in `docs/specs/2026-10-01-scope-the-edit-design.md`. The creed check from the first plan.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.2.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)` with both skills under it.

- [ ] **Step 1: Branch**

```bash
git switch -c feat/scope-the-edit
```

If the creed plugin is already on `main`, branch from `main` instead.

- [ ] **Step 2: Replace the check and confirm it fails**

Replace `tests/check_plugin.py` with the script in Step 2 below. Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `scope-the-edit`. The creed sections are not the failure.

- [ ] **Step 3: Write the skill, manifests, and README**

Create `skills/scope-the-edit/SKILL.md` from Step 3 below. Copy a paragraph from the spec when a line wrap differs.

Set `"version"` to `0.2.0` and `"description"` to `Voice, engineering principles, and edit scoping for DragonCrafted87's agents on Grok and Claude Code.` in `.claude-plugin/plugin.json`, in the marketplace object, and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave the other manifest fields as they are.

Replace `README.md` with the note in Step 3 below.

- [ ] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints:

```text
Plugin manifest is valid.
  name: kobold-codex
  version: 0.2.0
  description: Voice, engineering principles, and edit scoping for DragonCrafted87's agents on Grok and Claude Code.
  components: 1 skill dir(s), 0 command dir(s), 0 agent dir(s)
```

The component line counts the `skills/` directory. One directory and two skills is the passing result. Confirmed by validating a copy with both skills, a copy with only the creed, and a copy with only `scope-the-edit`: each reports `1 skill dir(s)`.

- [ ] **Step 5: Commit**

```bash
git add skills/scope-the-edit/SKILL.md tests/check_plugin.py .claude-plugin/plugin.json .claude-plugin/marketplace.json README.md docs/specs/2026-10-01-scope-the-edit-design.md docs/plans/2026-10-01-scope-the-edit.md
git commit -m "Add the scope-the-edit skill."
```

Do not push unless asked.

#### Step 2 script

```python
#!/usr/bin/env python3
"""Pin Kobold Codex to the specs."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/specs/2026-10-01-kobold-codex-design.md"
SKILL = ROOT / "skills/kobold-codex/SKILL.md"
SCOPE_SPEC = ROOT / "docs/specs/2026-10-01-scope-the-edit-design.md"
SCOPE_SKILL = ROOT / "skills/scope-the-edit/SKILL.md"
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

SCOPE_HEADINGS = (
    "Name the scope",
    "Small",
    "Intermediate",
    "Architectural",
    "Real code",
)

DESCRIPTION = (
    "Use before writing a reply, a diff, a commit message, or a document. "
    "Kobold Codex is the voice and the engineering principles for "
    "DragonCrafted87's agents on Grok and Claude Code."
)

SCOPE_DESCRIPTION = (
    "Use before changing a file or making a commit. "
    "Name the scope of the edit, then add only the plan and the proof "
    "that scope calls for."
)

PLUGIN_DESCRIPTION = (
    "Voice, engineering principles, and edit scoping for "
    "DragonCrafted87's agents on Grok and Claude Code."
)

INSTALL_LINES = (
    "grok plugin install DragonCrafted87/kobold-codex --trust",
    "grok plugin install . --trust",
    "/plugin marketplace add DragonCrafted87/kobold-codex",
    "/plugin install kobold-codex@kobold-codex",
)

README_LINKS = (
    "skills/kobold-codex/SKILL.md",
    "docs/specs/2026-10-01-kobold-codex-design.md",
    "skills/scope-the-edit/SKILL.md",
    "docs/specs/2026-10-01-scope-the-edit-design.md",
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


def check_one(path, spec_path, expected_name, description, headings):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    raw = path.read_text()
    if not raw.startswith("---\n"):
        fail(f"{expected_name} is missing frontmatter")
    end = raw.find("\n---\n", 4)
    if end < 0:
        fail(f"{expected_name} frontmatter does not close")
    front = raw[4:end]
    body = raw[end + 5 :]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if name is None or name.group(1).strip() != expected_name:
        fail(f"frontmatter name must be {expected_name}")
    if desc is None or desc.group(1).strip() != description:
        fail(f"frontmatter description does not match for {expected_name}")
    skill_sections = sections(body)
    spec_sections = sections(spec_path.read_text())
    readme = README.read_text()
    for heading in headings:
        if heading not in skill_sections:
            fail(f"{expected_name} missing heading {heading}")
        if heading not in spec_sections:
            fail(f"spec missing heading {heading}")
        if skill_sections[heading] != spec_sections[heading]:
            fail(f"section {heading!r} does not match the spec")
        if skill_sections[heading] in readme:
            fail(f"README restates {heading}")


def check_skills():
    check_one(SKILL, SPEC, "kobold-codex", DESCRIPTION, HEADINGS)
    check_one(
        SCOPE_SKILL,
        SCOPE_SPEC,
        "scope-the-edit",
        SCOPE_DESCRIPTION,
        SCOPE_HEADINGS,
    )


def check_manifests():
    plugin = json.loads(PLUGIN.read_text())
    market = json.loads(MARKET.read_text())
    if plugin["name"] != "kobold-codex":
        fail("plugin name")
    if plugin["version"] != "0.2.0":
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
    for line in README_LINKS:
        if line not in readme:
            fail(f"README missing link: {line}")
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
    check_skills()
    check_manifests()
    check_public_text()


if __name__ == "__main__":
    main()
```

A missing skill fails with `missing skills/scope-the-edit/SKILL.md`.

#### Step 3 skill

```markdown
---
name: scope-the-edit
description: Use before changing a file or making a commit. Name the scope of the edit, then add only the plan and the proof that scope calls for.
---

# Scope the edit

## Name the scope

Before editing, name the scope in the reply. The scopes are small,
intermediate, and architectural. Name the scope once, before the first
edit of a change. A commit of work already under that scope is part of
the same change. A settings change, or any other edit whose destination
is already known and that does not change behavior, is small. A bug
fix is intermediate. A change inside a function that has a decision is
intermediate, including a one-line fix. A new subsystem, or a change
that reshapes how the pieces fit together, is architectural. When two
scopes both fit, use the larger one.

## Small

Do the edit in the same turn. The edit is the whole task. The check is
the file that was written.

## Intermediate

Say what is wrong, what will change, and which check will show the
fix. The original repro, an existing command, or a run of the system
can be that check. Carry out the edit and the check in the same turn.
When two checks would change the work, stop and ask which one to run.

## Architectural

Write a plan the reviewer can read. Say what will change, which parts
of the system it touches, what the tests will cover, and what stays
the same. Write the plan where the project keeps plans. When the
project has nowhere for it, use docs/plans/. Stop after the plan.
Implementation starts after an explicit yes to that plan. A yes names
this plan. "Yes", "do it", or the choice the plan just offered counts.
Approval of an earlier piece of work does not carry forward. Once the
conversation has that yes, do the work.

## Real code

When the edit changes a function in C, C++, C#, Python, Java, or
another language in that class, the check follows the code. A
non-trivial function has a decision in it, and the check reaches each
branch. A complex algorithm is one whose decision combines several
conditions, or whose result depends on interacting decisions. Aim at
MC/DC for that algorithm: each condition can change the outcome on its
own. Say whether the check reached branch coverage or MC/DC. Exercise
the system. Use a mock when the dependency cannot be run, such as
hardware or a paid external service. When a branch cannot be reached
from the system boundary, cover that branch with a focused test. Add a
test when no existing run reaches the bar.
```

#### Step 3 README

````markdown
# Kobold Codex

Voice, engineering principles, and edit scoping for coding agents on Grok and Claude Code.
The creed lives in [skills/kobold-codex/SKILL.md](skills/kobold-codex/SKILL.md).
The 2026-10-01 creed is recorded in
[docs/specs/2026-10-01-kobold-codex-design.md](docs/specs/2026-10-01-kobold-codex-design.md).
Edit scoping lives in [skills/scope-the-edit/SKILL.md](skills/scope-the-edit/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-01-scope-the-edit-design.md](docs/specs/2026-10-01-scope-the-edit-design.md).

## Install

Grok, from GitHub:

```bash
grok plugin install DragonCrafted87/kobold-codex --trust
```

Grok, from a local checkout of this repository:

```bash
grok plugin install . --trust
```

Claude Code, in a session:

```text
/plugin marketplace add DragonCrafted87/kobold-codex
/plugin install kobold-codex@kobold-codex
```

Start a new session after installing so the skill is in the catalog.

## License

MIT. See [LICENSE](LICENSE).
````
