# Kobold Codex

Principles and workflow skills for coding agents on Grok and Claude Code.
The skills live under `skills/`, one folder each. Each skill's group, the phase of work it serves, is in its frontmatter, and [docs/skills.md](docs/skills.md) lists them by group. A session uses the skill whose description matches the task.
Install the plugin, then start a new session so the skills are in the catalog.
The map of which skill applies, and the design notes, live in [docs/skills.md](docs/skills.md).

## Install

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

Start a new session after installing so the skill is in the catalog.

## License

MIT. See [LICENSE](LICENSE).
