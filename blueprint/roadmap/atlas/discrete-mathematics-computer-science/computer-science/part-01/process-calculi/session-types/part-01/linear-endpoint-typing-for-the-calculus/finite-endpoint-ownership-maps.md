---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Capability, Cslib.SessionTypes.Endpoint.Context, Cslib.SessionTypes.Endpoint.Capability.dual, Cslib.SessionTypes.Endpoint.Capability.dual_dual, Cslib.SessionTypes.Endpoint.Context.rekey, Cslib.SessionTypes.Endpoint.Context.mem_rekey, Cslib.SessionTypes.Endpoint.Context.lookup_rekey, Cslib.SessionTypes.Endpoint.Context.disjoint_rekey
statement: formalized
proof: formalized
---

# Finite endpoint ownership maps

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html).

## Endpoint capability with a dependency rank

One linear protocol obligation with its dependency rank.

Formalized by `Cslib.SessionTypes.Endpoint.Capability`, a structure declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#capability).

## Finite endpoint ownership map

Finite ownership map, indexed by polarized keys rather than names.

Formalized by `Cslib.SessionTypes.Endpoint.Context`, an abbreviation declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#context).

## Dual of an endpoint capability

The peer's obligation has the same rank and dual subject protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.dual`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#dual).

## Capability duality is an involution

Capability duality does not change rank or lose protocol information.

Formalized by `Cslib.SessionTypes.Endpoint.Capability.dual_dual`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#dual-dual).

## Collision-free rekeying of an ownership map

Rekey a finite map when no two owned keys are merged. Global
injectivity is unnecessary, which matters for endpoint substitution.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#rekey).

## Keys of a rekeyed ownership map

Rekeying has precisely the image of the original owned keys.

Formalized by `Cslib.SessionTypes.Endpoint.Context.mem_rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#mem-rekey).

## Lookups in a rekeyed ownership map

Rekeying preserves each capability verbatim at its image key.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#lookup-rekey).

## Injective rekeying preserves disjoint ownership

Disjoint ownership remains disjoint when the combined owned domain
is rekeyed injectively. Opposite roles are not collapsed to physical names.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#disjoint-rekey).

## Uniqueness of capability lookups

Two lookups of the same linear key cannot give different capabilities.

Formalized by `Cslib.SessionTypes.Endpoint.Context.unique`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#unique).

## Completed ownership map

A context has no remaining communication obligation. End capabilities
may still be recorded, but an active protocol is never silently discarded.

Formalized by `Cslib.SessionTypes.Endpoint.Context.Completed`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#completed).

## The empty ownership map is completed

The empty ownership map is completed.

Formalized by `Cslib.SessionTypes.Endpoint.Context.completed_empty`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#completed-empty).

## Composition of collision-free rekeyings

Consecutive collision-free rekeyings compose on the same finite map.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#rekey-rekey).

## Identity rekeying fixes an ownership map

Identity rekeying retains the exact finite map, including end slots.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_id`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#rekey-id).

## Rekeying that fixes every owned key fixes the map

Rekeying that fixes all owned keys retains the exact map.

Formalized by `Cslib.SessionTypes.Endpoint.Context.rekey_eq`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#rekey-eq).

## Rekeying preserves completion

Completed protocols remain completed under collision-free name transport.

Formalized by `Cslib.SessionTypes.Endpoint.Context.Completed.rekey`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#rekey-2).

## Inserting a completed capability preserves completion

Recording a completed endpoint preserves completion of a finite map.

Formalized by `Cslib.SessionTypes.Endpoint.Context.Completed.insert`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#insert).

## Erasing a key preserves completion

Erasing a key preserves absence of any noncompleted obligation;
the empty map is not itself a completion claim about hidden ν processes.

Formalized by `Cslib.SessionTypes.Endpoint.Context.Completed.erase`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Context.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Context.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html#erase).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite endpoint ownership maps](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-endpoint-ownership-maps)
