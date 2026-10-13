---
name: cut-the-slop
description: Use when prose or a diff needs a pass for narration, stock phrasing, and comments that restate the code. Encode a real constraint in the structure, then drop the comment.
---

# Cut the slop

## The pass

Take one pass over the prose or the diff the user named. When
they name none, the pass is the uncommitted diff. When there is
no uncommitted diff, stop and ask which prose or which diff.

The pass covers that text and nothing past it. `kobold-codex` is
the voice for the prose that remains.

## What comes out

Narration comes out. Narration is a sentence that retells the
next line or the next step. Stock phrasing comes out. Stock
phrasing is a sentence that could sit on any other change and
names nothing in this one. A comment that restates the code comes
out.

A comment that names a constraint stays for the next section.

## A constraint

When a comment carries a constraint the code does not enforce,
put that constraint in the structure, then drop the comment. The
structure is a name, a type, a check, or the shape of the data.

When the constraint cannot move into the structure without
changing outward behavior, leave the comment and say why.

The pass does not change outward behavior. A spot that would
change it stays, and the reply names the spot.

The edit follows `scope-the-edit`. When the edit changes a
function, the check is the one that skill names.

## The same pass

A second run reads the same prose or the same diff. A sentence
that is already gone stays gone. A constraint that already lives
in the structure stays there. The reply points at the file.
