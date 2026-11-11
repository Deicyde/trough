---
declaration: section
origin: cited
lean: Cslib.SessionTypes.Endpoint.FiniteLinear, Cslib.SessionTypes.Endpoint.finiteLinear_lift, Cslib.SessionTypes.Endpoint.finiteLinear_swap, Cslib.SessionTypes.Endpoint.finiteLinear_cong, Cslib.SessionTypes.Endpoint.finiteLinear_subst, Cslib.SessionTypes.Endpoint.finiteLinear_select_eq, Cslib.SessionTypes.Endpoint.finiteLinear_step
statement: formalized
proof: formalized
---

# Finite linear π fragment and structural closure

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html).

## Finite linear π fragment without choice or replication

Existing π terms without choice or replication, including their bodies.

Formalized by `Cslib.SessionTypes.Endpoint.FiniteLinear`, a definition declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear).

## Lifting preserves and reflects the finite linear fragment

Lifting cannot add or remove unsupported process constructors.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_lift`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-lift).

## Restriction swap preserves and reflects the finite linear fragment

Swapping restrictions cannot add or remove choice or replication.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_swap`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-swap).

## Structural congruence preserves the finite linear fragment

All existing structural congruences preserve the finite linear
fragment. In particular, folding replication cannot introduce it.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_cong`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-cong).

## Substitution preserves and reflects the finite linear fragment

Substitution changes names, not the finite fragment's process shape.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_subst`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-subst).

## Selection is trivial on the choice-free fragment

Selection cannot discard a branch of a term in the choice-free fragment.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_select_eq`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-select-eq).

## Reduction preserves the finite linear fragment

All existing π reduction constructors preserve the finite fragment,
including arbitrary pre/post structural congruence and selection.

Formalized by `Cslib.SessionTypes.Endpoint.finiteLinear_step`, a theorem declared in [CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Languages/SessionTypes/Endpoint/Fragment.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html#finite-linear-step).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite linear π fragment and structural closure](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/process-calculi/session-types/linear-endpoint-typing-for-the-calculus/finite-linear-fragment-and-structural-closure)
