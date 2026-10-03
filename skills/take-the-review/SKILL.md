---
name: take-the-review
description: Use when review notes are in hand. Check each note against the code, implement the notes that hold, and for a note that does not hold say why and leave that code as it is.
---

# Take the review

## The notes

Start from the notes the user handed you. When the user names none,
use the findings the latest review in this session reported. When
there are none, stop and ask which notes to take.

Read the notes before you edit. A note you cannot place on a file
and a line is unclear. Ask about that note before you edit it. When
two notes are about the same lines, ask before you edit either. A
clear note that shares no lines with an unclear one can proceed.

## Against the code

Read the code at the file and line before you edit. The note holds
when that code does the thing the note calls wrong, and that thing
disagrees with the request. The request is what the user asked for,
and the plan when there is one. When the request asked for the code
the note objects to, the note does not hold. When no request is on
record, the note holds when the code does the thing the note calls
wrong.

When you cannot find the line, say so and leave the code.

The change is the diff the notes came from. When a note is about
code outside that change, and the user did not ask to take that
note, say so, leave that code, and go on to the next note. A note
the user asked to take counts as about the change.

## One note at a time

When the note holds, and it is about the change, make the fix the
note describes. `scope-the-edit` decides the plan and the proof for
that edit. Run the check that shows the note no longer holds.
Record the result you observed.

Finish that note before you start the next. Read the next note
against the code after the fix.

When the check fails, stop. Report the note, the change, and the
result. Leave every later note untouched.

## A note that does not hold

When the note does not hold, say why, and cite the file and line
you read. Leave that part of the code as it is.

Then go on to the next note.

## The same notes

On a second run, read the notes again. When the code already has
the fix, say the note is already there, and leave the code. When
you already said a note does not hold, give that same reason, and
leave the code. A note you have not checked yet is checked the way
the first run checks it.

When the files on disk make a note impossible to check, stop and
ask. Leave the code alone.
