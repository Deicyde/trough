---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.graphRefinementPOVM_isPVM, MIPRE.Introspection.graphRefinementPOVM_recover, MIPRE.Introspection.stageAnswerRefinement_commutator, MIPRE.Introspection.stageAnswerDecode_prefix, MIPRE.Introspection.stageAnswerDecode_next, MIPRE.Introspection.stageAnswerRefinementPOVM_decode_recover, MIPRE.Introspection.canonicalizeIntro_isPVM, MIPRE.Introspection.TypedEstimates.canonicalizeIntro_value
statement: formalized
proof: formalized
---

# Refining and updating the actual Introspect answer

Adding the deterministically reported current coordinate to each full Introspect answer preserves projectivity and the total commutator errors exactly. The updating decoder overwrites the visited coordinates, reports the advanced prefix, and recovers the old measurement under its old-prefix support invariant. The malformed outcome remains explicit. Replacing all malformed raw Introspect constructors by one fixed malformed constructor preserves the actual parsed-game value and projectivity exactly.

## Depends on

- [Advancing the actual prefix label](lem-intro-adaptive-advance.md)
- [Projective reassembly across adaptive prefixes](lem-intro-adaptive-reassembly.md)

## Proof depends on

- [Adaptive extraction and common-ancilla projectivization](lem-intro-adaptive-extraction.md)

## Proof

Embed outcomes in the graph of the selected-coordinate function. All off-graph operators are zero. The decoder identities follow from the disjoint visited, current, and remaining coordinates. Every malformed Introspect answer is rejected by the actual predicate's format check.

## Lean

Formalized as [`MIPRE.Introspection.graphRefinementPOVM_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.graphRefinementPOVM_isPVM), [`MIPRE.Introspection.graphRefinementPOVM_recover`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.graphRefinementPOVM_recover), [`MIPRE.Introspection.stageAnswerRefinement_commutator`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerRefinement_commutator), [`MIPRE.Introspection.stageAnswerDecode_prefix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerDecode_prefix), [`MIPRE.Introspection.stageAnswerDecode_next`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerDecode_next), [`MIPRE.Introspection.stageAnswerRefinementPOVM_decode_recover`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stageAnswerRefinementPOVM_decode_recover), [`MIPRE.Introspection.canonicalizeIntro_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.canonicalizeIntro_isPVM), [`MIPRE.Introspection.TypedEstimates.canonicalizeIntro_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.canonicalizeIntro_value).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2795](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2795)
