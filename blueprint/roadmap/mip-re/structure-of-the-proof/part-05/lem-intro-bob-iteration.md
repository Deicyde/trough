---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedPresentation.mu_swap, MIPRE.Introspection.TypedEstimates.parsedGame_transpose, MIPRE.Introspection.TypedEstimates.swap_reg_bornProb, MIPRE.Introspection.TypedEstimates.swap_reg_povmValue, MIPRE.Introspection.TypedEstimates.swap_reg_stateSqNorm, MIPRE.Introspection.TypedEstimates.swap_reg_swap_stateSqNorm, MIPRE.Introspection.TypedEstimates.swap_reg_xSqNorm, MIPRE.Introspection.TypedEstimates.parsedGame_value_swap, MIPRE.Introspection.TypedEstimates.introBobZError_swap, MIPRE.Introspection.TypedEstimates.introAliceZError_swap, MIPRE.Introspection.TypedEstimates.hidingAliceError_swap, MIPRE.Introspection.TypedEstimates.hidingBobError_swap, MIPRE.Introspection.TypedEstimates.exists_intro_bob_iteration
statement: formalized
proof: formalized
---

# Player exchange and the actual Bob iteration

Exchanging the players in the actual parsed game preserves its value after transposing the Pauli predicate. No symmetry of that predicate is required. The finite Alice construction therefore gives an actual Bob construction, with its prefix invariant, projectivity, untouched questions, and the same failure recurrence. The primitive errors required by the second player are preserved by the first player's ancillary extension. The Lean exchanges the players by swapping the model, whose register model is the swapped register model along a local isometry with identity homomorphisms (Definition [The register model](../../downstream-results/part-03/def-register-model.md)), so the value and every primitive and hiding error move across with no loss, and the Bob iteration is the Alice iteration in the swapped model, returning a model that reduces to the original one (Definition [Reduction of POVM strategies](../../downstream-results/part-03/def-povm-reduction.md)).

## Depends on

- [Finite iteration of the actual Alice strategy](lem-intro-actual-iteration.md)

## Proof

Swap the ordered type edge and the two seed coordinates. Check the actual directed predicates and transport the register state and state distances. Apply the proved Alice construction to the exchanged game and swap back.

## Lean

Formalized as [`MIPRE.Introspection.TypedPresentation.mu_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.mu_swap), [`MIPRE.Introspection.TypedEstimates.parsedGame_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.parsedGame_transpose), [`MIPRE.Introspection.TypedEstimates.swap_reg_bornProb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.swap_reg_bornProb), [`MIPRE.Introspection.TypedEstimates.swap_reg_povmValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.swap_reg_povmValue), [`MIPRE.Introspection.TypedEstimates.swap_reg_stateSqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.swap_reg_stateSqNorm), [`MIPRE.Introspection.TypedEstimates.swap_reg_swap_stateSqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.swap_reg_swap_stateSqNorm), [`MIPRE.Introspection.TypedEstimates.swap_reg_xSqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.swap_reg_xSqNorm), [`MIPRE.Introspection.TypedEstimates.parsedGame_value_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.parsedGame_value_swap), [`MIPRE.Introspection.TypedEstimates.introBobZError_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introBobZError_swap), [`MIPRE.Introspection.TypedEstimates.introAliceZError_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introAliceZError_swap), [`MIPRE.Introspection.TypedEstimates.hidingAliceError_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingAliceError_swap), [`MIPRE.Introspection.TypedEstimates.hidingBobError_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hidingBobError_swap), [`MIPRE.Introspection.TypedEstimates.exists_intro_bob_iteration`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.exists_intro_bob_iteration).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3031](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3031)
