# Review Skills Implementation Plan

> **For agentic workers:** Implement this task after the specs are reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `review-the-diff`, `take-the-review`, and `stress-the-change` in the existing plugin, with each skill's section bodies pinned to its spec, and bump the plugin to `0.6.0`.

**Architecture:** Each new spec is the only copy of that skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The check, the two manifests, and `docs/skills.md` are the other files this change edits. The three new skills land under `skills/`. The work stays on `feat/review-skills`, cut from `main`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-03-review-the-diff-design.md`
- `docs/specs/2026-10-03-take-the-review-design.md`
- `docs/specs/2026-10-03-stress-the-change-design.md`

This plan and those specs are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 4 of Task 2.

## Global Constraints

- Skill names are `review-the-diff`, `take-the-review`, and `stress-the-change`. Plugin name and marketplace name stay `kobold-codex`.
- `review-the-diff` description is one physical line: `Use before a merge, or when the user asks for a review. Review the diff against the request and the checks, report each finding with file and line, and leave the tree alone.`
- `take-the-review` description is one physical line: `Use when review notes are in hand. Check each note against the code, implement the notes that hold, and for a note that does not hold say why and leave that code as it is.`
- `stress-the-change` description is one physical line: `Use when a diff needs several independent reviews. Run separate passes on different angles, merge the findings into one list, and leave the tree alone.`
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.6.0` in both manifests. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order:
  - `review-the-diff`: `The diff`, `The request and the checks`, `Findings`, `Leave the tree`. The skill title is `Review the diff`.
  - `take-the-review`: `The notes`, `Against the code`, `One note at a time`, `A note that does not hold`, `The same notes`. The skill title is `Take the review`.
  - `stress-the-change`: `The diff`, `Three passes`, `One list`, `Leave the tree`. The skill title is `Stress the change`.
- Each section body equals that heading's body in its spec.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, `skills/write-the-plan/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs and its ship rule stay. The `carry-out-the-plan` spec keeps the sentence that names `review-the-diff` as the later review. The `how-it-fits` spec keeps the sentence that `write-the-plan` was unshipped when that spec was written.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links each shipped skill and its spec, including the three new pairs. The new map sentences are the paragraphs in Task 2 Step 3. They do not copy a skill section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.
- Publishing follows the resolved bounds. `commit-specs` governs the spec commit. `commit-plans` governs this plan. `commit` governs the skill, check, manifest, and map commit. `push` and `pull-request` govern publishing the branch. `merge` stays on its own key. Name each key, the value, and the layer that set it before that action.

## Review Focus

- A section body in a new skill is a paraphrase of its spec. The section compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.5.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts a new description on more than one line. The frontmatter compare must fail.
- A file named in Global Constraints as not edited shows a diff. That diff must fail the review.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Commit the specs and this plan

**Files:**

- Already written: `docs/specs/2026-10-03-review-the-diff-design.md`
- Already written: `docs/specs/2026-10-03-take-the-review-design.md`
- Already written: `docs/specs/2026-10-03-stress-the-change-design.md`
- Already written: `docs/plans/2026-10-03-review-skills.md`

**Interfaces:**

- Consumes: the three specs and this plan, already in the worktree on `feat/review-skills`.
- Produces: two commits when the resolved keys allow them. The spec commit contains only the three specs. The plan commit contains only this plan.

- [x] **Step 1: Commit the specs**

When the three specs are already committed on this branch, mark this step done and go to Step 2.

Otherwise resolve `commit-specs` and commit only those three files when that value allows it. Leave this plan unstaged. A second run leaves a finished spec commit as it is.

- [x] **Step 2: Commit this plan**

When this plan is already committed, mark this step done.

Otherwise resolve `commit-plans` and commit only this file when that value allows it. Leave the checkboxes empty in that commit. The checkbox update is Task 3.

### Task 2: Pin the check, add the skills, bump the plugin

**Files:**

- Create: `skills/review-the-diff/SKILL.md`
- Create: `skills/take-the-review/SKILL.md`
- Create: `skills/stress-the-change/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under each spec's `## Skill` heading. The checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.6.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [x] **Step 1: Extend the check and confirm it fails**

When `tests/check_plugin.py` already requires all three new skills, version `0.6.0`, and the six new guide links, mark this step done and go to Step 2.

Otherwise, add a spec path, a skill path, a description constant, and a headings tuple for each new skill. Point the spec paths at the three files named above. Add the three description lines from Global Constraints. Use the heading names from Global Constraints, in that order.

Leave `PLUGIN_DESCRIPTION` as the stable sentence. Change the required plugin version from `0.5.0` to `0.6.0`. Append these six strings to `GUIDE_LINKS`, after the `carry-out-the-plan` pair:

```text
skills/review-the-diff/SKILL.md
docs/specs/2026-10-03-review-the-diff-design.md
skills/take-the-review/SKILL.md
docs/specs/2026-10-03-take-the-review-design.md
skills/stress-the-change/SKILL.md
docs/specs/2026-10-03-stress-the-change-design.md
```

Call `check_one` for each new skill after the `carry-out-the-plan` call. Leave the existing `check_one` calls as they are.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `review-the-diff`. The creed sections are not the failure.

- [x] **Step 2: Write the three skills**

When a `SKILL.md` already carries the frontmatter and the section bodies from its spec, leave that file. Otherwise create it.

Each file starts with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The description stays on one physical line. The H1 titles are `Review the diff`, `Take the review`, and `Stress the change`. Copy each section body from that skill's spec. Do not rewrap a copied line.

- [x] **Step 3: Bump the manifests and the skill map**

Set `"version"` to `0.6.0` in `.claude-plugin/plugin.json`, in the marketplace object, and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave `"description"` as `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` Leave the other manifest fields as they are.

Leave `README.md` as it is. In `docs/skills.md`, under Which skill applies, add these three paragraphs after the `carry-out-the-plan` paragraph:

```markdown
A review before a merge, or a request to review a diff, uses [skills/review-the-diff/SKILL.md](../skills/review-the-diff/SKILL.md).

Review notes to check against the code use [skills/take-the-review/SKILL.md](../skills/take-the-review/SKILL.md).

Several independent passes over one diff use [skills/stress-the-change/SKILL.md](../skills/stress-the-change/SKILL.md).
```

Under Records, add these three items after the `carry-out-the-plan` item:

```markdown
- [skills/review-the-diff/SKILL.md](../skills/review-the-diff/SKILL.md) is recorded in [docs/specs/2026-10-03-review-the-diff-design.md](specs/2026-10-03-review-the-diff-design.md).
- [skills/take-the-review/SKILL.md](../skills/take-the-review/SKILL.md) is recorded in [docs/specs/2026-10-03-take-the-review-design.md](specs/2026-10-03-take-the-review-design.md).
- [skills/stress-the-change/SKILL.md](../skills/stress-the-change/SKILL.md) is recorded in [docs/specs/2026-10-03-stress-the-change-design.md](specs/2026-10-03-stress-the-change-design.md).
```

When those version fields and those six sentences are already present, leave them.

- [x] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.6.0`, the stable description, and `1 skill dir(s)`.

Confirm a drifted paragraph fails the check, then restore the copied body. Confirm the files Global Constraints says are not edited have an empty diff against `main`. The three specs and this plan are new files, so they sit outside that empty-diff check.

- [x] **Step 5: Commit the work**

`commit` governs this step. Stage the three skills, `tests/check_plugin.py`, both manifests, and `docs/skills.md`. Leave the specs and this plan in their own commits. A second run leaves a finished work commit as it is and commits a set only when it is still uncommitted and still allowed. Commit only when the resolved `commit` value allows it.

### Task 3: Mark the plan and publish

**Files:**

- Modify: `docs/plans/2026-10-03-review-skills.md`

- [x] **Step 1: Mark the finished checkboxes**

When every checkbox in this plan is `- [x]`, mark this step done.

Otherwise mark each finished step `- [x]`. Leave a step that did not run empty.

- [x] **Step 2: Commit the checkbox update**

`commit-plans` governs this step. Stage only this plan. Commit only when that value allows it and the plan file is still uncommitted. A second run leaves a finished plan commit as it is.

- [x] **Step 3: Push and open the pull request**

Resolve `push`. Push when that value allows it. Resolve `pull-request`. Open one pull request when that value allows it. Resolve `merge` and stop when that value is `never`. Do not force-push.
