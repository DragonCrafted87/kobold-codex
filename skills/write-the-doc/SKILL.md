---
name: write-the-doc
description: Use when writing or revising a README, a spec, a pull request, or a commit message. Use the headings the project already uses, in sentences a new reader can follow.
---

# Write the doc

## The document

Write or revise the document the user named. A README, a spec, a
pull request, and a commit message are the documents this skill
writes. When the user names another kind of document the project
already has, write that kind too.

When the user names none, stop and ask which document.

## The headings

Use the headings the project already uses for that kind of
document. Read an existing file of that kind before writing.

When the project has no file of that kind, a spec uses the
headings of the specs in the spec directory. A commit message
uses the subject shape of the repository's recent commits. A pull
request uses the sections of the repository's recent pull
requests. When no example exists, ask which headings to use, and
stop before writing.

A rule the project already records for that file still holds.
This skill does not move a section body into a file whose rule
keeps section bodies out.

## The sentences

Write sentences a new reader can follow without the session
transcript. Name the path, the command, or the result the reader
needs. `kobold-codex` is the voice. This skill does not restate
it.

The edit follows `scope-the-edit`.

## Where it stops

This skill writes the words. Committing them follows `commit`,
`commit-plans`, or `commit-specs`, whichever set the file belongs
to. Opening a pull request follows `pull-request`. For a pull
request that is already open, this skill drafts the words in the
reply and does not change the title or the body. A comment on that
pull request follows `github-write`. `set-the-bounds` resolves the
key. `ship-the-branch` is the skill that integrates the branch, and
it keeps an open pull request's title and body.

## The same document

A second run reads the document again. When it already uses the
project's headings and the sentences still match the work, leave
it. When the work has moved and the document has not, revise the
document.
