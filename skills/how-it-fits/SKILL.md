---
name: how-it-fits
description: Use before changing a subsystem. Name the runtime path, the package that owns the behavior, and the layer the change belongs on.
---

# How it fits

## Read first

Read the subsystem this change would touch before editing it. In the
reply, name the runtime path, the owner, and the layer. The read is
the work of this skill. An edit waits until the user asks for one.

## Runtime path

Follow one request, one command, or one event from the entry the user
named, through the place the behavior happens, and out to what the
caller observes. Name the functions or the modules on that path, in
order. When the path forks, follow the fork this question cares about,
and name the forks you left.

## Owner

Name the package, module, or directory that owns the behavior. A
change to that behavior lands there. A caller that only invokes the
behavior does not own it. When two places both look like the owner,
name both, say which one you would change, and say why.

## Layer

Name the layer the change belongs on. A layer is a boundary the code
already has. The usual ones are the interface a caller uses, the rule
behind that interface, the storage, and the edge that talks to another
system. Put a new rule on the layer that already decides that kind of
rule. When the change needs a layer the code does not have, say so and
stop. Adding that layer is an architectural edit.
