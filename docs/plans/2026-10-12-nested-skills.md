# Nested Skills Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

## Status

Current: done
Blocker: none
Next: review of the pull request

**Goal:** Move every skill under a group folder, list the groups in the manifest, check the layout, suggest the same groups in `adopt-the-repo`, and mark the plugin at `2.0.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. The work stays on `nested-skills`, cut from `main` at `1022fc0`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`, `grok inspect`, `claude plugin validate`, `claude plugin details`.

**Specs:**

- `docs/specs/2026-10-12-nested-skills-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- No skill is renamed. Every description stays.
- Only The file in `write-a-skill` and The move in `adopt-the-repo` change text under `skills/`. Every other skill file moves with `git mv` and no edit.
- No dated spec or plan changes.
- Version becomes `2.0.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. `1.5.0` is the version on `main`.
- Commit subjects: `Add the spec and plan for nested skills`, `Group the skills by phase`, `Check the skill layout`, `Mark the plugin at 2.0.0`.

---

### Task 1: Move the skills

Kind: rename-or-move

- [x] **Step 1: Make the groups and move the folders**

```bash
mkdir -p skills/ground skills/investigate skills/plan skills/build skills/review skills/ship skills/session skills/learn skills/write skills/setup
git mv skills/kobold-codex skills/ground/kobold-codex
git mv skills/scope-the-edit skills/ground/scope-the-edit
git mv skills/set-the-bounds skills/ground/set-the-bounds
git mv skills/debug-the-failure skills/investigate/debug-the-failure
git mv skills/how-it-fits skills/investigate/how-it-fits
git mv skills/why-it-is skills/investigate/why-it-is
git mv skills/write-the-plan skills/plan/write-the-plan
git mv skills/try-several-shapes skills/plan/try-several-shapes
git mv skills/run-the-play skills/plan/run-the-play
git mv skills/carry-out-the-plan skills/build/carry-out-the-plan
git mv skills/isolate-the-work skills/build/isolate-the-work
git mv skills/fan-out skills/build/fan-out
git mv skills/prove-the-product skills/build/prove-the-product
git mv skills/review-the-diff skills/review/review-the-diff
git mv skills/take-the-review skills/review/take-the-review
git mv skills/stress-the-change skills/review/stress-the-change
git mv skills/measure-the-blast skills/review/measure-the-blast
git mv skills/ship-the-branch skills/ship/ship-the-branch
git mv skills/pick-up-the-work skills/session/pick-up-the-work
git mv skills/leave-a-trail skills/session/leave-a-trail
git mv skills/learn-from-the-session skills/learn/learn-from-the-session
git mv skills/review-the-week skills/learn/review-the-week
git mv skills/write-a-skill skills/learn/write-a-skill
git mv skills/write-the-doc skills/write/write-the-doc
git mv skills/cut-the-slop skills/write/cut-the-slop
git mv skills/adopt-the-repo skills/setup/adopt-the-repo
```

- [x] **Step 2:** `ls skills/*/SKILL.md` prints nothing, and `find skills -name SKILL.md | wc -l` prints `26`.

- [x] **Step 3:** Replace The file in `skills/learn/write-a-skill/SKILL.md` with the spec's body.

### Task 2: List the groups

Kind: docs-or-config

- [x] **Step 1:** Add the `skills` key to `.claude-plugin/plugin.json`, after `license`, with the ten group paths.

### Task 3: Update the map

Kind: docs-or-config

- [x] **Step 1:** Rewrite each `skills/<name>/SKILL.md` link in `docs/skills.md` to `skills/<group>/<name>/SKILL.md`. Links into `docs/specs/` stay.
- [x] **Step 2:** Add a `###` heading per group in Which skill applies, and move each line under its group.
- [x] **Step 3:** README: the skills live under `skills/`, grouped by the phase of work they serve.
- [x] **Step 4:** `rg -n 'skills/[a-z-]+/SKILL\.md' . --glob '!docs/specs/**' --glob '!docs/plans/**'` finds only nested paths.

### Task 4: Check the layout

Kind: new-logic

- [x] **Step 1:** Add `check_layout()` to `tests/check_plugin.py`, called from `main()` after `check_manifests()`.
- [x] **Step 2: Prove it fails.** Each break below fails the check, and the check passes once it is restored:
  - a skill moved back to `skills/<name>/`;
  - a group removed from the `skills` key;
  - one skill copied into a second group;
  - a frontmatter `name` that does not match its folder;
  - a `SKILL.md` one level too deep;
  - a listed group that does not exist.

### Task 5: Project skill groups in adopt-the-repo

Kind: docs-or-config

- [x] **Step 1:** Replace the paragraph that starts "A project skill is one directory" with the spec's two paragraphs. Project skills stay flat by decision, so no nested project skill test is needed.

### Task 6: Version

Kind: docs-or-config

- [x] **Step 1:** Set `2.0.0` in both manifests.
- [x] **Step 2:** `python3 tests/check_plugin.py` exits 0.

### Task 7: Test both hosts

Kind: debugging

- [x] **Step 1: Grok.** Install the checkout into a scratch home with `grok plugin install <checkout> --trust`, then `grok inspect --json`. Result: 26 kobold-codex skills, no duplicate. `grok plugin validate` passes with 10 skill dirs.
- [x] **Step 2: Grok fallback.** Not needed.
- [x] **Step 3: Claude Code.** Add the checkout as a marketplace in a scratch home, install `kobold-codex@kobold-codex`, then `claude plugin details`. Result: 26 skills, each once. Without the `skills` key: 0. `claude plugin validate` passes.
