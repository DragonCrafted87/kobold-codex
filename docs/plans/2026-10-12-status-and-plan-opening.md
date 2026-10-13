# Status And Plan Opening Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

## Status

Current: done
Blocker: none
Next: review of the pull request

**Goal:** Add the Status block to long work and the Starting state, Expected state, and Reason lines to plans with no spec. The plugin becomes `1.5.0`.

**Architecture:** The spec is the only source for the text that ships. The work goes on `status-and-plan-opening`, cut from `main` at `3d596ac`, after PR #20 merged. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library.

**Specs:**

- `docs/specs/2026-10-12-status-and-plan-opening-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- No skill is added or renamed. Every description stays.
- No existing file under `docs/specs/` changes.
- Version becomes `1.5.0` in both manifests. `1.4.1` is the version before it.
- Commit subjects: `Add the spec and plan for status and plan opening`, `Keep a Status block and open plans with the reason`, `Mark the plugin at 1.5.0`.

---

### Task 1: Apply the sections

Kind: docs-or-config

**Files:**

- Modify: `skills/carry-out-the-plan/SKILL.md`
- Modify: `skills/leave-a-trail/SKILL.md`
- Modify: `skills/pick-up-the-work/SKILL.md`
- Modify: `skills/write-the-plan/SKILL.md`
- Modify: `skills/set-the-bounds/SKILL.md`
- Modify: `skills/review-the-week/SKILL.md`

- [x] **Step 1:** Add the Status paragraph to The check in `carry-out-the-plan`, and The status to `leave-a-trail` after The row.
- [x] **Step 2:** Add the paragraph and the sentence to `pick-up-the-work`.
- [x] **Step 3:** Add the two paragraphs to What the reviewer reads in `write-the-plan`.
- [x] **Step 4:** Add the Publishing sets paragraph to `set-the-bounds`: a changed Status block sends the whole plan file with the work commit.
- [x] **Step 5:** Add the sentence to The report in `review-the-week`.
- [x] **Step 6:** `rg -n "Status" skills` shows each addition once.

### Task 2: Records

Kind: docs-or-config

**Files:**

- Modify: `docs/skills.md`

- [x] **Step 1:** Add a Records bullet for this spec, naming the six skills.

### Task 3: Version

Kind: docs-or-config

- [x] **Step 1:** Set `1.5.0` in both manifests.
- [x] **Step 2:** `python3 tests/check_plugin.py` exits 0.
- [x] **Step 3:** Rewrite this plan's Status block to `Current: done`.
