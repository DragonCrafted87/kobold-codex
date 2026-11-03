# Allowed Checks Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `ship-the-branch` runs the allowed test and lint commands and reads their diagnostics before the commit, and the plugin is at `2.4.3`.

**Specs:**

- `docs/specs/2026-11-02-allowed-checks-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise ship-the-branch

Kind: docs-or-config

- [x] **Step 1:** Copy the paragraph from the spec into The branch in `skills/ship/ship-the-branch/SKILL.md`, after the narrow checks and the gate.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.4.3` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
