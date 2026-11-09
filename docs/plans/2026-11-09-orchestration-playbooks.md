# Orchestration Playbooks Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** Ship large-audit, large-migration, and cross-checked-research playbooks that compose the multi-agent habits, and the plugin is at `3.0.5`.

**Specs:**

- `docs/specs/2026-11-09-orchestration-playbooks-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Add three playbooks and revise run-the-play

Kind: docs-or-config

- [x] **Step 1:** Add the three playbook files, update The match and the plugin-playbooks sentence in `skills/run-the-play/SKILL.md`, and add the map line.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.5` in all four manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
