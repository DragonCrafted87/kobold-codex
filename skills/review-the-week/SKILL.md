---
name: review-the-week
description: Use once a week, or when asked, to review the session transcripts since the last review. Sort each lesson to this plugin, a project, or the user, and report before any edit.
---

# Review the week

## The window

Reviews are split by repo. A session belongs to the repo that holds
its working directory. A worktree belongs to the repo it was made
from. Each repo has its own report, in its review directory. The
review directory sits beside the plan and spec directories. When the
project names none, it is `docs/reviews/`. Name the file with the
date and `weekly-review`.

The newest report in a repo is that repo's last run. It records the
time that review started, in UTC, on one line near the top. This
run reads sessions written after that time. A repo with no report
reads the last seven days. Seven days is the guide. When the user
names a longer window, read that window instead.

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

## The transcripts

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

## The lessons

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

## The sort

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

## The report

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

## The edits

One lesson is one edit, and one commit in the repo that owns the
home. A lesson for this plugin and a lesson for a project never
share a commit. Hand each lesson to `learn-from-the-session`,
`write-a-skill`, or `set-the-bounds`. The report file commits under
`commit-reviews`. Pushing follows `set-the-bounds`.

## The same week

A second run in the same week reads from the newest report and its
ledger. A session already read to its end is skipped. A lesson the
report already lists is not raised again.
