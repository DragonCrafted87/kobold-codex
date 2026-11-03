# Flat skills, and manifests for other hosts

A layout change and a revision of `write-a-skill`, from KCO-2536.
It replaces the folder nesting from 2.0.0. The wording below is the
version to ship.

## Research (2026-11-03)

- Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, and
  OpenCode all read Agent Skills: a folder holding a `SKILL.md` with
  `name` and `description` frontmatter.
- `.agents/skills/<name>/SKILL.md` is read by Codex, Cursor, Copilot,
  Gemini CLI, and OpenCode. Claude Code reads `.claude/skills/`.
- The Agent Plugins standard (1.0.0) is a root `plugin.json` with
  `$schema` and `name`. Skills are the immediate children of
  `skills/`, and clients do not search deeper. Cursor and Codex load
  it. Codex also accepts `.claude-plugin/plugin.json`.
- A Gemini CLI extension is `gemini-extension.json` at the root. It
  has no skills path field. It finds skills in `skills/<name>/SKILL.md`.
- Cursor's own format, `.cursor-plugin/plugin.json`, is optional when
  the Agent Plugins manifest is present.

Every portable format looks for `skills/<name>/SKILL.md`. The 2.0.0
layout, `skills/<group>/<name>/SKILL.md`, worked only through the
group paths in the Claude manifest, so no other host found a skill.

## Decisions

- Option 1 of the three in the research, chosen by Scott: flatten
  `skills/` to one folder per skill. Each folder moves with
  `git mv`, so the history follows it.
- The group is frontmatter metadata: a `metadata` block holding
  `group`. Agent Skills defines `metadata` as a free map, so a
  strict host still accepts the file. A top-level `group` key is not
  in the standard, and the group lists in `plugin.json` are gone,
  because that manifest now names one path.
- The list of groups, in the order work moves, is the group
  headings in `docs/skills.md`. That page already sorted the skills
  by group, so the list lives once. The check fails a skill whose
  group is not a heading there, or that the page does not link under
  its group.
- `.claude-plugin/plugin.json` names `./skills/`. A root
  `plugin.json` in the Agent Plugins format and a
  `gemini-extension.json` are added, and the check holds their name,
  version, and description to the Claude manifest. No Cursor-only
  manifest and no `.agents/skills` copy are added; the Agent Plugins
  manifest covers Cursor and Codex, and a copy would be a second
  source.
- The manifest description still names Grok and Claude Code. It is
  the sentence the catalog's ship rule records, so changing it is
  left to its own change.
- Version `3.0.0`: every skill path changes, which breaks any link
  or install that named a nested path.

## Skill: write-a-skill

The file and the first paragraph of The check become the text below.

### The file


The skill file is `skills/<name>/SKILL.md`, one folder per skill
directly under `skills/`. Agent hosts find a skill only at that
depth, so a skill never sits in a deeper folder.

The group is the phase of work the skill serves. It is metadata, not
a folder. Use a group that already exists: the group headings in
`docs/skills.md` are the list, in the order work moves. A new group
is a new heading there, added in the same change.

The file starts with frontmatter. `name` is the skill name, and it
matches the folder. `description` is that same line. A `metadata`
block holds `group`, the group's heading in lower case.

The title is the skill name with hyphens written as spaces and the
first letter capitalized. Copy each section body from the spec.

### The check, first paragraph

`tests/check_plugin.py` checks the manifests, and it requires a
branch off main to be ahead on version. The manifests are
`.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`,
the Agent Plugins `plugin.json` at the root, and
`gemini-extension.json`; their name, version, and description
agree. It checks that each skill sits at `skills/<name>/SKILL.md`,
that its group is a heading in `docs/skills.md`, and that the map
links it under that heading. When a change needs a new check, add
it in the same change.

## What this change does not do

It does not edit a past spec or plan. Their nested paths stay as the
record of their time. Beyond the new `metadata` block, it changes no
skill's wording other than `write-a-skill`, no key, and no bound. It
does not change the
manifest description. Installs on Codex, Gemini CLI, and Cursor are
documented from their docs and not yet run.
