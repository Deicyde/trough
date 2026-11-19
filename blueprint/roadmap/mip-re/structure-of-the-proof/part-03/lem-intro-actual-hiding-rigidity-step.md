---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.mirror_retained_distance_le, MIPRE.Introspection.conditional_coarse_ideal_replacement_retained, MIPRE.Introspection.Honest.hideCoarseOp_transpose, MIPRE.Introspection.Honest.hideCoarseOp_epr_mirror, MIPRE.Introspection.Honest.hideNextRetain_mapped, MIPRE.Introspection.Honest.hideCoarseOp_step_of_normalizer, MIPRE.Introspection.Honest.hideCoarseOp_registerState_mirror, MIPRE.Introspection.Honest.hidingPrefixOp_registerState_mirror, MIPRE.Introspection.Honest.hideCoarseOp_aux_step_of_normalizer, MIPRE.Introspection.TypedEstimates.hiding_next_seed_rigidity, MIPRE.Introspection.TypedEstimates.hiding_next_register_rigidity
statement: formalized
proof: formalized
---

# An actual adjacent hiding rigidity step

On an extracted EPR seed register tensored with any normalized auxiliary state, let the actual parsed projective strategy fail with probability at most $\varepsilon$. Suppose its preceding Alice hiding coarse measurement has cross-party squared error at most $\varepsilon_f$ from the ideal, and its Bob Introspect prefix has squared error at most $\delta$ from the ideal prefix. Then the next Bob hiding coarse measurement has cross-party squared error at most

$$
(6+48(\ell-j+1)^2)|E|\varepsilon+6\delta+3\varepsilon_f.
$$

The conclusion concerns the actual complete parsed measurement, including malformed outcomes. No conditional estimate, ideal commutation, mirror or next-level rigidity hypothesis is assumed. Lemma [Full hiding rigidity](lem-hide-rigidity.md) below supplies the base, prefix estimates and iteration from the primitive extracted Pauli guarantees. The later product-strategy induction is separate.

## Depends on

- [The concrete ideal hiding step](lem-intro-concrete-ideal-step.md)
- [The actual later normalizer from the prefix chain](lem-intro-actual-normalizer-prefix.md)
- [Dimension-independent conditional normalizer replacement](lem-intro-conditional-normalizer.md)

## Proof depends on

- [The register model](../../downstream-results/part-03/lem-register-model.md)
- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

Prove transpose invariance of the adaptive honest operators and their exact EPR mirrors, then tensor with the arbitrary auxiliary state. Apply the actual conditional normalizer estimate and the actual prefix-chain bound. Transfer the paired ideal to the other party before coarse-graining cross-party consistency. The retained map on parsed answers and the concrete ideal product identity identify both sides with the next fine hiding families.

## Lean

Formalized as [`MIPRE.Introspection.mirror_retained_distance_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.mirror_retained_distance_le), [`MIPRE.Introspection.conditional_coarse_ideal_replacement_retained`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_coarse_ideal_replacement_retained), [`MIPRE.Introspection.Honest.hideCoarseOp_transpose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_transpose), [`MIPRE.Introspection.Honest.hideCoarseOp_epr_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_epr_mirror), [`MIPRE.Introspection.Honest.hideNextRetain_mapped`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideNextRetain_mapped), [`MIPRE.Introspection.Honest.hideCoarseOp_step_of_normalizer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_step_of_normalizer), [`MIPRE.Introspection.Honest.hideCoarseOp_registerState_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_registerState_mirror), [`MIPRE.Introspection.Honest.hidingPrefixOp_registerState_mirror`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hidingPrefixOp_registerState_mirror), [`MIPRE.Introspection.Honest.hideCoarseOp_aux_step_of_normalizer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.Honest.hideCoarseOp_aux_step_of_normalizer), [`MIPRE.Introspection.TypedEstimates.hiding_next_seed_rigidity`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_seed_rigidity), [`MIPRE.Introspection.TypedEstimates.hiding_next_register_rigidity`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.hiding_next_register_rigidity).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2334](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2334)
