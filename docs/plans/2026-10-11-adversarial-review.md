# Adversarial Review Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship the adversarial review revision. Each `stress-the-change` pass tries to break the change, every merged finding goes to a fresh verifier that rejects by default, a project can add its own reviewers and rules in a `project-review` skill, `adopt-the-repo` suggests and confirms a rigor level, a review of someone else's change comes out as comments ready to paste, `take-the-review` checks its fixes against the tree and takes blockers first, and the plugin becomes `1.2.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. Each `## Skill: <name>` region in the spec names one skill file. Each `###` section in a region replaces the `##` section with the same heading in that file, or is a new `##` section placed where the region says. Sections a region does not name stay as they are. `stress-the-change` is the main change: goals for the three passes, project reviewers, coverage, the refutation, and the merged list. `review-the-diff` holds the finding: project rules in the request pass, never-flag rules, the evidence bar, two severities, comments for another author, and the `project-review` format. `take-the-review` gains blockers first and the three fix claims. `carry-out-the-plan` reads a worker's diff from the tree. `set-the-bounds` gains the review-run yes. `adopt-the-repo` gains the rigor level and the review skill suggestion. The work stays on `adversarial-review`, cut from `main` at `c6a0411`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-11-adversarial-review-design.md`

The spec is already committed on this branch. Copy each `###` body in a Skill region into the matching `##` section of that skill file, including line breaks. If a sentence in this plan disagrees with the spec, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Task 3.

## Global Constraints

- Plugin name and marketplace name stay `kobold-codex`. No skill is added or renamed. `project-review` is a project skill a project writes, not a plugin skill.
- `stress-the-change` description becomes one physical line: `Use when a diff needs several independent reviews. Run separate passes that each try to break it, try to refute every finding, merge what survives into one list, and leave the tree alone.` Every other description stays.
- `stress-the-change` headings, in order: `The diff`, `Three passes`, `Project reviewers`, `One list`, `The refutation`, `Leave the tree`.
- `review-the-diff` headings, in order: `The diff`, `The request and the checks`, `Never flag`, `The evidence`, `Findings`, `For another author`, `The project's rules`, `Leave the tree`.
- `adopt-the-repo` headings, in order: `The choice`, `The sources`, `The move`, `The bounds`, `The rigor level`, `The review skill`, `The local repo`, `An empty tree`, `The same repo`.
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `1.2.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are. `1.2.0` is a minor bump because skills gain behavior and none is removed. `1.1.0` is the version on `main`.
- No skill names a Grok tool, a Claude tool, a model by brand, a code host, or a host review file. No hooks. The repo has no `hooks/` directory and no `hooks.json`.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/measure-the-blast/SKILL.md`, `skills/fan-out/SKILL.md`, `skills/ship-the-branch/SKILL.md`, `skills/run-the-play/SKILL.md`, the files in `skills/run-the-play/playbooks/`, every other skill outside the six in the spec's Where the words live, every earlier spec, `README.md`, and `tests/check_plugin.py`.
- `docs/skills.md` gains one bullet under Records and nothing else. The bullet does not restate a section body.
- No tracked file contains a hostname, a home-directory path, or a machine name.
- Publishing follows the resolved bounds. `commit-plans` governs this plan, and the repo layer sets it to `auto`. `commit` governs the skills, the map, and the manifests, and it is `ask` from the defaults. The user's request to commit those changes on this branch is the yes. `push` is `ask`, and this run does not push.
- Commit subjects are one line. The plan commit is `Add the plan for adversarial review`. The skill commit is `Make reviews try to break the change and refute their findings`. The version commit is `Mark the plugin at 1.2.0`. The checkbox commit is `Mark the finished adversarial review plan steps`.

## Review Focus

- A skill section paraphrases its spec region. The two copies must match, including line breaks.
- A section the spec region does not name shows a diff. That diff must fail the review.
- The `stress-the-change` description wraps onto a second physical line, or the headings of `stress-the-change`, `review-the-diff`, or `adopt-the-repo` are out of the order in Global Constraints. That file must fail the review.
- A skill names a host tool, a model by brand, a code host, or a host review file. The grep must fail.
- `adopt-the-repo` names a regulation. The grep must fail.
- A file named in Global Constraints as not edited shows a diff against `main`. That diff must fail the review.
- The two manifests disagree on version or description, or either is not `1.2.0`. The check must fail.
- `docs/skills.md` changes outside the one Records bullet. That diff must fail the review.

---

### Task 1: Write the spec

Kind: design

**Files:**

- Create: `docs/specs/2026-10-11-adversarial-review-design.md`

**Interfaces:**

- Consumes: the approved design and the review answers.
- Produces: the committed spec at `1982880`.

- [ ] **Step 1: Confirm the spec is committed**

The check is `git log --oneline -- docs/specs/2026-10-11-adversarial-review-design.md`. Done means the log shows `a85960e` and `1982880`, and `git status` shows no change to the spec.

### Task 2: Apply the Skill regions

Kind: docs-or-config

**Files:**

- Modify: `skills/stress-the-change/SKILL.md`
- Modify: `skills/review-the-diff/SKILL.md`
- Modify: `skills/take-the-review/SKILL.md`
- Modify: `skills/carry-out-the-plan/SKILL.md`
- Modify: `skills/set-the-bounds/SKILL.md`
- Modify: `skills/adopt-the-repo/SKILL.md`
- Modify: `docs/skills.md`

**Interfaces:**

- Consumes: the six `## Skill: <name>` regions of the spec.
- Produces: six skill files whose named sections match the spec, and one Records bullet.

- [ ] **Step 1: Replace and add the sections**

For each region, replace each named `##` section body with the `###` body from the spec. Add each new section where its region says. In `stress-the-change`, replace the description with the line in Global Constraints.

The check is a script that reads each region from the spec and compares each `###` body with the `##` body of the same heading in the skill file. Done means every body matches, and `git diff main -- skills/` shows changes only in the named sections and in the one description.

- [ ] **Step 2: Add the Records bullet**

In `docs/skills.md`, under Records, add this bullet after the model tier routing bullet:

```text
- The adversarial review revision of `stress-the-change`, `review-the-diff`, `take-the-review`, `carry-out-the-plan`, `set-the-bounds`, and `adopt-the-repo` is recorded in [docs/specs/2026-10-11-adversarial-review-design.md](specs/2026-10-11-adversarial-review-design.md).
```

The check is `git diff main -- docs/skills.md`. Done means the diff is that one line.

- [ ] **Step 3: Commit the skills and the map**

Resolve `commit`. Commit the six skill files and `docs/skills.md` when that value allows it. Leave the manifests and this plan out of that commit. The subject is in Global Constraints. The body names the pass goals, the refutation, the project review skill, the rigor level, the comments for another author, the fix claims, and the review-run yes.

### Task 3: Bump the version and run the checks

Kind: follow-a-pattern

**Files:**

- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Test: `python3 tests/check_plugin.py`
- Test: `grok plugin validate .`

**Interfaces:**

- Consumes: the manifests at `1.1.0`. The version bump commit `Mark the plugin at 1.1.0` is the pattern.
- Produces: both manifests at `1.2.0` with the stable description.

- [ ] **Step 1: Bump the manifests**

Set `version` to `1.2.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. Leave both descriptions as the stable sentence.

The check is a read of both `version` fields. Done means both are `1.2.0`.

- [ ] **Step 2: Run the checks**

Run `python3 tests/check_plugin.py` from the repository root. Then run the spec's Implementation check: compare each region with its skill file, read the heading order of `stress-the-change`, `review-the-diff`, `take-the-review`, and `adopt-the-repo` and the `stress-the-change` description, grep `skills/` for host tool names, model brand names, code-host names, and host review files, grep `adopt-the-repo` for a named regulation, run `git diff --stat main` over the files Global Constraints lists as not edited, confirm the repo has no `hooks/` directory and no `hooks.json`, and scan tracked files for a hostname, a home-directory path, or a machine name. Then run `grok plugin validate .`.

Done means `python3 tests/check_plugin.py` exits 0 with no stderr, with `1.2.0` ahead of `1.1.0` on `main`, and every Implementation check item holds. There is no new function in the check, so the real-code bar in `scope-the-edit` has no branch to cover. If `grok` is not on the path, say so and leave that check open.

- [ ] **Step 3: Commit the version**

Resolve `commit`. Commit the two manifests when that value allows it. The subject is in Global Constraints.

### Task 4: Mark the plan

Kind: docs-or-config

**Files:**

- Modify: `docs/plans/2026-10-11-adversarial-review.md`

**Interfaces:**

- Consumes: Tasks 1 to 3 finished.
- Produces: the finished checkboxes, committed under `commit-plans`.

- [ ] **Step 1: Mark and commit the finished steps**

Mark each finished step `- [x]`. Resolve `commit-plans` and commit only this file. The subject is in Global Constraints. Do not push. `push` is `ask`, and this run has no yes for it.

The check is `git status --short`. Done means the tree is clean and the plan shows every finished step marked.
