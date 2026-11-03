# Check The Licenses Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** Ship `check-the-licenses` in the ship group, and the plugin is at `2.5.0`.

**Specs:**

- `docs/specs/2026-11-02-check-the-licenses-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Add the skill

Kind: docs-or-config

- [x] **Step 1:** Copy the description and the section bodies from the spec into `skills/ship/check-the-licenses/SKILL.md`.
- [x] **Step 2:** Add the map line and the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.5.0` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
