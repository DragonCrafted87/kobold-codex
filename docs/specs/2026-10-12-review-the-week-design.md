# Review the week

Design for the weekly review skill. It reads the session transcripts
written since the last review, names the lessons, and sorts each to
its home. This spec also adds the `commit-reviews` bounds key and
moves the `commit-plans` default from `never` to `ask`. The wording
in the skill sections below is the version to ship. Later sessions
tune it by editing the skill files. This spec stays the record of
what we decided and why.

## Purpose

`learn-from-the-session` runs after one session. It sees one stumble
at a time. A week of sessions holds lessons that repeat across days
and across projects.

`review-the-week` reads every Grok and Claude Code transcript since
the last review, names the lessons, sorts each to a home, and writes
a report before any edit. The edits follow the rules
`learn-from-the-session` already has.

The main job is the sort. A lesson either changes this plugin,
belongs to one project, or belongs to the user. The report says
which, for every lesson.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, that never edits before the report, and
that never reads the same part of a transcript twice.

## Decisions

A separate skill, not a mode of `learn-from-the-session`. The two
triggers differ: one runs after a session, one runs once a week over
the transcripts. One description holding both would match worse.
`learn-from-the-session` stays the writer of a lesson edit and gains
no heading. A mode can be revisited later.

Reviews are split by repo. Each repo's report sits in its own review
directory, beside its plan and spec directories, `docs/reviews/` by
default. The newest report is that repo's last-run marker. There is
no separate marker file. The report records the start time, not the
end time, so a session that writes during the review is read next
week. The report file is written last, after the user accepts it.

The report keeps a ledger of host, session id, and byte offset.
Sessions read before may have been resumed and extended. Byte
offsets stay put while a file only grows. Line counts move when a
host rewrites a file. A file shorter than its offset is read again
from the start.

Sessions run in this plugin's repo are skipped, to avoid a loop.
Sessions outside any repo feed the user's global layer or a personal
skill only when the user says yes. A fork or a repo the user does
not own gets `adopt-the-repo` first, when the user says yes.

Subagent sessions are read for trigger misses only. Other stumbles
show up in the parent session.

There is no cap on sessions or lessons. Near the user's usage limit,
the review warns and offers a narrower window.

A lesson seen in two or more repos is a judgment call left to the
user. The plugin may get more users, so a shared lesson may belong
here. It may be personal. The report flags it and waits.

A committed report holds session ids, dates, offsets, and the
lessons in the skill's own words. No quoted transcript text is
written to a file. The reply may quote one line per sighting.

The reply opens with a status summary across repos, built from each
plan's or trail's Status lines. The Status lines ship in a later
version. Until then the summary is empty.

The skill names no host tool and no transcript path. On the hosts
this was written against, Grok keeps sessions under
`$GROK_HOME/sessions/<encoded-cwd>/<session-id>/`, with the
conversation in `updates.jsonl`. Claude Code keeps one JSONL file
per session under its config directory, in
`projects/<encoded-cwd>/`, and deletes old ones after a retention
period. These are recorded here, not in the skill.

`commit-reviews` joins `commit-plans` and `commit-specs`. Its values
are `ask`, `auto`, or `never`. It defaults to `ask`. `commit` leaves
review files to their own key.

`commit-plans` moves from `never` to `ask`. A plan that never leaves
the checkout is lost with it, and reviews and status point at plans.
`adopt-the-repo` suggested local plans because of the old default.
It now suggests tracked plans, and the paragraph changes in the
skill and in its spec together. The table pinned in
`2026-10-11-model-tier-routing-design.md` is a dated record and
stays. This spec now holds the Defaults rows for these two keys.

`ship-the-branch` commits review files under `commit-reviews`,
between the plans and the work.

The plugin version becomes `1.4.0`. The manifest description stays
the stable sentence. `docs/skills.md` links the skill and this spec.
The README stays.

## Where the words live

```text
skills/review-the-week/SKILL.md
skills/set-the-bounds/SKILL.md
skills/adopt-the-repo/SKILL.md
skills/ship-the-branch/SKILL.md
docs/specs/2026-10-12-review-the-week-design.md
docs/specs/2026-10-04-adopt-the-repo-design.md
docs/plans/2026-10-12-review-the-week.md
docs/skills.md
```

## Skill

Frontmatter `name` is `review-the-week`. Frontmatter `description`
is one physical line:

```text
Use once a week, or when asked, to review the session transcripts since the last review. Sort each lesson to this plugin, a project, or the user, and report before any edit.
```

The body is the seven sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Review the
week.

### The window

Reviews are split by repo. A session belongs to the repo that holds
its working directory. A worktree belongs to the repo it was made
from. Each repo has its own report, in its review directory. The
review directory sits beside the plan and spec directories. When the
project names none, it is `docs/reviews/`. Name the file with the
date and `weekly-review`.

The newest report in a repo is that repo's last run. It records the
time that review started, in UTC, on one line near the top. This
run reads sessions written after that time. A repo with no report
reads the last seven days.

Sessions run in this plugin's own repo are skipped and counted. A
review of them would feed its lessons back into the skill that
found them.

A session outside any repo has no report. Ask once whether its
lessons should feed the user's global bounds layer or a personal
skill. When the user says no, count those sessions and do not read
them.

A repo the user does not own, or a fork, may have no plan, spec, or
review directory. Ask whether to run `adopt-the-repo` on it first.
After that it is a normal repo. When the user says no, list its
lessons in the reply and write no file there.

### The transcripts

Read the transcripts the host already keeps. The user's setup, or
the project's instructions, name where they are. Do not ask the
host to export.

The newest report keeps a ledger: one line per session read, with
the host, the session id, and the byte offset where reading
stopped. A session in the ledger is read from that offset, so only
the part added since is reviewed. When the file is now shorter than
its offset, the host rewrote it. Read the whole file, and say so.

A subagent session is read for the trigger only. A skill that
should have loaded and did not is a lesson. So is a skill that
loaded when another one fit.

There is no cap on sessions or lessons. When the reading looks
likely to run into the user's usage limit, stop and say so. Offer
a narrower window: fewer repos, fewer days, or parent sessions
only. The report lists what was left out, and the next run reads
it.

### The lessons

Look for a correction from the user, a reverted edit, a failed
check run again, a rule repeated by hand, and a skill that should
have loaded. Each lesson says what happened and what the next
session should do.

Merge the same lesson across sessions. Keep each sighting: the
session id and the date. A lesson seen once is still listed.

Check each lesson against its home. When the home already says it,
point at the paragraph and mark the lesson held. A held lesson that
keeps coming back means the paragraph does not reach the session,
so say that. Check the past reports too. A lesson the user declined
before is listed as declined.

### The sort

Each lesson gets one home. Ask in this order.

When it would change how any project uses a skill in this plugin,
the home is in this plugin. A wrong or thin paragraph goes to
`learn-from-the-session`. A new skill, heading, or check goes to
`write-a-skill`. The creed and `scope-the-edit` are named and stay.

When it is a bounds value, name the key and the value.
`set-the-bounds` writes the layer.

When it depends on one repo, the home is in that repo: a project
skill, its instructions, or a new project skill.

When it is about the user across projects, the home is a personal
skill. Ask where it lives, as `learn-from-the-session` does.

When two homes fit, the narrower one wins, and the report names the
other. A lesson seen in two or more repos is flagged. The user
decides whether it belongs in this plugin or with them.

### The report

Write the report in the reply before any edit. Open with the status
of each piece of work across the repos read, taken from the Status
lines each plan or trail keeps. A blocked row goes first. When a
Status line disagrees with the plan's checkboxes, the checkbox wins,
and say so.

Then one section per repo: the window, the ledger, the counts of
sessions read, lost to the host's cleanup, skipped, and left out,
the lessons for that repo and its bounds keys, and the lessons for
this plugin, the user, and more than one repo seen there. Gather
those last three into one list at the top as well, so the user
places each once. Held lessons go last, short.

The reply may quote one line per sighting. Replace a token or a key
in a quote with its kind. The report file holds session ids, dates,
offsets, and the lessons in your own words. It holds no quoted
transcript text.

The user picks which lessons land. Silence is not a yes. Write each
repo's report file after the user accepts it. A review that stops
early writes no file, so the next run reads the same sessions.

### The edits

One lesson is one edit, and one commit in the repo that owns the
home. A lesson for this plugin and a lesson for a project never
share a commit. Hand each lesson to `learn-from-the-session`,
`write-a-skill`, or `set-the-bounds`. The report file commits under
`commit-reviews`. Pushing follows `set-the-bounds`.

### The same week

A second run in the same week reads from the newest report and its
ledger. A session already read to its end is skipped. A lesson the
report already lists is not raised again.

## Revision: set-the-bounds

In Defaults, the `commit-plans` row and a new `commit-reviews` row
after `commit-specs` read:

```text
| `commit-plans` | `ask` | Commit of plan files, in the directory `write-the-plan` uses. |
| `commit-reviews` | `ask` | Commit of review files, in the review directory `review-the-week` uses. |
```

In Values, the first sentence reads:

```text
`commit`, `commit-plans`, `commit-specs`, `commit-reviews`, and
`push` are `ask`, `auto`, or `never`.
```

In Publishing sets, the first paragraph reads:

```text
`commit` stages the work, which is every changed or untracked file
outside the plan, spec, and review directories. `commit-plans`
stages plan files. `commit-specs` stages spec files.
`commit-reviews` stages review files. A plan file sits in the
directory the `commit-plans` row names. A spec file sits in the
directory the `commit-specs` row names. A review file sits in the
directory the `commit-reviews` row names. When a path matches both
the plan and the spec directories, it is a spec.
```

The second paragraph begins "`commit: auto` leaves plans, specs, and
reviews to their own keys."

## Revision: adopt-the-repo

In The paths, the last two sentences read:

```text
Suggest tracked for plans, because `commit-plans` defaults to
`ask` and a plan is how the next session finds the work. Suggest
tracked for specs, because `commit-specs` defaults to `ask` and a
spec is the record of a decision.
```

## Revision: ship-the-branch

In Three commits, the first sentence reads "Commit the specs under
`commit-specs`, then the plans under `commit-plans`, then the
reviews under `commit-reviews`, then the work under `commit`." The
heading stays.

## What this skill does not do

It does not edit before the report.

It does not edit a home itself. It hands each lesson on.

It does not guess where a personal skill lives.

It does not read sessions run in this plugin's repo.

It does not decide the home of a lesson seen in several repos.

It does not write quoted transcript text into a file.

It does not push or open a pull request.

## Tuning

Edit `skills/review-the-week/SKILL.md` when a review shows a
paragraph is wrong, too thin, or too long. This document keeps the
2026-10-12 wording.

## Implementation check

The build is done when all of these are true:

- `skills/review-the-week/SKILL.md` carries the frontmatter and the
  seven sections above.
- `set-the-bounds`, `adopt-the-repo`, its spec, and `ship-the-branch`
  carry the revisions above.
- `docs/skills.md` links the skill and this spec.
- Plugin version is `1.4.0` in both manifests, with the stable
  description.
- `python3 tests/check_plugin.py` passes.
- No tracked file names a hostname, a user's home directory, or a
  machine.
