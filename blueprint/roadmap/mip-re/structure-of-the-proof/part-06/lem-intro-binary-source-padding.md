---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.SourcePadding.family_supported, MIPRE.Introspection.SourcePadding.depthFamily_exactlyOn, MIPRE.Introspection.SourcePadding.depthFamily_eval, MIPRE.Introspection.SourcePadding.strategy_isPCC, MIPRE.Introspection.SourcePadding.strategy_value, MIPRE.Introspection.SourcePadding.average_pull, MIPRE.Introspection.SourcePadding.restrictStrategy_value, MIPRE.Introspection.SourcePadding.exists_projStrat_value_ge, MIPRE.Introspection.SourcePadding.quantumValue_le, MIPRE.Introspection.SourcePadding.quantumValue_depthFamily_le, MIPRE.Introspection.BinaryComplete.paddingEmbedding_number, MIPRE.Introspection.BinaryComplete.card_seed, MIPRE.Introspection.BinaryComplete.exists_padded_perfectPCC, MIPRE.Introspection.BinaryComplete.exists_depthPadded_perfectPCC
statement: formalized
proof: formalized
---

# Arbitrary binary source registers and exact padding

For $s\leq2^m t$, explicitly embed an arbitrary $s$-bit source register into the Pauli qubit register. Padding preserves perfect PCC play and source dimension. Every projective strategy for the padded source game, in any bipartite model, restricts to one of the original source game in the same model with exactly the same value; so the padded game's value is at most the original's in every value model approached by the projective strategies of the models it dominates, $\mathrm{val}^*$ and ${\omega^{\mathrm{co}}}$ among them. For positive depth and exact original partitions, unused coordinates can be consumed by a zero component of the first factor without changing depth or evaluation. The resulting full typed game has a perfect PCC strategy of dimension $2^{2^m t+1}D$.

## Depends on

- [Concrete completeness for the full typed introspection game](../part-05/lem-intro-full-typed-completeness.md)
- [Conditionally linear function](../part-01/def-cl-function.md)
- [Domination of the POVM strategies, and approximation by projective strategies](../../downstream-results/part-03/def-povm-domination.md)

## Proof

Number the Boolean cube and basis-bit coordinates explicitly. Pull source questions along the embedding and retain the original measurement rule. Positive padded question mass has a common source seed, proving PCC and perfect acceptance. Split a uniform padded seed into its original and unused coordinates to prove exact value preservation for arbitrary strategies. A direct sum with a zero map on the complement consumes every unused coordinate while preserving the CL evaluation. Apply the full binary completeness construction.

## Lean

Formalized as [`MIPRE.Introspection.SourcePadding.family_supported`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.family_supported), [`MIPRE.Introspection.SourcePadding.depthFamily_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.depthFamily_exactlyOn), [`MIPRE.Introspection.SourcePadding.depthFamily_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.depthFamily_eval), [`MIPRE.Introspection.SourcePadding.strategy_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.strategy_isPCC), [`MIPRE.Introspection.SourcePadding.strategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.strategy_value), [`MIPRE.Introspection.SourcePadding.average_pull`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.average_pull), [`MIPRE.Introspection.SourcePadding.restrictStrategy_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.restrictStrategy_value), [`MIPRE.Introspection.SourcePadding.exists_projStrat_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.exists_projStrat_value_ge), [`MIPRE.Introspection.SourcePadding.quantumValue_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.quantumValue_le), [`MIPRE.Introspection.SourcePadding.quantumValue_depthFamily_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SourcePadding.quantumValue_depthFamily_le), [`MIPRE.Introspection.BinaryComplete.paddingEmbedding_number`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.paddingEmbedding_number), [`MIPRE.Introspection.BinaryComplete.card_seed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.card_seed), [`MIPRE.Introspection.BinaryComplete.exists_padded_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.exists_padded_perfectPCC), [`MIPRE.Introspection.BinaryComplete.exists_depthPadded_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.BinaryComplete.exists_depthPadded_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3760](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3760)
