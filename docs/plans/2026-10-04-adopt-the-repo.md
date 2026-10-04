# Adopt the Repo Implementation Plan

> **For agentic workers:** Implement this task after the spec is reviewed. Steps use checkbox (`- [ ]`) syntax for tracking. Superpowers is disabled. Do not invoke it.

**Goal:** Ship `adopt-the-repo`, the skill that joins Kobold to another repository on one of two paths, and bump the plugin to `0.10.0`.

**Architecture:** The new spec is the record of the decision. The skill file is the copy a session loads. `adopt-the-repo` owns the two paths, the split of an instruction file into why versus what and how, the project skill and playbook files, the adopt record, and the choice of how a path stays out of the project repository. That choice is gitignore or git exclude. When the specs stay out of the project, the skill also asks whether a local config repository should keep the history of the skills and the config, and that repository has its own bounds. `set-the-bounds` still writes each bounds layer and still owns the ignore line for `.kobold/bounds.local.yaml`. It writes the project layer at the project root and the config-repo layer at the config repo root. `write-the-plan` still owns where a plan file goes. `leave-a-trail` still owns the ignore line for `.kobold/trail.md`. `run-the-play` keeps the match, and its match also includes a project playbook directory this skill records. `write-a-skill` still owns skills in this plugin and `docs/specs/` for this plugin. The work stays on `feat/adopt-the-repo`, cut from `main` at `d0212db`. No worktree.

**Tech Stack:** Markdown skills, JSON manifests, Python 3 standard library, `grok plugin validate`.

**Specs:**

- `docs/specs/2026-10-04-adopt-the-repo-design.md`

The spec is written by Task 1. This plan is the source for that spec. The spec's Skill section holds the section bodies that ship. Copy those bodies into `skills/adopt-the-repo/SKILL.md`. If a sentence in this plan disagrees with the spec after Task 1, the spec wins. The stable manifest description lives in the catalog's ship rule.

What will change is the goal above. What the change touches is the architecture above. What stays the same is Global Constraints. What the checks cover is Step 5 of Task 2.

## Global Constraints

- The skill name is `adopt-the-repo`. Plugin name and marketplace name stay `kobold-codex`.
- `adopt-the-repo` description is one physical line: `Use when adding Kobold to a repository. Convert its instructions into skills and playbooks, either by minimizing the root instruction files or by leaving those files alone, and ask which bounds fit what the files already say.`
- Heading names, in order: `The choice`, `The sources`, `The move`, `The bounds`, `The local repo`, `An empty tree`, `The same repo`. The skill title is `Adopt the repo`.
- Plugin and marketplace description stay the stable sentence: `Principles and workflow skills for DragonCrafted87's agents on Grok and Claude Code.`
- Version becomes `0.10.0` in `.claude-plugin/plugin.json` and in the one plugin entry inside `.claude-plugin/marketplace.json`. The marketplace object has no version field. Leave it that way. License, author, repository, and marketplace `source` stay as they are. `0.10.0` is a minor bump because the change adds a skill. `0.9.2` is the version on `main`.
- The skill names no host tool. It adds no hooks. The repo has no `hooks/` directory and no `hooks.json`.
- These files are not edited: `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`, `skills/set-the-bounds/SKILL.md`, `skills/debug-the-failure/SKILL.md`, `skills/how-it-fits/SKILL.md`, `skills/why-it-is/SKILL.md`, `skills/write-the-plan/SKILL.md`, `skills/carry-out-the-plan/SKILL.md`, `skills/review-the-diff/SKILL.md`, `skills/take-the-review/SKILL.md`, `skills/stress-the-change/SKILL.md`, `skills/ship-the-branch/SKILL.md`, the four files in `skills/run-the-play/playbooks/`, `skills/isolate-the-work/SKILL.md`, `skills/fan-out/SKILL.md`, `skills/try-several-shapes/SKILL.md`, `skills/measure-the-blast/SKILL.md`, `skills/prove-the-product/SKILL.md`, `skills/leave-a-trail/SKILL.md`, `skills/pick-up-the-work/SKILL.md`, `skills/learn-from-the-session/SKILL.md`, `skills/write-a-skill/SKILL.md`, `skills/cut-the-slop/SKILL.md`, `skills/write-the-doc/SKILL.md`, the specs those skills pin, `docs/specs/2026-10-02-remaining-skills-design.md`, and `README.md`. The catalog's skill briefs, playbook briefs, and ship rule stay. `skills/run-the-play/SKILL.md` is the one existing skill this change edits, and the edit is the paragraph in Task 2 Step 2.
- `tests/check_plugin.py` gains no section pin and no new function. It already requires a branch off `main` to be ahead on version. Do not restore body pinning.
- The README keeps the four install lines, points at `docs/skills.md`, does not link a spec, and does not restate a section body. `docs/skills.md` links the new skill and its spec. The new map sentences are the paragraphs in Task 2 Step 4. They do not copy a skill section body.
- No tracked file contains a hostname, a home-directory path, or a machine name. The user config path stays the portable tilde path where a bounds file is named, and that sentence stays in `set-the-bounds`.
- This skill does not convert the `kobold-codex` plugin into a target. When the repository's `.claude-plugin/plugin.json` names `kobold-codex`, the skill says so and stops.
- Publishing follows the resolved bounds. `commit-specs` governs the spec commit. `commit-plans` governs this plan. `commit` governs the skill, the `run-the-play` paragraph, the manifests, and the map. `push` and `pull-request` govern publishing the branch. `merge` stays on its own key. Name each key, the value, and the layer that set it before that action.
- Commit subjects are one line. The spec commit is `Record the adopt-the-repo spec`. The plan commit is `Add the plan for adopt-the-repo`. The work commit is `Add the adopt-the-repo skill`. The checkbox commit is `Mark the finished adopt-the-repo plan steps`. The commit after the pull request is open is `Mark the adopt-the-repo plan published`.

## The behavior the spec records

The spec's Decisions section records the notes below. The spec's Skill section turns them into the seven section bodies. Wording follows `kobold-codex`. A paragraph taken from another skillset does not ship.

### The choice

Two paths. Ask which one, unless `.kobold/adopt.yaml` already records it.

- **Full.** Convert the sources. Rewrite each instruction file so it keeps the why and loses the what and the how. The root instruction file points at the `kobold-codex` plugin and at the project skill root. Minimize means the why stays, in sentences, and the procedures and the subject facts do not remain underneath a pointer.
- **Shadow.** Convert the sources into skills and playbooks. Do not edit the repository's instruction files. The converted files stay out of the project repository. The hide choice in The local repo covers the skill root and the playbook directory when that root has no tracked files yet. When the root already has tracked files, the hide choice covers each new skill directory and each new playbook file, and it does not cover the root.

The record is `.kobold/adopt.yaml` at the repository root. It names `mode`, `skill-root`, `playbooks`, `plans`, `specs`, `plans-tracked`, `specs-tracked`, `hide`, and `config-repo`. `hide` is `gitignore` or `exclude`, and it is absent when every Kobold path is tracked. `config-repo` is the path of the local repository, or absent when the user declines one. The adopt record is tracked with the project when every Kobold path it names is tracked. When any of those paths stays out, the record stays out with them.

Suggest `.kobold/bounds.yaml` as the bounds layer on the full path, because the sources are team instructions. Suggest `.kobold/bounds.local.yaml` on the shadow path. The user can name the other writable layer. `set-the-bounds` writes the file. This skill does not write a bounds key itself.

### The sources

Read instruction files and skills. Do not sweep the repository for every Markdown file. A README, a contributing guide, and a doc are sources only when the user names them.

Instruction file names, at the repository root and in subdirectories: `AGENTS.md`, `AGENT.md`, `Agents.md`, `CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`, plus `.claude/CLAUDE.md` and `.claude/CLAUDE.local.md`. Also every Markdown file placed directly in `.grok/rules/`, `.claude/rules/`, or `.cursor/rules/`. A session skips an instruction file that git is ignoring, including a file matched from `.git/info/exclude`. A shadow must not depend on one of those files for the converted what and how.

Skill files are `SKILL.md` under a directory the project already uses for skills a session loads. Command files are Markdown files placed directly in a `commands/` directory beside such a skill root. Those are sources too.

A skill directory the project already has is the skill root. When several exist, ask which one receives the converted skills. When none exist, ask, and offer `.claude/skills/` and `.agents/skills/`. `.claude/skills/` is a directory sessions on both hosts already read. `.agents/skills/` is the host-neutral name. The playbook directory is `playbooks` beside that skills directory.

### The move

Split each source by job.

- **Why** explains a constraint: the purpose, and the reason a rule exists. On the full path it stays in that instruction file. On the shadow path it stays where it was, because the instruction file is not edited, and it is not copied into a second always-on file.
- **What** is a fact, a table, or a rule about a subject. It becomes a skill, grouped with the other facts for that subject.
- **How** is an ordered procedure for a kind of task. It becomes a playbook. A procedure that only makes sense inside one subject stays in that subject's skill.

Group by subject. A subject is the thing the paragraphs are about. Do not make a skill per heading, and do not make a skill whose body is one sentence when that sentence belongs with a subject already being written.

A project skill is one directory under the skill root with one `SKILL.md`. The description is one physical line and says when the skill applies. The wording is original and follows `kobold-codex`. The file names no host tool. These files are not skills in this plugin, and they do not bump this plugin's version. `write-a-skill` remains the skill that authors a skill here.

A project playbook is a Markdown file in the playbook directory. It has a title and headings. The text under a heading is the procedure. It has no frontmatter. The four plugin playbooks stay the files for the task kinds they already name. A project playbook does not reuse those four names.

On the full path, every instruction file that had a why keeps that why, rewritten in the same voice, plus one pointer: this repository uses Kobold Codex, and the project skills live at the skill root. Put that pointer in each root instruction file that remains, so a session that reads any one of them still finds Kobold. Delete an instruction file that has no why left. When that deletion would remove the last root instruction file, keep one root file and let the pointer be its body. When the repository had both `AGENTS.md` and `CLAUDE.md`, minimize both. When it had neither, the empty-tree rule creates `AGENTS.md` and does not also create `CLAUDE.md`. A command file on the full path becomes a one-line pointer at the skill that now holds its procedure. On the shadow path, command files stay as they are.

A sentence that sets a bound stays in the source until The bounds has recorded the suggestion. After the user accepts a key, the full path does not also leave that sentence in the instruction file as a second copy of the key. The sentence's why can stay. The value lives in the bounds file `set-the-bounds` writes.

Show the file map before writing. The map names each source, each skill or playbook it will become, and each instruction file the full path will edit. Write after the user accepts the map. The choice of path is part of that acceptance.

When the user marks plans or specs tracked, leave that directory visible to the project repository. When the directory is empty and tracked, add a `.gitkeep` so the folder stays in git. A local directory is created on disk and hidden by The local repo, with no `.gitkeep`.

The plan directory is the one `write-the-plan` would use. The spec directory is the one the project already uses for design specs. When the project has neither, the paths are `docs/plans/` and `docs/specs/` until a config repo takes the local ones. When a directory already has tracked files, record it as tracked and do not ask. Ask only when the directory is absent or untracked. Suggest local for plans, because `commit-plans` defaults to `never`. Suggest tracked for specs, because `commit-specs` defaults to `ask` and a spec is the record of a decision.

### The bounds

After the sources are read, and in the same question set as the path and the skill root, show a table. The columns are the key, the suggested value, the file and the sentence that suggested it, and the value that applies if this repository writes nothing.

Suggest a key only when a sentence is about the action that key controls.

- A file that forbids commits outright suggests `commit: never`. A file that says to commit without asking suggests `commit: auto`. Anything softer, including commits that depend on the branch, suggests `commit: ask`.
- The same three values apply to `push`, `commit-plans`, and `commit-specs`, using the sentences about those actions.
- Always opening a pull request suggests `pull-request: auto`. Never opening one suggests `pull-request: never`.
- A ban on merge suggests `merge: never`. Merge only when asked suggests `merge: ask`.
- A ban on rewriting the remote suggests `force-push: never`.
- Work that continues through publish while the user is away suggests `unattended: through-publish`. Stopping at the plan suggests `unattended: stop-at-plan`.
- A ban on other agents suggests `subagents: deny`. Permission to start them suggests `subagents: allow`.
- The same allow or deny reading applies to `browser`, `shell-network`, `github-write`, and `worktrees`.

A branch policy the keys cannot express is not a suggestion. It stays a skill or a playbook, and the reply names the sentence. Two sentences that suggest different values for one key are both shown. Do not pick one silently. A key with no sentence has no suggestion. Its row shows the inherited value.

Ask which layer, with the suggestion from The choice, and which keys to write. Then `set-the-bounds` writes only the keys the user named, on the one layer they named, at the project root. When the user names no keys, write no project bounds file. That includes a user who keeps the inherited values.

### The local repo

When the user keeps the specs out of the project repository, ask two more questions before writing. Ask the same two questions when the specs are tracked and another Kobold path is staying out, so the choice is made once for every path this run keeps out of the project. When every Kobold path is tracked, skip this section.

The first question is how the project repository should leave those paths alone.

- **Gitignore.** Put the patterns in the project's ignore file. That file is committed with the project, so the team receives the patterns.
- **Git exclude.** Put the patterns in `.git/info/exclude` for this clone. That file stays in the clone. It is not a commit in the project.

One answer covers every path this run is keeping out. The paths are the local spec directory, the local plan directory, the shadow skill root or the new skill directories, the shadow playbook paths, `.kobold/adopt.yaml` when the record stays out, and the config repo directory when one is created. Append a pattern when that path is not already ignored. Gitignore creates the ignore file when the repository has none. Exclude appends to `.git/info/exclude`. Do not write the same pattern in both places. Do not add `.kobold/bounds.local.yaml`. Do not add `.kobold/trail.md`. A path that is already tracked is not hidden. This skill does not untrack it.

The second question is whether a separate git repository should keep the history of the skills and the config. Suggest `.kobold/local` as its root. The user can name another directory. That directory is the repository root. The same hide choice covers it. Decline leaves the local files in place in the project tree, hidden and without their own history.

The config repo tracks the Kobold files this run is keeping out of the project: local specs, local plans, local skills, local playbooks, and the adopt record. Skills that the project repository tracks stay there. The config repo has its own root so its bounds file is not the project's bounds file.

A session loads skills from a scanned skill root. When the skills live in the config repo, the skill root in the project is a symlink to `<config-repo>/skills`. The hide choice covers that symlink. The recorded playbook directory is `<config-repo>/playbooks`. The recorded spec directory is `<config-repo>/specs` when the specs are local. The recorded plan directory is `<config-repo>/plans` when the plans are local. The adopt record that sessions read stays `.kobold/adopt.yaml`. When the record lives in the config repo, that path is a symlink to `<config-repo>/adopt.yaml`, and the hide choice covers the symlink.

The config repo starts with `git init` in its root. Do not add a remote unless the user names one.

Its bounds are a second table, for that repository only. The project's bounds do not govern it. Its bounds do not govern the project. The machine bounds file still sits behind both, and a key written in the config repo replaces the machine value for that repo only. Suggest these keys, because the repo exists to record local history: `commit: auto`, `commit-specs: auto` when the specs live there, `commit-plans: auto` when the plans live there, `push: never`, `pull-request: never`, `merge: never`, and `force-push: never`. Leave every other key with no suggestion and show the inherited value. Do not copy a suggestion that came from the project's instruction files into this table.

Ask which of those keys to write. Suggest the committed layer of the config repo, `.kobold/bounds.yaml` at the config repo root. `set-the-bounds` writes only the keys the user named, at that root. When the user names no keys, write no bounds file in the config repo.

After that write, the first commit of the config repo follows the `commit` key resolved at the config repo root. Name the key, the value, and the layer. An `auto` value commits the files that repo tracks. An `ask` value offers that commit. A `never` value leaves the files uncommitted. The project's `commit` key is not the key for this commit. Do not push the config repo during setup unless the user named a remote and the `push` key resolved at the config repo root allows it.

### An empty tree

When the read finds no instruction files and no skills, skip The move's conversion. Still ask the path, the skill root, the bounds table, the plans and specs question, and The local repo when a path will stay out of the project.

Create the skill root and the playbook directory. Create the plan directory and the spec directory. Apply the hide choice. Write `.kobold/adopt.yaml`.

On the full path, create `AGENTS.md` at the repository root. Its body is the pointer, unless the user supplies a why sentence, in which case the why comes first and the pointer follows. Do not invent a product purpose. On the shadow path, create no instruction file.

The bounds table on an empty tree has no file sentences. Every row shows the inherited value and no suggestion. Writing still waits for keys the user names.

### The same repo

A second run reads `.kobold/adopt.yaml`. The recorded path, the hide choice, and the config repo stay. Ask again only when the user names a different path, a different hide choice, or a config repo after declining one. Read the sources again. Leave a skill or a playbook whose source would produce the same file. Convert a source that changed. On the shadow path, do not write instruction files on the second run either. A new local file goes into the config repo when one is recorded, and a commit of that file uses the config repo's bounds. An empty tree that now has the folders and the record is done. Name those files.

When the repository is this plugin, stop before the questions.

### Project playbooks and the match

`run-the-play` owns the match. Add this to `The match`, after the sentence that names the `playbooks` directory beside that skill, wrapped like the rest of that file:

```text
The match also includes a project playbook directory when
`adopt-the-repo` has recorded one for this repository. A file
there is a file the match can use. There means the plugin
directory and that project directory. The four plugin playbooks
stay the files for the task kinds they already name.
```

The existing rules then apply to both directories. Do not add a second copy of the rule that asks when more than one file fits.

## Review Focus

- The skill file paraphrases its spec. The two copies of a section body must match.
- The description wraps onto a second physical line. That frontmatter must fail review.
- `plugin.json` stays at `0.9.2`, or the two manifests disagree on version or description. The manifest compare must fail.
- The README links the new spec, or restates a section body. That diff must fail the review.
- A file named in Global Constraints as not edited shows a diff. `skills/run-the-play/SKILL.md` may change only by the paragraph in Task 2 Step 2. Any other diff in that file must fail the review.
- `tests/check_plugin.py` grows a section pin or a skill-file list. That diff must fail the review.
- The skill tells `set-the-bounds` to write a key the user did not name, or it writes `.kobold/bounds.yaml` itself. That behavior must fail the review.
- The shadow path edits an instruction file. That behavior must fail the review.
- The full path leaves a procedure or a subject-fact in a root instruction file. That behavior must fail the review.
- An ignore pattern for `.kobold/bounds.local.yaml` or `.kobold/trail.md` is added by this skill. That behavior must fail the review.
- Specs the user kept out of the project are hidden with gitignore after the user chose exclude, or hidden in both places. That behavior must fail the review.
- A config repo is created after the user declined one, or its bounds keys are written into the project's bounds file. That behavior must fail the review.
- The first commit in the config repo uses the project's `commit` key. That behavior must fail the review.
- A public file names a machine or a home path. The needle scan must fail.
- The skill names a host tool. That wording must fail the review.

---

### Task 1: Write the spec

**Files:**

- Create: `docs/specs/2026-10-04-adopt-the-repo-design.md`

**Interfaces:**

- Consumes: this plan's Goal, Architecture, Global Constraints, and "The behavior the spec records".
- Produces: a spec whose Skill heading has the seven sections, with the description on one physical line. The Decisions heading holds the discovery notes: a session loads the instruction names listed in The sources and skips an instruction file git is ignoring, including a match from `.git/info/exclude`; a session loads a skill under `.grok/skills/`, `.agents/skills/`, `.claude/skills/`, and `.cursor/skills/` even when that directory is ignored. The spec does not bump the version. The catalog is not edited.

- [x] **Step 1: Write the spec**

Write `docs/specs/2026-10-04-adopt-the-repo-design.md` in the shape of `docs/specs/2026-10-03-write-the-doc-design.md`: a title, a purpose, the decisions, where the words live, and a Skill heading whose subsection bodies are the text that will ship. The seven subsection titles are the heading names in Global Constraints. The description under Skill is the one line in Global Constraints.

The check is a read of that file. Done means the seven titles are present, the description is that one line, and the bodies cover the two paths, the why split, the project bounds table, the hide choice, the config repo and its own bounds, the empty tree, and the second run.

- [x] **Step 2: Commit the spec**

When the spec is already committed on this branch, mark this step done.

Otherwise resolve `commit-specs` and commit only that file when that value allows it. Leave this plan unstaged. The subject is `Record the adopt-the-repo spec`. The body says the spec records `adopt-the-repo`, and that the skill file is not in this commit. A second run leaves a finished spec commit as it is.

### Task 2: Add the skill, point the match at project playbooks, bump the plugin

**Files:**

- Create: `skills/adopt-the-repo/SKILL.md`
- Modify: `skills/run-the-play/SKILL.md`
- Modify: `.claude-plugin/plugin.json`
- Modify: `.claude-plugin/marketplace.json`
- Modify: `docs/skills.md`
- Test: `python3 tests/check_plugin.py`
- Test: `grok plugin validate .`

**Interfaces:**

- Consumes: the Skill section of `docs/specs/2026-10-04-adopt-the-repo-design.md`. The current manifests at `0.9.2`. The match section of `skills/run-the-play/SKILL.md`.
- Produces: a skill whose section bodies match the spec, a match that can see a recorded project playbook directory, both manifests at `0.10.0` with the stable description, and a map entry. `tests/check_plugin.py` is unchanged.

- [x] **Step 1: Add the skill file**

Create `skills/adopt-the-repo/SKILL.md`. Frontmatter `name` is `adopt-the-repo`. Frontmatter `description` is the one line in Global Constraints. The title is `Adopt the repo`. Copy each section body from the spec, including line breaks.

The check is a read of the skill file against the spec. Done means each section body matches and the description is one physical line.

- [x] **Step 2: Extend the match**

Edit `skills/run-the-play/SKILL.md` only by inserting the paragraph under "Project playbooks and the match" into `The match`, after the sentence that names the plugin `playbooks` directory. Leave the rest of that skill as it is. Do not edit `docs/specs/2026-10-03-run-the-play-design.md`.

The check is `git diff -- skills/run-the-play/SKILL.md`. Done means the diff is that paragraph and nothing else.

- [x] **Step 3: Bump the manifests**

Set `version` to `0.10.0` in `.claude-plugin/plugin.json` and in the plugin entry in `.claude-plugin/marketplace.json`. Leave both descriptions as the stable sentence.

The check is a read of both `version` fields. Done means both are `0.10.0` and the descriptions still match the sentence in Global Constraints.

- [x] **Step 4: Link the skill from the map**

In `docs/skills.md`, under "Which skill applies", add this paragraph after the `write-the-doc` paragraph:

```text
Adding Kobold to a repository uses [skills/adopt-the-repo/SKILL.md](../skills/adopt-the-repo/SKILL.md). The skill converts the repository's instructions into project skills and playbooks, or lays the folder and bounds foundation when the repository has none.
```

Under "Records", add this bullet after the `write-the-doc` bullet:

```text
- [skills/adopt-the-repo/SKILL.md](../skills/adopt-the-repo/SKILL.md) is recorded in [docs/specs/2026-10-04-adopt-the-repo-design.md](specs/2026-10-04-adopt-the-repo-design.md).
```

The check is a read of `docs/skills.md`. Done means both entries are present and neither repeats a section body from the skill.

- [x] **Step 5: Run the checks**

Run `python3 tests/check_plugin.py` from the repository root. Then run `grok plugin validate .`.

Done means `python3 tests/check_plugin.py` exits 0, and `grok plugin validate .` accepts the plugin. The version on this branch is `0.10.0`, ahead of `0.9.2` on `main`. There is no new function in the check, so the real-code bar in `scope-the-edit` has no branch to cover. If `grok` is not on the path, say so and leave that check open.

### Task 3: Commit the work and publish as the bounds allow

**Files:**

- Modify: `docs/plans/2026-10-04-adopt-the-repo.md`
- Commit: the spec, this plan, and the work, as three commits when the keys allow them

**Interfaces:**

- Consumes: Task 1 and Task 2 finished, with Step 5 of Task 2 passing. `commit-specs`, `commit-plans`, `commit`, `push`, `pull-request`, and `merge` from `set-the-bounds`.
- Produces: the commits the keys allow, a pull request when `pull-request` allows one, and the finished checkboxes. `merge` is not this task unless that key is `ask` and the user says yes.

- [x] **Step 1: Commit the plan**

When this plan is already committed and the committed file matches the worktree, mark this step done.

When the worktree plan differs from the committed plan, resolve `commit-plans` and commit only this file when that value allows it. The subject of the first plan commit is `Add the plan for adopt-the-repo`. The subject of a revision before the work is `Revise the adopt-the-repo plan`. The subject of the checkbox update is `Mark the finished adopt-the-repo plan steps`. Checkboxes that Task 1 and Task 2 have finished are marked only in the checkbox commit.

- [x] **Step 2: Commit the work**

When the skill, the match paragraph, the manifests, and the map are already committed, mark this step done.

Otherwise resolve `commit` and commit those files when that value allows it. Leave the spec and this plan out of that commit. The subject is `Add the adopt-the-repo skill`. The body says the skill joins a repository on the full path or the shadow path, a local spec can stay out through gitignore or git exclude, a config repo keeps its own bounds, `run-the-play` can match a project playbook directory, and the plugin is `0.10.0`. Include a test plan that names the two checks from Task 2 Step 5 and the result you observed.

- [ ] **Step 3: Push and open the pull request**

Resolve `push` and `pull-request`. Push the branch when `push` allows it. Open one pull request when `pull-request` allows it. The base is `main`. The title is `Add the adopt-the-repo skill`. The body follows the work commit. Do not force-push. `force-push` is `never` from the skill defaults unless a nearer layer sets it, and a force-push still requires `push` to be `ask` or `auto`.

When the pull request is open, mark this step and commit that mark under `commit-plans`. The subject is `Mark the adopt-the-repo plan published`.

Resolve `merge`. When the value is `never`, stop after the pull request and say that merge did not run. Name the key, the value, and the layer.

The check is the pull request URL, or the name of the key that stopped the push. Done means the branch is on the remote and the pull request is open, or the reply names the key that stopped that step.
