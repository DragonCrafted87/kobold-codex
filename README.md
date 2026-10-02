# Kobold Codex

Voice and engineering principles for coding agents on Grok and Claude Code.
The wording lives in [skills/kobold-codex/SKILL.md](skills/kobold-codex/SKILL.md).
The 2026-10-01 decision is recorded in
[docs/specs/2026-10-01-kobold-codex-design.md](docs/specs/2026-10-01-kobold-codex-design.md).

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
