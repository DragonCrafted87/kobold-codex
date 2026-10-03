# Run the play

Design for the playbook skill and the first playbooks. The catalog
in `docs/specs/2026-10-02-remaining-skills-design.md` named this
skill on 2026-10-02, as build-order step 6, once a few playbooks
had real text to route to. The wording in the skill sections and
the playbook sections below is the version to ship. Later sessions
tune it by editing the skill file or a playbook file. This spec
stays the record of what we decided and why.

## Purpose

`run-the-play` matches a task to one playbook and runs that
playbook's steps. The playbooks are files beside the skill. Each
one is a short procedure. The skill is the trigger.

This version's playbooks are the basic set: `feature`, `bug-fix`,
`refactor`, and `investigation`. Their steps name skills this
plugin already has.

`set-the-bounds` resolves a key. This skill reads the resolved
value and stops where that value says to stop. It does not revise
a layer.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for.

Success for this version is a skill that a Grok session and a
Claude Code session can both load, whose section bodies match the
skill sections below, and four playbook files whose section bodies
match the playbook sections below.

## Decisions

The catalog brief is the content. Match the task to one playbook,
copy that playbook's steps into the working list, record a skip
with a reason, and stop where the resolved bounds say to stop.

The four playbooks above are the ones whose steps can be written
against skills already in the plugin. The build order asked for a
few playbooks with real text before this skill could route. A
one-line stub is not a file this router should offer.

The other nine briefs stay in the catalog: `perf`, `hillclimb`,
`prototype`, `multi-phase`, `visual-parity`, `eval`, `unattended`,
`pause`, and `pickup`. A file for one of them waits for a later
spec whose steps are as specific as the four below.

`review-the-diff` and `ship-the-branch` stay outside these four.
The feature brief stops at the proof. The bug-fix brief stops at
the second run of the failure. The investigation brief stops at
the read. A session that has finished a playbook, and is then
asked to review or to integrate, uses those skills on their own.

The working list is the list in the reply. It is not a plan file,
and it is not a log in the repository. `carry-out-the-plan` owns
the checkboxes in a plan. `leave-a-trail` is the later skill for a
log.

A skip is a step the playbook says does not apply, or a step the
user told the session to leave out. The reason is recorded, and
the later steps run. A stop is the bounds, or a skill the step
called that itself stopped. The step stays waiting, so a later run
can start there.

The playbook files are not skills. They have no frontmatter and no
trigger of their own. The description on `run-the-play` is the
trigger. A playbook title is the file name with hyphens written as
spaces and the first letter capitalized. `bug-fix` is titled Bug
fix. That is the same spelling the skill titles already use.

Nothing in the skill or the playbooks names a Grok tool or a
Claude tool. No hooks.

The plugin version becomes `0.8.0` in the change that ships the
skill. The manifest description stays the stable sentence in the
catalog's ship rule.

`tests/check_plugin.py` pins the new section bodies to this
document the same way it pins the earlier skills. It also pins
each playbook by name and by section. It discovers the playbooks
from the `## Playbook:` headings below, so this spec is the list.
Two playbooks both have a section named Scope. The check reads
each playbook's sections inside that playbook's region, so those
bodies stay distinct. It requires version `0.8.0` and the stable
description.

This skill ships with the four playbooks. The root README stays
the introduction and the install guide. It does not record this
decision. `docs/skills.md` links the skill and this spec, and it
does not restate a section body. Install commands stay as they
are.

The catalog keeps the skillset list, the playbook briefs, and the
build order. Its text for this skill stays the brief.

## Where the words live

```text
skills/run-the-play/SKILL.md
skills/run-the-play/playbooks/feature.md
skills/run-the-play/playbooks/bug-fix.md
skills/run-the-play/playbooks/refactor.md
skills/run-the-play/playbooks/investigation.md
docs/specs/2026-10-03-run-the-play-design.md
docs/plans/2026-10-03-run-the-play.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the three
investigation skills, the two plan skills, the three review
skills, and `ship-the-branch` stay. The sentences in the
investigation specs that mention the investigation playbook stay.
This playbook agrees with them: the read does not edit, and
`debug-the-failure` is the skill that changes code for a failure.

## Skill

Frontmatter `name` is `run-the-play`. Frontmatter `description`
is one physical line:

```text
Use when a task should follow a playbook. Match it to one playbook, copy that playbook's steps into the working list, record a skip with a reason, and stop where the resolved bounds say to stop.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Run the
play.

### The match

Match the task to one file in the `playbooks` directory beside
this skill.

When the user names one of those files, or names its title, use
that file. When the name is not a file there, name the files that
are there, and stop.

When the user names none, choose from the files that are there. A
failure they want fixed is `bug-fix`. An explanation or a
diagnosis, with no edit asked for, is `investigation`. A reshape
that keeps the outward behavior is `refactor`. New behavior is
`feature`.

When more than one of those fits, name the matching files and ask
which one to run. When none of them fits, name the files that are
there and stop.

A file that no rule above names stays unused until the user names
it.

### The list

Copy that playbook's steps into the working list, in the order of
its headings. A step is one heading. The text under the heading is
the procedure.

The list is part of the reply. It is not a file in the repository,
and it is not a plan file. Show the list before the first step
starts. Each entry is waiting, done, or skipped.

Follow one step, then update the list, before the next step
starts. When a step names a skill, follow that skill for the part
the step describes. A later step that continues the same pass
picks up where that part stopped. When the named skill stops the
work, this playbook stops with it, and the later steps stay
waiting.

When every step is done or skipped, say that the playbook is done.

### A step left out

Leave a step out when the playbook says it does not apply, or when
the user says to leave it out. Record the step and the reason on
that list entry, then continue with the later steps.

The reason names the scope, or it names what the user said. An
entry with no reason stays waiting.

### Where it stops

When the user is away, or has asked the session to continue
without them, resolve `unattended` before the first step.
`set-the-bounds` is that rule. This skill does not loosen it.

Do not start a step the resolved value does not allow. Leave that
step and the later steps waiting, and stop. Name the key, the
value, and the layer that set it.

While the user is directing the next step, the publishing keys and
the tool keys decide. A step that commits, pushes, opens a pull
request, merges, force-pushes, or uses a named tool follows
`set-the-bounds`.

### The same task

Read the playbook again and rebuild the list. A step is done when
its result is already true and you can point at the evidence in
the tree or in the earlier record. Name that evidence. A skip
whose reason still holds stays skipped. A step that stopped on the
bounds is waiting.

Begin at the first step that is waiting. When the evidence for a
finished step is gone, that step is waiting.

## Playbook files

Each region below is one file in
`skills/run-the-play/playbooks/`. The region heading names the
file. `## Playbook: feature` is `feature.md`. The file has no
frontmatter. Its title is the file name with hyphens written as
spaces and the first letter capitalized. Its `##` sections are the
`###` sections in that region, in that order, with the same
bodies.

## Playbook: feature

### Scope

`scope-the-edit` names the scope before the first edit. Follow
that skill, including the edit it requires for a small or
intermediate scope. An architectural scope names the scope and
does not edit in this step.

### Shape

When the scope is architectural, `write-the-plan` writes the plan.
That step is done when the plan file is written. The later steps
stay waiting until the user approves that plan. When the scope is
small or intermediate, leave this step out. The reason is that
scope.

### Build

When Scope already made the edit, leave this step out. The reason
is that scope. When a plan is required and it is not approved yet,
stop and leave this step waiting. When the user has approved the
plan, `carry-out-the-plan` runs it.

### Prove

Record the check the scope or the plan named, and the result you
observed. Run the check when it has not been run. When the edit
changed a function, the bar for that check is `scope-the-edit`. A
failed check stops the playbook.

## Playbook: bug-fix

### Reproduce

Follow `debug-the-failure` from its first step through the run
that repeats the failure. When that skill stops because the
failure cannot be run, stop this playbook. The later steps stay
waiting.

### Cause

Continue that same pass. One hypothesis, then a check against the
running system. Stop when that skill says to stop.

### Fix

Continue that same pass. The change lands on the producer. The
plan and the proof for the change follow `scope-the-edit`.

### Again

Continue that same pass. Run the original failure. The result that
failed is the result that has to succeed.

## Playbook: refactor

### Behavior

Name the outward behavior this reshape must keep. Run the check
that shows that behavior now, and record the command and the
result. When no check shows it, stop and ask which check does.
Leave the later steps waiting.

### Scope

`scope-the-edit` names the scope before the first edit. Follow
that skill, including the edit it requires for a small or
intermediate scope. An architectural scope names the scope and
does not edit in this step.

### Shape

When the scope is architectural, `write-the-plan` writes the plan.
That step is done when the plan file is written. The later steps
stay waiting until the user approves that plan. When the scope is
small or intermediate, leave this step out. The reason is that
scope.

### Reshape

When Scope already made the edit, leave this step out. The reason
is that scope. When a plan is required and it is not approved yet,
stop and leave this step waiting. When the user has approved the
plan, `carry-out-the-plan` runs it. The outward behavior stays the
one Behavior recorded.

### The same behavior

Run the check from the first step again. The result has to match
the result recorded there. Another check may run beside it. The
first check is still one of the runs.

## Playbook: investigation

### The question

Name the question. A question about why a behavior or a threshold
exists is `why-it-is`. A question about where a change would land
is `how-it-fits`. When the task is both, name both.

A failure the user wants fixed is the `bug-fix` playbook. Say
that, and stop. Leave the later steps waiting.

### The read

Follow each skill the question named. Report what that skill
reports. When both apply, give both reads, and say which question
each read answers.

When the question is a failure and the user has not asked for a
fix, record the command, the input, and the result of a run that
uses the code as it stands.

### No edit

Leave the tree as it was at the start of this playbook. An edit is
a separate request.

## What this skill does not do

It does not write a playbook file that this spec does not name.
The nine briefs listed in Decisions stay briefs.

It does not review the diff. `review-the-diff` does that. It does
not integrate the branch. `ship-the-branch` does that.

It does not resolve a bounds file and it does not revise one.
`set-the-bounds` does that. This skill reads the resolved value
before it starts a step the bounds govern.

It does not restate the procedure of a skill a step names. The
step says which part of that skill this pass is in.

It does not edit during `investigation`. A fix is `bug-fix`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, or the catalog.

## Tuning

Edit `skills/run-the-play/SKILL.md`, or a playbook file beside it,
when a session shows that a paragraph is wrong, too thin, or too
long. Keep one copy. When the meaning of a section changes, note
the change in a later spec or in the commit message. This document
keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/run-the-play/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs
  match this document. The title is Run the play.
- The four playbook files exist at the paths in Where the words
  live. Each title follows the hyphen rule above. Each `##` body
  matches the `###` body in that file's region. The `##` headings
  are those `###` headings, in that order. No playbook has
  frontmatter. The directory has no other markdown file.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  the two plan skills, the three review skills,
  `skills/ship-the-branch/SKILL.md`, and the specs those skills pin
  are unchanged. The catalog's briefs stay. Its ship rule records
  the stable manifest description and points the skill map at
  `docs/skills.md`.
- `tests/check_plugin.py` fails when a skill paragraph, a playbook
  paragraph, the playbook heading order, the new frontmatter, the
  version, the manifest description, or a restatement of a skill
  or playbook paragraph in the README drifts.
- Plugin version is `0.8.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match
  the stable sentence in the catalog's ship rule.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.8.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires the skill file and each playbook file.
- No tracked file names a hostname, a home directory, or a machine.
