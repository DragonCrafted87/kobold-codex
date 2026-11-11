# Optional Tracker Notes Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `keep-the-findings` and `map-the-handoffs` keep local files and the plan as source of truth, with OPTIONAL structured notes on a work item when one already exists, and the plugin is at `3.0.4`.

**Specs:**

- `docs/specs/2026-11-09-optional-tracker-notes-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise keep-the-findings and map-the-handoffs

Kind: docs-or-config

- [x] **Step 1:** Copy the optional notes wording from the spec into both skills, and update their descriptions.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.4` in all four manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
