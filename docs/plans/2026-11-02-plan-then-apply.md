# Plan Then Apply Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `carry-out-the-plan` previews a multi-file change before applying it, and the plugin is at `2.4.1`.

**Specs:**

- `docs/specs/2026-11-02-plan-then-apply-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise carry-out-the-plan

Kind: docs-or-config

- [x] **Step 1:** Copy the A multi-file change heading from the spec into `skills/build/carry-out-the-plan/SKILL.md`, before A failed run.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.4.1` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
