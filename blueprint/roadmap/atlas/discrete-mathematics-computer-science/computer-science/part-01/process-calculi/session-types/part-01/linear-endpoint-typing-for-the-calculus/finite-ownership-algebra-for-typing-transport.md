---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Context.rekey_insert, Cslib.SessionTypes.Endpoint.Context.rekey_erase, Cslib.SessionTypes.Endpoint.Context.rekey_union, Cslib.SessionTypes.Endpoint.Context.lift_insert, Cslib.SessionTypes.Endpoint.Context.fresh_of_disjoint, Cslib.SessionTypes.Endpoint.Context.fresh_insert_owned, Cslib.SessionTypes.Endpoint.Context.disjoint_insert_owned, Cslib.SessionTypes.Endpoint.Context.union_insert_owned
statement: formalized
proof: formalized
---

# Finite ownership algebra for typing transport

28 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html).

## Collision-free rekeying commutes with insertion

Rekeying commutes with capability insertion when the combined domain
has no key collision. The condition is on ownership, not execution.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#rekey-insert).

## Collision-free rekeying commutes with erasing an owned key

Erasing an owned key commutes with collision-free rekeying.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#rekey-erase).

## Collision-free rekeying commutes with a disjoint union

Collision-free rekeying commutes with a linear parallel split.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#rekey-union).

## Context lifting commutes with insertion

Context lifting commutes with endpoint advancement at any cutoff.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#lift-insert).

## Owned keys are absent from the other side of a disjoint split

A sent endpoint is absent from the other side of a linear split.

Formalized by `Cslib.SessionTypes.Endpoint.Context.fresh_of_disjoint`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#fresh-of-disjoint).

## Updating an owned key keeps absent keys absent

Advancing another already-owned carrier does not create a payload alias.

Formalized by `Cslib.SessionTypes.Endpoint.Context.fresh_insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#fresh-insert-owned).

## Updating an owned key preserves a disjoint split

Advancing an already-owned endpoint preserves a disjoint split.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#disjoint-insert-owned).

## Updating owned keys on both sides of a disjoint union

Advancing both peers across a disjoint split advances exactly those
two keys in the combined interface, with no other capability change.

Formalized by `Cslib.SessionTypes.Endpoint.Context.union_insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#union-insert-owned).

## Capability transfer with carrier updates preserves disjointness

Capability transfer is a disjoint ownership move, including when the
sender and receiver also advance their distinct carrier roles.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_transfer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#disjoint-transfer).

## Moving a capability across a union preserves the union

Moving a capability out of one map into the other preserves the exact
combined interface, including completed endpoint slots.

Formalized by `Cslib.SessionTypes.Endpoint.Context.transfer_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#transfer-union).

## Erase-and-insert transfer preserves disjointness

Removing a key from the sender and inserting it at the receiver
preserves disjoint endpoint ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_erased_transfer`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#disjoint-erased-transfer).

## Combined context after delegation and two carrier updates

Delegation plus two carrier advances preserves every other key in the
combined context; the sent capability is moved, not duplicated or dropped.

Formalized by `Cslib.SessionTypes.Endpoint.Context.transfer_union_insert_owned`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#transfer-union-insert-owned).

## Erasing a different key commutes with insertion

Erasing a different endpoint commutes with insertion, which is needed
when an unused completed slot passes through a delegation prefix.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erase_insert_ne`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#erase-insert-ne).

## Inserting a key absent from the other side preserves disjointness

An insertion disjoint from the other side preserves a linear split,
including the unused completed slots transported by structural congruence.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_insert_fresh`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#disjoint-insert-fresh).

## Restriction binding commutes with inserting an outer key

Inserting an outer endpoint before restriction is the same as
inserting its lifted key after the fresh dual pair has been bound.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind_insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#bind-insert).

## Inserting a left-absent key into a union updates the right part

Inserting a key absent from the left component updates only the right
component of a left-biased finite-map union.

Formalized by `Cslib.SessionTypes.Endpoint.Context.insert_union_right_of_fresh`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#insert-union-right-of-fresh).

## Context lifting commutes with erasing an owned key

Erasing an owned outer key commutes with canonical context lifting.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#lift-erase).

## Restriction binding commutes with erasing an owned outer key

Erasing an owned outer role commutes with restriction's fresh dual pair.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind_erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#bind-erase).

## Erasure distributes over union

Erasure distributes through the exact finite ownership union.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erase_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#erase-union).

## Erasing an absent key changes nothing

Erasing an absent key changes no ownership entry.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erase_of_notMem`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#erase-of-not-mem).

## Context lifting preserves a disjoint union

Canonical lifting preserves a disjoint ownership union exactly.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lift_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#lift-union).

## Binding a fresh pair keeps disjointness from a lifted context

A fresh bound pair belongs only to the left component of a lifted split.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_bind_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#disjoint-bind-lift).

## Restriction binding of a disjoint union

Scope extrusion keeps the dual pair on the restricted component and
lifts exactly the unrelated outer partner ownership.

Formalized by `Cslib.SessionTypes.Endpoint.Context.bind_union`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#bind-union).

## Reinserting an owned capability changes nothing

Reinstalling exactly an already-owned capability changes no entry.

Formalized by `Cslib.SessionTypes.Endpoint.Context.insert_of_lookup`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#insert-of-lookup).

## Insertion after erasing the same key

Reinstalling a key overrides any previous entry, so prior erasure of
that same key is immaterial.

Formalized by `Cslib.SessionTypes.Endpoint.Context.insert_erase_same`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#insert-erase-same).

## Erasure after inserting the same key

Erasing an inserted key removes its entry, independently of its value.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erase_insert_same`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#erase-insert-same).

## Reinstalling the bound pair after erasing its slots

Reinstalling the bound pair after removing its old slots restores the
same exact map as installing that pair directly.

Formalized by `Cslib.SessionTypes.Endpoint.Context.restore_erased_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#restore-erased-pair).

## Erasing the bound pair leaves the lifted context

Removing the two freshly bound roles exposes exactly the lifted
external context, including every unrelated completed resource.

Formalized by `Cslib.SessionTypes.Endpoint.Context.erase_bind_pair`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Languages/SessionTypes/Endpoint/ContextAlgebra.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html#erase-bind-pair).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite ownership algebra for typing transport](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-algebra-for-typing-transport)
