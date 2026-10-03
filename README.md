# Kobold Codex

Principles and workflow skills for coding agents on Grok and Claude Code.
The skills live under `skills/`. A session uses the skill whose description matches the task.
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

Start a new session after installing so the skill is in the catalog.

## License

MIT. See [LICENSE](LICENSE).
