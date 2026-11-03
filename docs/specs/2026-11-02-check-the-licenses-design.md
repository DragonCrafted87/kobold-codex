# Check the licenses

A new skill in the ship group. The wording below is the version to
ship.

## Why

A code toolkit's requirements had every dependency's license checked
in CI before a release, each bundled grammar checked and listed in
the deployment docs, and nothing GPL-licensed bundled. Those are
habits a session needs on any project that ships what it depends
on, not features of one tool. The skill holds them once.

The no-GPL rule is a default, not a fixed rule: a project's own
policy wins, so the skill carries no per-project case. A tool that
runs beside the project but is not bundled is reported, not
stopped, because bundling is where the license terms bite.

## Skill: check-the-licenses

```text
description: Use before adding a dependency, a bundled grammar or data file, or a language server or other tool to a project, and before a release. Check each license against the project policy, bundle nothing under the GPL unless the policy allows it, and record the result where the project keeps its deployment docs.
```

## What gets checked

Check the license of each thing the change adds to what the project
ships or installs: a library, a bundled grammar or data file, a
language server, and any other tool the project runs or packages.
A dependency pulled in by one of those counts too. Check again
before a release, over everything the release ships.

Read the license from the package's own metadata and its license
file. When the two disagree, or the text is not a known license
identifier, record the wording and treat the license as unknown.

## The policy

The project's policy decides which licenses it accepts. A project
skill, an instruction file, a decisions doc, or a license check in
CI can hold it. When the project has none, the default is that
nothing under the GPL family (GPL, LGPL, or AGPL) is bundled into
what the project ships, and the user decides anything else.

A license the policy rejects, or an unknown one, stops the change
before the commit. Name the package, its license, and the rule it
breaks, and ask whether to drop it, replace it, or change the
policy. A tool that runs beside the project and is not bundled with
it is named in the reply and is not a stop.

When the project has a license check in CI, run it, and treat its
failure as a failed check. When it has none, say so. Adding one is
a change the user asks for.

## The record

Record each checked item, its version, its license, and the result
where the project keeps its deployment docs or third-party notices.
When the project keeps neither, put the list in the reply and ask
where it goes.

## The same check

A second run reads the record. An item already recorded at the same
version and license is left as it is.

## What this change does not do

It does not edit a past spec. It adds no key and no bound. It adds no
CI job to any project, and it names no project, host, or tool.
