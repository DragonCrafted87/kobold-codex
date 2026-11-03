# Map the handoffs

A new skill in the plan group, from KCO-2602. The wording below is
the version to ship.

## Why

Plans in this plugin are ordered task lists. Some work is not a line:
a review can send a change back to the build step, a check can route
to one of two fixes, or agents pass work between them. When those
routes live only in a session's head, a later session or another
agent cannot follow them, and a loop back has no limit. A graph in the
plan makes each route explicit: nodes are steps or skills with a check
that ends them, and edges are readable conditions with the payload
they carry.

The graph lives in the plan, not a separate file, so the plan stays
the one record of the work. It complements `loop-to-the-goal`, which
loops one step, and `fan-out`, which runs independent work side by
side.

## Skill: map-the-handoffs

```text
description: Use when work passes between skills or agents along more than one path, such as a review that can send work back or a step that can branch. Write the handoffs as a graph in the plan, with each node a step or a skill and each edge a condition and the payload it carries, and follow only the edges the graph names.
```

## When a graph

A straight list of tasks needs no graph; `write-the-plan` covers it.
Write a graph when a step can go to more than one next step, when a
step can send work back to an earlier one, or when several agents
hand work to each other.

## The graph

The graph goes in the plan, under a Handoffs heading, as two lists.

Each node has a name, the skill or the agent that runs it, and the
check that ends it. One node is the start, and at least one is an
end.

Each edge names the node it leaves, the node it enters, the condition
that sends work along it, and the payload: the files, the result, and
the notes the next node needs, and nothing it does not. A condition
is something the session can read, such as a check result or a
finding's severity, not a judgment made later.

An edge that goes back to an earlier node names how many times it
can be taken. When that count is used up, the work goes to an end
node that reports, not round again.

## Following it

At the end of a node, read its check, find the edge whose condition
holds, and hand over that edge's payload. When no edge's condition
holds, or two do, stop and report the node and the result. Do not
pick an edge the graph does not name.

A handoff to another agent follows `subagents`, and the payload is
that agent's brief. Record each edge taken in the plan's Status
block.

## The same graph

A second run reads the Status block and continues from the last edge
taken, with the counts on edges that go back already used.

## What this change does not do

It does not edit a past spec. It does not change `write-the-plan`
or `carry-out-the-plan`. It adds no key and no bound, and it names
no project, host, or tool.
