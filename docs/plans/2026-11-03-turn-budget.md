# Turn Budget Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `kobold-codex` batches probes, uses the cheapest tool, and labels claims seen, inferred, or unknown, and the plugin is at `2.5.3`.

**Specs:**

- `docs/specs/2026-11-03-turn-budget-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise kobold-codex

Kind: docs-or-config

- [x] **Step 1:** Copy Few turns, cited claims from the spec into `skills/ground/kobold-codex/SKILL.md`, before Requirements.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `2.5.3` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
