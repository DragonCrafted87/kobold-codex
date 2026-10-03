---
name: run-the-play
description: Use when a task should follow a playbook. Match it to one playbook, copy that playbook's steps into the working list, record a skip with a reason, and stop where the resolved bounds say to stop.
---

# Run the play

## The match

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

## The list

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

## A step left out

Leave a step out when the playbook says it does not apply, or when
the user says to leave it out. Record the step and the reason on
that list entry, then continue with the later steps.

The reason names the scope, or it names what the user said. An
entry with no reason stays waiting.

## Where it stops

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

## The same task

Read the playbook again and rebuild the list. A step is done when
its result is already true and you can point at the evidence in
the tree or in the earlier record. Name that evidence. A skip
whose reason still holds stays skipped. A step that stopped on the
bounds is waiting.

Begin at the first step that is waiting. When the evidence for a
finished step is gone, that step is waiting.
