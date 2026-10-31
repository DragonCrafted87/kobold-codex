# Tracker Requirements Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request, after the neutral token-env rule and the ship-the-branch description from review

**Goal:** Let a project keep its requirements in a tracker, cut duplication between specs, plans, and skills, and mark the plugin at `2.3.0`.

**Specs:**

- `docs/specs/2026-10-31-tracker-requirements-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

## Global Constraints

- No skill is added or renamed. Every description stays.
- No skill names a project, a host, or a tracker product.
- Version becomes `2.3.0` in both manifests.

---

### Task 1: Skills

- [x] Copy each section in the spec into its skill.

### Task 2: Check and index

- [x] Extend `tests/check_plugin.py` with the checks the spec lists.
- [x] Link the spec from `docs/skills.md`.
- [x] Bump both manifests to `2.3.0`.
- [x] `python3 tests/check_plugin.py` passes.

### Task 3: Review fixes

- [x] Derive the token variable from the agent's vault name; drop `token-env` from the record.
- [x] Name the Implements links in the ship-the-branch description.
- [x] `python3 tests/check_plugin.py` passes.

### Task 4: Neutral token variable

- [x] Restore `token-env` as a required, repository-chosen neutral name; drop the vault-name derivation.
- [x] `python3 tests/check_plugin.py` passes.
