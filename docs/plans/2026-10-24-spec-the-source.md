# Spec The Source Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `spec-the-source` in the investigate group and mark the plugin at `2.2.0`.

**Architecture:** The spec is the record of the decision and the only source for the text that ships. The skill body is copied from the spec's Skill region. The work stays on `spec-the-source`, cut from `main` at `56d84a6`.

**Specs:**

- `docs/specs/2026-10-24-spec-the-source-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- One skill is added. No skill is renamed. Every existing description stays.
- Version becomes `2.2.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`.
- The skill names no project, host tool, or model.
- Source mode and clean-room mode live in the one skill.

---

### Task 1: Add the skill

Kind: docs-or-config

**Files:**

- Create: `skills/investigate/spec-the-source/SKILL.md`

- [x] **Step 1:** Copy the frontmatter and the sections from the spec's Skill region. Headings become `##`.
- [x] **Step 2:** Add clean-room mode, contamination, the output location, and the requirement IDs from the revised spec.
- [x] **Step 3:** Add the `UI` and `PERM` kinds, the requirement language section, and the template.

### Task 2: Map

Kind: docs-or-config

**Files:**

- Modify: `docs/skills.md`

- [x] **Step 1:** Add the skill line under Investigate and the Records bullet.

### Task 3: Requirement language check

Kind: code

**Files:**

- Modify: `tests/check_plugin.py`

- [x] **Step 1:** Fail when the spec-the-source skill uses MUST, SHOULD, MAY, or REQUIRED outside the line that lists them and the search command.

### Task 4: Version

Kind: docs-or-config

- [x] **Step 1:** Set `2.2.0` in both manifests.
- [x] **Step 2:** `python3 tests/check_plugin.py` exits 0.
