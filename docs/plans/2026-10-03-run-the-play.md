# Run the Play Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `run-the-play` and the four playbooks `feature`, `bug-fix`, `refactor`, and `investigation`, with the skill's section bodies and each playbook's section bodies pinned to the spec, and bump the plugin to `0.8.0`.

**Architecture:** The new spec is the only copy of the skill's section bodies and of the playbook section bodies. `tests/check_plugin.py` reads the skill headings from the spec and from `SKILL.md` and requires the paragraphs to match. It discovers each `## Playbook:` region in the spec and requires the matching file under `skills/run-the-play/playbooks/`. The check, the two manifests, and `docs/skills.md` are the other files this change edits. The new skill and the playbooks land under `skills/`. The work stays on `feat/run-the-play`, cut from `main`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-03-run-the-play-design.md`

This plan and that spec are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. Copy each playbook region into its file as this plan's Task 2 Step 2 describes. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 4 of Task 2.

## Global Constraints

- The skill name is `run-the-play`. Plugin name and marketplace name stay `kobold-codex`.
- `run-the-play` description is one physical line: `Use when a task should follow a playbook. Match it to one playbook, copy that playbook's steps into the working list, record a skip with a reason, and stop where the resolved bounds say to stop.`
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.8.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are.
- Skill heading names, in order: `The match`, `The list`, `A step left out`, `Where it stops`, `The same task`. The skill title is `Run the play`.
- Playbook files, titles, and `##` headings, in order. The title is the file name with hyphens written as spaces and the first letter capitalized.
  - `feature.md`, title `Feature`: `Scope`, `Shape`, `Build`, `Prove`.
  - `bug-fix.md`, title `Bug fix`: `Reproduce`, `Cause`, `Fix`, `Again`.
  - `refactor.md`, title `Refactor`: `Behavior`, `Scope`, `Shape`, `Reshape`, `The same behavior`.
  - `investigation.md`, title `Investigation`: `The question`, `The read`, `No edit`.
- Each skill section body equals that heading's body in the spec. Each playbook section body equals that heading's body in its `## Playbook:` region. `feature` and `refactor` both have a section named `Scope`. Compare each one inside its own region.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, `skills/write-the-plan/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, `skills/review-the-diff/SKILL.md`, `skills/take-the-review/SKILL.md`, `skills/stress-the-change/SKILL.md`, `skills/ship-the-branch/SKILL.md`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs, playbook briefs, and ship rule stay.
- No new skill and no playbook names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`. Playbook files have no frontmatter.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links the new skill and its spec. The new map sentences are the paragraphs in Task 2 Step 3. They do not copy a skill section body or a playbook section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.
- Publishing follows the resolved bounds. `commit-specs` governs the spec commit. `commit-plans` governs this plan. `commit` governs the skill, playbooks, check, manifest, and map commit. `push` and `pull-request` govern publishing the branch. `merge` stays on its own key. Name each key, the value, and the layer that set it before that action.
- Commit subjects are one line. The spec commit is `Record the run-the-play spec`. The plan commit is `Add the plan for run-the-play`. The work commit is `Add the run-the-play skill`. The checkbox commit is `Mark the finished run-the-play plan steps`. The commit after the pull request is open is `Mark the run-the-play plan published`.

## Review Focus

- A section body in the new skill, or in a playbook, is a paraphrase of its spec. The section compare must fail.
- Two `Scope` sections are compared through the flat heading map of the whole spec, so one playbook's body is checked against the other's. That compare must fail closed: each region is sliced on its own.
- A playbook's `##` headings are swapped. The order compare must fail.
- The `playbooks` directory contains a markdown file the spec does not name, or omits one the spec names. The name compare must fail.
- The README repeats a section body from any shipped skill or from a playbook. The README compare must fail.
- `plugin.json` stays at `0.7.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts the new description on more than one line, or a playbook file starts with frontmatter. The frontmatter compare must fail.
- A file named in Global Constraints as not edited shows a diff. That diff must fail the review.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Commit the spec and this plan

**Files:**

- Already written: `docs/specs/2026-10-03-run-the-play-design.md`
- Already written: `docs/plans/2026-10-03-run-the-play.md`

**Interfaces:**

- Consumes: the spec and this plan, already in the worktree on `feat/run-the-play`.
- Produces: two commits when the resolved keys allow them. The spec commit contains only the spec. The plan commit contains only this plan. The checkboxes in that plan commit are still empty.

- [ ] **Step 1: Commit the spec**

When the spec is already committed on this branch, mark this step done and go to Step 2.

Otherwise resolve `commit-specs` and commit only that file when that value allows it. Leave this plan unstaged. The subject is `Record the run-the-play spec`. The body says the spec records `run-the-play` and the four playbooks, and that the skill file is not in this commit. A second run leaves a finished spec commit as it is.

- [ ] **Step 2: Commit this plan**

When this plan is already committed, mark this step done.

Otherwise resolve `commit-plans` and commit only this file when that value allows it. Leave the checkboxes empty in that commit. The subject is `Add the plan for run-the-play`. The checkbox update is Task 3.

### Task 2: Pin the check, add the skill and the playbooks, bump the plugin

**Files:**

- Create: `skills/run-the-play/SKILL.md`
- Create: `skills/run-the-play/playbooks/feature.md`
- Create: `skills/run-the-play/playbooks/bug-fix.md`
- Create: `skills/run-the-play/playbooks/refactor.md`
- Create: `skills/run-the-play/playbooks/investigation.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under the spec's `## Skill` heading, and each `## Playbook:` region. The checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.8.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [ ] **Step 1: Extend the check and confirm it fails**

When `tests/check_plugin.py` already requires the new skill, version `0.8.0`, the two new guide links, and one file per `## Playbook:` region, mark this step done and go to Step 2.

Otherwise, add a spec path, a skill path, a description constant, and a headings tuple for the new skill. Point the spec path at `docs/specs/2026-10-03-run-the-play-design.md`. Add the description line from Global Constraints. Use the skill heading names from Global Constraints, in that order.

Leave `PLUGIN_DESCRIPTION` as the stable sentence. Change the required plugin version from `0.7.0` to `0.8.0`. Append these two strings to `GUIDE_LINKS`, after the `ship-the-branch` pair:

```text
skills/run-the-play/SKILL.md
docs/specs/2026-10-03-run-the-play-design.md
```

Call `check_one` for the new skill after the `ship-the-branch` call. Leave the existing `check_one` calls as they are.

Add a playbook check that runs after that `check_one`. Discover regions from lines that match `## Playbook: <name>`, where the name is lowercase words separated by hyphens. Do not hardcode the four names. The spec is the list. A spec with no such region fails the check.

A region runs from the line after its heading to the line before the next `## ` heading that is not `###`. Inside the region, every heading is level 3. Those titles, in order, are the steps. Their bodies are normalized the same way `sections` normalizes a body.

The file is `skills/run-the-play/playbooks/<name>.md`. Its title is the name with hyphens written as spaces and the first letter capitalized. Fail when any of these is true:

- The file is missing. The message names that path and says `missing`.
- The file starts with frontmatter (`---`).
- The text before the first `##` heading, with the `# <title>` line removed, is not empty.
- The file's first heading is not that title at level 1.
- The file's level-2 headings are not exactly those step titles, in that order.
- A step body differs from the region's level-3 body for that title.
- A step body is empty.
- A step body appears in `README.md`.
- A `*.md` file in that directory is not one of the discovered names.

`feature` and `refactor` both use the heading `Scope`. Look up each body inside its own region. A flat map of the whole spec is the wrong lookup.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `run-the-play`. The creed sections are not the failure.

- [ ] **Step 2: Write the skill and the four playbooks**

When `skills/run-the-play/SKILL.md` already carries the frontmatter and the section bodies from the spec, leave that file. Otherwise create it.

The file starts with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The description stays on one physical line. The H1 title is `Run the play`. Copy each section body from the spec. Do not rewrap a copied line.

When a playbook file already carries the title and the section bodies from its region, leave that file. Otherwise create it. The first line is `#` and the title from Global Constraints. Then a blank line. Then each `###` step from that region copied as `##`, with the same body and the same line breaks. No frontmatter. No extra prose. The directory contains only the four files the spec names.

- [ ] **Step 3: Bump the manifests and the skill map**

Set `"version"` to `0.8.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave `"description"` as `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` Leave the other manifest fields as they are. Do not add a version field to the marketplace object.

Leave `README.md` as it is. In `docs/skills.md`, under Which skill applies, add this paragraph after the `ship-the-branch` paragraph:

```markdown
A task that should follow a playbook uses [skills/run-the-play/SKILL.md](../skills/run-the-play/SKILL.md).
```

Under Records, add this item after the `ship-the-branch` item:

```markdown
- [skills/run-the-play/SKILL.md](../skills/run-the-play/SKILL.md) is recorded in [docs/specs/2026-10-03-run-the-play-design.md](specs/2026-10-03-run-the-play-design.md).
```

When that version and those two sentences are already present, leave them.

- [ ] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.8.0`, the stable description, and `1 skill dir(s)`.

Confirm a drifted playbook paragraph fails the check, then restore the copied body. Confirm two `##` headings in one playbook swapped in order fail the check, then restore the order. Confirm a version left at `0.7.0` in both manifests fails the check, then restore `0.8.0`. Confirm the files Global Constraints says are not edited have an empty diff against `main`. The spec and this plan are new files, so they sit outside that empty-diff check.

The new playbook check has branches for a missing file, frontmatter, a wrong title, a wrong heading order, a mismatched body, an empty body, a README restatement, and an extra markdown file. The missing-file branch is the failure in Step 1. The body branch and the order branch are the two confirms above. The other branches are the conditions in Step 1. Say in the reply which of those confirms were run.

- [ ] **Step 5: Commit the work**

`commit` governs this step. Stage the skill, the four playbooks, `tests/check_plugin.py`, both manifests, and `docs/skills.md`. Leave the spec and this plan in their own commits. A second run leaves a finished work commit as it is and commits a set only when it is still uncommitted and still allowed. Commit only when the resolved `commit` value allows it.

The subject is `Add the run-the-play skill`. The body names the skill, the four playbooks, and version `0.8.0`. Under a Test plan heading, write three GitHub task items:

1. `python3 tests/check_plugin.py` exits 0.
2. A drifted playbook paragraph, a swapped playbook heading order, and a version left at `0.7.0` each fail that check.
3. `grok plugin validate .` reports version `0.8.0` and `1 skill dir(s)`.

Mark an item done only when that command was run and passed, and the tree was restored afterward. Those three items belong to the commit message. They are not steps of this plan. The version drift is part of item 2. Run it in Step 4 with the other two confirms, then restore `0.8.0`.

### Task 3: Mark the plan and publish

**Files:**

- Modify: `docs/plans/2026-10-03-run-the-play.md`

- [ ] **Step 1: Mark the finished checkboxes**

When every checkbox in this plan except Step 3 and Step 4 of this task is `- [x]`, mark this step done.

Otherwise mark each finished step `- [x]`. Leave Step 3 and Step 4 of this task empty. Leave a step that did not run empty.

- [ ] **Step 2: Commit the checkbox update**

`commit-plans` governs this step. Stage only this plan. The subject is `Mark the finished run-the-play plan steps`. Commit only when that value allows it and the plan file is still uncommitted. A second run leaves a finished plan commit as it is.

- [ ] **Step 3: Push and open the pull request**

Resolve `push`. Push when that value allows it. Resolve `pull-request`. Open one pull request when that value allows it. Resolve `merge` and stop when that value is `never`. Do not force-push. There is no worktree to remove.

- [ ] **Step 4: Mark this publish step**

When Step 3 did not open the pull request, leave this step empty.

When the pull request is open, mark Step 3 and this step `- [x]`. Resolve `commit-plans` and commit only this plan when that value allows it and the plan file is still uncommitted. The subject is `Mark the run-the-play plan published`.
