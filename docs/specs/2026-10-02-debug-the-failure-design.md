# Debug the failure

Design for the failure skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `how-it-fits` and `why-it-is`.
The wording in the skill sections below is the version to ship. Later
sessions tune it by editing the skill file. This spec stays the record
of what we decided and why.

## Purpose

`debug-the-failure` is the procedure for a failure that can be run
again. The session holds one hypothesis at a time, checks it against
the running system and the trace, and changes the code that produces
the bad result.

The creed's "Fix the cause" principle stays in
`skills/kobold-codex/SKILL.md`. This skill is the steps. It does not
restate that paragraph. `scope-the-edit` still decides how much plan
and proof the edit gets. `how-it-fits` and `why-it-is` stay read-only.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

Runtime evidence and trace evidence are one skill. The catalog said
so. A separate trace skill was not added. The trace says where to
look. The run says what the value was.

The session names the failure and runs it again before editing. A
second run that differs means the failure is not stable yet. The
session narrows the input or the environment until a run repeats.
When the failure cannot be run, the session asks for what is missing
and stops.

One hypothesis is open at a time. It names a place in the code and a
reason that place would produce this result. A check that disagrees
retires it. The next hypothesis starts from what the check showed.

Three is the stop. After three checks that disagree, or three edits
that leave the same failure in place, the session stops editing and
reports what the three showed. The design is then the question, and
that question is an architectural edit under `scope-the-edit`. The
number is there so a session does not keep patching past that point.

A temporary observation is how the session sees a value the trace
does not show. A log line, a print, or a breakpoint counts. It comes
out before the work is called done, unless the project already keeps
that kind of trace.

The fix lands on the code that produces the bad result. A change that
hides the result, swallows the error, or special-cases the one input
that failed stays out. After the fix, the original failure is run
again. Another check may run beside it. The original failure is still
one of the runs.

This skill does edit. The investigation playbook does not, and
`how-it-fits` and `why-it-is` do not. The catalog brief for this skill
includes the fix, so the edit is part of the procedure once the
producer is known.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These three investigation skills ship together. The plugin version
becomes `0.4.0` in that change. The plugin and marketplace
description becomes the following sentence.

```text
Voice, engineering principles, edit scoping, action bounds, and investigation for DragonCrafted87's agents on Grok and Claude Code.
```

The README points at the new skill and at this spec. It does not
restate the skill paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, and
`set-the-bounds`, and it requires version `0.4.0` and the description
above.

## Where the words live

```text
skills/debug-the-failure/SKILL.md
docs/specs/2026-10-02-debug-the-failure-design.md
```

The creed, `scope-the-edit`, and `set-the-bounds` stay. The catalog
keeps the skillset list and the build order. Its text for this skill
stays the brief.

## Skill

Frontmatter `name` is `debug-the-failure`. Frontmatter `description`
is one physical line:

```text
Use when a failure can be reproduced. Hold one hypothesis at a time, check it on the running system, and put the fix at the producer of the symptom.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### Reproduce

Name the failure before changing code. Record the command or the
action, the input, and the result you observed. Run that failure
again. When the second run produces a different result, the failure
is not stable yet. Narrow the input or the environment until a run
repeats the same result. When it still does not repeat, say so and
stop.

When you cannot run the failure, ask for the input, the environment,
or the steps that are missing, and stop.

### One hypothesis

State one hypothesis. It names a place in the code and a reason that
place would produce this result. Check that hypothesis before you
write another. A check that disagrees retires it. The next hypothesis
starts from what the check showed.

After three checks that disagree, or three edits that leave this
failure in place, stop editing. Report what those three showed. The
design is now the question, and that question is an architectural
edit.

### Evidence

Read the trace for this failure. That means the stack, the log line,
the test name, and the exit status. Then observe the running system
at the place the hypothesis named. A frame in the trace is a place to
look. The value at that frame, on this input, is the evidence.

When the trace does not show the value, add a temporary observation.
A log line, a print, or a breakpoint counts. Remove that observation
before calling the work done, unless the project already keeps that
kind of trace.

Report the value you observed. Leave out a value the run did not show.

### The producer

Change the code that produces the bad result. Leave out a change that
hides the result, swallows the error, or special-cases the one input
that failed.

The plan and the proof for that change follow the scope of the edit.

### The same failure

Run the original failure again. The result that failed is the result
that has to succeed. Another check may run beside it. The original
failure still has to be one of the runs.

When you cannot run the original failure again, say so, and name the
run you did execute.

## What this skill does not do

It does not start from a failure that cannot be run. It asks for the
missing piece and stops.

It does not keep a temporary observation in place of a fix.

It does not restate the scopes in `scope-the-edit`. It does not read
a subsystem the way `how-it-fits` does, and it does not recover a
historical reason the way `why-it-is` does, beyond what the current
hypothesis needs.

It does not change the creed, `scope-the-edit`, `set-the-bounds`, or
the catalog.

## Tuning

Edit `skills/debug-the-failure/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-02 wording.

## Implementation check

The build is done when all of these are true:

- `skills/debug-the-failure/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs match
  this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three 2026-10-01 and
  2026-10-02 specs those skills pin, and the catalog are unchanged.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.4.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  sentence in Decisions. `how-it-fits` and `why-it-is` ship in that
  same version.
- The README links this spec and the new skill, keeps the install
  commands, and does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.4.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
