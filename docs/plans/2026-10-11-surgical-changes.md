# Surgical Changes Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship the surgical changes revision. The creed gains Read the request, Smallest change gains the style, orphan, and impossible-case rules, Remove dead weight first follows the rigor level, `review-the-diff` agrees with it, and the plugin becomes `1.3.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. Each `###` section in a Skill region replaces the `##` section with the same heading in that file, or is a new `##` section placed where the region says. The work stays on `surgical-changes`, cut from `main` at `8b6a83c`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-11-surgical-changes-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- No skill is added or renamed. Every description stays.
- Version becomes `1.3.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. `1.2.0` is the version on `main`.
- No skill names a Grok tool, a Claude tool, or a model by brand. No hooks.
- Only `skills/kobold-codex/SKILL.md` and `skills/review-the-diff/SKILL.md` change under `skills/`. `docs/skills.md` gains one Records bullet.
- `commit-plans` and `commit-specs` are `auto`. `commit` is `ask`, and the user's request to commit on this branch is the yes. `push` is `ask`, and the user's request to push and open a pull request is the yes for this branch.
- Commit subjects: `Add the plan for surgical changes`, `Make edits surgical and dead weight follow the rigor level`, `Mark the plugin at 1.3.0`, `Mark the finished surgical changes plan steps`.

---

### Task 1: Apply the Skill regions

Kind: docs-or-config

**Files:**

- Modify: `skills/kobold-codex/SKILL.md`
- Modify: `skills/review-the-diff/SKILL.md`
- Modify: `docs/skills.md`

- [ ] **Step 1: Replace and add the sections**

Copy each `###` body from the spec into its skill file. Add Read the request after Voice in `kobold-codex`.

The check is a script that compares each `###` body with the `##` body of the same heading. Done means every body matches and `git diff main -- skills/` shows only those sections.

- [ ] **Step 2: Add the Records bullet**

In `docs/skills.md`, under Records, add after the adversarial review bullet:

```text
- The surgical changes revision of `kobold-codex` and `review-the-diff` is recorded in [docs/specs/2026-10-11-surgical-changes-design.md](specs/2026-10-11-surgical-changes-design.md).
```

The check is `git diff main -- docs/skills.md`. Done means the diff is that one line.

- [ ] **Step 3: Commit the skills and the map**

Commit the two skill files and `docs/skills.md`. The subject is in Global Constraints.

### Task 2: Bump the version and run the checks

Kind: follow-a-pattern

**Files:**

- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Test: `python3 tests/check_plugin.py`

- [ ] **Step 1: Bump the manifests**

Set `version` to `1.3.0` in both manifests, following `Mark the plugin at 1.2.0`. The check is a read of both fields.

- [ ] **Step 2: Run the checks**

Run `python3 tests/check_plugin.py`, then the spec's Implementation check: the region comparison, the `kobold-codex` heading order, the brand and host-tool grep over `skills/`, `git diff --stat main` over every other skill, the earlier specs, and the README, the hooks check, and the hostname scan. Then `grok plugin validate .`; if `grok` is not on the path, say so and leave it open.

Done means the checker exits 0 with `1.3.0` ahead of `1.2.0` on `main`, and every Implementation check item holds.

- [ ] **Step 3: Commit the version**

Commit the two manifests. The subject is in Global Constraints.

### Task 3: Mark the plan and publish

Kind: docs-or-config

**Files:**

- Modify: `docs/plans/2026-10-11-surgical-changes.md`

- [ ] **Step 1: Mark, commit, and open the pull request**

Mark each finished step `- [x]` and commit only this file. Push `surgical-changes` and open a pull request against `main`.

The check is `git status --short` and the pull request URL. Done means the tree is clean and the pull request is open.
