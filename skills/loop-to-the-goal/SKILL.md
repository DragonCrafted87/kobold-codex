---
name: loop-to-the-goal
description: Use when a task is to keep changing and checking until a stated goal holds, such as a passing suite, a metric under a limit, or a clean scan. State the goal as a check that can be run, set the stop conditions and the attempt limit before the first pass, and loop change then check until the goal holds or a stop condition hits.
metadata:
  group: build
---

# Loop to the goal

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
