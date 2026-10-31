# Live System Trigger Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `set-the-bounds` loads before a change to a live system, and the plugin is at `2.3.1`.

**Specs:**

- `docs/specs/2026-10-31-live-system-trigger-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise set-the-bounds

Kind: docs-or-config

- [x] **Step 1:** Copy the description and the Resolve first paragraph from the spec into `skills/ground/set-the-bounds/SKILL.md`.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.3.1` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
