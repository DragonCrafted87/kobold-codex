# Review the diff

Design for the review skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `take-the-review` and
`stress-the-change`. The wording in the skill sections below is the
version to ship. Later sessions tune it by editing the skill file.
This spec stays the record of what we decided and why.

## Purpose

`review-the-diff` is the review a session runs before a merge, or
when the user asks for a review. It reads the diff against the
request and the checks, and it reports each finding with a file and
a line.

The report is the work. The tree stays as it was.
`take-the-review` is the skill that checks a finding and implements
it when it holds. `stress-the-change` is the skill that runs the
same diff through separate passes. This skill is one pass.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. One review, in this session,
against the request and the checks. Findings carry a file and a
line. The tree stays untouched unless the user asks for fixes, and
that ask is `take-the-review`.

`carry-out-the-plan` does not review each task. Its spec names this
skill as the later review. That sentence stays. This skill runs
once, on the change, after the tasks or whenever the user asks. It
does not run once per task, and it does not start another agent.
The several-pass review is `stress-the-change`, specified in the
same build step.

The diff is the change the user named: a branch, a range, a pull
request, or a set of files. That review stays on the named change.
When the user names none, the diff is the current branch against
the branch it would merge into, and uncommitted work is included
and labeled uncommitted. A named review does not pick up other
local edits.

The request is what the user asked for. The plan counts as part of
the request when there is one. A missing piece is a finding. A
change the request did not ask for is a finding. The checks are the
ones the plan or the change named. The session runs a check when it
can. A failure is a finding. A check that cannot be run is a
finding that names the reason. A check that passes without reaching
the behavior it claims is a finding.

A defect in a line the diff adds or changes is a finding when the
request and the checks do not already state that fault. A problem
in a line the diff does not touch stays out of the findings. The
report names each of those left-out items in one line, with the
reason, so a silent drop is visible. `measure-the-blast` is the
later skill that proves what could break outside the diff. This
skill does not do that proof.

A finding has no rank. File, line, what is wrong, and why it
matters are the whole record. A ranked list was set aside. A rank
would invite a session to skip a finding `take-the-review` is
supposed to check. When the line cannot be named, the item stays
out of the findings and the report says what was looked at.

The report lives in the reply. An empty review says so and names
the diff. A request to post the report follows `github-write`. This
skill stops at the report. A merge follows `set-the-bounds`.
`ship-the-branch` is the later skill that integrates the branch.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These three review skills ship together. The plugin version becomes
`0.6.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule, and later skills leave that
sentence as it is. The root README stays the introduction and the
install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, and the plan skills, and it requires
version `0.6.0` and the stable description.

## Where the words live

```text
skills/review-the-diff/SKILL.md
docs/specs/2026-10-03-review-the-diff-design.md
docs/plans/2026-10-03-review-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the three
investigation skills, and the two plan skills stay. The catalog
keeps the skillset list and the build order. Its text for this
skill stays the brief. The `carry-out-the-plan` spec keeps the
sentence that names this skill as the later review.

## Skill

Frontmatter `name` is `review-the-diff`. Frontmatter `description`
is one physical line:

```text
Use before a merge, or when the user asks for a review. Review the diff against the request and the checks, report each finding with file and line, and leave the tree alone.
```

The body is the four sections below. Heading text matches. Paragraphs
match, including line breaks.

### The diff

Review the change the user named. A named branch, a named range, a
pull request, or a named set of files is that change. Review that
change on its own.

When the user names none, review the current branch against the
branch it would merge into. Include uncommitted work in that
review, and say in the report that it is uncommitted.

Read the diff before you report. Read the request, and the plan
when there is one. The request is what the user asked for.

### The request and the checks

A missing piece of the request is a finding. A change the request
did not ask for is a finding.

Run the checks the plan or the change named, when they can be run.
A failed check is a finding. A check that cannot be run is a
finding, and the finding names the reason. A check that passes
without reaching the behavior it claims is a finding.

A defect in a line the diff adds or changes is a finding when the
request and the checks do not already state it. A problem in a line
the diff does not touch stays out of the findings.

### Findings

A finding names the file, the line, what is wrong, and why it
matters to the request or to a check. When you cannot name the
line, say what you looked at, and leave that item out of the
findings.

Report the findings in the reply. When there are none, say that,
and name the diff you reviewed.

After the findings, name anything you considered and left out
because it sits outside the diff. One line each, with the reason.
When you left nothing out, say so.

### Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks a finding and implements it when it holds.

The report stays in the reply. A request to post it follows
`github-write`.

This review is one pass in this session. `stress-the-change` runs
the separate passes. This skill stops at the report. A merge
follows `set-the-bounds`.

## What this skill does not do

It does not edit. The user asks for a fix before any file is
written, and that fix is `take-the-review`.

It does not start another agent, and it does not run a pass per
task. `carry-out-the-plan` left this review until the change is
ready to review.

It does not rank a finding. It does not drop a placed finding for
being small.

It does not prove what could break outside the diff.
`measure-the-blast` is the later skill for that.

It does not merge the branch. A request to post the report follows
`github-write`. A merge follows `set-the-bounds`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, or the catalog.

## Tuning

Edit `skills/review-the-diff/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/review-the-diff/SKILL.md` carries the frontmatter and the
  four sections above. The heading text matches. The paragraphs
  match this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  the two plan skills, and the specs those skills pin are unchanged.
  The catalog's skill briefs stay. Its ship rule records the stable
  manifest description and points the skill map at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a
  restatement of a skill paragraph in the README drifts.
- Plugin version is `0.6.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule. `take-the-review` and
  `stress-the-change` ship in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.6.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
