# Audit And Excluded Paths Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `review-the-diff` checks an agent's edit log against the commits and flags edits to excluded paths, and the plugin is at `2.5.1`.

**Specs:**

- `docs/specs/2026-11-02-audit-and-excluded-paths-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise review-the-diff

Kind: docs-or-config

- [x] **Step 1:** Copy the paragraph from the spec to the end of The request and the checks in `skills/review/review-the-diff/SKILL.md`.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.5.1` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
