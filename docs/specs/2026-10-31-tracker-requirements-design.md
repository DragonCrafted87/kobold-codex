# Requirements in a tracker, and one source of truth

A revision of `kobold-codex`, `adopt-the-repo`, `set-the-bounds`,
`spec-the-source`, `ship-the-branch`, `write-the-plan`,
`review-the-diff`, and `write-a-skill`. The wording below is the
version to ship.

## Purpose

A project can move its requirements out of repository Markdown and
into a requirements tracker that has an MCP server and a REST API
with an OpenAPI document. The plugin had no way to say so. Its
`specs` key means the design-spec directory, the records of
decisions, but a project had pointed it at a requirements tree, so
one word carried two meanings.

The same release cuts duplication between specs, plans, and skills:
a fact lives in one place, and the rest link to it. Git history
keeps older wording.

## Decisions

- Requirements get their own `requirements` key in
  `.kobold/adopt.yaml`. `specs` keeps its meaning. A record with no
  `requirements` key behaves as before, so repositories that keep
  requirements in Markdown need no change.
- The lookup order, the token rule, and the unreachable rule live
  once, in `kobold-codex`. The other skills point at it.
- MCP first, then REST through the OpenAPI document by
  `operationId`.
- The token is read from an environment variable named after the
  token's item in the user's vault. Each agent has its own token. It
  is never printed.
- No offline export. A read that fails after one retry marks the
  claims that depend on it UNKNOWN. A write that fails is queued
  outside the repository, and the user is told.
- In tracker mode `spec-the-source` writes Draft items straight to
  the tracker, under a new `write-requirements` bound. The progress
  file is unchanged.
- `ship-the-branch` adds Implements links on its own, under the same
  bound.
- No skill names a project, a host, or a tracker product. The check
  enforces it.
- Version `2.3.0`: a new optional key, a new bound, and new
  headings, all backward compatible.

## Skill: kobold-codex

Two new headings at the end.

## Requirements

Requirements are the rules a project's behavior is held to.
`.kobold/adopt.yaml` names where they live under `requirements`.
When the record has no `requirements` key, look for the project's
own convention: a `specs/` or `docs/specs/` directory, a
requirements file, or an instruction that names one.

`source: markdown` means the files under `path`. `source: tracker`
means items in a requirements tracker at `url`, in the project
`project`. Reach the tracker through its MCP server first, at
`mcp-url`, when the host has that server connected. Otherwise use
its REST API: read the OpenAPI document at `openapi` and call each
operation by its `operationId`, not by a path written from memory.
`transport` can change that order.

The tracker token is read from the environment variable that
`token-env` names. That name is the name of the token's item in
the user's vault, so one name finds the secret in both places.
Each agent has its own token. The token goes only into the
request's authorization header. It is not printed, logged,
committed, written into a tracked file, or asked for in chat. When
the variable is unset, stop and ask the user to set it. A 401 or a
403 stops the work; say which one, and do not try another
credential.

When the tracker does not answer, retry once. Then go on without
it, and mark every claim that depended on a requirement UNKNOWN. A
write that could not reach the tracker is queued in a file outside
the repository, and the reply names that file and what it holds.
Requirements are never written into repository Markdown as a
fallback. No session deletes or archives a tracker item or board.

## One source of truth

A fact lives in one place, and everything else links to it. A plan
links the spec and the requirement IDs it serves and does not copy
their text. An index links the skill and its spec and does not
restate a section. A dated spec is the record of a decision, not a
second copy of the skill. Git history keeps older wording, so a
superseded file is not kept beside the current one.

## Skill: adopt-the-repo

The record's key list gains `requirements`. A new heading before
The bounds.

## The requirements

Ask where the project's requirements live: nowhere yet, in Markdown
files, or in a requirements tracker. When a tracked directory of
requirement files already exists, record it and do not ask. The
`specs` key is the directory for design specs, the records of
decisions. It never names requirements. When the repository's
`specs` path holds requirements, say so and suggest moving that
path to `requirements`.

The `requirements` key is a mapping. `source` is `markdown` or
`tracker`. For `markdown`, `path` is the directory, `specs` when
the user names none, and `tracked` is `true` or `false`. For
`tracker`, `url` is the tracker's base address, `project` is the
project key, and `token-env` is the environment variable that holds
the token, named after the token's item in the vault. `transport`
is optional and defaults to `[mcp, rest]`. `mcp-url` defaults to
`<url>/mcp`, and `openapi` defaults to `/api/openapi.json`. The
record holds the variable's name and never the token. A tracker
source creates no directory. The key is omitted when the project
has no requirements. `kobold-codex` says how a session reads them.

## Skill: set-the-bounds

A new row before `push`:

| `write-requirements` | `ask` | Create or update a requirement in a tracker, or add or delete a tracker link. |

Values gains: `write-requirements` is `ask`, `auto`, or `never`. A
tracker holds no files, so no commit stages requirements kept there.

## Skill: spec-the-source

A new opening paragraph in Where the specs go:

When the target repo's `.kobold/adopt.yaml` names `requirements`,
follow it. With `source: tracker`, each requirement is written
straight to the tracker as an item with status Draft, as
`write-requirements` allows. Its ID is the tracker's next free ID
for its module and kind, and the provenance header goes in the
item's body. The progress file stays where this section puts it.
With `source: markdown`, the specs go under `path`.

## Skill: ship-the-branch

A new heading before The worktree.

## Implements links

When the project's requirements live in a tracker, add an
Implements link on each tracker item the branch carries out, as
`write-requirements` allows. The items are the ones the plan or the
commits cite. A link already there is left as it is. A tracker that
does not answer follows `kobold-codex`, and the reply names each
link still to add.

## Skill: write-the-plan

After the sentence that links the spec:

When the change carries out requirements, list their IDs as links
to where they live. The plan does not copy a spec's or a
requirement's text.

## Skill: review-the-diff

A new paragraph at the end of The request and the checks:

When the plan or the commits cite requirement IDs, read each one
from where `kobold-codex` says requirements live, and check the
diff against it. A cited requirement the diff does not meet is a
finding.

## Skill: write-a-skill

A new paragraph at the end of The spec:

The plan for a skill change links the spec for the wording and
does not copy a section body.

## What this change does not do

It does not edit a past spec. It does not delete or archive a
tracker item. It does not store a token. It does not change the
progress file of `spec-the-source`. It does not edit any project
that uses the plugin.

## Implementation check

- Each skill above carries the wording above.
- Plugin version is `2.3.0` in both manifests.
- `python3 tests/check_plugin.py` passes, including the new checks:
  no project or host names in a skill, the `requirements` keys in
  `adopt-the-repo`, no command that prints a token, `operationId`
  only in `kobold-codex`, and the RFC 2119 subset in the new
  Requirements heading.
