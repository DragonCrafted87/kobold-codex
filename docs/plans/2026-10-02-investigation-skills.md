# Investigation Skills Implementation Plan

> **For agentic workers:** Implement this task after the specs are reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `debug-the-failure`, `how-it-fits`, and `why-it-is` in the existing plugin, with each skill's section bodies pinned to its spec, and bump the plugin to `0.4.0`.

**Architecture:** Each new spec is the only copy of that skill's section bodies. `tests/check_plugin.py` reads those headings from the spec and from `SKILL.md` and requires the paragraphs to match. The creed, `scope-the-edit`, `set-the-bounds`, and the remaining-skills catalog stay untouched. The same check still pins the three shipped skills to their specs. The README points at the new skills and does not restate a section body.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-02-debug-the-failure-design.md`
- `docs/specs/2026-10-02-how-it-fits-design.md`
- `docs/specs/2026-10-02-why-it-is-design.md`

This plan and those specs are already in the worktree. Do not rewrite a section body while implementing. Copy each `###` body under that spec's `## Skill` heading into the matching `##` section of `SKILL.md`, including line breaks. If a sentence in this plan disagrees with a spec, the spec wins. The three specs state the same plugin description. If those three sentences disagree, stop.

## Global Constraints

- Skill names are `debug-the-failure`, `how-it-fits`, and `why-it-is`. Plugin name and marketplace name stay `kobold-codex`.
- `debug-the-failure` description is one physical line: `Use when a failure can be reproduced. Hold one hypothesis at a time, check it on the running system, and put the fix at the producer of the symptom.`
- `how-it-fits` description is one physical line: `Use before changing a subsystem. Name the runtime path, the package that owns the behavior, and the layer the change belongs on.`
- `why-it-is` description is one physical line: `Use when you need the reason for a behavior or a threshold. Recover it from the code, the history, the issues, and the docs, and cite each source.`
- Plugin and marketplace description becomes: `Voice, engineering principles, edit scoping, action bounds, and investigation for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.4.0` in both manifests. License, author, repository, and marketplace `source` stay as they are.
- Heading names, in order:
  - `debug-the-failure`: `Reproduce`, `One hypothesis`, `Evidence`, `The producer`, `The same failure`. The skill title is `Debug the failure`.
  - `how-it-fits`: `Read first`, `Runtime path`, `Owner`, `Layer`. The skill title is `How it fits`.
  - `why-it-is`: `The question`, `Sources`, `The read`, `No reason on record`. The skill title is `Why it is`.
- Each section body equals that heading's body in its spec.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, their specs, and `docs/specs/2026-10-02-remaining-skills-design.md` are not edited.
- No new skill names a Grok tool or a Claude tool. The repo has no `hooks/` directory and no `hooks.json`.
- The README keeps the four install lines, links the three new skills and their specs, and does not restate a section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The check builds those needles by concatenation.

## Review Focus

- A section body in a new skill is a paraphrase of its spec. The section compare must fail.
- The README repeats a section body from any shipped skill. The README compare must fail.
- `plugin.json` stays at `0.3.0`, or the two manifests disagree on version or description. The manifest compare must fail.
- Frontmatter puts a new description on more than one line. The frontmatter compare must fail.
- The creed, `scope-the-edit`, `set-the-bounds`, or the catalog changes. Those compares, and a diff of the catalog, must fail the review.
- A public file names a machine or a home path. The needle scan must fail.

---

### Task 1: Pin the check, add the skills, bump the plugin

**Files:**

- Create: `skills/debug-the-failure/SKILL.md`
- Create: `skills/how-it-fits/SKILL.md`
- Create: `skills/why-it-is/SKILL.md`
- Modify: `tests/check_plugin.py`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `README.md`
- Test: `tests/check_plugin.py`

**Interfaces:**

- Consumes: the `###` bodies under each spec's `## Skill` heading. The creed, scope, and bounds checks already in `tests/check_plugin.py`.
- Produces: a tree where `python3 tests/check_plugin.py` exits 0 and `grok plugin validate .` reports version `0.4.0`. Validate counts the `skills/` directory, so the component line stays `1 skill dir(s)`.

- [ ] **Step 1: Extend the check and confirm it fails**

In `tests/check_plugin.py`, add a spec path, a skill path, a description constant, and a headings tuple for each new skill. Point the spec paths at the three files named above. Add the three description lines from Global Constraints. Use the heading names from Global Constraints, in that order.

Change the required plugin version from `0.3.0` to `0.4.0`. Change `PLUGIN_DESCRIPTION` to the sentence in Global Constraints. Append these paths to `README_LINKS`, skill then spec, in this order:

```text
skills/debug-the-failure/SKILL.md
docs/specs/2026-10-02-debug-the-failure-design.md
skills/how-it-fits/SKILL.md
docs/specs/2026-10-02-how-it-fits-design.md
skills/why-it-is/SKILL.md
docs/specs/2026-10-02-why-it-is-design.md
```

Call `check_one` for each new skill after the `set-the-bounds` call. Leave the creed, scope, and bounds calls as they are.

Run:

```bash
python3 tests/check_plugin.py
```

Expected: exit 1, and stderr contains `missing` and `debug-the-failure`. The creed sections are not the failure.

- [ ] **Step 2: Write the three skills**

Create each `SKILL.md` with `---` frontmatter, `name`, and the one-line `description` from Global Constraints. The H1 titles are `Debug the failure`, `How it fits`, and `Why it is`. Copy each section body from that skill's spec. Do not rewrap a copied line.

- [ ] **Step 3: Bump the manifests and the README**

Set `"version"` to `0.4.0` and `"description"` to `Voice, engineering principles, edit scoping, action bounds, and investigation for DragonCrafted87's agents on Grok and Claude Code.` in `.claude-plugin/plugin.json`, in the marketplace object, and in the one plugin entry inside `.claude-plugin/marketplace.json`. Leave the other manifest fields as they are.

Replace `README.md` with the note in Step 3 below.

- [ ] **Step 4: Run the check and validate the plugin**

```bash
python3 tests/check_plugin.py
grok plugin validate .
```

Expected: `check_plugin.py` exits 0 with no stderr. `grok plugin validate .` exits 0 and prints version `0.4.0`, the description from Global Constraints, and `1 skill dir(s)`.

Confirm a drifted paragraph fails the check, then restore the copied body. Confirm the creed files, `set-the-bounds`, and the catalog have an empty diff against `HEAD` of the spec commit.

- [ ] **Step 5: Commit the work**

`commit` governs this step. Stage the three skills, `tests/check_plugin.py`, both manifests, and `README.md`. Leave the specs and this plan in their own commits. Commit only when the resolved `commit` value allows it.

#### Step 3 README

````markdown
# Kobold Codex

Voice, engineering principles, edit scoping, action bounds, and investigation for coding agents on Grok and Claude Code.
The creed lives in [skills/kobold-codex/SKILL.md](skills/kobold-codex/SKILL.md).
The 2026-10-01 creed is recorded in
[docs/specs/2026-10-01-kobold-codex-design.md](docs/specs/2026-10-01-kobold-codex-design.md).
Edit scoping lives in [skills/scope-the-edit/SKILL.md](skills/scope-the-edit/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-01-scope-the-edit-design.md](docs/specs/2026-10-01-scope-the-edit-design.md).
Action bounds live in [skills/set-the-bounds/SKILL.md](skills/set-the-bounds/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-02-set-the-bounds-design.md](docs/specs/2026-10-02-set-the-bounds-design.md).
Failure diagnosis lives in [skills/debug-the-failure/SKILL.md](skills/debug-the-failure/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-02-debug-the-failure-design.md](docs/specs/2026-10-02-debug-the-failure-design.md).
A subsystem read lives in [skills/how-it-fits/SKILL.md](skills/how-it-fits/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-02-how-it-fits-design.md](docs/specs/2026-10-02-how-it-fits-design.md).
A reason for a behavior lives in [skills/why-it-is/SKILL.md](skills/why-it-is/SKILL.md).
That decision is recorded in
[docs/specs/2026-10-02-why-it-is-design.md](docs/specs/2026-10-02-why-it-is-design.md).

## Install

Grok, from GitHub:

```bash
grok plugin install DragonCrafted87/kobold-codex --trust
```

Grok, from a local checkout of this repository:

```bash
grok plugin install . --trust
```

Claude Code, in a session:

```text
/plugin marketplace add DragonCrafted87/kobold-codex
/plugin install kobold-codex@kobold-codex
```

Start a new session after installing so the skill is in the catalog.

## License

MIT. See [LICENSE](LICENSE).
````
