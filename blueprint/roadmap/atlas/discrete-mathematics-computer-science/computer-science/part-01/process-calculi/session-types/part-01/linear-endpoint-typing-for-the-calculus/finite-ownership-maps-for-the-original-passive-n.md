---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.Context.ofFinite, Cslib.SessionTypes.Endpoint.Context.lookup_ofFinite, Cslib.SessionTypes.Endpoint.Context.mem_ofFinite, Cslib.SessionTypes.Endpoint.Context.ofFinite_advance, Cslib.SessionTypes.Endpoint.Context.disjoint_ofFinite, Cslib.SessionTypes.Endpoint.Context.completed_ofFinite
statement: formalized
proof: formalized
---

# Finite ownership maps for the original passive-name typing judgement

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html).

## Polarized ownership map of a finite channel context

Turn finitely many original channel slots into polarized finite-map
ownership. The supplied rank assignment adds no execution hypothesis.

Formalized by `Cslib.SessionTypes.Endpoint.Context.ofFinite`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#of-finite).

## Lookup in the finite-context ownership map

Exact lookup specification for the finite-resource bridge.

Formalized by `Cslib.SessionTypes.Endpoint.Context.lookup_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#lookup-of-finite).

## Keys of the finite-context ownership map

Finite bridge ownership has exactly the bounded constant keys.

Formalized by `Cslib.SessionTypes.Endpoint.Context.mem_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#mem-of-finite).

## Finite ownership map commutes with channel advancement

Advancing an original channel advances precisely its finite-map role.

Formalized by `Cslib.SessionTypes.Endpoint.Context.ofFinite_advance`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#of-finite-advance).

## Ownership maps for opposite roles are disjoint

Opposite finite roles split without duplicating any endpoint key.

Formalized by `Cslib.SessionTypes.Endpoint.Context.disjoint_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#disjoint-of-finite).

## Completed finite contexts give completed ownership maps

Original completed contexts have no active finite-map protocol.

Formalized by `Cslib.SessionTypes.Endpoint.Context.completed_ofFinite`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/FiniteContext.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html#completed-of-finite).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite ownership maps for the original passive-name typing judgement](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-ownership-maps-for-the-original-passive-n)
