# Fan out

Design for the parallel-work skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`fan-out` splits work that does not share state into workers, waits
for them, and returns one report. The catalog names independent
tasks, coverage, races, and exploration as the uses. `subagents` has
to allow the parallel form.

`carry-out-the-plan` already sends independent tasks in one plan to
another agent. `stress-the-change` already runs three review passes.
`try-several-shapes` is the skill for several shapes of one change.
This skill is the wider split those three do not own.

`set-the-bounds` resolves `subagents` and `model`. This skill reads
the resolved values. It does not revise a layer.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Split work that shares no state,
wait, and return one report.

Two pieces share state when they would change the same file, the
same checkout, or the same record outside the repo. Those pieces
stay together. The split is the rest.

The pieces come from the user, or from another skill in this plugin
that asked for the split. Independent tasks are pieces already
separated. Coverage is a set of areas, each read or run on its own.
A race is the same check run more than once, to see whether the
result changes. Exploration is a set of questions, each read on its
own. When only the kind of split is named, the session names up to
three pieces and runs those. Three is a bound so a vague request
does not become an open-ended set of workers. A wider set waits
until the extra pieces are named.

The parallel form follows `subagents`, the same way
`carry-out-the-plan` and `stress-the-change` already do. When the
key does not allow another agent, the pieces run one after another
in this session, and the report says the run was serial. The
catalog's "has to allow it" is the gate on the parallel form. The
report still comes back either way.

A worker returns a result. It does not write the report, and it
does not change a file another piece changes. This session writes
the report. When `model` is set, a worker in another agent uses
that model. When `model` is absent, the worker uses the model
already running the session. That matches `stress-the-change`.

A worker that does not return leaves the report unfinished. The
finished pieces stay unmerged until the missing one returns. A
partial merge would look like a finished split.

The report stays in the reply. Posting it follows `github-write`.
While the user is away, `unattended` still applies, and a named
tool stays on its own key.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These eleven step-7 skills ship together. The plugin version becomes
`0.9.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the earlier skills, and it requires version
`0.9.0` and the stable description.

The root README stays the introduction and the install guide. It
does not record this decision. `docs/skills.md` links the skill and
this spec, and it does not restate the skill paragraphs. Install
commands stay as they are.

The catalog keeps the skillset list, the playbook briefs, and the
build order. Its text for this skill stays the brief.

## Where the words live

```text
skills/fan-out/SKILL.md
docs/specs/2026-10-03-fan-out-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the investigation
skills, the plan skills, the review skills, `ship-the-branch`, and
`run-the-play` stay. The sentences in `carry-out-the-plan` and
`stress-the-change` that leave a wider split to this skill stay.
This skill agrees with them: plan tasks and the three review passes
keep their own skills.

## Skill

Frontmatter `name` is `fan-out`. Frontmatter `description` is one
physical line:

```text
Use when work that does not share state should run as parallel workers. Split it, wait for the workers, and return one report. subagents has to allow the parallel form.
```

The body is the four sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Fan out.

### The pieces

Split work that does not share state. Two pieces share state when
they would change the same file, the same checkout, or the same
record outside the repo. Keep those pieces together.

The pieces are the ones the user named. When another skill in this
plugin asks for the split, the pieces it named are the pieces.
Independent tasks are pieces already separated. Coverage is a set
of areas, each read or run on its own. A race is the same check
run more than once, to see whether the result changes. Exploration
is a set of questions, each read on its own.

When the kind of split is named and the pieces are not, name up to
three pieces and run those. A wider set waits until the extra
pieces are named.

`carry-out-the-plan` splits tasks inside one plan.
`stress-the-change` runs the three review passes.
`try-several-shapes` runs the candidates for one change. This
skill is the split those three do not already cover.

### The workers

Resolve `subagents` before starting another agent. When that key
allows another agent, the pieces run together. A worker returns
its result. It does not write the report, and it does not change
a file another piece changes. This session writes the report.

When `subagents` does not allow another agent, run the pieces one
after another in this session, and say that the run was serial.

When `model` is set, a worker in another agent uses that model.
When `model` is absent, the worker uses the model already running
the session.

While the user is away, `unattended` still applies. A named tool
stays on its own key. `set-the-bounds` is that rule.

A worker that does not return leaves the report unfinished. Name
the missing piece and stop. Leave the finished pieces unmerged.

### One report

Write one report in the reply, in the order the pieces were named.
Each piece names what it was, the result, and whether it finished.
A piece that found nothing says so.

The report stays in the reply. A request to post it follows
`github-write`.

### The same split

A second run splits the work as it stands now. The new report
replaces the earlier report. A piece whose result is already
recorded, and whose inputs are unchanged, can be cited from that
record. Name the record. Run a piece whose inputs changed.

## What this skill does not do

It does not mark a plan checkbox. `carry-out-the-plan` does that.

It does not run the three review passes. `stress-the-change` does
that.

It does not pick a base or fold candidates.
`try-several-shapes` does that.

It does not resolve a bounds file and it does not revise one.
`set-the-bounds` does that.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/fan-out/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/fan-out/SKILL.md` carries the frontmatter and the four
  sections above. The heading text matches. The paragraphs match
  this document. The title is Fan out.
- The skills already in the plugin, the specs those skills pin, the
  four playbooks, the catalog, and the root README are unchanged.
  The other ten step-7 skills ship in the same change, each from
  its own spec.
- `tests/check_plugin.py` fails when a paragraph, the frontmatter,
  the version, the manifest description, or a restatement of a
  section in the README drifts.
- Plugin version is `0.9.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match
  the stable sentence in the catalog's ship rule.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the skill. The README
  does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.9.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires the skill file.
- No tracked file names a hostname, a home directory, or a machine.
