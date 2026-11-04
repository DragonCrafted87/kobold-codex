# Kobold Codex

Principles and workflow skills for coding agents on Grok, Claude Code, Codex, Gemini CLI, Cursor, and any host that reads Agent Skills.

## How

Kobold Codex is a set of skills. Each skill is one folder under `skills/` holding a `SKILL.md`: a one-line description that says when it applies, then short sections that say what to do.

The agent's host lists every installed skill by its description. When a task matches a description, the agent loads that skill and follows it. One skill, `kobold-codex`, is the voice and the engineering principles every other skill leans on.

Each skill belongs to a group, the phase of work it serves: ground, investigate, plan, build, review, ship, session, learn, write, and setup. The group is a `group` field in the skill's frontmatter. [docs/skills.md](docs/skills.md) lists the skills by group, says which one applies to what, and links each skill to the spec that records it.

Some skills read project settings from `.kobold/` in the repository you are working in. `set-the-bounds` decides what an agent may do on its own, such as commit, push, open a pull request, or merge. `adopt-the-repo` sets a repository up for the plugin.

### Install

Grok, from GitHub:

```bash
grok plugin install DragonCrafted87/kobold-codex --trust
```

Grok, from a local checkout of this repository:

```bash
grok plugin install . --trust
```

Claude Code, in a session:

```text
/plugin marketplace add DragonCrafted87/kobold-codex
/plugin install kobold-codex@kobold-codex
```

Codex, from GitHub (reads the Agent Plugins `plugin.json` at the root, or the Claude manifest):

```bash
codex plugin marketplace add DragonCrafted87/kobold-codex
codex plugin add kobold-codex@kobold-codex
```

Gemini CLI, from GitHub (reads `gemini-extension.json` and `skills/`):

```bash
gemini extensions install https://github.com/DragonCrafted87/kobold-codex
```

Cursor: install it as an Agent Plugin from a team marketplace, or copy a checkout into `~/.cursor/plugins/local/kobold-codex` and reload the window.

Any host that reads `.agents/skills/` (Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode): copy or link each folder under `skills/` into the project's or the user's `.agents/skills/`. Claude Code reads `.claude/skills/` the same way.

Start a new session after installing so the skills are in the catalog.

## Why

Agents drift without a few firm habits. Kobold Codex writes those habits down as small skills an agent can load when it needs them, instead of one long instruction file it has to hold in mind all the time.

- **Small, generic skills.** Each skill does one job and has one trigger. Skills name no project, host, or tool, and a check enforces it, so the same skill works in any repository. Project rules live in that project's own skills.
- **Scope decides the process.** A small edit is just done. A bug fix names what is wrong and the check that proves the fix. An architectural change gets a written plan, and work starts only after that plan is approved.
- **Specs and plans.** Every change to a skill has a dated design spec that records what was decided and why, and a plan with checkboxes and a Status block. A later session can pick up a plan where the last one stopped. Past specs never change; git history keeps older wording.
- **Checks, not claims.** A step is done when its check ran and showed the expected result. Reviews cite a file and a line. Answers mark what was seen, what was inferred, and what is unknown.
- **Bounds the user sets.** Commits, pushes, pull requests, merges, and changes to live systems follow bounds the user controls, so an agent working alone does not go further than it was allowed.
- **Safe to run again.** A second run of a skill from a finished state changes nothing, and a run that stopped halfway can be finished.
- **It learns.** `learn-from-the-session` and `review-the-week` turn what went wrong in real sessions into edits to the skills.

## License

MIT. See [LICENSE](LICENSE).
