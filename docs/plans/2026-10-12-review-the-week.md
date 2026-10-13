# Review The Week Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `review-the-week`, add the `commit-reviews` bounds key, move the `commit-plans` default to `ask`, and mark the plugin at `1.4.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. The skill body is copied from the spec's Skill region. Each Revision region replaces the named text in its file. The work stays on `review-the-week`, cut from `main` at `974fcaa`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library.

**Specs:**

- `docs/specs/2026-10-12-review-the-week-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- One skill is added. No skill is renamed. Every existing description stays.
- Version becomes `1.4.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. `1.3.0` is the version on `main`.
- No skill names a Grok tool, a Claude tool, a transcript path, or a model by brand. No hooks.
- `commit-plans` and `commit-specs` are `auto` in this repo. `commit` and `push` follow the user's request for this branch.
- Commit subjects: `Add the spec and plan for review-the-week`, `Add review-the-week and the commit-reviews key`, `Mark the plugin at 1.4.0`.

---

### Task 1: Add the skill

Kind: docs-or-config

**Files:**

- Create: `skills/review-the-week/SKILL.md`

- [x] **Step 1:** Copy the frontmatter and the seven sections from the spec's Skill region. Headings become `##`.

### Task 2: Apply the revisions

Kind: docs-or-config

**Files:**

- Modify: `skills/set-the-bounds/SKILL.md`
- Modify: `skills/adopt-the-repo/SKILL.md`
- Modify: `skills/ship-the-branch/SKILL.md`
- Modify: `docs/skills.md`

- [x] **Step 1:** Apply each Revision region from the spec.
- [x] **Step 2:** Add the skill line and the Records bullet to `docs/skills.md`.

### Task 3: Version

Kind: docs-or-config

- [x] **Step 1:** Set `1.4.0` in both manifests.
- [x] **Step 2:** `python3 tests/check_plugin.py` exits 0.
