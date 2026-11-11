# Isolate Colliding Pieces Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** `isolate-the-work` gives each colliding parallel piece its own checkout when writes would conflict, and the plugin is at `3.0.3`.

**Specs:**

- `docs/specs/2026-11-09-isolate-colliding-pieces-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Revise isolate-the-work

Kind: docs-or-config

- [x] **Step 1:** Copy Parallel pieces that collide from the spec into `skills/isolate-the-work/SKILL.md`, and update the description.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.3` in all four manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
