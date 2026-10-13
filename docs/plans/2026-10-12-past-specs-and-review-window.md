# Past Specs And Review Window Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Past specs never change, the newest spec records a change, and `review-the-week` gets a `review-window` bounds key. The plugin becomes `1.4.1`.

**Architecture:** The spec is the only source for the text that ships. The work stays on `past-specs-and-review-window`, cut from `review-the-week` at `ca1d11f`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library.

**Specs:**

- `docs/specs/2026-10-12-past-specs-and-review-window-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- No skill is added or renamed. Every description stays.
- No existing file under `docs/specs/` changes.
- Version becomes `1.4.1` in both manifests. `1.4.0` is the version on `review-the-week`.
- Commit subjects: `Add the spec and plan for past specs and the review window`, `Keep past specs and add review-window`, `Mark the plugin at 1.4.1`.

---

### Task 1: Apply the sections

Kind: docs-or-config

**Files:**

- Modify: `skills/write-a-skill/SKILL.md`
- Modify: `skills/learn-from-the-session/SKILL.md`
- Modify: `skills/set-the-bounds/SKILL.md`
- Modify: `skills/review-the-week/SKILL.md`
- Modify: `docs/skills.md`

- [x] **Step 1:** Replace each paragraph and add each row the spec names.
- [x] **Step 2:** Add the Records bullet to `docs/skills.md`.

### Task 2: Version

Kind: docs-or-config

- [x] **Step 1:** Set `1.4.1` in both manifests.
- [x] **Step 2:** `python3 tests/check_plugin.py` exits 0.
