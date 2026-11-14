---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.sum_pvm_snorm_sq, MIPRE.Introspection.sum_pvm_difference_snorm_sq_le, MIPRE.Introspection.sum_stateSqNorm_state_transfer_le, MIPRE.Introspection.sum_bob_snorm_state_transfer_le, MIPRE.Introspection.extractedSoundnessCoefficient_one_le, MIPRE.Introspection.extractedSoundness_power_bound, MIPRE.Introspection.exists_extractedSoundness_errorProfile, MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_extracted_state
statement: formalized
proof: formalized
---

# Soundness on the approximately extracted state

The preceding soundness theorem also applies when the primitive X/Z guarantees hold on a normalized state at squared distance at most $t$ from the ideal EPR-register state. If those errors and actual game failure are at most $t\geq0$, the original-game loss is at most $20C t^{2^{-(6\ell+1)}}$. The constants again admit the paper's two-term profile uniformly in the register dimension.

## Depends on

- [Finite-game soundness from the primitive Pauli guarantees](lem-intro-primitive-soundness.md)
- [Quantitative measurement and state replacement](../part-04/lem-intro-value-stability.md)

## Proof

For two PVMs the summed squared difference on a nearby state is bounded by twice its old value plus eight times the squared vector distance. Projective normalization sums over all outcomes before estimating, so there is no answer-cardinality factor. Transfer game failure using value stability. For $t\leq1$, all three inputs are at most $20\sqrt t$; apply the primitive soundness theorem and absorb this extra root. For $t>1$ the bound follows from nonnegative quantum value.

## Lean

Formalized as [`MIPRE.Introspection.sum_pvm_snorm_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_pvm_snorm_sq), [`MIPRE.Introspection.sum_pvm_difference_snorm_sq_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_pvm_difference_snorm_sq_le), [`MIPRE.Introspection.sum_stateSqNorm_state_transfer_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_stateSqNorm_state_transfer_le), [`MIPRE.Introspection.sum_bob_snorm_state_transfer_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.sum_bob_snorm_state_transfer_le), [`MIPRE.Introspection.extractedSoundnessCoefficient_one_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.extractedSoundnessCoefficient_one_le), [`MIPRE.Introspection.extractedSoundness_power_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.extractedSoundness_power_bound), [`MIPRE.Introspection.exists_extractedSoundness_errorProfile`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_extractedSoundness_errorProfile), [`MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_extracted_state`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_extracted_state).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3176](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3176)
