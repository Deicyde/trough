---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.DecisionCompiler.resources_with_cutoff, MIPRE.Introspection.DecisionCompiler.raw_accepts_iff, MIPRE.Introspection.DecisionCompiler.output_hasPerfectPCC_of_raw, MIPRE.Introspection.DecisionCompiler.exists_raw_failure_le, MIPRE.Introspection.DecisionCompiler.val_reference, MIPRE.Introspection.DecisionCompiler.output_val_cutoff, MIPRE.Introspection.DecisionCompiler.output_val_eq_reference, MIPRE.Introspection.CanonicalDecoded.value_le, MIPRE.Introspection.CanonicalDecoded.supported_A, MIPRE.Introspection.CanonicalDecoded.supported_B
statement: formalized
proof: formalized
---

# The ambient compiler's resources and raw-game bridge

The compiled five-level verifier satisfies the ambient resource contract on every program input and index, including the output-description and answer-cutoff bounds. At positive indices its actual acceptance is the canonical raw kernel. Finite graph detyping transfers raw perfect PCC completeness outward and transfers high output value inward with the fixed graph loss. Total finite answer decoding then increases value and enforces the full Pauli support required by QLD soundness. The value identities hold in every value model (Definition [Value models](../../downstream-results/part-01/def-value-model.md)); the restriction to the cutoff, the detyping transport and the decoding hold for projective strategies in any bipartite model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)).

## Depends on

- [The canonical sampler at every index](lem-intro-canonical-sampler.md)
- [Executable quotient hiding and the finite decision kernel](lem-intro-quotient-kernel.md)
- [The executable five-level introspection sampler](../part-02/lem-intro-executable-sampler.md)

## Proof depends on

- [Detyping PCC completeness](../part-01/lem-detype-completeness.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Proof

Prepare the shared clock and canonical resources once, clamp source descriptions, and route every source call through the same bounded simulation interface. Combine the all-index sampler, decider and cutoff estimates into one budget exponent. Restrict to the enforced finite answer cutoff, apply the graph-detyping transport, and merge each question's answer fibers under the finite decoder. Its range gives the Pauli support directly.

## Lean

Formalized as [`MIPRE.Introspection.DecisionCompiler.resources_with_cutoff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.resources_with_cutoff), [`MIPRE.Introspection.DecisionCompiler.raw_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.raw_accepts_iff), [`MIPRE.Introspection.DecisionCompiler.output_hasPerfectPCC_of_raw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.output_hasPerfectPCC_of_raw), [`MIPRE.Introspection.DecisionCompiler.exists_raw_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.exists_raw_failure_le), [`MIPRE.Introspection.DecisionCompiler.val_reference`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.val_reference), [`MIPRE.Introspection.DecisionCompiler.output_val_cutoff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.output_val_cutoff), [`MIPRE.Introspection.DecisionCompiler.output_val_eq_reference`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.output_val_eq_reference), [`MIPRE.Introspection.CanonicalDecoded.value_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CanonicalDecoded.value_le), [`MIPRE.Introspection.CanonicalDecoded.supported_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CanonicalDecoded.supported_A), [`MIPRE.Introspection.CanonicalDecoded.supported_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.CanonicalDecoded.supported_B).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3926](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3926)
