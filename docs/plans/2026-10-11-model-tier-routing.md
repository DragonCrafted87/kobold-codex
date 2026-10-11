# Model Tier Routing Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship the model tier routing revision. Plan tasks carry a work kind, fast kinds go to the fast model under `model-fast`, one `subagents` yes covers a plan run, a commit is gated on a filtered test list when the repo can produce one, `adopt-the-repo` suggests both model keys from the host's own list, and the plugin becomes `1.1.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. Each `## Skill: <name>` region in the spec names one skill file. Each `###` section in a region replaces the `##` section with the same heading in that file, or is a new `##` section placed where the region says. Sections a region does not name stay as they are. `carry-out-the-plan` is the main change: kinds, the fast model, the brief, one takeover from the worker's diff, a fixed list of moves after a failed run, narrow checks, and the gate. `ship-the-branch` carries the same gate for commits outside a plan run. `set-the-bounds` gains `model-fast` and the plan-run yes. `write-the-plan` gains the kind line. `fan-out` and `try-several-shapes` read `model` and the fast model. `adopt-the-repo` gains the two model rows. `write-a-skill` loses its stale line about the check. The work stays on `model-tier-routing`, cut from `main` at `9532657`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-11-model-tier-routing-design.md`

The spec is already committed on this branch. Copy each `###` body in a Skill region into the matching `##` section of that skill file, including line breaks. If a sentence in this plan disagrees with the spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Task 3.

## Global Constraints

- Plugin name and marketplace name stay `kobold-codex`. No skill is added or renamed.
- `carry-out-the-plan` description becomes one physical line: `Use when a plan has been approved. Run its tasks in order, hand fast tasks and independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.` Every other description stays.
- `carry-out-the-plan` headings, in order: `An approved plan`, `In order`, `Beside this session`, `The fast model`, `The brief`, `The check`, `A failed run`, `The same plan`.
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `1.1.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are. `1.1.0` is a minor bump because skills gain behavior and none is removed. `1.0.0` is the version on `main`.
- No skill names a Grok tool, a Claude tool, or a model by brand. No hooks. The repo has no `hooks/` directory and no `hooks.json`.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/stress-the-change/SKILL.md`, `skills/review-the-diff/SKILL.md`, `skills/run-the-play/SKILL.md`, the four files in `skills/run-the-play/playbooks/`, every other skill outside the eight in the spec's Where the words live, every earlier spec, `README.md`, and `tests/check_plugin.py`.
- `docs/skills.md` gains one bullet under Records and nothing else. The bullet does not restate a section body.
- A plan run that never commits leaves the gate to `ship-the-branch`. The gate in `carry-out-the-plan` runs before each commit of the work, so a run with no commit runs no gate of its own. `ship-the-branch` runs the gate before its first commit, so the work is still gated before it lands. That is acceptable, and this change adds no gate at the end of a plan run.
- No tracked file contains a hostname, a home-directory path, or a machine name.
- Publishing follows the resolved bounds. `commit-plans` governs this plan, and the repo layer sets it to `auto`. `commit` governs the skills, the map, and the manifests, and it is `ask` from the defaults. The user's request to commit those changes on this branch is the yes. `push` is `ask`, and this run does not push.
- Commit subjects are one line. The plan commit is `Add the plan for model tier routing`. The skill commit is `Route fast plan tasks to a faster model`. The version commit is `Mark the plugin at 1.1.0`. The checkbox commit is `Mark the finished model tier routing plan steps`.

## Review Focus

- A skill section paraphrases its spec region. The two copies must match, including line breaks.
- A section the spec region does not name shows a diff. That diff must fail the review.
- The `carry-out-the-plan` description wraps onto a second physical line, or its headings are out of the order in Global Constraints. That file must fail the review.
- A skill names a host tool or a model by brand. The grep must fail.
- A file named in Global Constraints as not edited shows a diff against `main`. That diff must fail the review.
- The two manifests disagree on version or description, or either is not `1.1.0`. The check must fail.
- `docs/skills.md` changes outside the one Records bullet. That diff must fail the review.

---

### Task 1: Write the spec

Kind: design

**Files:**

- Create: `docs/specs/2026-10-11-model-tier-routing-design.md`

**Interfaces:**

- Consumes: the approved design and the review answers.
- Produces: the committed spec at `fbb3e5a`.

- [ ] **Step 1: Confirm the spec is committed**

The check is `git log --oneline -- docs/specs/2026-10-11-model-tier-routing-design.md`. Done means the log shows `6f7c4a1` and `fbb3e5a`, and `git status` shows no change to the spec.

### Task 2: Apply the Skill regions

Kind: docs-or-config

**Files:**

- Modify: `skills/set-the-bounds/SKILL.md`
- Modify: `skills/write-the-plan/SKILL.md`
- Modify: `skills/carry-out-the-plan/SKILL.md`
- Modify: `skills/fan-out/SKILL.md`
- Modify: `skills/try-several-shapes/SKILL.md`
- Modify: `skills/ship-the-branch/SKILL.md`
- Modify: `skills/adopt-the-repo/SKILL.md`
- Modify: `skills/write-a-skill/SKILL.md`
- Modify: `docs/skills.md`

**Interfaces:**

- Consumes: the eight `## Skill: <name>` regions of the spec.
- Produces: eight skill files whose named sections match the spec, and one Records bullet.

- [ ] **Step 1: Replace and add the sections**

For each region, replace each named `##` section body with the `###` body from the spec. In `carry-out-the-plan`, add `The fast model` and `The brief` after `Beside this session`, add `A failed run` after `The check`, and replace the description with the line in Global Constraints. The `write-a-skill` region carries the fix for the stale line about the check.

The check is a script that reads each region from the spec and compares each `###` body with the `##` body of the same heading in the skill file. Done means every body matches, and `git diff main -- skills/` shows changes only in the named sections and in the one description.

- [ ] **Step 2: Add the Records bullet**

In `docs/skills.md`, under Records, add this bullet after the `adopt-the-repo` bullet:

```text
- The model tier routing revision of `set-the-bounds`, `write-the-plan`, `carry-out-the-plan`, `fan-out`, `try-several-shapes`, `ship-the-branch`, `adopt-the-repo`, and `write-a-skill` is recorded in [docs/specs/2026-10-11-model-tier-routing-design.md](specs/2026-10-11-model-tier-routing-design.md).
```

The check is `git diff main -- docs/skills.md`. Done means the diff is that one line.

- [ ] **Step 3: Commit the skills and the map**

Resolve `commit`. Commit the eight skill files and `docs/skills.md` when that value allows it. Leave the manifests and this plan out of that commit. The subject is in Global Constraints. The body names the routing, the plan-run yes, the gate, the model rows, and the stale-line fix.

### Task 3: Bump the version and run the checks

Kind: follow-a-pattern

**Files:**

- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Test: `python3 tests/check_plugin.py`
- Test: `grok plugin validate .`

**Interfaces:**

- Consumes: the manifests at `1.0.0`. The version bump commit `Mark the plugin at 1.0.0` is the pattern.
- Produces: both manifests at `1.1.0` with the stable description.

- [ ] **Step 1: Bump the manifests**

Set `version` to `1.1.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. Leave both descriptions as the stable sentence.

The check is a read of both `version` fields. Done means both are `1.1.0`.

- [ ] **Step 2: Run the checks**

Run `python3 tests/check_plugin.py` from the repository root. Then run the spec's Implementation check: compare each region with its skill file, read the `carry-out-the-plan` heading order and description, grep `skills/` for host tool names and model brand names, run `git diff --stat main` over the files Global Constraints lists as not edited, confirm the repo has no `hooks/` directory and no `hooks.json`, and scan tracked files for a hostname, a home-directory path, or a machine name. Then run `grok plugin validate .`.

Done means `python3 tests/check_plugin.py` exits 0 with no stderr, with `1.1.0` ahead of `1.0.0` on `main`, and every Implementation check item holds. There is no new function in the check, so the real-code bar in `scope-the-edit` has no branch to cover. If `grok` is not on the path, say so and leave that check open.

- [ ] **Step 3: Commit the version**

Resolve `commit`. Commit the two manifests when that value allows it. The subject is in Global Constraints.

### Task 4: Mark the plan

Kind: docs-or-config

**Files:**

- Modify: `docs/plans/2026-10-11-model-tier-routing.md`

**Interfaces:**

- Consumes: Tasks 1 to 3 finished.
- Produces: the finished checkboxes, committed under `commit-plans`.

- [ ] **Step 1: Mark and commit the finished steps**

Mark each finished step `- [x]`. Resolve `commit-plans` and commit only this file. The subject is in Global Constraints. Do not push. `push` is `ask`, and this run has no yes for it.

The check is `git status --short`. Done means the tree is clean and the plan shows every finished step marked.
