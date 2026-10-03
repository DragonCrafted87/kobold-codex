# Set the bounds

Design for the bounds skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill and
the bounds rule on 2026-10-02. The wording in the skill sections below
is the version to ship. Later sessions tune it by editing the skill
file. This spec stays the record of what we decided and why.

## Purpose

`set-the-bounds` is the setup skill for actions a person turns on
deliberately: commits, push, pull requests, merge, force-push,
unattended continuation, and named tools. It writes one bounds layer
with the user, and it resolves the four layers before any of those
actions.

The creed in `skills/kobold-codex/SKILL.md` and
`skills/scope-the-edit/SKILL.md` stay as they are. This skill does not
restate them. The catalog stays the record of the skillset and the
build order. This spec is the copy the check pins.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog's bounds rule is the rule this skill ships. Four layers,
nearest key wins. A missing key inherits. A nearer file may allow more
than the file behind it. A tighten-only ceiling, where a nearer file
may only forbid what a farther file allows, was rejected in the
catalog. Replacement is the rule because the closest setting is the
one that applies.

`commit` is the work. `commit-plans` and `commit-specs` are their own
keys, so a repository can commit the work and leave the plans
unstaged. The default for plans is `never`. The default for specs is
`ask`. `commit: auto` does not stage plans or specs.

The writable layers are the user config file, the committed repo file,
and the checkout file. The defaults live in the skill. Changing them
is a change to this skill.

`stop-at-plan` stops once the plan is written, and stops before the
edit when the work has no plan. `safe-steps` is read, edit, the
project's checks, the plan, and the trail. `through-publish` follows
`commit`, `commit-plans`, `commit-specs`, `push`, `pull-request`, and
`merge`. An `ask` still asks. A `never` still stops. Force-push is not
one of those keys. A named tool stays on its own key.

A path that sits in both the plan directory and the spec directory is
a spec. The spec key is the one that decides it.

`model` is optional. Absent, the session's current model stays. A
model-per-role table stays out.

`auto` is a proceed value on `pull-request`, on a tool key, and on
`unattended`. On `pull-request` it matches `open`. On a tool key it
matches `allow`. On `unattended` it matches `through-publish`.

Each bounds file is YAML, one key per line. A Markdown file of bare
keys is a broken document to a Markdown formatter. The user config
path is `~/.config/kobold-codex/bounds.yaml`. The committed repo file
is `.kobold/bounds.yaml`. The checkout file is
`.kobold/bounds.local.yaml`, and writing it includes that path in the
repository ignore rules when the path is not already ignored. When the
user names a layer and names no keys, the reply is the table of key,
implicit value, and description, and the file is left unwritten.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

The plugin version becomes `0.3.0` when the skill is added. The plugin
and marketplace description becomes the following sentence.

```text
Voice, engineering principles, edit scoping, and action bounds for DragonCrafted87's agents on Grok and Claude Code.
```

The README points at the new skill and at this spec. It does not
restate the skill paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed and `scope-the-edit`, and it requires
version `0.3.0` and the description above.

## Where the words live

```text
skills/set-the-bounds/SKILL.md
docs/specs/2026-10-02-set-the-bounds-design.md
```

The creed and `scope-the-edit` stay. The catalog keeps the skillset
list. Its bounds filenames are the YAML paths above.

## Skill

Frontmatter `name` is `set-the-bounds`. Frontmatter `description` is
one physical line:

```text
Use before a commit, a push, a pull request, a merge, a force-push, an unattended stretch, or a named tool. Resolve the four bounds layers, and revise one layer when the user wants a change.
```

The body is the seven sections below. Heading text matches. Paragraphs
match, including line breaks.

### Resolve first

Before a commit of the work, a commit of plans, a commit of specs, a
push, a pull request, a merge, a force-push, an unattended stretch, or
a named tool, read the four layers and use the resolved value. Say each
key that governs the action, the value, and the layer that set it.
Reading the repo, editing files, and running the project's own checks
are ordinary work. Those actions have no key.

`ask` stops for a yes that names this action. A yes for a different
action does not carry. `auto`, `open`, and `allow` proceed. `never`
and `deny` stop the action.

### Layers

The same keys exist at every layer. A missing key inherits from the
layer behind it. The nearest layer that sets a key wins for that key.
A nearer file may allow more than the file behind it. A second run
reads the files again, so an edit to a bounds file is what the next
run uses. A file supplies only the keys it names.

The layers, from farthest to nearest, are the defaults in this skill,
the user config file `~/.config/kobold-codex/bounds.yaml` (one file per
machine, outside every repository), the committed repo file
`.kobold/bounds.yaml` at the repository root, and the checkout file
`.kobold/bounds.local.yaml` at the repository root. The checkout file
stays out of git. A missing file is an empty layer. Each bounds file
is a YAML mapping, one key per line.

### Defaults

| Key | Default | Description |
| --- | --- | --- |
| `commit` | `ask` | Work commit. Changed and untracked files outside the plan directory and the spec directory. |
| `commit-plans` | `never` | Commit of plan files, in the project's plans directory or `docs/plans/`. |
| `commit-specs` | `ask` | Commit of spec files. In this plugin, `docs/specs/`. |
| `push` | `ask` | Update the remote branch. |
| `pull-request` | `ask` | Open a pull request. `open` and `auto` do this without a fresh ask. |
| `merge` | `never` | Merge the pull request. |
| `force-push` | `never` | Rewrite the remote branch. Also requires `push` to be `ask` or `auto`. |
| `shell-network` | `ask` | A shell command that reaches the network. |
| `browser` | `ask` | Driving a browser. |
| `github-write` | `ask` | Comments, labels, issues, and review submission. |
| `subagents` | `ask` | Starting other agents. |
| `worktrees` | `ask` | An isolated checkout. |
| `unattended` | `stop-at-plan` | How far a session goes while the user is away. |
| `model` | absent | Optional model name for routed work. Absent keeps the session's current model. |

### Values

`commit`, `commit-plans`, `commit-specs`, and `push` are `ask`, `auto`,
or `never`. `pull-request` is `never`, `ask`, `open`, or `auto`.
`merge` and `force-push` are `never` or `ask`. A tool key is `ask`,
`allow`, `auto`, or `deny`. The tool keys in the default set are
`shell-network`, `browser`, `github-write`, `subagents`, and
`worktrees`. A bounds file may add a tool name. `github-write` is
comments, labels, issues, and review submission. `unattended` is
`stop-at-plan`, `safe-steps`, `through-publish`, or `auto`.

`auto` on `pull-request` opens one pull request without a fresh ask,
the same as `open`. `auto` on a tool key proceeds, the same as
`allow`. `auto` on `unattended` follows the publishing keys, the same
as `through-publish`.

A setting line is a key, a colon, and a value. Blank lines are skipped.
A line that is not a setting stays in the file and sets nothing. A
value outside the set for a key that has one does not resolve. `model`
takes a name, so that check skips it. Tell the user the line, and keep
the value from the layer behind that file.

### Publishing sets

`commit` stages the work, which is every changed or untracked file
outside the plan directory and the spec directory. `commit-plans`
stages plan files. `commit-specs` stages spec files. A plan file sits
in the directory the project uses for plans. When the project has
nowhere else, that directory is `docs/plans/`. A spec file sits in the
directory the project uses for design specs. In this plugin that
directory is `docs/specs/`. When a path matches both directories, it
is a spec.

`commit: auto` leaves plans and specs to their own keys. Each set that
is `auto` is its own commit. Each set that is `ask` is offered on its
own. Each set that is `never` stays unstaged. An empty set is skipped.
A second run leaves a finished commit as it is and commits only a set
that is still uncommitted and still allowed.

`auto` on `push` pushes without a fresh ask. `open` on `pull-request`
opens one pull request without a fresh ask. Force-push runs only when
`force-push` is `ask` and `push` is `ask` or `auto`.

### Unattended

`unattended` applies when the user is away or has asked the session to
continue without them. While the user is directing the next step, the
publishing keys and the tool keys decide.

`stop-at-plan` stops once the plan is written. When the work has no
plan, it stops before the edit.

`safe-steps` may read, edit, run the project's checks, and write the
plan and the trail. Publishing and named tools stay outside that list.

`through-publish` may commit the work, the plans, and the specs, then
push, open a pull request, or merge, only as far as those keys already
allow. An `ask` still asks. A `never` still stops. Force-push and a
named tool stay on their own keys.

### Revise a layer

Revise one writable layer at a time. The writable layers are the user
config file, the committed repo file, and the checkout file. The
defaults change when this skill changes. When the user has not named
the layer, ask which writable layer they mean.

When the user names no keys, leave every bounds file as it is. Do not
create a file. Reply with a table of every key in Defaults, plus any
extra key a farther layer sets. The columns are the key, the value
that applies while this layer leaves the key unset, and the
description from Defaults. An extra key uses the description "A tool
key added in a bounds file."

When the user names keys, show the resolved value of each of those
keys, and the layer that sets it now, before writing. Replace the line
for a key they named. Append a key that was not already in the file.
Leave every other line as it was. Create the file when it is missing,
and write only the keys they named. Write a default key in the
spelling the defaults use. An added tool name is lowercase.

When the file is the checkout file, the repository ignore rules include
`.kobold/bounds.local.yaml`. Add that pattern when the path is not
already ignored.

## What this skill does not do

It does not ship the branch. The skill that integrates a branch reads
the resolved keys and acts.

It does not restate the creed or `scope-the-edit`.

It does not add a model-per-role table. The optional `model` key is
the menu.

It does not change the 2026-10-01 creed or the 2026-10-01 scoping
skill. The catalog's bounds filenames follow this spec.

## Tuning

Edit `skills/set-the-bounds/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-02 wording.

The catalog still describes the bounds rule, because it is the record
of the whole skillset. The paragraphs the check compares live here.

## Implementation check

The build is done when all of these are true:

- `skills/set-the-bounds/SKILL.md` carries the frontmatter and the
  seven sections above. The heading text matches. The paragraphs match
  this document.
- `skills/kobold-codex/SKILL.md`,
  `skills/scope-the-edit/SKILL.md`,
  `docs/specs/2026-10-01-kobold-codex-design.md`, and
  `docs/specs/2026-10-01-scope-the-edit-design.md` are unchanged.
  The catalog's bounds files are the YAML paths in Decisions.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.3.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  sentence in Decisions.
- The README links this spec and the new skill, keeps the install
  commands, and does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.3.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
  The user config path is the portable tilde path.
