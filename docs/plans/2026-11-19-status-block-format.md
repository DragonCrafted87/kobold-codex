# Status Block Format Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

- **Current:** done
- **Blocker:** none
- **Next:** the review of this pull request

**Goal:** Status fields and Starting / Expected / Reason render as bold labels on separate lines, and the plugin is at `3.0.6`.

**Specs:**

- `docs/specs/2026-11-19-status-block-format-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise the Status format

Kind: docs-or-config

- [x] **Step 1:** Copy the Status and opening-state wording from the spec into `skills/write-the-plan/SKILL.md`, `skills/leave-a-trail/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, and `skills/review-the-week/SKILL.md`.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.6` in all four manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
