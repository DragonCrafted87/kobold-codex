# Status block list items

A revision of `write-the-plan`, `leave-a-trail`, `carry-out-the-plan`,
and `review-the-week`. The wording below is the version to ship.

## Why

The Status block and the opening Starting / Expected / Reason lines
were written as plain consecutive lines with a bare label prefix.
A Markdown renderer merges those lines into one paragraph, so the
fields did not stay on their own lines and the labels did not show
as bold. A list item per field, with a bold label, keeps each field
on its own line when the plan is rendered.

## Skill: write-the-plan

In What the reviewer reads, the Status block and the three opening
lines become:

A new plan opens with a Status block, after the title: a `## Status`
heading and three list items, each a bold label and its value on
one line:

```markdown
## Status

- **Current:** not started
- **Blocker:** none
- **Next:** the first task
```

`carry-out-the-plan` keeps it current. A list item per field, not
plain consecutive lines, so a Markdown renderer keeps each field on
its own line.

When no spec records the change, three list items follow the Status
block, one sentence each:

```markdown
- **Starting state:** what is true today
- **Expected state:** what is true when the work is done
- **Reason:** why the change is needed
```

## Skill: leave-a-trail

In The status, the block shape becomes:

The block is a `## Status` heading and three list items, each a
bold label and its value on one line, the same shape
`write-the-plan` uses: `- **Current:**`, `- **Blocker:**`, and
`- **Next:**`. `- **Blocker:** none` when nothing blocks.

## Skill: carry-out-the-plan

In The check, the rewrite sentence becomes:

Rewrite the plan's Status block when the status changes, at the
moment it changes: a task starts or ends, a blocker appears or
clears, or the next step moves. Keep the list-item shape
`write-the-plan` uses. `- **Current:**` names the task and step.
`- **Blocker:**` names what stops the work, or `none`. `- **Next:**`
names the next step. When the block disagrees with the checkboxes,
the checkbox wins. Rewrite the block to match.

## Skill: review-the-week

In The report, "Status lines" becomes "Status fields", twice, so the
wording matches a list item rather than a bare line.

## What this change does not do

It does not edit a past spec or a past plan file. It adds no key
and no bound. It does not change `pick-up-the-work`, which already
reads the Status block without naming the field shape. It names no
project, host, or tool.
