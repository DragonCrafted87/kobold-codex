# Loop to the goal

A new skill in the build group, from KCO-2601. The wording below is
the version to ship.

## Why

Some tasks are not a fixed list of steps but a target: make the suite
pass, get a build under a size, clear a scan. `carry-out-the-plan`
runs known tasks once each. Without a loop rule, a session either
stops after one try or keeps going with no limit, and it can reach
"done" by loosening the check. This skill names the goal as a check,
fixes the limits before the first pass, and keeps the check fixed.

The default limit of five passes is a starting point that bounds an
unattended loop; the user's number replaces it. The stop on two
same-shaped failures catches a loop that is not learning.

## Skill: loop-to-the-goal

```text
description: Use when a task is to keep changing and checking until a stated goal holds, such as a passing suite, a metric under a limit, or a clean scan. State the goal as a check that can be run, set the stop conditions and the attempt limit before the first pass, and loop change then check until the goal holds or a stop condition hits.
```

## The goal

Before the first pass, write the goal as a check that can be run and
the result that means done: a command and its exit code, a number
and its limit, or a list that has to be empty. A goal that cannot be
run as a check is not a loop goal. Ask for one, or use
`scope-the-edit` for the task instead.

Run the check once before any change. When it already holds, say so
and stop.

## The limits

Set these before the first pass and say them in the reply:

- The attempt limit: how many change-then-check passes this loop
  runs. The user's number wins. Without one it is five.
- The stop conditions: the check fails the same way twice in a row
  after different changes, a pass makes the result worse, or a
  change would go past the scope or the bounds the task started
  under.

A loop that runs while the user is away follows `unattended`, and
each commit, push, or named tool in it follows `set-the-bounds`.

## A pass

One pass makes one change aimed at the gap the last check showed,
then runs the check. Record the change and the result in the reply,
one line per pass. Keep a change that moved the result toward the
goal. Undo one that moved it away before the next pass.

The check is the goal's check, unchanged. Loosening the check, its
limit, or its inputs to make it pass ends the loop as a failure, not
a success.

## The end

The loop ends when the check holds, the attempt limit is reached, or
a stop condition hits. The reply says which, the last result, and
each pass. When it stopped short, it names the gap left and what the
next pass would try.

## The same loop

A second run reads the recorded passes, runs the check again, and
continues from the next pass with the attempts already used counted.

## What this change does not do

It does not edit a past spec. It adds no key and no bound, and it
names no project, host, or tool.
