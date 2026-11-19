---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.CLChecks.residual_supported, MIPRE.Introspection.CLChecks.residual_exactlyOn, MIPRE.Introspection.CLChecks.stageFactor_subset_residual, MIPRE.Introspection.CLChecks.residualRegister_step, MIPRE.Introspection.CLChecks.dualReadout_stageLinear, MIPRE.Introspection.prefixWeight_eq_card, MIPRE.Introspection.prefixWeight_pos_iff, MIPRE.Introspection.sum_prefixWeight_supported, MIPRE.Introspection.hidingPrefixOp_registerState_weight, MIPRE.Introspection.prefixResidual_distance_sum, MIPRE.Introspection.prefixResidual_commutator_sum
statement: formalized
proof: formalized
---

# Actual adaptive prefix law and residual registers

The actual CL continuation acts only on the complement of the visited registers. Its next factor and linear map are computed from the original presentation. The prefix weights are the uniform seed fibre probabilities, agree with the Born law on the EPR register with arbitrary normalized auxiliary state, and sum to one. Full-carrier distances and commutators are exactly the weighted residual errors; impossible prefixes have weight zero.

## Depends on

- [Conditioning on part of a question](../part-02/lem-conditional-measurement.md)
- [Full hiding rigidity](../part-03/lem-hide-rigidity.md)

## Proof

Split the actual visited coordinates from their complement. Factor the diagonal prefix projector by fibre locality, evaluate its EPR mass, and apply the tensor squared-norm identity. The continuation support follows by recursion on the CL presentation.

## Lean

Formalized as [`MIPRE.Introspection.CLChecks.residual_supported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.residual_supported), [`MIPRE.Introspection.CLChecks.residual_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.residual_exactlyOn), [`MIPRE.Introspection.CLChecks.stageFactor_subset_residual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.stageFactor_subset_residual), [`MIPRE.Introspection.CLChecks.residualRegister_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.residualRegister_step), [`MIPRE.Introspection.CLChecks.dualReadout_stageLinear`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CLChecks.dualReadout_stageLinear), [`MIPRE.Introspection.prefixWeight_eq_card`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixWeight_eq_card), [`MIPRE.Introspection.prefixWeight_pos_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixWeight_pos_iff), [`MIPRE.Introspection.sum_prefixWeight_supported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_prefixWeight_supported), [`MIPRE.Introspection.hidingPrefixOp_registerState_weight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.hidingPrefixOp_registerState_weight), [`MIPRE.Introspection.prefixResidual_distance_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_distance_sum), [`MIPRE.Introspection.prefixResidual_commutator_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.prefixResidual_commutator_sum).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2641](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2641)
