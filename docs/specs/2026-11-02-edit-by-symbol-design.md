# Edit by symbol

A new skill in the build group. The wording below is the version to
ship.

## Why

A code toolkit that answers by symbol (an overview of files and
symbols, a lookup by name path, a context call, references, symbol
edits, an exact-text edit, and content hashes that refuse a stale
edit) saves reading whole files, but only when a session uses it in
the right order. The toolkit's requirements state what each tool
does. They do not say when an agent reaches for which one, when it
falls back to text, or what it does after a stale-hash refusal. This
skill is that habit.

The skill names no tool. It describes the kinds of call, so it fits
any host whose tools look up symbols, and it does nothing when the
workspace has none.

## Skill: edit-by-symbol

```text
description: Use when reading or changing code in a workspace whose tools can look up symbols. Move from an overview of the files to the symbol and its context before reading whole files, fall back to text search or an exact-text edit when no symbol tool covers the file, and read again when a file has changed since it was read.
```

## Overview first

Start from an overview, not from whole files. List the files under
the directory the task touches, then the top-level symbols of the
files that look relevant. Go one level deeper only in the file that
holds the work.

Find the symbol by its name path, such as a type and its method.
Narrow the lookup to a file or a directory when the name is common.
Then ask for the symbol's context: its signature, its doc, its body,
and its callers. Read the whole file only when that context leaves
the question open.

Find the references before changing a symbol's signature or its
behavior. Each reference the change reaches is part of the change.

## Edit by symbol

Replace, or insert before or after, the definition found by its
name path. When the name path matches more than one symbol, the tool
refuses the edit. Pick the one meant with a longer name path, and do
not fall back to a text edit to get around the refusal.

## The fallback

When no symbol tool covers a file, because its language has no
server or the server is not ready, use text search to find the code
and an exact-text edit to change it. Give the exact edit enough of
the old text that it occurs once. When the tool says the old text
occurs zero times or more than once, read the file again and widen
or correct the text. Do not edit by line number from memory.

A result found by text search or by a syntax parser is a likely
match, not a confirmed one. Say so when a claim rests on it, and
check it by reading the lines.

## A stale read

An edit carries what the session last read of each file it changes.
When the tool says a file changed since that read, read the file
again, then make the edit against what is there now. Do not repeat
the old edit unchanged.

## The same edit

A second run reads the symbol again. When it already holds the
change, leave it.

## What this change does not do

It does not edit a past spec. It adds no key and no bound. It names
no project, host, or tool.
