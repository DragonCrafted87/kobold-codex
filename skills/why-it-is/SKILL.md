---
name: why-it-is
description: Use when you need the reason for a behavior or a threshold. Recover it from the code, the history, the issues, and the docs, and cite each source.
---

# Why it is

## The question

Name the behavior or the threshold you were asked about. A threshold
is a number, a limit, a timeout, a flag, or a special case. Quote the
line that sets it, and name the file. The question is why that line
exists.

## Sources

Read the code that sets the behavior and the code that reads it, the
history of that line, the issues and review notes that mention it, and
the docs the repository keeps. Record a source you could not open as
unopened, with the reason.

History means the commits that introduced or changed the line. An
issue means a tracked report in the project. Docs mean the documents
the repository already has.

## The read

Answer with a short read. State the reason, then cite each source you
used. A citation is the file and the line, the commit, the issue, or
the document. A statement with no citation is a guess. Keep a guess
out of the reason. If you mention a guess, label it as a guess.

When the sources disagree, report each side with its citations. Leave
the disagreement in the read.

## No reason on record

When the code, the history, the issues, and the docs do not state a
reason, say that. Name what you opened. A story that would make the
line sensible stays out of the read.

The read is the work of this skill. An edit waits until the user asks
for one.
