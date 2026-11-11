---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Context.lift, Cslib.SessionTypes.Endpoint.Context.lookup_lift, Cslib.SessionTypes.Endpoint.Context.bind, Cslib.SessionTypes.Endpoint.Context.fresh_lift, Cslib.SessionTypes.Endpoint.Context.lookup_bind_positive, Cslib.SessionTypes.Endpoint.Context.lookup_bind_negative, Cslib.SessionTypes.Endpoint.Context.lift_singleton, Cslib.SessionTypes.Endpoint.Context.lift_empty
statement: formalized
proof: formalized
---

# Binder transport of finite ownership maps

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html).

## Lifting an ownership map past a binder

Insert an ambient name binder at any cutoff in an ownership context.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lift).

## Lookups in a lifted ownership map

Lifting keeps the entire capability at the corresponding lifted key.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lookup-lift).

## Binding a fresh dual pair under restriction

A restriction binds one physical name and creates its two distinct
linear roles. Lifted outer keys cannot be overwritten by these insertions.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#bind).

## Both roles of the new name are fresh for a lifted map

Both roles of the newly inserted name are fresh for the lifted context.

Formalized by `Cslib.SessionTypes.Endpoint.Context.fresh_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#fresh-lift).

## Positive role lookup after restriction binding

Restriction installs the positive capability without losing it to the
opposite role's insertion.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_bind_positive`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lookup-bind-positive).

## Negative role lookup after restriction binding

The same restriction installs the negative peer at the SAME name.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_bind_negative`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lookup-bind-negative).

## Lifting a singleton ownership map

Lifting a single capability shifts its name, not its protocol or role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_singleton`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lift-singleton).

## Lifting the empty ownership map

Inserting a binder does not manufacture an outer capability.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#lift-empty).

## Restriction binding over the empty map

In an empty outer context, restriction exposes exactly its two peers.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#bind-empty).

## Entries of a restriction-bound ownership map

The exact restriction context has two fresh entries plus all shifted
outer ownership. No old entry is overwritten by a new endpoint role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.entries_bind`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#entries-bind).

## Lifting preserves absence of a key

Lifting preserves absence of an outer role from its finite context.

Formalized by `Cslib.SessionTypes.Endpoint.Context.fresh_lift_of_fresh`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#fresh-lift-of-fresh).

## Restriction binding preserves absence of an outer key

An absent outer key remains absent after adding the fresh bound dual pair.

Formalized by `Cslib.SessionTypes.Endpoint.Context.fresh_bind_of_fresh`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/ContextTransport.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html#fresh-bind-of-fresh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binder transport of finite ownership maps](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/binder-transport-of-finite-ownership-maps)
