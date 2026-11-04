# Prove the product: a screen the user sees

A revision of `prove-the-product`, from research item KCO-2374. The
wording below is the version to ship.

## Research

ux-ui-agent-skills (plugin87, MIT, about 1.9k stars when filed,
release 3.0.0 when read on 2026-11-03) is a design-system layer for
coding agents: runnable skills, component specs, design tokens, and
52 gates, 34 of which open a real browser. The gates that matter here
are objective: contrast in every control state, an accessibility
audit, keyboard reach and focus, target size, no sideways overflow at
280 px, and reduced motion. They fail a page on measurements, not
taste.

What Kobold Codex takes: the habit of measuring a screen instead of
trusting the agent's account of it, which fits `prove-the-product`'s
drive. What it does not take: the design tokens, the design-system
catalog, the framework adapters, the taste rules, the hooks, and the
gate scripts themselves. Those are a design practice and a toolset, not
a workflow habit, and a project that wants them can install that
plugin. Its evals layout is noted as a model if this plugin gains
skill evals; that is not part of this change. The wording below is
original.

## Skill: prove-the-product

A new heading before A later pass.

## A screen the user sees

When a step ends on a screen, check what the user would see with a
measurement, not a look. Run each check the app can reach in a real
browser or on a device:

- The contrast of text and controls against what is behind them, in
  every state a control has: default, hover, focus, pressed,
  disabled, and loading.
- An accessibility audit of roles, names, and landmarks.
- The keyboard: every control is reachable, the focus is visible,
  and the order matches the screen.
- The size of each target a user taps or clicks.
- A narrow screen: no content scrolls sideways at the narrowest width
  the app supports.
- Reduced motion: when the user asks for it, nothing moves that the
  task does not need.

When the project already has a tool for one of these, the step runs
that tool. When it has none, say which checks the drive could not
run. Adding a tool follows `check-the-licenses` and is a change the
user asks for. A check that fails is a failed step, the same as any
other.

## What this change does not do

It does not edit a past spec. It adds no key, no bound, and no tool,
and it names no project or tool.
