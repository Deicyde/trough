---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.DeciderProgram.numbered_clDist, MIPRE.CL.Detyping.DeciderProgram.verifier_game_mu, MIPRE.CL.Detyping.DeciderProgram.toFinite_value, MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_failure_le, MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_value_ge, MIPRE.CL.Detyping.DeciderProgram.fromFiniteSync_isPCC, MIPRE.CL.Detyping.DeciderProgram.exists_ambientPerfectPCC
statement: formalized
proof: formalized
---

# Strategy transfer for the executable detyping verifier

The actual program-defined detyped verifier has exactly the finite detyping distribution and predicate under the explicit coordinate-numbering equivalence. Every strategy for it restricts to a typed-game strategy on the same state with failure at most $16^{|T|}$ times its failure. Conversely, a perfect PCC strategy for the typed game gives an actual ambient perfect PCC strategy with the same local dimension. Both sides use the outer answer alphabet and the typed predicate includes rejection beyond the source typed-answer cut; there is no implicit comparison of two different answer alphabets. The Lean restricts a projective strategy in a bipartite model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)), of which a tensor-product strategy is the case of its tensor-product model, to one in the same model.

## Depends on

- [Executable detyping decider with two answer cuts](lem-detype-executable-decider.md)
- [Finite-game detyping PCC completeness](lem-detype-game-completeness.md)
- [Finite-game detyping soundness](../part-02/lem-detype-game-soundness.md)

## Proof depends on

- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)
- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

Transport the common seed and questions along the register equivalence. Finite-sum reindexing proves the distribution identity and exact strategy value preservation. Apply finite-game restriction and completeness, then transport the resulting strategies, including the doubling tags and PCC commutation clauses, to the actual verifier.

## Lean

Formalized as [`MIPRE.CL.Detyping.DeciderProgram.numbered_clDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.numbered_clDist), [`MIPRE.CL.Detyping.DeciderProgram.verifier_game_mu`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.verifier_game_mu), [`MIPRE.CL.Detyping.DeciderProgram.toFinite_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.toFinite_value), [`MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_failure_le), [`MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.restrictAmbient_value_ge), [`MIPRE.CL.Detyping.DeciderProgram.fromFiniteSync_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.fromFiniteSync_isPCC), [`MIPRE.CL.Detyping.DeciderProgram.exists_ambientPerfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.DeciderProgram.exists_ambientPerfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 683](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L683)
