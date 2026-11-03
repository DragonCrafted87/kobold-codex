# Flat Skills Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax for tracking.

## Status

Current: done
Blocker: none
Next: the review of this pull request

**Goal:** Every skill sits at `skills/<name>/SKILL.md` with its group as frontmatter metadata, the plugin ships Agent Plugins and Gemini CLI manifests, and the plugin is at `3.0.0`.

**Specs:**

- `docs/specs/2026-11-03-flat-skills-design.md`

If a sentence in this plan disagrees with the spec, the spec wins.

### Task 1: Flatten the layout

Kind: docs-or-config

- [x] **Step 1:** Move each `skills/<group>/<name>/` to `skills/<name>/` with `git mv`, add the `metadata` group to each frontmatter, set `.claude-plugin/plugin.json` `skills` to `["./skills/"]`, add the root `plugin.json` and `gemini-extension.json`, update `tests/check_plugin.py`, the path references in `docs/skills.md` and the check, the README install guidance, and the two write-a-skill sections from the spec.
- [x] **Step 2:** Add the record line to `docs/skills.md`.
- [x] **Step 3:** Bump the version to `3.0.0` in both manifests.
- [x] **Step 4:** Run `python3 tests/check_plugin.py`.
