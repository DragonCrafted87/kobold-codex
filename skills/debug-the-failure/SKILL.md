---
name: debug-the-failure
description: Use when a failure can be reproduced. Hold one hypothesis at a time, check it on the running system, and put the fix at the producer of the symptom.
---

# Debug the failure

## Reproduce

Name the failure before changing code. Record the command or the
action, the input, and the result you observed. Run that failure
again. When the second run produces a different result, the failure
is not stable yet. Narrow the input or the environment until a run
repeats the same result. When it still does not repeat, say so and
stop.

When you cannot run the failure, ask for the input, the environment,
or the steps that are missing, and stop.

## One hypothesis

State one hypothesis. It names a place in the code and a reason that
place would produce this result. Check that hypothesis before you
write another. A check that disagrees retires it. The next hypothesis
starts from what the check showed.

After three checks that disagree, or three edits that leave this
failure in place, stop editing. Report what those three showed. The
design is now the question, and that question is an architectural
edit.

## Evidence

Read the trace for this failure. That means the stack, the log line,
the test name, and the exit status. Then observe the running system
at the place the hypothesis named. A frame in the trace is a place to
look. The value at that frame, on this input, is the evidence.

When the trace does not show the value, add a temporary observation.
A log line, a print, or a breakpoint counts. Remove that observation
before calling the work done, unless the project already keeps that
kind of trace.

Report the value you observed. Leave out a value the run did not show.

## The producer

Change the code that produces the bad result. Leave out a change that
hides the result, swallows the error, or special-cases the one input
that failed.

The plan and the proof for that change follow the scope of the edit.

## The same failure

Run the original failure again. The result that failed is the result
that has to succeed. Another check may run beside it. The original
failure still has to be one of the runs.

When you cannot run the original failure again, say so, and name the
run you did execute.
