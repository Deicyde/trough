---
declaration: lemma
origin: cited
lean: MIPRE.CL.Graph.presentation, MIPRE.CL.Graph.presentation_exactlyOn, MIPRE.CL.Graph.presentation_eval, MIPRE.CL.Graph.localValid_output_iff, MIPRE.CL.Graph.localValid_both_iff, MIPRE.CL.Graph.card_validSeeds, MIPRE.CL.Graph.mem_validSeeds_iff, MIPRE.CL.Graph.invalid_seed_locally_detected, MIPRE.CL.Graph.opposite_output_zero_of_invalid, MIPRE.CL.Graph.card_seeds, MIPRE.CL.Graph.validProbability_eq, MIPRE.CL.Graph.inv_pow_le_validProbability, MIPRE.CL.Graph.conditional_average
statement: formalized
proof: formalized
---

# Graph rejection sampling

Put $t=|T|$. Two independent $2t$-bit blocks encode a vertex indicator and its neighbor indicator. A two-level CL graph sampler has a valid-edge event $E_G$ with $p=\Pr(E_G)=(2m_G-k_G)/16^t\geq16^{-t}>0$. Each ordered adjacent pair has exactly one seed preimage; conditionally on $E_G$ the types have the specified graph law, with loops counted once. On its support, an invalid edge exposes a zero opposite-neighbor block to at least one player, enabling a trivial local measurement on that branch.

## Depends on

- [Structure of a CL function](lem-cl-structure.md)

## Proof

The first CL factor reads the player's two indicator blocks. The second factor is the whole complementary pair of blocks, with a linear map keeping only the opposite neighbor bit selected by a successful first-block decode. The one-hot indicator makes vertex encodings injective. Thus each ordered edge has exactly one valid seed, out of $16^{|T|}$ seeds. Reindexing the valid-seed sum by ordered edges proves the conditional law. The sampled question preserves the own block and the selected bit; a failed local validity test has zero opposite block. This proves the semantic sampler and its law. The ambient program is the separate obligation of Lemma [Implementing the detyped sampler](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L633).

## Lean

Formalized as [`MIPRE.CL.Graph.presentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.presentation), [`MIPRE.CL.Graph.presentation_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.presentation_exactlyOn), [`MIPRE.CL.Graph.presentation_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.presentation_eval), [`MIPRE.CL.Graph.localValid_output_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.localValid_output_iff), [`MIPRE.CL.Graph.localValid_both_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.localValid_both_iff), [`MIPRE.CL.Graph.card_validSeeds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.card_validSeeds), [`MIPRE.CL.Graph.mem_validSeeds_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.mem_validSeeds_iff), [`MIPRE.CL.Graph.invalid_seed_locally_detected`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.invalid_seed_locally_detected), [`MIPRE.CL.Graph.opposite_output_zero_of_invalid`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.opposite_output_zero_of_invalid), [`MIPRE.CL.Graph.card_seeds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.card_seeds), [`MIPRE.CL.Graph.validProbability_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.validProbability_eq), [`MIPRE.CL.Graph.inv_pow_le_validProbability`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.inv_pow_le_validProbability), [`MIPRE.CL.Graph.conditional_average`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Graph.conditional_average).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 402](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L402)
