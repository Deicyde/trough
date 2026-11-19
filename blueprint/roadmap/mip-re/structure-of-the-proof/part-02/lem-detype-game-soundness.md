---
declaration: lemma
origin: cited
lean: MIPRE.SampledGame.game, MIPRE.SampledGame.sum_dist_mul, MIPRE.SampledGame.one_sub_value, MIPRE.CL.Detyping.typedGame, MIPRE.CL.Detyping.game, MIPRE.CL.Detyping.game_mu_eq_clDist, MIPRE.CL.Detyping.view_disjoint, MIPRE.CL.Detyping.restrict, MIPRE.CL.Detyping.restrict_state, MIPRE.CL.Detyping.restrict_failAt, MIPRE.CL.Detyping.valid_average_le, MIPRE.CL.Detyping.restrict_failure_eq, MIPRE.CL.Detyping.restrict_failure_le, MIPRE.CL.Detyping.restrict_value_ge
statement: formalized
proof: formalized
---

# Finite-game detyping soundness

Fix positive-level typed CL presentations, a symmetric type graph with at least one edge, finite answer alphabets, and a decision predicate. Construct the typed finite game by sampling a uniform ordered edge and a common seed. Construct the detyped finite game using the detyped presentations and the same answer alphabets, accepting outside valid edge views. Any strategy $S$ for the latter restricts to a strategy $S'$ for the former on literally the same state and local dimensions, with

$$
1-\mathrm{val}(S')\leq16^{|T|}(1-\mathrm{val}(S)).
$$

The finite detyped game's distribution equals the CL distribution of the constructed presentations. The two families of fixed player views are disjoint.

## Depends on

- [Detyped conditionally linear functions](../part-01/lem-detype-cl.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Proof depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Restrict the measurements to the fixed graph view of each typed question. On every ordered edge the decision predicate and conditional failure probability agree. The typed failure is therefore exactly the detyped failure conditioned on valid graph seeds. Nonnegativity lets us bound this subsum by the whole failure sum; there is at least one ordered edge among $16^{|T|}$ graph seeds. This proves the stated bound and its near-perfect value form. This finite-game result does not yet implement the machine wrapper's answer cutoff, truncation, or runtime.

## Lean

Formalized as [`MIPRE.SampledGame.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SampledGame.game), [`MIPRE.SampledGame.sum_dist_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SampledGame.sum_dist_mul), [`MIPRE.SampledGame.one_sub_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SampledGame.one_sub_value), [`MIPRE.CL.Detyping.typedGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.typedGame), [`MIPRE.CL.Detyping.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.game), [`MIPRE.CL.Detyping.game_mu_eq_clDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.game_mu_eq_clDist), [`MIPRE.CL.Detyping.view_disjoint`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.view_disjoint), [`MIPRE.CL.Detyping.restrict`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict), [`MIPRE.CL.Detyping.restrict_state`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_state), [`MIPRE.CL.Detyping.restrict_failAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_failAt), [`MIPRE.CL.Detyping.valid_average_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.valid_average_le), [`MIPRE.CL.Detyping.restrict_failure_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_failure_eq), [`MIPRE.CL.Detyping.restrict_failure_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_failure_le), [`MIPRE.CL.Detyping.restrict_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.restrict_value_ge).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 796](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L796)
