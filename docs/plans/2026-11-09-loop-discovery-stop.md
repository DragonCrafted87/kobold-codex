# Loop Discovery Stop Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `loop-to-the-goal` stops a discovery search when N consecutive rounds add no new items, and the plugin is at `3.0.2`.

**Specs:**

- `docs/specs/2026-11-09-loop-discovery-stop-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise loop-to-the-goal

Kind: docs-or-config

- [x] **Step 1:** Copy the discovery goal, discovery stop, and discovery pass wording from the spec into `skills/loop-to-the-goal/SKILL.md`, and update the description.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.2` in all four manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
