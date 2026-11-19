---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.TypedEstimates.introAliceZError_le_of_bob, MIPRE.Introspection.primitiveBudgetCoefficient_bounds, MIPRE.Introspection.primitiveSoundnessCoefficient_one_le, MIPRE.Introspection.primitiveSoundness_power_bounds, MIPRE.Introspection.exists_primitiveSoundness_errorProfile, MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_pauli, MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_profile
statement: formalized
proof: formalized
---

# Finite-game soundness from the primitive Pauli guarantees

Suppose the actual parsed-game strategy is projective on an EPR register tensored with a normalized auxiliary state. Assume its failure and only the primitive Alice-X and Bob-Z squared errors are at most $t\geq0$. For a source CL presentation covering the whole register exactly, the original game's quantum value is at least $1-Ct^{2^{-6\ell}}$, for an explicit coefficient depending only on depth and type-graph size. There is no assumed hiding estimate, future strategy, or smallness condition. If $t$ has the paper's two-term profile, the conclusion has that profile with uniform adjusted constants. The Lean's EPR register tensored with a normalized auxiliary state is the register model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)) of a normalized auxiliary model, and it bounds the value of every value model dominating the POVM strategies of the auxiliary model (Definition [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)), of which the quantum value is the case of a tensor-product model.

## Depends on

- [Both actual terminal measurements](lem-intro-two-sided-iteration.md)
- [Ordinary-answer extraction from actual terminal invariants](lem-intro-terminal-option-extraction.md)
- [A power bound for the entire finite recurrence](lem-intro-recurrence-power.md)
- [Full hiding rigidity](../part-03/lem-hide-rigidity.md)

## Proof depends on

- [Domination and approximation in the two models](../../downstream-results/part-03/lem-povm-domination.md)

## Proof

The tested Pauli-Z loop transfers Bob's primitive estimate to Alice. Full hiding rigidity derives both required hiding families from the actual game and the original two primitive estimates. A fixed coefficient bounds all these inputs simultaneously. Apply the two-block construction and ordinary-answer extraction in the small-error regime. Outside it the same power bound is at least one, and quantum value is nonnegative. Absorb the fixed coefficients and roots into the required profile.

## Lean

Formalized as [`MIPRE.Introspection.TypedEstimates.introAliceZError_le_of_bob`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.introAliceZError_le_of_bob), [`MIPRE.Introspection.primitiveBudgetCoefficient_bounds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.primitiveBudgetCoefficient_bounds), [`MIPRE.Introspection.primitiveSoundnessCoefficient_one_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.primitiveSoundnessCoefficient_one_le), [`MIPRE.Introspection.primitiveSoundness_power_bounds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.primitiveSoundness_power_bounds), [`MIPRE.Introspection.exists_primitiveSoundness_errorProfile`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_primitiveSoundness_errorProfile), [`MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_pauli), [`MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_profile`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_primitive_profile).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3137](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3137)
