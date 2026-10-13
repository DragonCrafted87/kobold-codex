# Nested skills

Design for grouping the plugin's skills into folders. `skills/` held
26 skill folders side by side. This change moves each one under a
group folder named for the phase of work it serves. No skill is
renamed. Two section bodies change: The file in `write-a-skill`, and
one paragraph in The move in `adopt-the-repo`. Past specs and plans
keep the paths they were written with. This spec stays the record of
what we decided and why.

## Purpose

A reader opening `skills/` should see the workflow, not a long list.
Ten groups read faster than 26 names.

Success for this version is a plugin that a Grok session and a
Claude Code session both load with every skill found once, under the
same name as before.

## Decisions

### The groups

The groups follow the order a piece of work moves in. The creed and
the guardrails come first, because every phase uses them.

| Group | Skills |
| --- | --- |
| `ground` | `kobold-codex`, `scope-the-edit`, `set-the-bounds` |
| `investigate` | `debug-the-failure`, `how-it-fits`, `why-it-is` |
| `plan` | `write-the-plan`, `try-several-shapes`, `run-the-play` |
| `build` | `carry-out-the-plan`, `isolate-the-work`, `fan-out`, `prove-the-product` |
| `review` | `review-the-diff`, `take-the-review`, `stress-the-change`, `measure-the-blast` |
| `ship` | `ship-the-branch` |
| `session` | `pick-up-the-work`, `leave-a-trail` |
| `learn` | `learn-from-the-session`, `review-the-week`, `write-a-skill` |
| `write` | `write-the-doc`, `cut-the-slop` |
| `setup` | `adopt-the-repo` |

`run-the-play` sits in plan, because it picks the playbook before the
work. `prove-the-product` sits in build, because it builds the drive.
`measure-the-blast` sits in review, because it reads a diff. The
one-skill groups, ship and setup, stay. A group is a phase, not a
count.

### The path

A skill file is `skills/<group>/<name>/SKILL.md`. The skill name stays
the folder name. The group is not part of the name. Both hosts name a
plugin skill `kobold-codex:<name>`, so triggers, cross-references, and
user habits do not change. A skill sits in exactly one group. A group
holds at least one skill.

### The manifest

`.claude-plugin/plugin.json` gains a `skills` key that lists each
group:

```json
"skills": [
  "./skills/ground/",
  "./skills/investigate/",
  "./skills/plan/",
  "./skills/build/",
  "./skills/review/",
  "./skills/ship/",
  "./skills/session/",
  "./skills/learn/",
  "./skills/write/",
  "./skills/setup/"
]
```

Claude Code's default scan reads `skills/<name>/SKILL.md`, one level
down. Without the key it finds no skill in the nested layout. With
the key it reads each group as a directory of skill folders.

Grok walks a plugin's `skills/` up to five levels deep, and it reads
`.claude-plugin/plugin.json`. It finds the nested skills with or
without the key.

### The double-load risk

A skill found by Grok's walk and by a listed group could load twice.
This was tested on 2026-10-12 with Grok 1.0.52 and Claude Code
2.1.296, each installed into a scratch home from the branch checkout:

- Grok, `grok inspect --json`: 26 kobold-codex skills, 26 unique
  names, no duplicate, with or without the key. Paths resolve
  through the group folders.
- Claude Code, `claude plugin details`: 26 skills with the key, each
  once. 0 skills without the key.
- `grok plugin validate` and `claude plugin validate` pass. Grok
  reports 10 skill dirs.

No fallback is needed. Had Grok loaded a skill twice, the fallback
was a Grok manifest with no `skills` key, so Grok walks `skills/`
alone.

### The check

`tests/check_plugin.py` gains a layout check. It fails when:

- a `SKILL.md` sits anywhere but `skills/<group>/<name>/SKILL.md`;
- a frontmatter `name` does not match its folder;
- a skill name appears in two groups;
- a folder under `skills/` holds no skill, or is missing from the
  `skills` key;
- a path in the `skills` key does not exist, names more than one
  folder, or holds no skill.

The check still reads no section body. It reads the frontmatter
`name` line only.

### The links

`docs/skills.md` links each skill by its new path, in Which skill
applies and in Records. Which skill applies gains one heading per
group, in the table's order, over the lines it already had. The root
README says the skills are grouped by phase.

### Project skills in adopted repos

`adopt-the-repo` suggests the same groups for the project skills it
writes, but project skills stay flat: one directory per skill,
directly under the skill root. This is the decision, not a fallback.
The plugin exists to keep per-project special casing small. A flat
project skill root is the layout both hosts already document, so a
project needs no manifest and no layout of its own. The groups are
named in the report of what was written, and they head the
project's list of skills when it keeps one.

### What stays

The dated specs and plans keep their paths. They are records of what
shipped then. A reader who follows an old path finds the skill by
name under its group.

### The version

The plugin moves from `1.5.0` to `2.0.0`, in `plugin.json` and in the
marketplace entry. No skill name changes, but every skill path does.
A user or a project that links a skill file by path breaks, so this
is a major version.

## Where the words live

```text
skills/<group>/<name>/SKILL.md
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
tests/check_plugin.py
docs/skills.md
README.md
docs/specs/2026-10-12-nested-skills-design.md
docs/plans/2026-10-12-nested-skills.md
```

## Skill: write-a-skill

The section below replaces The file. The other sections stay.

### The file

The skill file is `skills/<group>/<name>/SKILL.md`. The group is
the phase of work the skill serves. Use a group that already
exists. A new group is a folder under `skills/` and a path in the
manifest's `skills` list, added in the same change.

The file starts with frontmatter. `name` is the skill name, and it
matches the folder. `description` is that same line.

The title is the skill name with hyphens written as spaces and the
first letter capitalized. Copy each section body from the spec.

## Skill: adopt-the-repo

In The move, the paragraph that starts "A project skill is one
directory" becomes the two paragraphs below.

### The move

A project skill is one directory under the skill root with one
`SKILL.md`. The description is one physical line and says when
the skill applies. The wording is original and follows
`kobold-codex`. The file names no host tool. These files are not
skills in this plugin, and they do not bump this plugin's
version.

Group the project skills by this plugin's phases: ground,
investigate, plan, build, review, ship, session, learn, write, and
setup. A skill that fits none takes a group named for its subject.
The skill directories stay one level under the skill root, so a
project needs no layout of its own. Name each
skill's group when you report what was written. When the project
keeps a list of its skills, the groups are its headings.

## What this change does not do

It does not rename a skill or change a description.

It does not change a section body, except The file in `write-a-skill`
and The move in `adopt-the-repo`.

It does not rewrite a dated spec or plan.

It does not add a hook.

## Implementation check

- Every skill sits at `skills/<group>/<name>/SKILL.md`, in the group
  the table names. No skill folder is left at `skills/<name>/`.
- `.claude-plugin/plugin.json` lists the ten group folders under
  `skills`.
- `tests/check_plugin.py` passes, and fails when a skill is moved out
  of its group, sits in two groups, sits too deep, has a name that
  does not match its folder, or sits in a group the manifest does not
  list.
- On Grok and on Claude Code, each of the 26 names loads once.
- `docs/skills.md` links every skill at its new path, under its group
  heading.
- `write-a-skill` and `adopt-the-repo` carry the sections above.
- Plugin version is `2.0.0` in both manifests.
- No dated spec or plan is changed.
