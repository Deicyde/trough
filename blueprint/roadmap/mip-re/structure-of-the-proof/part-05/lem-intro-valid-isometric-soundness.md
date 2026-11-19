---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.transportA_map_op, MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_isometric_images, MIPRE.Introspection.submeasurement_extension_mass, MIPRE.Introspection.submeasurement_extension_dist, MIPRE.Introspection.valid_outcome_error_le, MIPRE.Introspection.isometric_valid_outcome_alice_error_le, MIPRE.Introspection.isometric_valid_outcome_bob_error_le, MIPRE.Introspection.validSoundnessCoefficient_one_le, MIPRE.Introspection.exists_validSoundness_errorProfile, MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_valid_isometric_images
statement: formalized
proof: formalized
---

# Finite soundness from the valid-answer extraction interface

Suppose an actual projective parsed-game strategy has failure at most $t$, and supplied local isometries put its state within vector distance $t$ of the ideal register state. Suppose also that the image measurements have summed squared error at most $t$ on valid full-register Alice-X and Bob-Z answers. The original game has quantum value at least $1-C\,\mathrm{root}_{6\ell+2}(t)$, for an explicit coefficient depending only on depth and graph size. The estimate holds for every $t\geq0$ and retains all malformed answers and image-complement mass. The local isometries and their estimates are inputs here; Lemma [Pauli extraction for the introspection game](lem-intro-pauli-extraction.md) supplies them for the actual game from Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md). The final loss preserves the paper's two-term error profile with uniform constants and a positive exponent at most one. The Lean states it for a strategy in any bipartite model, with one local isometry of models (Definition [Local isometries of bipartite models](../../downstream-results/part-03/def-local-isometry.md)) into the register model of a normalized auxiliary model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)), and bounds the value of every value model dominating the POVM strategies of the auxiliary model (Definition [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)), of which the quantum value is the case of a tensor-product model.

## Depends on

- [Local-isometry transport and image-complement completion](lem-intro-isometric-strategy.md)
- [Finite-game soundness from the primitive Pauli guarantees](lem-intro-primitive-soundness.md)

## Proof depends on

- [Soundness on the approximately extracted state](lem-intro-extracted-state-soundness.md)

## Proof

A positive submeasurement within squared distance $\delta$ of a PVM has missing mass at most $2\sqrt\delta$. Extending it inside the identity therefore changes the error to at most $2\delta+4\sqrt\delta$. Apply this to the valid raw effects inside the complete coarse images, including their malformed outcome. Complete the local isometry images, preserve the actual embedded game value, and apply finite soundness. For $t\leq1$ the common input is at most $6\sqrt t$; for $t>1$ use nonnegative quantum value. No outcome-cardinality factor appears.

## Lean

Formalized as [`MIPRE.Introspection.transportA_map_op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.transportA_map_op), [`MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_isometric_images`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_isometric_images), [`MIPRE.Introspection.submeasurement_extension_mass`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_extension_mass), [`MIPRE.Introspection.submeasurement_extension_dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_extension_dist), [`MIPRE.Introspection.valid_outcome_error_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.valid_outcome_error_le), [`MIPRE.Introspection.isometric_valid_outcome_alice_error_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometric_valid_outcome_alice_error_le), [`MIPRE.Introspection.isometric_valid_outcome_bob_error_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.isometric_valid_outcome_bob_error_le), [`MIPRE.Introspection.validSoundnessCoefficient_one_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.validSoundnessCoefficient_one_le), [`MIPRE.Introspection.exists_validSoundness_errorProfile`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_validSoundness_errorProfile), [`MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_valid_isometric_images`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedEstimates.quantumValue_ge_of_valid_isometric_images).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3391](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3391)
