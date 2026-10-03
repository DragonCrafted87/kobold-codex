# Ship the branch

Design for the shipping skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as build-order step 5. The wording in the skill sections
below is the version to ship. Later sessions tune it by editing the
skill file. This spec stays the record of what we decided and why.

## Purpose

`ship-the-branch` integrates a branch once its checks have passed.
It commits the specs, the plans, and the work under their own keys,
then pushes, opens one pull request, or merges, and removes an
isolated checkout. Each of those actions follows the resolved
bounds.

`set-the-bounds` is the skill that resolves a key and the skill
that revises a layer. This skill reads the resolved values and
walks the sequence. `review-the-diff` is the review a session runs
when the user asks for one. This skill does not start that review.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. One branch, integrated in this
session, with each publishing action on its own key. The plugin
version becomes `0.7.0` in the change that ships the skill. The
manifest description stays the stable sentence in the catalog's
ship rule.

The checks are the gate. They are the checks the plan or the change
named, and a check the user names for this ship. They run before
any commit, push, pull request, merge, or checkout removal. A
failed check stops the ship. A check that cannot be run stops the
ship. When none is named, the session asks which check to run and
does not supply one. That matches `carry-out-the-plan`, which
refuses to invent a check the plan left out. A passing check is a
pass here. Whether the check reached the behavior it claims is a
question for `review-the-diff`. This skill does not reopen it, and
it does not refuse to ship because no review was run. The build
order put review before this skill because the review had to exist.
It is not a gate inside this sequence.

The branch is the one the user named. When they name none, it is
the current branch. A checkout with no branch is not a ship. The
branch a pull request would merge into is not a ship either.
Integrating that branch onto itself is a different request.

The three sets are the ones `set-the-bounds` already defined. This
skill does not restate which directory is which. The order is
specs, then plans, then the work. The catalog names the three sets
without an order. The order here matches the commits this plugin
already makes, so a spec commit does not contain the skill and a
plan commit does not contain the work. Each set is its own commit
under `commit-specs`, `commit-plans`, or `commit`. An empty set is
skipped. A second run leaves a finished commit as it is.

`ask` stops for a yes that names that action. A yes does the action
and the ship continues. A no leaves the action undone and stops the
ship. A later `auto` must not run on the strength of a refusal. The
user can ask to continue, and the second run starts at the first
action that is still undone. `never` skips only that action. `merge`
defaults to `never`, and the checkout removal still has a job after
that skip, so a skipped action is not the end of the ship. `auto`
and `open` proceed. `deny` on `worktrees` leaves the checkout.

A push the remote rejects stops the ship. This skill does not
force-push. `force-push` stays on its own key, in `set-the-bounds`,
for a request that names a rewrite. A pull request opens against
the base the user named, or against the branch this one would merge
into. One pull request for the branch is enough. An existing one
keeps its title and its body. Changing them is a different write,
and `github-write` stays the key for comments, labels, issues, and
review submission. This skill does not take that key. It also does
not stack `shell-network` on a push or a pull request. Those
actions already have their own keys.

`merge` merges the pull request. It does not merge locally. When
no pull request is open, the merge is skipped. Deleting the local
branch or the remote branch was set aside. The catalog names the
checkout, not the branch.

The checkout removal uses `worktrees`. `isolate-the-work` is the
later skill that records a path, and this skill does not invent
that record. The user names the checkout, or the ship removes the
isolated checkout this branch is already in. The primary checkout
stays. A checkout with uncommitted files stays. When no separate
checkout exists, the reply says so. That is the usual case for a
branch that was cut in the primary checkout. The session returns
to the primary checkout before removing the one it is standing in.
A removal that cannot be done leaves the checkout and says why.

While the user is away, `unattended` still limits the ship.
`set-the-bounds` is that rule. This skill does not loosen it.
While the user is directing the next step, the publishing keys and
`worktrees` decide.

Commit subjects and the pull request follow the creed and the
records this repository already has. `write-the-doc` is the later
skill for that prose. This skill does not add a second template.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

This skill ships alone. The root README stays the introduction and
the install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, and the review skills,
and it requires version `0.7.0` and the stable description.

## Where the words live

```text
skills/ship-the-branch/SKILL.md
docs/specs/2026-10-03-ship-the-branch-design.md
docs/plans/2026-10-03-ship-the-branch.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the three
investigation skills, the two plan skills, and the three review
skills stay. The catalog keeps the skillset list and the build
order. Its text for this skill stays the brief. The
`review-the-diff` spec keeps the sentence that names this skill as
the later skill that integrates the branch.

## Skill

Frontmatter `name` is `ship-the-branch`. Frontmatter `description`
is one physical line:

```text
Use when the checks pass and the branch should be integrated. Commit the specs, the plans, and the work under their own keys, then push, open a pull request, or merge, and remove the worktree, each as the resolved bounds allow.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### The branch

Ship the branch the user named. When the user names none, ship the
current branch. When the checkout has no branch, stop, and say so.

When that branch is the branch a pull request would merge into,
stop, and name it.

Run every check the plan or the change named. A check the user
names for this ship is one of those checks. Run them before any
later action in this skill. A failed check stops the ship. A check
that cannot be run stops the ship, and the reply names the reason.
When no check is named, stop and ask which check to run.

When the user is away, `unattended` still decides how far the ship
goes. `set-the-bounds` is that rule. This skill does not loosen it.

The reply names each action this run took and each one it skipped.
Name the key that governed it. A ship that stops on the checks does
not commit, push, open a pull request, merge, or remove a checkout.

### Three commits

Commit the specs under `commit-specs`, then the plans under
`commit-plans`, then the work under `commit`. Each set is its own
commit. `set-the-bounds` says which files belong in each set and
which value applies. Say the key, the value, and the layer that
set it before the commit.

`ask` stops for a yes that names this commit. A yes makes the
commit, and the ship continues. A no leaves the set unstaged and
stops the ship. `never` leaves the set unstaged, and the ship
continues. `auto` makes the commit. An empty set is skipped.

A second run leaves a finished commit as it is. It commits a set
only when that set is still uncommitted and still allowed. When a
commit fails, stop the ship, and say what failed.

### The remote

Push the branch under `push`, then open one pull request under
`pull-request`, then merge that pull request under `merge`. Say the
key, the value, and the layer that set it before the action.

`ask` stops for a yes that names this action. A yes does it, and
the ship continues. A no skips it and stops the ship. `never`
skips that action, and the ship continues. `auto` and `open`
proceed.

This skill does not force-push. A push the remote rejects stops
the ship. Say what was rejected, and leave the remote as it is.

When `push` did not update the remote, and the remote does not
have the commits this ship would push, stop before the pull
request. Say that the remote does not have them.

The pull request targets the base the user named. When the user
names none, it targets the branch this one would merge into. When
a pull request for this branch is already open, leave that pull
request as it is, including its title and its body.

Merge the pull request. When none is open, skip the merge and say
so.

When an action fails, stop the ship, and say what failed.

### The worktree

Remove the isolated checkout for this branch when that checkout is
not the primary one. When the user names a checkout, that is the
one. When no separate checkout exists, say so.

Leave the checkout in place when it is the primary one, or when it
still has uncommitted files. Say which of those is true.

When a clean isolated checkout is the one to remove, `worktrees`
is the key. Say the value and the layer that set it. `ask` stops
for a yes that names this removal. A yes removes the checkout. A
no leaves it. `deny` leaves it. `allow` and `auto` remove it.

When the removal goes ahead and the session is standing in that
checkout, return to the primary checkout first. When that return
cannot be done, say so and leave the checkout. When the removal
fails, say what failed, and leave the checkout in place.

### The same branch

A second run reads the bounds again and starts at the first action
in this skill that is not done and that the bounds still allow.
The checks run again. The earlier sections say what a finished
commit, an open pull request, a merged pull request, and a removed
checkout look like on that run.

## What this skill does not do

It does not review the diff and it does not apply review notes.
`review-the-diff`, `take-the-review`, and `stress-the-change` are
those skills.

It does not resolve a bounds file and it does not revise one.
`set-the-bounds` does that. This skill reads the resolved value
before each action.

It does not invent a check, and it does not treat a missing review
as a failed check.

It does not force-push, and it does not delete the local branch or
the remote branch.

It does not create an isolated checkout. `isolate-the-work` is the
later skill for that. It does not invent the record that skill will
use for the checkout path.

It does not edit an existing pull request's title or body.
`github-write` stays the key for the other GitHub writes.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills, or
the catalog.

## Tuning

Edit `skills/ship-the-branch/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/ship-the-branch/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs
  match this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  the two plan skills, the three review skills, and the specs those
  skills pin are unchanged. The catalog's skill briefs stay. Its
  ship rule records the stable manifest description and points the
  skill map at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a
  restatement of a skill paragraph in the README drifts.
- Plugin version is `0.7.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.7.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
