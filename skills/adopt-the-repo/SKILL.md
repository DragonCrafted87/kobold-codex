---
name: adopt-the-repo
description: Use when adding Kobold to a repository. Convert its instructions into skills and playbooks, either by minimizing the root instruction files or by leaving those files alone, and ask which bounds fit what the files already say.
---

# Adopt the repo

## The choice

When `.claude-plugin/plugin.json` names `kobold-codex`, say so
and stop. This skill does not convert the plugin into a target.

Ask which path to use, unless `.kobold/adopt.yaml` already
records one.

Full converts the sources. Each instruction file keeps the why
and loses the what and the how. Each root instruction file that
remains points at the `kobold-codex` plugin and at the project
skill root. The why stays in sentences. A procedure or a subject
fact does not remain under that pointer.

Shadow converts the sources into skills and playbooks. Leave the
instruction files as they are. The converted files stay out of
the project repository. When the skill root has no tracked files,
the hide choice in The local repo covers the skill root and the
playbook directory. When the root already has tracked files, the
hide choice covers each new skill directory and each new playbook
file, and the root stays visible.

The record is `.kobold/adopt.yaml` at the repository root. It
names `mode`, `skill-root`, `playbooks`, `plans`, `specs`,
`plans-tracked`, `specs-tracked`, `hide`, and `config-repo`.
`mode` is `full` or `shadow`. `hide` is `gitignore` or `exclude`,
and it is omitted when every Kobold path is tracked.
`config-repo` is the path of the local repository, and it is
omitted when the user declines one. The adopt record is tracked
with the project when every Kobold path it names is tracked.
When any of those paths stays out, the record stays out with
them.

On the full path, suggest `.kobold/bounds.yaml` as the bounds
layer. The sources are team instructions. On the shadow path,
suggest `.kobold/bounds.local.yaml`. The user can name the other
writable layer. `set-the-bounds` writes the file. This skill
writes no bounds key.

## The sources

Read instruction files and skills. Leave the rest of the
repository's Markdown unread. A README, a contributing guide, and
a doc are sources only when the user names them.

Instruction file names, at the repository root and in
subdirectories, are `AGENTS.md`, `AGENT.md`, `Agents.md`,
`CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`, `.claude/CLAUDE.md`,
and `.claude/CLAUDE.local.md`. Also read every Markdown file
placed directly in `.grok/rules/`, `.claude/rules/`, or
`.cursor/rules/`. A session skips an instruction file that git is
ignoring, including a file matched from `.git/info/exclude`. On
the shadow path, the converted what and how go in a skill or a
playbook, not in one of those files.

Skill files are `SKILL.md` under a directory the project already
uses for skills a session loads. Command files are Markdown files
placed directly in a `commands/` directory beside such a skill
root. Those files are sources too.

A skill directory the project already has is the skill root. When
several exist, ask which one receives the converted skills. When
none exist, ask, and offer `.claude/skills/` and
`.agents/skills/`. `.claude/skills/` is a directory sessions on
both hosts already read. `.agents/skills/` is the host-neutral
name. The playbook directory is `playbooks` beside that skills
directory.

## The move

Split each source by job.

Why explains a constraint: the purpose, and the reason a rule
exists. On the full path it stays in that instruction file. On
the shadow path it stays where it was. The instruction file is
not edited, and the why is not copied into a second always-on
file.

What is a fact, a table, or a rule about a subject. It becomes a
skill, grouped with the other facts for that subject.

How is an ordered procedure for a kind of task. It becomes a
playbook. A procedure that only makes sense inside one subject
stays in that subject's skill.

Group by subject. A subject is the thing the paragraphs are
about. Do not make a skill per heading. Do not make a skill whose
body is one sentence when that sentence belongs with a subject
already being written.

A project skill is one directory under the skill root with one
`SKILL.md`. The description is one physical line and says when
the skill applies. The wording is original and follows
`kobold-codex`. The file names no host tool. These files are not
skills in this plugin, and they do not bump this plugin's
version.

A project playbook is a Markdown file in the playbook directory.
It has a title and headings. The text under a heading is the
procedure. It has no frontmatter. The files in the plugin
playbook directory stay the files for the task kinds they already
name. A project playbook does not reuse one of those names.

On the full path, every instruction file that had a why keeps
that why, rewritten in the same voice, plus one pointer. The
pointer says this repository uses Kobold Codex, and it names the
skill root. Put that pointer in each root instruction file that
remains, so a session that reads any one of them still finds
Kobold. Delete an instruction file that has no why left. When
that deletion would remove the last root instruction file, keep
one root file and let the pointer be its body. When the
repository had both `AGENTS.md` and `CLAUDE.md`, minimize both.
When it had neither, An empty tree creates `AGENTS.md` and does
not also create `CLAUDE.md`. A command file on the full path
becomes a one-line pointer at the skill that now holds its
procedure. On the shadow path, command files stay as they are.

A sentence that sets a bound stays in the source until The bounds
has recorded the suggestion. After the user accepts a key, the
full path does not also leave that sentence in the instruction
file as a second copy of the key. The sentence's why can stay.
The value lives in the bounds file `set-the-bounds` writes.

Show the file map before writing. The map names each source, each
skill or playbook it will become, and each instruction file the
full path will edit. Write after the user accepts the map. The
choice of path is part of that acceptance.

When the user marks plans or specs tracked, leave that directory
visible to the project repository. When the directory is empty
and tracked, add a `.gitkeep` so the folder stays in git. A local
directory is created on disk and hidden by The local repo, with
no `.gitkeep`.

The plan directory is the one `write-the-plan` would use. The
spec directory is the one the project already uses for design
specs. When the project has neither, the paths are `docs/plans/`
and `docs/specs/` until a config repo takes the local ones. When
a directory already has tracked files, record it as tracked and
do not ask. Ask only when the directory is absent or untracked.
Suggest local for plans, because `commit-plans` defaults to
`never`. Suggest tracked for specs, because `commit-specs`
defaults to `ask` and a spec is the record of a decision.

## The bounds

After the sources are read, and in the same question set as the
path and the skill root, show a table. The columns are the key,
the suggested value, the file and the sentence that suggested it,
and the value that applies if this repository writes nothing.

Suggest a key only when a sentence is about the action that key
controls.

A file that forbids commits outright suggests `commit: never`. A
file that says to commit without asking suggests `commit: auto`.
Anything softer, including commits that depend on the branch,
suggests `commit: ask`. The same three values apply to `push`,
`commit-plans`, and `commit-specs`, using the sentences about
those actions.

Always opening a pull request suggests `pull-request: auto`.
Never opening one suggests `pull-request: never`. A ban on merge
suggests `merge: never`. Merge only when asked suggests
`merge: ask`. A ban on rewriting the remote suggests
`force-push: never`.

Work that continues through publish while the user is away
suggests `unattended: through-publish`. Stopping at the plan
suggests `unattended: stop-at-plan`. A ban on other agents
suggests `subagents: deny`. Permission to start them suggests
`subagents: allow`. The same allow or deny reading applies to
`browser`, `shell-network`, `github-write`, and `worktrees`.

A branch policy the keys cannot express is not a suggestion. It
stays a skill or a playbook, and the reply names the sentence.
Two sentences that suggest different values for one key are both
shown. Ask which value. A key with no sentence has no
suggestion. Its row shows the inherited value.

Ask which layer, with the suggestion from The choice, and which
keys to write. Then `set-the-bounds` writes only the keys the
user named, on the one layer they named, at the project root.
When the user names no keys, write no project bounds file. That
includes a user who keeps the inherited values.

## The local repo

When the user keeps the specs out of the project repository, ask
two more questions before writing. Ask the same two questions
when the specs are tracked and another Kobold path is staying
out, so the choice is made once for every path this run keeps out
of the project. When every Kobold path is tracked, skip this
section.

The first question is how the project repository should leave
those paths alone. Gitignore puts the patterns in the project's
ignore file. That file is committed with the project, so the team
receives the patterns. Git exclude puts the patterns in
`.git/info/exclude` for this clone. That file stays in the clone.
It is not a commit in the project.

One answer covers every path this run is keeping out. The paths
are the local spec directory, the local plan directory, the
shadow skill root or the new skill directories, the shadow
playbook paths, `.kobold/adopt.yaml` when the record stays out,
and the config repo directory when one is created. Append a
pattern when that path is not already ignored. Gitignore creates
the ignore file when the repository has none. Exclude appends to
`.git/info/exclude`. Do not write the same pattern in both
places. Do not add `.kobold/bounds.local.yaml`. Do not add
`.kobold/trail.md`. A path that is already tracked is not hidden.
This skill does not untrack it.

The second question is whether a separate git repository should
keep the history of the skills and the config. Suggest
`.kobold/local` as its root. The user can name another directory.
That directory is the repository root. The same hide choice
covers it. A decline leaves the local files in place in the
project tree, hidden and without their own history.

The config repo tracks the Kobold files this run is keeping out
of the project: local specs, local plans, local skills, local
playbooks, and the adopt record. Skills that the project
repository tracks stay there. The config repo has its own root
so its bounds file is not the project's bounds file.

A session loads skills from a scanned skill root. When the skills
live in the config repo, the skill root in the project is a
symlink to `<config-repo>/skills`. The hide choice covers that
symlink. The recorded playbook directory is
`<config-repo>/playbooks`. The recorded spec directory is
`<config-repo>/specs` when the specs are local. The recorded plan
directory is `<config-repo>/plans` when the plans are local. The
adopt record that sessions read stays `.kobold/adopt.yaml`. When
the record lives in the config repo, that path is a symlink to
`<config-repo>/adopt.yaml`, and the hide choice covers the
symlink.

The config repo starts with `git init` in its root. Do not add a
remote unless the user names one.

Its bounds are a second table, for that repository only. The
project's bounds do not govern it. Its bounds do not govern the
project. The user config file still sits behind both
repositories. A key written in the config repo replaces the user
config value for that repo only. Suggest `commit: auto`, because
the repo exists to record local history. Suggest
`commit-specs: auto` when the specs live there. Suggest
`commit-plans: auto` when the plans live there. Suggest
`push: never`, `pull-request: never`, `merge: never`, and
`force-push: never`. Leave every other key with no suggestion
and show the inherited value. Do not copy a suggestion that came
from the project's instruction files into this table.

Ask which of those keys to write. Suggest the committed layer of
the config repo, `.kobold/bounds.yaml` at the config repo root.
`set-the-bounds` writes only the keys the user named, at that
root. When the user names no keys, write no bounds file in the
config repo.

After that write, the first commit of the config repo follows the
`commit` key resolved at the config repo root. Name the key, the
value, and the layer. An `auto` value commits the files that repo
tracks. An `ask` value offers that commit. A `never` value leaves
the files uncommitted. The project's `commit` key is not the key
for this commit. Do not push the config repo during setup unless
the user named a remote and the `push` key resolved at the config
repo root allows it.

## An empty tree

When the read finds no instruction files and no skills, skip The
move's conversion. Still ask the path, the skill root, the bounds
table, the plans and specs question, and The local repo when a
path will stay out of the project.

Create the skill root and the playbook directory. Create the plan
directory and the spec directory. When The local repo holds one
of those directories, create it inside the config repo, and make
the project skill root the symlink that section names. Apply the
hide choice. Write `.kobold/adopt.yaml`.

On the full path, create `AGENTS.md` at the repository root. Its
body is the pointer, unless the user supplies a why sentence, in
which case the why comes first and the pointer follows. Do not
invent a product purpose. On the shadow path, create no
instruction file.

The bounds table on an empty tree has no file sentences. Every
row shows the inherited value and no suggestion. Writing still
waits for keys the user names.

## The same repo

A second run reads `.kobold/adopt.yaml`. The recorded path, the
hide choice, and the config repo stay. Ask again only when the
user names a different path, a different hide choice, or a config
repo after declining one. Read the sources again. Leave a skill
or a playbook whose source would produce the same file. Convert
a source that changed. On the shadow path, do not write
instruction files on the second run either. A new local file goes
into the config repo when one is recorded, and a commit of that
file uses the config repo's bounds. An empty tree that now has
the folders and the record is done. Name those files.

The choice stops before the questions when this repository is the
`kobold-codex` plugin. A second run stops there too.
