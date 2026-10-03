# Remaining skills

Catalog of the Kobold Codex skills still to write. Approved in conversation
on 2026-10-02. Each brief below is the scope of one later skill. The spec
for that skill holds the wording that ships. This document stays the
record of the set, the bounds rule, and the build order.

## Purpose

The creed and `scope-the-edit` are already in the plugin. The rest of
the skillset is the workflows those two skills left for later:
investigation, a written plan, execution, review, parallel work, proof,
and shipping. The set is drawn from the shape of Superpowers and pstack
and written as original prose. The same skills load in a Grok session
and a Claude Code session.

Success for this catalog is a list a later session can implement one
skill at a time, plus a bounds rule every skill that publishes or
spends a tool can read.

## Decisions

The 2026-10-01 creed spec deferred playbooks, investigation skills, and
multi-model review. The 2026-10-01 scoping spec deferred the same three.
This catalog is that follow-on. The creed file and the scoping file stay
as they are.

Parity is the behavior, in skills this plugin owns. The repo does not
vendor either source, and a skill file does not paste upstream wording.
A TypeScript house style, a bot UI, and issue-bot automations are
outside this set. A plain restatement of the last message stays with
the creed's voice.

There is no skill whose job is to force every other skill to load. The
description on each skill is the trigger. Nothing in a skill names a
Grok tool or a Claude tool. No hooks.

`set-the-bounds` is the setup skill. It is aimed at the actions people
turn on deliberately: commits, push, pull requests, merge, force-push,
unattended continuation, and named tools. `commit` is the work. Plan
docs and spec docs have their own keys, `commit-plans` and
`commit-specs`, so a repository can commit the work and leave the plans
unstaged. The default for plans is `never`. The default for specs is
`ask`, because a spec is the record of a decision and the next session
should hear about it before it lands or stays local. A model menu is
not a second setup skill. One optional `model` key may name the model
for routed work. Absent, the session's current model stays.

The nearest layer that sets a key wins for that key. A nearer file may
be more permissive than the file behind it. A rule where a nearer file
may only tighten was considered, for a machine that must forbid a push
no repository can allow. Replacement is the rule, because the closest
setting is the one that applies.

This catalog does not bump the plugin version and does not change the
README. The spec that ships a skill does both.

## Already in the plugin

`skills/kobold-codex/SKILL.md` is the voice and the eight principles.
The pstack principle skills fold in there: cause, proof, idempotence,
the shape of the data, redesign, removing dead weight, and leaving a
rerunnable tool. Claim-before-evidence is the proof principle.

`skills/scope-the-edit/SKILL.md` decides how much plan and proof an edit
gets. A small edit happens in the same turn. An intermediate edit names
the defect, the change, and the check. An architectural edit stops for
a written plan and an explicit yes. The scope of the edit is the gate
a flat failing-test rule fills in the source skillsets. A new test is
added when no existing run reaches the real-code bar. That is the
test-first behavior and the always-stop design behavior for this
plugin.

## Bounds

`set-the-bounds` reads and writes the files below. Every later skill
that commits, pushes, opens or merges a pull request, force-pushes, or
uses a named tool reads the resolved keys first.

Four layers, from farthest to nearest:

1. Defaults in `skills/set-the-bounds/SKILL.md`.
2. The user config file `~/.config/kobold-codex/bounds.yaml`, one per
   machine, outside every repository.
3. The committed repo file `.kobold/bounds.yaml` at the repository root.
4. The checkout file `.kobold/bounds.local.yaml`, gitignored.

The same keys exist at every layer. A missing key inherits from the
layer behind it. The nearest layer that sets a key wins for that key.
A second run reads the files again, so an edit to a bounds file is what
the next run uses. A checkout file supplies only the keys it names. The
repo file still fills the rest, then the user config file, then the
defaults.

A publishing key stands on its own. `commit: auto` leaves plans and
specs to `commit-plans` and `commit-specs`. `force-push` also requires
`push` to be `ask` or `auto`. `unattended: through-publish` goes only
as far as `commit`, `commit-plans`, `commit-specs`, `push`,
`pull-request`, and `merge` already allow. An `ask` still asks. A
`never` still stops.

Reading the repo, editing files, and running the project's own checks
are ordinary work. The keys cover actions that publish, leave the
checkout, or start other agents.

`commit` stages the work, which is every changed file outside the plan
directory and the spec directory. `commit-plans` stages plan files.
`commit-specs` stages spec files. A plan file sits in the directory the
project uses for plans. When the project has nowhere else, that
directory is `docs/plans/`. A spec file sits in the directory the
project uses for design specs. In this plugin that directory is
`docs/specs/`. Each set that is `auto` is its own commit. Each set that
is `ask` is offered on its own. Each set that is `never` stays
unstaged. An empty set is skipped. A second run leaves a finished
commit as it is and commits only a set that is still uncommitted and
still allowed.

Defaults:

```text
commit: ask
commit-plans: never
commit-specs: ask
push: ask
pull-request: ask
merge: never
force-push: never
shell-network: ask
browser: ask
github-write: ask
subagents: ask
worktrees: ask
unattended: stop-at-plan
```

Values:

- `commit`, `commit-plans`, `commit-specs`, and `push` are `ask`,
  `auto`, or `never`.
- `pull-request` is `never`, `ask`, `open`, or `auto`. `open` and
  `auto` each open one without a fresh ask. `github-write` is the
  other GitHub writes: comments, labels, issues, and review submission.
- `merge` and `force-push` are `never` or `ask`.
- Each tool key is `ask`, `allow`, `auto`, or `deny`. `auto` proceeds,
  the same as `allow`. The tool names in the default set are
  `shell-network`, `browser`, `github-write`, `subagents`, and
  `worktrees`. A file may add a name.
- `unattended` is `stop-at-plan`, `safe-steps`, `through-publish`, or
  `auto`. `auto` follows the publishing keys, the same as
  `through-publish`. Safe steps are read, edit, run the project's
  checks, and write the plan and the trail.
- `model` is optional. Absent means the model already running the
  session.

The file is YAML, one `key: value` line per setting. Re-running setup
overwrites only the layer the user named, and leaves every key they
did not mention as it was. When the user names no keys, the reply is
the table from `set-the-bounds` and the file is left unwritten.

## Skills

### set-the-bounds

Write or revise one bounds layer with the user. Resolve the four layers
before a commit of the work, a commit of plans, a commit of specs, a
push, a pull request, a merge, a force-push, an unattended stretch, or
a named tool. The keys, the files, and the precedence rule are the
Bounds section.

### run-the-play

Match the task to one playbook, copy that playbook's steps into the
working list, and record a skip with a reason when a step is left out.
Stop where the resolved bounds say to stop. The playbooks are files
beside the skill, under `skills/run-the-play/playbooks/`, and each file
is a short procedure rather than its own skill.

### write-the-plan

Write the plan an architectural change already stops for. Say what will
change, which parts it touches, what the checks cover, what stays the
same, and the ordered tasks. Put it where the project keeps plans, and
in `docs/plans/` when the project has nowhere else.

### carry-out-the-plan

Run an approved plan task by task in the current session. Independent
tasks may go to subagents when `subagents` allows them. Each task ends
on the check the plan named.

### isolate-the-work

Put feature work, or the execution of a plan, in a worktree or another
isolated checkout when `worktrees` allows it. Record the path so
`ship-the-branch` can remove it.

### debug-the-failure

Start from a failure that can be reproduced. Hold one hypothesis at a
time, check it against the running system, and put the fix at the
producer of the symptom. Runtime evidence and trace evidence are part
of the same skill.

### how-it-fits

Read a subsystem before changing it. Name the runtime path, which
package owns the behavior, and which layer the change belongs on.

### why-it-is

Recover why a behavior or a threshold exists, from the code, the
history, the issues, and the docs. Return a short read that cites those
sources.

### review-the-diff

Before a merge, review the branch against the request and the checks.
Report findings with file and line. Leave the tree alone unless the
user asks for fixes.

### stress-the-change

Send the same diff to several independent reviewers on different
angles, then merge their findings into one list. When only one model is
available, the passes still run separately, one after another, each
with a fresh context.

### take-the-review

Check each review note against the code before editing. Implement the
notes that hold. For a note that does not hold, say why and leave that
part of the code as it is.

### measure-the-blast

Before a small diff ships, name what else could break outside the diff.
Prove the safety claim by running the code that would show the break.

### fan-out

Split work that does not share state into parallel workers, wait for
them, and return one report. Use it for independent tasks, coverage,
races, and exploration. `subagents` has to allow it.

### try-several-shapes

When the first shape of a change would stick, run several candidates in
parallel, pick a base, and fold the strongest pieces of the others into
it.

### prove-the-product

When a repo has no scripted way to drive the app the way a user does,
write a project-local verification skill and prove it once. A later
pass re-reads the features and re-runs that skill so the map stays
honest.

### ship-the-branch

When the checks pass, integrate the branch. Commit the work, the plans,
and the specs under their own keys, then push, open a pull request, or
merge, and remove the worktree. Each of those actions follows the
resolved bounds.

### leave-a-trail

For a long run or an unattended run, append one row per decision, with
what, why, evidence, and result, to a log a reviewer can read
afterward. Keep the log local unless the reviewer needs it in the
branch. A large migration with no narrower playbook uses `multi-phase`
and this log.

### pick-up-the-work

Rebuild a short brief of where the work stands from the branch, the
transcript, and the trail, so a new session can continue.

### learn-from-the-session

After a session that stumbled, or that found a preference worth
keeping, name the lesson and edit the existing skill, playbook, or
bounds file that should carry it. A new personal skill is created when
no current file is the right home.

### write-a-skill

Author or revise a skill in this plugin's voice: one trigger
description, original wording, and a check that the skill file matches
its spec. The skill ships in the plugin so a Claude Code session has
it.

### cut-the-slop

Take a pass over prose or a diff and remove narration, stock phrasing,
and comments that restate the code. When a comment was carrying a real
constraint, encode that constraint in the structure and drop the
comment.

### write-the-doc

Write or revise a README, a spec, a pull request, or a commit message
in the headings the project already uses, in sentences a new reader can
follow.

## Playbooks

These files live under `skills/run-the-play/playbooks/`. `run-the-play`
is the skill that selects one.

### feature

New behavior. Scope it, shape it, implement it, and prove it.

### bug-fix

Reproduce the failure, find the cause, fix that point, and re-run the
repro.

### refactor

Reshape the code with the same outward behavior, proved before and
after.

### perf

Measure first, change the hot path, and measure again.

### hillclimb

Repeat a measured change until the metric stops moving.

### prototype

A throwaway spike. The spike's code is not the thing that ships.

### investigation

Explain or diagnose. No edit unless the user then asks for one.

### multi-phase

A change large enough to be a sequence of verifiable units.

### visual-parity

Match an existing screen or asset by looking at it.

### eval

Score a behavior against a fixed set of cases.

### unattended

Keep going through the steps `unattended` allows while the user is
away, including overnight.

### pause

Stop at a resumable point: the plan is written, the tree is clean, and
the next step is named.

### pickup

Resume from that point, or from a branch and a transcript.
`pick-up-the-work` is the skill that rebuilds the brief.

## Build order

1. `set-the-bounds`, because shipping, unattended runs, and fan-out all
   read it.
2. `debug-the-failure`, `how-it-fits`, and `why-it-is`.
3. `write-the-plan` and `carry-out-the-plan`.
4. `review-the-diff`, `take-the-review`, and `stress-the-change`.
5. `ship-the-branch`.
6. `run-the-play`, once a few playbooks have real text to route to.
7. `isolate-the-work`, `fan-out`, `try-several-shapes`,
   `measure-the-blast`, `prove-the-product`, `leave-a-trail`,
   `pick-up-the-work`, `learn-from-the-session`, `write-a-skill`,
   `cut-the-slop`, and `write-the-doc`, in any order.

## What this catalog leaves out

The creed and `scope-the-edit` stay the skills they already are. This
file does not restate their paragraphs.

A per-language house style, a bot UI, and issue-bot automations stay
out. A model-per-role table stays out until the single optional `model`
key is not enough.

## How a skill from this list ships

The session that builds a skill writes a spec for that skill, with the
frontmatter description on one physical line and the section bodies
that ship. `tests/check_plugin.py` pins those bodies to that spec the
same way it pins the creed and `scope-the-edit`. The skill names no
Grok tool and no Claude tool. The README links the new skill and its
spec and does not restate a section body. Plugin version and the
manifest description bump in that same change. The playbook files ship
with `run-the-play` and are pinned by name and by section, in that
skill's spec.

## Implementation check

This catalog is recorded when all of these are true:

- This file is `docs/specs/2026-10-02-remaining-skills-design.md` and it
  carries the bounds rule, the skill briefs, the playbook briefs, and
  the build order above.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `docs/specs/2026-10-01-kobold-codex-design.md`,
  `docs/specs/2026-10-01-scope-the-edit-design.md`, the README, and both
  manifests are unchanged.
- `python3 tests/check_plugin.py` still exits 0.
- No tracked file names a hostname or a particular machine's home path.
  The user config path in Bounds is the portable tilde path.
