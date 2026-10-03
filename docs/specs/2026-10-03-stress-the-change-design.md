# Stress the change

Design for the several-pass review. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `review-the-diff` and
`take-the-review`. The wording in the skill sections below is the
version to ship. Later sessions tune it by editing the skill file.
This spec stays the record of what we decided and why.

## Purpose

`stress-the-change` sends one diff through several independent
passes, then merges their findings into one list. The passes use
different angles. The list is something `take-the-review` can check.

`review-the-diff` is one pass in the current session. This skill is
the review you run when one pass is too easy on its own findings. A
pass that can see the others can talk itself out of a real fault.
Separate passes keep that from happening. The merge keeps a fault
that only one pass raised.

The tree stays as it was. The creed stays in
`skills/kobold-codex/SKILL.md`. This skill does not restate those
principles.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Several reviewers, then one list.
When only one model is available, the passes still run separately,
one after another, each without the other passes' findings. Fresh
context means the pass is given the diff, the request, the checks,
and its angle, and it is not given another pass's notes. The
session may already hold those notes. The pass does not use them.

The angles are three, and they are the whole review. A fourth angle
was set aside. `measure-the-blast` is the later skill for what could
break outside the diff, and `fan-out` is the later skill for a wider
split. This skill does not become either of those.

The three angles are the request, the checks, and the changed lines.
The request pass looks for a missing piece and for a change the
request did not ask for. The checks pass runs the checks the plan or
the change named. A failure, a check that cannot be run, and a check
that passes without reaching the behavior it claims are findings.
The other two passes do not run the checks. The changed-lines pass
looks for a defect in a line the diff adds or changes. A problem in
a line the diff does not touch stays out of that pass.

The diff rule matches `review-the-diff`, and the words are repeated
here so this skill can run on its own. A named branch, range, pull
request, or set of files is the change, reviewed on its own. When
the user names none, the diff is the current branch against the
branch it would merge into, including uncommitted work, labeled
uncommitted.

`subagents` is resolved before another agent starts. When that key
allows another agent, the three passes may run together. Each agent
returns findings and does not edit. This session writes the list.
When the key does not allow another agent, the passes run one after
another here. The optional `model` key, when set, names the model
for a pass that runs in another agent. When it is absent, that pass
uses the model already running the session. There is no
model-per-angle table. The catalog left that table out until one
`model` key is not enough. One model still means three passes.

A pass that does not come back leaves the list unfinished. The
session names the missing pass and stops. The passes stay unmerged.

The merged list uses the same finding shape as `review-the-diff`:
file, line, what is wrong, and why it matters. This skill adds the
passes that raised it. The same file, line, and fault from more than
one pass is one finding. A finding only one pass raised stays. A
vote does not remove it. When the passes disagree, the finding stays
and the list names the passes on each side. `take-the-review` checks
the code. This skill does not pick a winner. The list is ordered by
file, then by line. A pass that raised nothing is named, so a quiet
pass is visible. An item with no line stays out of the list, and the
report says what was looked at.

The list lives in the reply. A second run reviews the diff as it is
now and replaces the list. It does not append. A request to post
the list follows `github-write`. This skill stops at the list.

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
skills/stress-the-change/SKILL.md
docs/specs/2026-10-03-stress-the-change-design.md
docs/plans/2026-10-03-review-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the three
investigation skills, and the two plan skills stay. The catalog
keeps the skillset list and the build order. Its text for this
skill stays the brief.

## Skill

Frontmatter `name` is `stress-the-change`. Frontmatter `description`
is one physical line:

```text
Use when a diff needs several independent reviews. Run separate passes on different angles, merge the findings into one list, and leave the tree alone.
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

Read the request, and the plan when there is one. The request is
what the user asked for. The checks are the ones the plan or the
change named.

### Three passes

Run three passes on that same diff. A pass sees the diff, the
request, the checks, and its own angle. A pass does not see another
pass's findings. A finding from a pass names the file, the line,
what is wrong, and why it matters.

The first pass is the request. A missing piece of the request is a
finding. A change the request did not ask for is a finding.

The second pass is the checks. Run the checks when they can be run.
A failed check is a finding. A check that cannot be run is a
finding, and the finding names the reason. A check that passes
without reaching the behavior it claims is a finding. The other
passes do not run the checks.

The third pass is the changed lines. A defect in a line the diff
adds or changes is a finding. A problem in a line the diff does not
touch stays out of this pass.

When only one model is available, run the three passes one after
another. Each pass starts without the other passes' findings.

Resolve `subagents` before starting another agent. When that key
allows another agent, the three passes may run together. The other
agent returns its findings and does not edit. This session writes
the list. When `subagents` does not allow another agent, run the
three passes one after another in this session.

When `model` is set, a pass in another agent uses that model. When
`model` is absent, the pass uses the model already running the
session. Keep all three passes when `model` is set and when it is
absent.

A pass that does not return leaves the list unfinished. Name the
missing pass and stop. Leave the passes unmerged.

### One list

Merge the finished passes into one list in the reply. A finding
names the file, the line, what is wrong, why it matters, and which
passes raised it. The same file, line, and fault from more than one
pass is one finding. A finding only one pass raised stays on the
list. When one pass calls a line wrong and another pass calls that
line fine, keep the finding and name the passes on each side.

Order the list by file, then by line. When a pass raised nothing,
say so.

When you cannot name the line, say what the pass looked at, and
leave that item out of the list.

### Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks this list.

A second run reviews the diff as it is now. The new list replaces
the earlier list.

The list stays in the reply. A request to post it follows
`github-write`. This skill stops at the list.

## What this skill does not do

It does not edit. The user asks for a fix before any file is
written, and that fix is `take-the-review`.

It does not drop a finding because only one pass raised it, and it
does not pick a side when the passes disagree.

It does not add a fourth angle. It does not walk callers outside
the diff. `measure-the-blast` is that later skill. It does not
become the general split of work. `fan-out` is that later skill.

It does not assign a model per angle. One `model` key, or the
session's model, covers every pass.

It does not merge the branch. A merge follows `set-the-bounds`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, or the catalog.

## Tuning

Edit `skills/stress-the-change/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/stress-the-change/SKILL.md` carries the frontmatter and
  the four sections above. The heading text matches. The paragraphs
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
  stable sentence in the catalog's ship rule. `review-the-diff` and
  `take-the-review` ship in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.6.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
