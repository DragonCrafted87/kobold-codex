# Scope the edit

Design for the second Kobold Codex skill. Approved in conversation on
2026-10-01. The wording in the skill sections below is the version to
ship. Later sessions tune it by editing the skill file. This spec stays
the record of what we decided and why.

## Purpose

`scope-the-edit` tells an agent how much plan and proof an edit gets.
The amount follows the scope of the edit. A settings change and a new
subsystem do not get the same ceremony.

The 2026-10-01 creed in `skills/kobold-codex/SKILL.md` stays as it is.
This skill does not restate those principles. Both skills ship in the
`kobold-codex` plugin.

Success for this version is a second skill that a Grok session and a
Claude Code session can both load, whose section bodies match the
skill sections below.

## Decisions

The first spec deferred one rule: an edit is preceded by a short design
and an explicit yes, including when the task already looks clear.
Superpowers and pstack both push a failing test before a fix. This
skill replaces that flat gate. The scope of the edit decides the plan
and the proof.

A small edit is done in the same turn. An intermediate edit carries
its check in the same turn, and stops when two checks would change the
work. An architectural edit stops for a written plan and an explicit
yes.

Branch coverage is the minimum proof for a function that decides
something. MC/DC (Modified Condition/Decision Coverage) is the aim when
that decision is a complex algorithm, because a covered branch can
still hide a condition that never changes the outcome on its own. A
run of the system is the default proof. A mock stands in when the real
dependency cannot be run. A focused test covers a branch the system
boundary cannot reach.

The intermediate section and the real-code section are read together.
An existing repro or system run is enough for a bug fix when that run
reaches the real-code bar. A new test is added when no existing run
reaches it.

Playbooks, investigation skills, and multi-model review stay later.
Nothing in the skill names a Grok tool or a Claude tool. No hooks, no
model routing.

The plugin version becomes `0.2.0` when the skill is added. The plugin
and marketplace description becomes the following sentence.

```text
Voice, engineering principles, and edit scoping for DragonCrafted87's agents on Grok and Claude Code.
```

The README points at the new skill and at this spec. It does not
restate the skill paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, and it requires version `0.2.0` and
the description above.

## Where the words live

```text
skills/scope-the-edit/SKILL.md
docs/specs/2026-10-01-scope-the-edit-design.md
docs/plans/2026-10-01-scope-the-edit.md
```

The creed files stay. This work does not edit their paragraphs.

## Skill

Frontmatter `name` is `scope-the-edit`. Frontmatter `description` is
one physical line:

```text
Use before changing a file or making a commit. Name the scope of the edit, then add only the plan and the proof that scope calls for.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### Name the scope

Before editing, name the scope in the reply. The scopes are small,
intermediate, and architectural. Name the scope once, before the first
edit of a change. A commit of work already under that scope is part of
the same change. A settings change, or any other edit whose destination
is already known and that does not change behavior, is small. A bug
fix is intermediate. A change inside a function that has a decision is
intermediate, including a one-line fix. A new subsystem, or a change
that reshapes how the pieces fit together, is architectural. When two
scopes both fit, use the larger one.

### Small

Do the edit in the same turn. The edit is the whole task. The check is
the file that was written.

### Intermediate

Say what is wrong, what will change, and which check will show the
fix. The original repro, an existing command, or a run of the system
can be that check. Carry out the edit and the check in the same turn.
When two checks would change the work, stop and ask which one to run.

### Architectural

Write a plan the reviewer can read. Say what will change, which parts
of the system it touches, what the tests will cover, and what stays
the same. Write the plan where the project keeps plans. When the
project has nowhere for it, use docs/plans/. Stop after the plan.
Implementation starts after an explicit yes to that plan. A yes names
this plan. "Yes", "do it", or the choice the plan just offered counts.
Approval of an earlier piece of work does not carry forward. Once the
conversation has that yes, do the work.

### Real code

When the edit changes a function in C, C++, C#, Python, Java, or
another language in that class, the check follows the code. A
non-trivial function has a decision in it, and the check reaches each
branch. A complex algorithm is one whose decision combines several
conditions, or whose result depends on interacting decisions. Aim at
MC/DC for that algorithm: each condition can change the outcome on its
own. Say whether the check reached branch coverage or MC/DC. Exercise
the system. Use a mock when the dependency cannot be run, such as
hardware or a paid external service. When a branch cannot be reached
from the system boundary, cover that branch with a focused test. Add a
test when no existing run reaches the bar.

## What this skill does not do

It does not stop a small edit for a design.

It does not require a new test suite for every bug fix. The real-code
bar still applies when the edit changes a non-trivial function.

It does not require a written spec for every edit. An architectural
change gets a plan. A written spec is a separate request.

It does not add playbooks, investigation skills, or a second model.

It does not change the 2026-10-01 creed.

## Tuning

Edit `skills/scope-the-edit/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-01 wording.

## Implementation check

The build is done when all of these are true:

- `skills/scope-the-edit/SKILL.md` carries the frontmatter and the five
  sections above. The heading text matches. The paragraphs match this
  document.
- `skills/kobold-codex/SKILL.md` and
  `docs/specs/2026-10-01-kobold-codex-design.md` are unchanged.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.2.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  sentence in Decisions.
- The README links this spec and the new skill, keeps the install
  commands, and does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.2.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while both skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
