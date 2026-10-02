# Kobold Codex Implementation Plan

> **For agentic workers:** Implement these tasks in order. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Publish one Grok and Claude Code plugin whose skill text is the voice paragraph and eight principles in the spec.

**Architecture:** The skill file is the only copy of the principles. A Python check reads the same headings from the spec and from `SKILL.md` and requires the paragraphs to match. `plugin.json` makes the repo a plugin. `marketplace.json` makes that plugin installable from GitHub in Claude Code. The README carries the install commands and points at the skill.

**Tech Stack:** Markdown skill, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Spec:** `docs/specs/2026-10-01-kobold-codex-design.md`

## Global Constraints

- Plugin name, marketplace name, and skill name are `kobold-codex`.
- Skill description is exactly: `Use before writing a reply, a diff, a commit message, or a document. Kobold Codex is the voice and the engineering principles for DragonCrafted87's agents on Grok and Claude Code.`
- Plugin and marketplace description is exactly: `Voice and engineering principles for DragonCrafted87's agents on Grok and Claude Code.`
- Version is `0.1.0`. License is `MIT`. Author name is `Scott Gudeman`. Author email is `24697493+DragonCrafted87@users.noreply.github.com`. Repository URL is `https://github.com/DragonCrafted87/kobold-codex`.
- Marketplace plugin `source` is `./`.
- The voice section and the eight principle sections in `SKILL.md` use the heading names in the spec, and each section body equals that heading's body in the spec.
- The skill names no Grok tool and no Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README contains the four install lines from the spec and does not restate a principle paragraph.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation so the check itself does not contain them as one string.
- `LICENSE` from the GitHub seed stays as it is.

## Review Focus

- A principle paragraph in the skill is a paraphrase of the spec. The section compare must fail.
- The README repeats a principle paragraph. The README compare must fail.
- `plugin.json` and `marketplace.json` disagree on name, version, or description. The manifest compare must fail.
- Frontmatter puts the description on more than one line, so the trigger sentence is not the catalog sentence. The frontmatter compare must fail.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Bring in the GitHub license and README

**Files:**

- Modify: `README.md` (arrives from GitHub; leave the stub until Task 3)
- Create: `LICENSE` (arrives from GitHub; do not edit)

**Interfaces:**

- Consumes: local `main` with the spec, and `origin/main` at the GitHub initial commit (`LICENSE`, stub `README.md`)
- Produces: one `main` history that contains both, with `LICENSE` unchanged

- [ ] **Step 1: Add the remote and merge the unrelated seed**

The local repository and the GitHub repository were created separately. Merge them. Do not push.

```bash
git remote add origin https://github.com/DragonCrafted87/kobold-codex.git
git fetch origin
git merge origin/main --allow-unrelated-histories -m "Merge the GitHub license and README."
```

If `origin` already exists, skip `git remote add` and run the fetch and merge.

- [ ] **Step 2: Confirm the seed landed**

Run:

```bash
git status -sb
test -f LICENSE
head -n 2 LICENSE
head -n 1 README.md
```

Expected: `main` tracks or includes `origin/main`, `LICENSE` starts with `MIT License`, and the README's first line is `# kobold-codex`. No push.

### Task 2: Pin the skill text to the spec

**Files:**

- Create: `skills/kobold-codex/SKILL.md`
- Create: `tests/check_plugin.py`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: heading bodies under `Voice`, `Smallest change`, `Prove the real artifact`, `Fix the cause`, `Re-running converges`, `Data shape before logic`, `Redesign instead of bolting on`, `Remove dead weight first`, and `Build a rerunnable tool` in the spec
- Produces: `SKILL.md` whose frontmatter `name` is `kobold-codex` and whose section bodies equal the spec. `tests/check_plugin.py` exits 0 only when that is true.

- [ ] **Step 1: Write the failing check**

Create `tests/check_plugin.py` with this content:

```python
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
```

- [ ] **Step 2: Run the check and confirm it fails**

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `SKILL.md`.

- [ ] **Step 3: Write the skill**

Create `skills/kobold-codex/SKILL.md`. The description is one physical line. Each section body is the paragraph already under that heading in the spec, copied unchanged.

```markdown
---
name: kobold-codex
description: Use before writing a reply, a diff, a commit message, or a document. Kobold Codex is the voice and the engineering principles for DragonCrafted87's agents on Grok and Claude Code.
---

# Kobold Codex

## Voice

Write the way your PR descriptions read. Use complete sentences, and
name the specific thing you mean: a path, a package, a command, or a
result you actually observed. Open with what is true or with what the
reader should do. When another option matters, give it a sentence of its
own and say why it is on the table. A chat reply stays in this register.
A pull request, a commit message, or a doc keeps the headings that
project already uses.

## Smallest change

Change what the problem requires and leave the rest of the tree alone. A
new file, a new abstraction, or a second code path belongs in the diff
when some caller already needs it. If you cannot name that caller, leave
the extra piece out of this change.

## Prove the real artifact

Before you call the work done, exercise the thing someone will actually
touch. Run the command, use the screen, read the file that was written,
or read the diff that will ship. A clean compile, or an explanation of
why the change ought to work, tells you where to look next. If a check
is still open, name that check in the reply.

## Fix the cause

Start from a symptom you can reproduce. Follow it until you can see what
produces it, and put the fix at that point. A guard that only stops the
failure from being reported leaves the producer in place, and the next
caller runs into the same behavior.

## Re-running converges

An operation should be safe to run again. A second run that starts from
a finished state stays on that state. A run that stopped halfway is a
valid place to start, and finishing it reaches the same result as a run
that succeeded the first time. Role installers already work this way:
running the role again is how a machine picks up changes.

## Data shape before logic

Before writing branches, name the records you are storing, what type
each one has, and which part of the program owns them. With that
settled, the code that reads and updates those records gets shorter,
because the awkward cases have a place to live in the shape.

## Redesign instead of bolting on

Some requests are a founding assumption the current design never had.
Reshape the surrounding code so the new requirement sits where that
assumption would have sat from the start. Keep a compatibility shim
while a real caller still depends on the old shape, and remove the shim
in the same change when no caller does.

## Remove dead weight first

Before adding the new behavior, look for the unused path, the check that
no longer protects anything, and the stub left from an earlier attempt.
Remove those, then build on the code that remains.

## Build a rerunnable tool

A one-off edit can be done by hand. Work that will happen again, such as
a migration across many call sites, a repeated check, or a sweep of
similar edits, should leave a script or a skill behind. The next person
runs that artifact a second time instead of reconstructing the steps
from the last session.
```

The paragraphs above are wrapped at the same width as the spec. The check strips trailing spaces on each line and then compares the section text, including line breaks. Copy a paragraph from the spec when a line wrap differs. A wording change is a failure.

- [ ] **Step 4: Run the check and confirm it passes**

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 0 and no stderr.

- [ ] **Step 5: Commit**

```bash
git add skills/kobold-codex/SKILL.md tests/check_plugin.py
git commit -m "Add the Kobold Codex skill pinned to the spec."
```

### Task 3: Manifests, install note, and validate

**Files:**

- Create: `.claude-plugin/plugin.json`
- Create: `.claude-plugin/marketplace.json`
- Modify: `README.md`
- Modify: `tests/check_plugin.py`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the skill and the section check from Task 2. `LICENSE` from Task 1.
- Produces: a directory `grok plugin validate` accepts. README install lines are `grok plugin install DragonCrafted87/kobold-codex --trust`, `grok plugin install . --trust`, `/plugin marketplace add DragonCrafted87/kobold-codex`, and `/plugin install kobold-codex@kobold-codex`.

- [ ] **Step 1: Replace the check with the full check**

Replace `tests/check_plugin.py` with this content. It keeps the Task 2 assertions and adds the manifest, README, hook, and tree-wide needle checks.

```python
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
```

- [ ] **Step 2: Run the check and confirm it fails**

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1 because `plugin.json` or `README.md` does not satisfy the new assertions. The failure is a missing file or a missing install line, not a skill-section mismatch.

- [ ] **Step 3: Write the manifests and the README**

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "kobold-codex",
  "description": "Voice and engineering principles for DragonCrafted87's agents on Grok and Claude Code.",
  "version": "0.1.0",
  "author": {
    "name": "Scott Gudeman",
    "email": "24697493+DragonCrafted87@users.noreply.github.com"
  },
  "repository": "https://github.com/DragonCrafted87/kobold-codex",
  "license": "MIT"
}
```

Create `.claude-plugin/marketplace.json`:

```json
{
  "name": "kobold-codex",
  "description": "Voice and engineering principles for DragonCrafted87's agents on Grok and Claude Code.",
  "owner": {
    "name": "Scott Gudeman",
    "email": "24697493+DragonCrafted87@users.noreply.github.com"
  },
  "plugins": [
    {
      "name": "kobold-codex",
      "description": "Voice and engineering principles for DragonCrafted87's agents on Grok and Claude Code.",
      "version": "0.1.0",
      "source": "./",
      "license": "MIT",
      "author": {
        "name": "Scott Gudeman",
        "email": "24697493+DragonCrafted87@users.noreply.github.com"
      }
    }
  ]
}
```

Replace `README.md` with:

```markdown
# Kobold Codex

Voice and engineering principles for coding agents on Grok and Claude Code.
The wording lives in [skills/kobold-codex/SKILL.md](skills/kobold-codex/SKILL.md).
The 2026-10-01 decision is recorded in
[docs/specs/2026-10-01-kobold-codex-design.md](docs/specs/2026-10-01-kobold-codex-design.md).

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
```

- [ ] **Step 4: Run the check and validate the plugin**

Run:

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0. `grok plugin validate` exits 0 and reports `name: kobold-codex`, `version: 0.1.0`, and one skill directory.

- [ ] **Step 5: Commit**

```bash
git add .claude-plugin/plugin.json .claude-plugin/marketplace.json README.md tests/check_plugin.py
git commit -m "Add the plugin manifests and the install note."
```

Do not push unless asked.
