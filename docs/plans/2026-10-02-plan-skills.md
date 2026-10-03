# Plan Skills Implementation Plan

> **For agentic workers:** Implement this task after the specs are reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `write-the-plan` and `carry-out-the-plan` in the existing plugin, with each skill's section bodies pinned to its spec, and bump the plugin to `0.5.0`.

**Architecture:** Each new spec is the only copy of that skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The check, the two manifests, and `docs/skills.md` are the other files this change edits. The two new skills land under `skills/`.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-02-write-the-plan-design.md`
- `docs/specs/2026-10-02-carry-out-the-plan-design.md`

This plan and those specs are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 4.

## Global Constraints

- Skill names are `write-the-plan` and `carry-out-the-plan`. Plugin name and marketplace name stay `kobold-codex`.
- `write-the-plan` description is one physical line: `Use when an architectural change needs a written plan, or the user asks for one. Write what will change, what it touches, what stays the same, what the checks cover, and the ordered tasks, then stop.`
- `carry-out-the-plan` description is one physical line: `Use when a plan has been approved. Run its tasks in order in this session, send independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.`
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.5.0` in both manifests. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order:
  - `write-the-plan`: `The document`, `Where it goes`, `What the reviewer reads`, `Tasks`, `Stop there`. The skill title is `Write the plan`.
  - `carry-out-the-plan`: `An approved plan`, `In order`, `Beside this session`, `The check`, `The same plan`. The skill title is `Carry out the plan`.
- Each section body equals that heading's body in its spec.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs and its ship rule stay. The `how-it-fits` spec keeps its sentence that `write-the-plan` was unshipped when that spec was written.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links each shipped skill and its spec, including the two new pairs. The new map sentences are the two paragraphs in Step 3. They do not copy a skill section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.

## Review Focus

- A section body in a new skill is a paraphrase of its spec. The section compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.4.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts a new description on more than one line. The frontmatter compare must fail.
- A file named in Global Constraints as not edited shows a diff. That diff must fail the review.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Pin the check, add the skills, bump the plugin

**Files:**

- Create: `skills/write-the-plan/SKILL.md`
- Create: `skills/carry-out-the-plan/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under each spec's `## Skill` heading. The checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.5.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [ ] **Step 1: Extend the check and confirm it fails**

When `tests/check_plugin.py` already requires both new skills, version `0.5.0`, and the four new guide links, mark this step done and go to Step 2.

Otherwise, add a spec path, a skill path, a description constant, and a headings tuple for each new skill. Point the spec paths at the two files named above. Add the two description lines from Global Constraints. Use the heading names from Global Constraints, in that order.

Leave `PLUGIN_DESCRIPTION` as the stable sentence. Change the required plugin version from `0.4.0` to `0.5.0`. Append these four strings to `GUIDE_LINKS`, after the `why-it-is` pair:

```text
skills/write-the-plan/SKILL.md
docs/specs/2026-10-02-write-the-plan-design.md
skills/carry-out-the-plan/SKILL.md
docs/specs/2026-10-02-carry-out-the-plan-design.md
```

Call `check_one` for each new skill after the `why-it-is` call. Leave the existing `check_one` calls as they are.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `write-the-plan`. The creed sections are not the failure.

- [ ] **Step 2: Write the two skills**

When a `SKILL.md` already carries the frontmatter and the section bodies from its spec, leave that file. Otherwise create it.

Each file starts with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The description stays on one physical line. The H1 titles are `Write the plan` and `Carry out the plan`. Copy each section body from that skill's spec. Do not rewrap a copied line.

- [ ] **Step 3: Bump the manifests and the skill map**

Set `"version"` to `0.5.0` in `.claude-plugin/plugin.json`, in the marketplace object, and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave `"description"` as `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` Leave the other manifest fields as they are.

Leave `README.md` as it is. In `docs/skills.md`, under Which skill applies, add these two paragraphs after the `why-it-is` paragraph:

```markdown
An architectural change, or a request for a plan, uses [skills/write-the-plan/SKILL.md](../skills/write-the-plan/SKILL.md).

An approved plan uses [skills/carry-out-the-plan/SKILL.md](../skills/carry-out-the-plan/SKILL.md).
```

Under Records, add these two items after the `why-it-is` item:

```markdown
- [skills/write-the-plan/SKILL.md](../skills/write-the-plan/SKILL.md) is recorded in [docs/specs/2026-10-02-write-the-plan-design.md](specs/2026-10-02-write-the-plan-design.md).
- [skills/carry-out-the-plan/SKILL.md](../skills/carry-out-the-plan/SKILL.md) is recorded in [docs/specs/2026-10-02-carry-out-the-plan-design.md](specs/2026-10-02-carry-out-the-plan-design.md).
```

When those version fields and those four sentences are already present, leave them.

- [ ] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.5.0`, the stable description, and `1 skill dir(s)`.

Confirm a drifted paragraph fails the check, then restore the copied body. Confirm the files Global Constraints says are not edited have an empty diff against the commit this branch started from. The spec diff and this plan are the earlier commits on the branch, so they are outside that empty-diff check.

- [ ] **Step 5: Commit the work**

`commit` governs this step. Stage the two skills, `tests/check_plugin.py`, both manifests, and `docs/skills.md`. Leave the specs and this plan in their own commits. A second run leaves a finished work commit as it is and commits a set only when it is still uncommitted and still allowed. Commit only when the resolved `commit` value allows it.
