---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.Honest.parsedCoreOp_isPVM, MIPRE.Introspection.Honest.parsedReadOp_isPVM, MIPRE.Introspection.Honest.parsedHideOp_isPVM, MIPRE.Introspection.Honest.parsedCore_read_commute, MIPRE.Introspection.Honest.parsedRead_core_commute, MIPRE.Introspection.Honest.parsedCore_read_reject_zero, MIPRE.Introspection.Honest.parsedRead_core_reject_zero, MIPRE.Introspection.Honest.parsedHide_next_commute, MIPRE.Introspection.Honest.parsedHide_next_commute_reversed, MIPRE.Introspection.Honest.parsedHide_read_commute, MIPRE.Introspection.Honest.parsedRead_hide_commute, MIPRE.Introspection.Honest.parsedHide_next_reject_zero, MIPRE.Introspection.Honest.parsedHide_next_reject_zero_reversed, MIPRE.Introspection.Honest.parsedHide_read_reject_zero, MIPRE.Introspection.Honest.parsedRead_hide_reject_zero
statement: formalized
proof: formalized
---

# Honest operators on the complete parsed alphabet

The actual core, full Read, and Hide measurements extend to PVMs on the common parsed-answer alphabet, acting on one register/source space. Wrong constructors have zero effect. In both orientations of the Introspect/Read edge, every pair of effects commutes and every rejected answer pair has zero product. The same all-constructor guarantees hold in both orientations of every adjacent Hide edge and the terminal Hide/Read edge, with their actual index conditions and parsed verifier predicates.

## Depends on

- [Adaptive honest Read and Hide measurements](lem-intro-honest-adaptive.md)
- [Honest hiding marginals and edge compatibility](lem-intro-honest-hiding.md)
- [The parsed introspection decision predicate](../part-02/lem-intro-parsed-predicate.md)

## Proof

Embed the proper pair, Read, or Hide labels and extend by zero. For Hide, tensor the adaptive register PVM with the identity on the source register. Summing over all constructors recovers the original PVM normalization. Constructor case analysis reduces the reading edge to its exact refinement identity; all other products vanish. For hiding edges, identify the parsed check exactly with the corresponding CL relation and apply the honest hiding product theorem. Tensoring with the source identity preserves both commutation and rejected-product vanishing.

## Lean

Formalized as [`MIPRE.Introspection.Honest.parsedCoreOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedCoreOp_isPVM), [`MIPRE.Introspection.Honest.parsedReadOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedReadOp_isPVM), [`MIPRE.Introspection.Honest.parsedHideOp_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHideOp_isPVM), [`MIPRE.Introspection.Honest.parsedCore_read_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedCore_read_commute), [`MIPRE.Introspection.Honest.parsedRead_core_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedRead_core_commute), [`MIPRE.Introspection.Honest.parsedCore_read_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedCore_read_reject_zero), [`MIPRE.Introspection.Honest.parsedRead_core_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedRead_core_reject_zero), [`MIPRE.Introspection.Honest.parsedHide_next_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_next_commute), [`MIPRE.Introspection.Honest.parsedHide_next_commute_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_next_commute_reversed), [`MIPRE.Introspection.Honest.parsedHide_read_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_read_commute), [`MIPRE.Introspection.Honest.parsedRead_hide_commute`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedRead_hide_commute), [`MIPRE.Introspection.Honest.parsedHide_next_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_next_reject_zero), [`MIPRE.Introspection.Honest.parsedHide_next_reject_zero_reversed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_next_reject_zero_reversed), [`MIPRE.Introspection.Honest.parsedHide_read_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedHide_read_reject_zero), [`MIPRE.Introspection.Honest.parsedRead_hide_reject_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.parsedRead_hide_reject_zero).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2074](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2074)
