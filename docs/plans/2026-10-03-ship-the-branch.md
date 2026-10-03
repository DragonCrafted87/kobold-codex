# Ship the Branch Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `ship-the-branch` in the existing plugin, with the skill's section bodies pinned to its spec, and bump the plugin to `0.7.0`.

**Architecture:** The new spec is the only copy of the skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The check, the two manifests, and `docs/skills.md` are the other files this change edits. The new skill lands under `skills/`. The work stays on `feat/ship-the-branch`, cut from `main`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-03-ship-the-branch-design.md`

This plan and that spec are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 4 of Task 2.

## Global Constraints

- The skill name is `ship-the-branch`. Plugin name and marketplace name stay `kobold-codex`.
- `ship-the-branch` description is one physical line: `Use when the checks pass and the branch should be integrated. Commit the specs, the plans, and the work under their own keys, then push, open a pull request, or merge, and remove the worktree, each as the resolved bounds allow.`
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.7.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order: `The branch`, `Three commits`, `The remote`, `The worktree`, `The same branch`. The skill title is `Ship the branch`.
- Each section body equals that heading's body in the spec.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, `skills/write-the-plan/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, `skills/review-the-diff/SKILL.md`, `skills/take-the-review/SKILL.md`, `skills/stress-the-change/SKILL.md`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs and its ship rule stay. The `review-the-diff` spec keeps the sentence that names `ship-the-branch` as the later skill that integrates the branch. The `carry-out-the-plan` spec keeps the sentence that names `review-the-diff` as the later review. The `how-it-fits` spec keeps the sentence that `write-the-plan` was unshipped when that spec was written.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links each shipped skill and its spec, including the new pair. The new map sentences are the paragraphs in Task 2 Step 3. They do not copy a skill section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.
- Publishing follows the resolved bounds. `commit-specs` governs the spec commit. `commit-plans` governs this plan. `commit` governs the skill, check, manifest, and map commit. `push` and `pull-request` govern publishing the branch. `merge` stays on its own key. Name each key, the value, and the layer that set it before that action.

## Review Focus

- A section body in the new skill is a paraphrase of its spec. The section compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.6.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts the new description on more than one line. The frontmatter compare must fail.
- A file named in Global Constraints as not edited shows a diff. That diff must fail the review.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Commit the spec and this plan

**Files:**

- Already written: `docs/specs/2026-10-03-ship-the-branch-design.md`
- Already written: `docs/plans/2026-10-03-ship-the-branch.md`

**Interfaces:**

- Consumes: the spec and this plan, already in the worktree on `feat/ship-the-branch`.
- Produces: two commits when the resolved keys allow them. The spec commit contains only the spec. The plan commit contains only this plan.

- [x] **Step 1: Commit the spec**

When the spec is already committed on this branch, mark this step done and go to Step 2.

Otherwise resolve `commit-specs` and commit only that file when that value allows it. Leave this plan unstaged. A second run leaves a finished spec commit as it is.

- [x] **Step 2: Commit this plan**

When this plan is already committed, mark this step done.

Otherwise resolve `commit-plans` and commit only this file when that value allows it. Leave the checkboxes empty in that commit. The checkbox update is Task 3.

### Task 2: Pin the check, add the skill, bump the plugin

**Files:**

- Create: `skills/ship-the-branch/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under the spec's `## Skill` heading. The checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.7.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [x] **Step 1: Extend the check and confirm it fails**

When `tests/check_plugin.py` already requires the new skill, version `0.7.0`, and the two new guide links, mark this step done and go to Step 2.

Otherwise, add a spec path, a skill path, a description constant, and a headings tuple for the new skill. Point the spec path at `docs/specs/2026-10-03-ship-the-branch-design.md`. Add the description line from Global Constraints. Use the heading names from Global Constraints, in that order.

Leave `PLUGIN_DESCRIPTION` as the stable sentence. Change the required plugin version from `0.6.0` to `0.7.0`. Append these two strings to `GUIDE_LINKS`, after the `stress-the-change` pair:

```text
skills/ship-the-branch/SKILL.md
docs/specs/2026-10-03-ship-the-branch-design.md
```

Call `check_one` for the new skill after the `stress-the-change` call. Leave the existing `check_one` calls as they are.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `ship-the-branch`. The creed sections are not the failure.

- [x] **Step 2: Write the skill**

When `skills/ship-the-branch/SKILL.md` already carries the frontmatter and the section bodies from the spec, leave that file. Otherwise create it.

The file starts with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The description stays on one physical line. The H1 title is `Ship the branch`. Copy each section body from the spec. Do not rewrap a copied line.

- [x] **Step 3: Bump the manifests and the skill map**

Set `"version"` to `0.7.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave `"description"` as `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` Leave the other manifest fields as they are. Do not add a version field to the marketplace object.

Leave `README.md` as it is. In `docs/skills.md`, under Which skill applies, add this paragraph after the `stress-the-change` paragraph:

```markdown
Integrating a branch after its checks pass uses [skills/ship-the-branch/SKILL.md](../skills/ship-the-branch/SKILL.md).
```

Under Records, add this item after the `stress-the-change` item:

```markdown
- [skills/ship-the-branch/SKILL.md](../skills/ship-the-branch/SKILL.md) is recorded in [docs/specs/2026-10-03-ship-the-branch-design.md](specs/2026-10-03-ship-the-branch-design.md).
```

When that version and those two sentences are already present, leave them.

- [x] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.7.0`, the stable description, and `1 skill dir(s)`.

Confirm a drifted paragraph fails the check, then restore the copied body. Confirm the files Global Constraints says are not edited have an empty diff against `main`. The spec and this plan are new files, so they sit outside that empty-diff check.

- [x] **Step 5: Commit the work**

`commit` governs this step. Stage the skill, `tests/check_plugin.py`, both manifests, and `docs/skills.md`. Leave the spec and this plan in their own commits. A second run leaves a finished work commit as it is and commits a set only when it is still uncommitted and still allowed. Commit only when the resolved `commit` value allows it.

### Task 3: Mark the plan and publish

**Files:**

- Modify: `docs/plans/2026-10-03-ship-the-branch.md`

- [x] **Step 1: Mark the finished checkboxes**

When every checkbox in this plan is `- [x]`, mark this step done.

Otherwise mark each finished step `- [x]`. Leave a step that did not run empty.

- [x] **Step 2: Commit the checkbox update**

`commit-plans` governs this step. Stage only this plan. Commit only when that value allows it and the plan file is still uncommitted. A second run leaves a finished plan commit as it is.

- [ ] **Step 3: Push and open the pull request**

Resolve `push`. Push when that value allows it. Resolve `pull-request`. Open one pull request when that value allows it. Resolve `merge` and stop when that value is `never`. Do not force-push. There is no worktree to remove.
