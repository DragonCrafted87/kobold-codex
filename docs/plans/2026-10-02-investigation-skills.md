# Investigation Skills Implementation Plan

> **For agentic workers:** Implement this task after the specs are reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `debug-the-failure`, `how-it-fits`, and `why-it-is` in the existing plugin, with each skill's section bodies pinned to its spec, and bump the plugin to `0.4.0`.

**Architecture:** Each new spec is the only copy of that skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The creed, `scope-the-edit`, and `set-the-bounds` stay untouched. The catalog's ship rule is amended: the manifest description stays one sentence, and decision records move to `docs/skills.md`. The root README stays the introduction and the install guide.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-02-debug-the-failure-design.md`
- `docs/specs/2026-10-02-how-it-fits-design.md`
- `docs/specs/2026-10-02-why-it-is-design.md`

This plan and those specs are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule. If the three specs disagree with that sentence, stop.

## Global Constraints

- Skill names are `debug-the-failure`, `how-it-fits`, and `why-it-is`. Plugin name and marketplace name stay `kobold-codex`.
- `debug-the-failure` description is one physical line: `Use when a failure can be reproduced. Hold one hypothesis at a time, check it on the running system, and put the fix at the producer of the symptom.`
- `how-it-fits` description is one physical line: `Use before changing a subsystem. Name the runtime path, the package that owns the behavior, and the layer the change belongs on.`
- `why-it-is` description is one physical line: `Use when you need the reason for a behavior or a threshold. Recover it from the code, the history, the issues, and the docs, and cite each source.`
- Plugin and marketplace description becomes the stable sentence, and later skills leave it as it is: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.4.0` in both manifests. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order:
  - `debug-the-failure`: `Reproduce`, `One hypothesis`, `Evidence`, `The producer`, `The same failure`. The skill title is `Debug the failure`.
  - `how-it-fits`: `Read first`, `Runtime path`, `Owner`, `Layer`. The skill title is `How it fits`.
  - `why-it-is`: `The question`, `Sources`, `The read`, `No reason on record`. The skill title is `Why it is`.
- Each section body equals that heading's body in its spec.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, and their specs are not edited. The catalog's skill briefs stay. Its ship rule records the stable description and `docs/skills.md`.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links each shipped skill and its spec.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.

## Review Focus

- A section body in a new skill is a paraphrase of its spec. The section compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.3.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts a new description on more than one line. The frontmatter compare must fail.
- The creed, `scope-the-edit`, or `set-the-bounds` changes. Those compares must fail the review. A catalog brief changes. That diff must fail the review. The ship rule in the catalog is the amendment this plan carries.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Pin the check, add the skills, bump the plugin

**Files:**

- Create: `skills/debug-the-failure/SKILL.md`
- Create: `skills/how-it-fits/SKILL.md`
- Create: `skills/why-it-is/SKILL.md`
- Create: `docs/skills.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `README.md`
- Modify: `docs/specs/2026-10-02-remaining-skills-design.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under each spec's `## Skill` heading. The creed, scope, and bounds checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.4.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [ ] **Step 1: Extend the check and confirm it fails**

In `tests/check_plugin.py`, add a spec path, a skill path, a description constant, and a headings tuple for each new skill. Point the spec paths at the three files named above. Add the three description lines from Global Constraints. Use the heading names from Global Constraints, in that order.

Change the required plugin version from `0.3.0` to `0.4.0`. Change `PLUGIN_DESCRIPTION` to the stable sentence in Global Constraints. Move the skill and spec link check from `README.md` to `docs/skills.md`, and include the three new pairs below with the three already shipped. Fail when `README.md` contains `docs/specs/`. Require `docs/skills.md` in the README.

```text
skills/debug-the-failure/SKILL.md
docs/specs/2026-10-02-debug-the-failure-design.md
skills/how-it-fits/SKILL.md
docs/specs/2026-10-02-how-it-fits-design.md
skills/why-it-is/SKILL.md
docs/specs/2026-10-02-why-it-is-design.md
```

Call `check_one` for each new skill after the `set-the-bounds` call. Leave the creed, scope, and bounds calls as they are.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `debug-the-failure`. The creed sections are not the failure.

- [ ] **Step 2: Write the three skills**

Create each `SKILL.md` with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The H1 titles are `Debug the failure`, `How it fits`, and `Why it is`. Copy each section body from that skill's spec. Do not rewrap a copied line.

- [ ] **Step 3: Bump the manifests and the README**

Set `"version"` to `0.4.0` and `"description"` to `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` in `.claude-plugin/plugin.json`, in the marketplace object, and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave the other manifest fields as they are.

Replace `README.md` with the note in Step 3 below. Create `docs/skills.md` with the map in Step 3 below. The catalog edit is the ship rule, and it belongs in the spec commit.

- [ ] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.4.0`, the description from Global Constraints, and `1 skill dir(s)`.

Confirm a drifted paragraph fails the check, then restore the copied body. Confirm the creed files and `set-the-bounds` have an empty diff against the commit this branch started from. The catalog diff is the ship rule only.

- [ ] **Step 5: Commit the work**

`commit` governs this step. Stage the three skills, `tests/check_plugin.py`, both manifests, `README.md`, and `docs/skills.md`. Leave the specs and this plan in their own commits. Commit only when the resolved `commit` value allows it.

#### Step 3 README

````markdown
# Kobold Codex

Principles and workflow skills for coding agents on Grok and Claude Code.
The skills live under `skills/`. A session uses the skill whose description matches the task.
Install the plugin, then start a new session so the skills are in the catalog.
The map of which skill applies, and the design notes, live in [docs/skills.md](docs/skills.md).

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

#### Step 3 skill map

`docs/skills.md` names which skill applies, then links each shipped skill and its spec. Use repo-root paths in the link text so the check can find `skills/<name>/SKILL.md` and `docs/specs/<file>`. Do not copy a skill section body into that page.
