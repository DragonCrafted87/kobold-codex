# Remaining Skills Implementation Plan

> **For agentic workers:** Implement this task after the specs are reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship the eleven build-order step 7 skills, with each skill's section bodies pinned to its spec, and bump the plugin to `0.9.0`.

**Architecture:** Each new spec is the only copy of that skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The check, the two manifests, and `docs/skills.md` are the shared files this change edits. The eleven skills land under `skills/`. The work stays on `feat/remaining-skills`, cut from `main` at `5342007`. No worktree. The eleven skills share those three files, so they land in one work commit.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-03-isolate-the-work-design.md`
- `docs/specs/2026-10-03-fan-out-design.md`
- `docs/specs/2026-10-03-try-several-shapes-design.md`
- `docs/specs/2026-10-03-measure-the-blast-design.md`
- `docs/specs/2026-10-03-prove-the-product-design.md`
- `docs/specs/2026-10-03-leave-a-trail-design.md`
- `docs/specs/2026-10-03-pick-up-the-work-design.md`
- `docs/specs/2026-10-03-learn-from-the-session-design.md`
- `docs/specs/2026-10-03-write-a-skill-design.md`
- `docs/specs/2026-10-03-cut-the-slop-design.md`
- `docs/specs/2026-10-03-write-the-doc-design.md`

This plan and those specs are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 4 of Task 2.

## Global Constraints

- Skill names, in this order: `isolate-the-work`, `fan-out`, `try-several-shapes`, `measure-the-blast`, `prove-the-product`, `leave-a-trail`, `pick-up-the-work`, `learn-from-the-session`, `write-a-skill`, `cut-the-slop`, `write-the-doc`. Plugin name and marketplace name stay `kobold-codex`.
- Each description is one physical line.
  - `isolate-the-work`: `Use when feature work, or the execution of a plan, should sit in its own checkout. Create that checkout when worktrees allows it, and record the path so ship-the-branch can remove it.`
  - `fan-out`: `Use when work that does not share state should run as parallel workers. Split it, wait for the workers, and return one report. subagents has to allow the parallel form.`
  - `try-several-shapes`: `Use when the first shape of a change would stick. Run several candidates, pick a base, and fold the strongest pieces of the others into it.`
  - `measure-the-blast`: `Use before a small diff ships. Name what else could break outside the diff, and prove that claim by running the code that would show the break.`
  - `prove-the-product`: `Use when a repo has no scripted way to drive the app the way a user does. Write a project-local verification skill, prove it once, and re-run it so the map stays honest.`
  - `leave-a-trail`: `Use for a long run or an unattended run. Append one row per decision, with what, why, evidence, and result, to a log a reviewer can read afterward.`
  - `pick-up-the-work`: `Use when a new session should continue work already in progress. Rebuild a short brief from the branch, the transcript, and the trail.`
  - `learn-from-the-session`: `Use after a session that stumbled, or that found a preference worth keeping. Name the lesson and edit the skill, playbook, or bounds file that should carry it.`
  - `write-a-skill`: `Use when authoring or revising a skill in this plugin. Write one trigger description, original wording, and a check that the skill file matches its spec.`
  - `cut-the-slop`: `Use when prose or a diff needs a pass for narration, stock phrasing, and comments that restate the code. Encode a real constraint in the structure, then drop the comment.`
  - `write-the-doc`: `Use when writing or revising a README, a spec, a pull request, or a commit message. Use the headings the project already uses, in sentences a new reader can follow.`
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.9.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order. The title is the skill name with hyphens written as spaces and the first letter capitalized.
  - `isolate-the-work`, title `Isolate the work`: `The work`, `The key`, `The checkout`, `The path`, `The same work`.
  - `fan-out`, title `Fan out`: `The pieces`, `The workers`, `One report`, `The same split`.
  - `try-several-shapes`, title `Try several shapes`: `The moment`, `The candidates`, `The base`, `The fold`, `The same attempt`.
  - `measure-the-blast`, title `Measure the blast`: `The diff`, `The claim`, `The run`, `Leave the tree`, `The same diff`.
  - `prove-the-product`, title `Prove the product`: `The drive`, `The skill file`, `Prove it once`, `A later pass`, `The same map`.
  - `leave-a-trail`, title `Leave a trail`: `When it starts`, `The row`, `Where it lives`, `The same run`.
  - `pick-up-the-work`, title `Pick up the work`: `The sources`, `The brief`, `Leave the tree`, `The same point`.
  - `learn-from-the-session`, title `Learn from the session`: `The lesson`, `The home`, `The edit`, `The same lesson`.
  - `write-a-skill`, title `Write a skill`: `The trigger`, `The spec`, `The file`, `The check`, `The same skill`.
  - `cut-the-slop`, title `Cut the slop`: `The pass`, `What comes out`, `A constraint`, `The same pass`.
  - `write-the-doc`, title `Write the doc`: `The document`, `The headings`, `The sentences`, `Where it stops`, `The same document`.
- Each section body equals that heading's body in its own spec. `measure-the-blast` and `pick-up-the-work` both have a section named `Leave the tree`. Compare each one inside its own spec.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, `skills/write-the-plan/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, `skills/review-the-diff/SKILL.md`, `skills/take-the-review/SKILL.md`, `skills/stress-the-change/SKILL.md`, `skills/ship-the-branch/SKILL.md`, `skills/run-the-play/SKILL.md`, the four files in `skills/run-the-play/playbooks/`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs, playbook briefs, and ship rule stay. The nine playbook briefs that are not files yet stay briefs.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links each new skill and its spec. The new map sentences are the paragraphs in Task 2 Step 3. They do not copy a skill section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.
- Publishing follows the resolved bounds. `commit-specs` governs the spec commit. `commit-plans` governs this plan. `commit` governs the skill, check, manifest, and map commit. `push` and `pull-request` govern publishing the branch. `merge` stays on its own key. Name each key, the value, and the layer that set it before that action.
- Commit subjects are one line. The spec commit is `Record the remaining skill specs`. The plan commit is `Add the plan for the remaining skills`. The work commit is `Add the remaining skills`. The checkbox commit is `Mark the finished remaining-skills plan steps`. The commit after the pull request is open is `Mark the remaining-skills plan published`.
- `tests/check_plugin.py` gains no new function. `check_one` already compares a skill to its spec. This change adds constants and eleven `check_one` calls. It does not add a heading-order check. Copy the sections in the spec's order anyway.

## Review Focus

- A section body in a new skill is a paraphrase of its spec. The section compare must fail.
- `Leave the tree` from `measure-the-blast` is compared with `Leave the tree` from `pick-up-the-work` through one shared lookup. That compare must fail closed: each spec is passed to its own `check_one`.
- A new skill file is missing. The missing-file compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.8.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts a new description on more than one line. The frontmatter compare must fail.
- A file named in Global Constraints as not edited shows a diff. That diff must fail the review.
- A public file names a machine or a home path. The needle scan must fail.
- The nine playbook briefs gain files under `skills/run-the-play/playbooks/`. The playbook name compare must fail.

---

### Task 1: Commit the specs and this plan

**Files:**

- Already written: the eleven specs listed above
- Already written: `docs/plans/2026-10-03-remaining-skills.md`

**Interfaces:**

- Consumes: the specs and this plan, already in the worktree on `feat/remaining-skills`.
- Produces: two commits when the resolved keys allow them. The spec commit contains only the eleven specs. The plan commit contains only this plan. The checkboxes in that plan commit are still empty.

- [x] **Step 1: Commit the specs**

When the eleven specs are already committed on this branch, mark this step done and go to Step 2.

Otherwise resolve `commit-specs` and commit only those eleven files when that value allows it. Leave this plan unstaged. The subject is `Record the remaining skill specs`. The body says the specs record the eleven step-7 skills, and that the skill files are not in this commit. A second run leaves a finished spec commit as it is.

- [x] **Step 2: Commit this plan**

When this plan is already committed, mark this step done.

Otherwise resolve `commit-plans` and commit only this file when that value allows it. Leave the checkboxes empty in that commit. The subject is `Add the plan for the remaining skills`. The checkbox update is Task 3.

### Task 2: Pin the check, add the eleven skills, bump the plugin

**Files:**

- Create: `skills/isolate-the-work/SKILL.md`
- Create: `skills/fan-out/SKILL.md`
- Create: `skills/try-several-shapes/SKILL.md`
- Create: `skills/measure-the-blast/SKILL.md`
- Create: `skills/prove-the-product/SKILL.md`
- Create: `skills/leave-a-trail/SKILL.md`
- Create: `skills/pick-up-the-work/SKILL.md`
- Create: `skills/learn-from-the-session/SKILL.md`
- Create: `skills/write-a-skill/SKILL.md`
- Create: `skills/cut-the-slop/SKILL.md`
- Create: `skills/write-the-doc/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under each spec's `## Skill` heading. The checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.9.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [x] **Step 1: Extend the check and confirm it fails**

When `tests/check_plugin.py` already requires the eleven skills, version `0.9.0`, and the twenty-two new guide links, mark this step done and go to Step 2.

Otherwise add a spec path, a skill path, a description constant, and a headings tuple for each skill. Point each spec path at the file listed under Specs. Add each description line from Global Constraints. Use the heading names from Global Constraints, in that order.

Constants, in the skill order above:

- `ISOLATE_SPEC`, `ISOLATE_SKILL`, `ISOLATE_DESCRIPTION`, `ISOLATE_HEADINGS`
- `FAN_SPEC`, `FAN_SKILL`, `FAN_DESCRIPTION`, `FAN_HEADINGS`
- `SHAPES_SPEC`, `SHAPES_SKILL`, `SHAPES_DESCRIPTION`, `SHAPES_HEADINGS`
- `BLAST_SPEC`, `BLAST_SKILL`, `BLAST_DESCRIPTION`, `BLAST_HEADINGS`
- `PROVE_SPEC`, `PROVE_SKILL`, `PROVE_DESCRIPTION`, `PROVE_HEADINGS`
- `TRAIL_SPEC`, `TRAIL_SKILL`, `TRAIL_DESCRIPTION`, `TRAIL_HEADINGS`
- `PICKUP_SPEC`, `PICKUP_SKILL`, `PICKUP_DESCRIPTION`, `PICKUP_HEADINGS`
- `LEARN_SPEC`, `LEARN_SKILL`, `LEARN_DESCRIPTION`, `LEARN_HEADINGS`
- `AUTHOR_SPEC`, `AUTHOR_SKILL`, `AUTHOR_DESCRIPTION`, `AUTHOR_HEADINGS` for `write-a-skill`
- `SLOP_SPEC`, `SLOP_SKILL`, `SLOP_DESCRIPTION`, `SLOP_HEADINGS` for `cut-the-slop`
- `DOC_SPEC`, `DOC_SKILL`, `DOC_DESCRIPTION`, `DOC_HEADINGS` for `write-the-doc`

Leave `PLUGIN_DESCRIPTION` as the stable sentence. Change the required plugin version from `0.8.0` to `0.9.0`. Append these twenty-two strings to `GUIDE_LINKS`, after the `run-the-play` pair, in the skill order above. Each pair is the skill path, then the spec path:

```text
skills/isolate-the-work/SKILL.md
docs/specs/2026-10-03-isolate-the-work-design.md
skills/fan-out/SKILL.md
docs/specs/2026-10-03-fan-out-design.md
skills/try-several-shapes/SKILL.md
docs/specs/2026-10-03-try-several-shapes-design.md
skills/measure-the-blast/SKILL.md
docs/specs/2026-10-03-measure-the-blast-design.md
skills/prove-the-product/SKILL.md
docs/specs/2026-10-03-prove-the-product-design.md
skills/leave-a-trail/SKILL.md
docs/specs/2026-10-03-leave-a-trail-design.md
skills/pick-up-the-work/SKILL.md
docs/specs/2026-10-03-pick-up-the-work-design.md
skills/learn-from-the-session/SKILL.md
docs/specs/2026-10-03-learn-from-the-session-design.md
skills/write-a-skill/SKILL.md
docs/specs/2026-10-03-write-a-skill-design.md
skills/cut-the-slop/SKILL.md
docs/specs/2026-10-03-cut-the-slop-design.md
skills/write-the-doc/SKILL.md
docs/specs/2026-10-03-write-the-doc-design.md
```

Call `check_one` for each new skill after the `run-the-play` call and before `check_playbooks`. Leave the existing `check_one` calls as they are. Pass each skill its own spec. Do not build one heading map from all eleven specs.

Wrap each description constant the way the existing description constants are wrapped. The concatenated value equals the one physical line in Global Constraints.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `isolate-the-work`. The creed sections are not the failure. This exercises the missing-file branch of `check_one`. No new function was added, so there is no new branch to cover.

- [x] **Step 2: Write the eleven skills**

When a skill file already carries the frontmatter and the section bodies from its spec, leave that file. Otherwise create it.

The file starts with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The description stays on one physical line. The H1 title is the title from Global Constraints. Copy each section body from that skill's spec. Do not rewrap a copied line.

- [x] **Step 3: Bump the manifests and the skill map**

Set `"version"` to `0.9.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave `"description"` as `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.` Leave the other manifest fields as they are. Do not add a version field to the marketplace object.

Leave `README.md` as it is. In `docs/skills.md`, under Which skill applies, add these paragraphs after the `run-the-play` paragraph:

```markdown
Feature work, or the execution of a plan, in its own checkout uses [skills/isolate-the-work/SKILL.md](../skills/isolate-the-work/SKILL.md).

Work that does not share state uses [skills/fan-out/SKILL.md](../skills/fan-out/SKILL.md).

A change whose first shape would stick uses [skills/try-several-shapes/SKILL.md](../skills/try-several-shapes/SKILL.md).

A small diff, before it ships, uses [skills/measure-the-blast/SKILL.md](../skills/measure-the-blast/SKILL.md).

A repo with no scripted way to drive the app the way a user does uses [skills/prove-the-product/SKILL.md](../skills/prove-the-product/SKILL.md).

A long run or an unattended run uses [skills/leave-a-trail/SKILL.md](../skills/leave-a-trail/SKILL.md).

A new session continuing work already in progress uses [skills/pick-up-the-work/SKILL.md](../skills/pick-up-the-work/SKILL.md).

A lesson from a session that stumbled, or from a preference worth keeping, uses [skills/learn-from-the-session/SKILL.md](../skills/learn-from-the-session/SKILL.md).

Authoring or revising a skill in this plugin uses [skills/write-a-skill/SKILL.md](../skills/write-a-skill/SKILL.md).

A pass over prose or a diff for narration, stock phrasing, and comments that restate the code uses [skills/cut-the-slop/SKILL.md](../skills/cut-the-slop/SKILL.md).

A README, a spec, a pull request, or a commit message uses [skills/write-the-doc/SKILL.md](../skills/write-the-doc/SKILL.md).
```

Under Records, add these items after the `run-the-play` item:

```markdown
- [skills/isolate-the-work/SKILL.md](../skills/isolate-the-work/SKILL.md) is recorded in [docs/specs/2026-10-03-isolate-the-work-design.md](specs/2026-10-03-isolate-the-work-design.md).
- [skills/fan-out/SKILL.md](../skills/fan-out/SKILL.md) is recorded in [docs/specs/2026-10-03-fan-out-design.md](specs/2026-10-03-fan-out-design.md).
- [skills/try-several-shapes/SKILL.md](../skills/try-several-shapes/SKILL.md) is recorded in [docs/specs/2026-10-03-try-several-shapes-design.md](specs/2026-10-03-try-several-shapes-design.md).
- [skills/measure-the-blast/SKILL.md](../skills/measure-the-blast/SKILL.md) is recorded in [docs/specs/2026-10-03-measure-the-blast-design.md](specs/2026-10-03-measure-the-blast-design.md).
- [skills/prove-the-product/SKILL.md](../skills/prove-the-product/SKILL.md) is recorded in [docs/specs/2026-10-03-prove-the-product-design.md](specs/2026-10-03-prove-the-product-design.md).
- [skills/leave-a-trail/SKILL.md](../skills/leave-a-trail/SKILL.md) is recorded in [docs/specs/2026-10-03-leave-a-trail-design.md](specs/2026-10-03-leave-a-trail-design.md).
- [skills/pick-up-the-work/SKILL.md](../skills/pick-up-the-work/SKILL.md) is recorded in [docs/specs/2026-10-03-pick-up-the-work-design.md](specs/2026-10-03-pick-up-the-work-design.md).
- [skills/learn-from-the-session/SKILL.md](../skills/learn-from-the-session/SKILL.md) is recorded in [docs/specs/2026-10-03-learn-from-the-session-design.md](specs/2026-10-03-learn-from-the-session-design.md).
- [skills/write-a-skill/SKILL.md](../skills/write-a-skill/SKILL.md) is recorded in [docs/specs/2026-10-03-write-a-skill-design.md](specs/2026-10-03-write-a-skill-design.md).
- [skills/cut-the-slop/SKILL.md](../skills/cut-the-slop/SKILL.md) is recorded in [docs/specs/2026-10-03-cut-the-slop-design.md](specs/2026-10-03-cut-the-slop-design.md).
- [skills/write-the-doc/SKILL.md](../skills/write-the-doc/SKILL.md) is recorded in [docs/specs/2026-10-03-write-the-doc-design.md](specs/2026-10-03-write-the-doc-design.md).
```

When that version and those sentences are already present, leave them.

- [x] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.9.0`, the stable description, and `1 skill dir(s)`.

Confirm a drifted paragraph in `skills/isolate-the-work/SKILL.md` fails the check, then restore the copied body. Confirm a version left at `0.8.0` in both manifests fails the check, then restore `0.9.0`. Confirm the files Global Constraints says are not edited have an empty diff against `main`. The specs and this plan are new files, so they sit outside that empty-diff check.

The missing-file branch is the failure in Step 1. The body branch is the drifted paragraph. The version branch is the version confirm. Say in the reply which of those confirms were run. `check_one` is unchanged, so this task adds no new branch.

- [x] **Step 5: Commit the work**

`commit` governs this step. Stage the eleven skills, `tests/check_plugin.py`, both manifests, and `docs/skills.md`. Leave the specs and this plan in their own commits. A second run leaves a finished work commit as it is and commits a set only when it is still uncommitted and still allowed. Commit only when the resolved `commit` value allows it.

The subject is `Add the remaining skills`. The body names the eleven skills and version `0.9.0`. Under a Test plan heading, write three GitHub task items:

1. `python3 tests/check_plugin.py` exits 0.
2. A drifted paragraph in `skills/isolate-the-work/SKILL.md`, and a version left at `0.8.0`, each fail that check.
3. `grok plugin validate .` reports version `0.9.0` and `1 skill dir(s)`.

Mark an item done only when that command was run and passed, and the tree was restored afterward. Those three items belong to the commit message. They are not steps of this plan.

### Task 3: Mark the plan and publish

**Files:**

- Modify: `docs/plans/2026-10-03-remaining-skills.md`

- [x] **Step 1: Mark the finished checkboxes**

When every checkbox in this plan except Step 3 and Step 4 of this task is `- [x]`, mark this step done.

Otherwise mark each finished step `- [x]`. Leave Step 3 and Step 4 of this task empty. Leave a step that did not run empty.

- [x] **Step 2: Commit the checkbox update**

`commit-plans` governs this step. Stage only this plan. The subject is `Mark the finished remaining-skills plan steps`. Commit only when that value allows it and the plan file is still uncommitted. A second run leaves a finished plan commit as it is.

- [x] **Step 3: Push and open the pull request**

Resolve `push`. Push when that value allows it. Resolve `pull-request`. Open one pull request when that value allows it. Resolve `merge` and stop when that value is `never`. Do not force-push. There is no worktree to remove.

- [x] **Step 4: Mark this publish step**

When Step 3 did not open the pull request, leave this step empty.

When the pull request is open, mark Step 3 and this step `- [x]`. Resolve `commit-plans` and commit only this plan when that value allows it and the plan file is still uncommitted. The subject is `Mark the remaining-skills plan published`.
