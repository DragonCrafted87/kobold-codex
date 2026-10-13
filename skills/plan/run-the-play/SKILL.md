---
name: run-the-play
description: Use when a task should follow a playbook. Match it to one playbook, copy that playbook's steps into the working list, record a skip with a reason, and stop where the resolved bounds say to stop.
---

# Run the play

## The match

Match the task to one file in the `playbooks` directory beside
this skill.

The match also includes the project playbook directory recorded
under `playbooks` in `.kobold/adopt.yaml`, when that file records
one. Those files are the files in the plugin directory and the
files in that project directory. There means both directories.

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

The four plugin playbooks stay the files for the task kinds they
already name.

A file that no rule above names stays unused until the user names
it.

## The shared steps

`feature` and `refactor` share the scope step, the shape step, and
the build step. `refactor` calls the build step Reshape.

In the scope step, `scope-the-edit` names the scope before the
first edit. For a small or intermediate scope, follow that skill,
including the edit it requires. An architectural scope only names
the scope in this step. Writing the plan is the shape step.

The shape step writes the plan when the scope is architectural.
`write-the-plan` writes it. That step is done when the plan file
is written. The later steps stay waiting until the user approves
that plan. When the scope is small or intermediate, leave this
step out. The reason is that scope.

The build step stays out when the scope step already made the
edit. The reason is that scope. When a plan is required and it is
not approved yet, stop and leave this step waiting. When the user
has approved the plan, `carry-out-the-plan` runs it.

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
picks up where that part stopped. When the playbook says the step
is done, mark it done. The later steps stay waiting. When the
named skill stops because it cannot continue, this playbook stops
with it, and the later steps stay waiting.

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
`set-the-bounds` is that rule.

Do not start a step the resolved value does not allow. Leave that
step and the later steps waiting, and stop. Name the key, the
value, and the layer that set it.

`stop-at-plan` may start a step that names a scope or writes a
plan.

A step that commits, pushes, opens a pull request, merges,
force-pushes, or uses a named tool follows `set-the-bounds`.

## The same task

Read the playbook again and rebuild the list. A step is done when
its result is already true and you can point at the evidence in
the tree or in the earlier record. Name that evidence. A skip
whose reason still holds stays skipped. A step that stopped on the
bounds is waiting.

Begin at the first step that is waiting. When the evidence for a
finished step is gone, that step is waiting.
