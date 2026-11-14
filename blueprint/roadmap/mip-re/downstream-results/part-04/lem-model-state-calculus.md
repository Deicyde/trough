---
declaration: lemma
origin: cited
lean: MIPRE.Op.abs_qform_sub_qform_le, MIPRE.StateModel.snorm_sq_sum_orthogonal, MIPRE.StateModel.snorm_sq_sum_orthogonal', MIPRE.StateModel.sum_snorm_sq_chain_le, MIPRE.StateModel.snorm_sq_obs_sub_le, MIPRE.StateModel.abs_qform_sub_qform_le, MIPRE.StateModel.abs_qform_withState_sub_qform_le, MIPRE.BipartiteModel.sum_stateSqNorm_sub_le, MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four_of_le, MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four
statement: formalized
proof: formalized
---

# The state calculus of the Pauli basis test, in a model

For elements of the represented algebra of a bipartite model, with $\|T\|_\psi = \|\pi(T)\psi\|$ the state norm of Remark [The operator calculus in a bipartite model](../README.md):

1. if $\{S_g\}$ is a projective measurement, then $\|\sum_{g \in s} S_g R_g\|_\psi^2 = \sum_{g \in s} \|S_g R_g\|_\psi^2$, and in particular $\|(\sum_{g \in s} S_g) R\|_\psi^2 = \sum_{g \in s} \|S_g R\|_\psi^2$;
2. a chain of $n$ deviations costs a factor $n$: $\sum_i \|T^0_i - T^n_i\|_\psi^2 \leq n \sum_{k < n} \sum_i \|T^k_i - T^{k+1}_i\|_\psi^2$;
3. weighting two families by coefficients of modulus at most one costs the size of the outcome set: $\|\sum_a c_a A_a - \sum_a c_a B_a\|_\psi^2 \leq |\Lambda| \sum_a \|A_a - B_a\|_\psi^2$;
4. for an operator of norm at most $K$ and two vectors $v$, $w$ of norm at most one, the quadratic forms of the operator on $v$ and on $w$ differ by at most $2K\|v - w\|$;
5. two families of a player's operators whose squared state norms sum to at most one are at summed squared distance at most $4$, the summed squared distance being at most twice the sum of the two families' summed squared norms; in particular two projective measurements on a unit vector are at summed squared distance at most $4$, which is the trivial bound for item 2 of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md).

## Depends on

- [Bipartite model](../part-02/def-bipartite-model.md)
- [Local isometries of bipartite models](../part-03/def-local-isometry.md)

## Proof

Item 1: distinct outcomes of a projective measurement are orthogonal, so the cross terms vanish. Item 2 telescopes the deviation and applies the Cauchy–Schwarz inequality against the constant one, item 3 the triangle inequality over the outcomes and then the same inequality. In item 4 the difference splits into two terms, each with the deviation on one side, and each is bounded by the Cauchy–Schwarz inequality against a vector of norm at most one. Item 5 is the triangle inequality through $0$, and a projective measurement on a unit vector has summed squared state norm one.

## Lean

Formalized as [`MIPRE.Op.abs_qform_sub_qform_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Op.abs_qform_sub_qform_le), [`MIPRE.StateModel.snorm_sq_sum_orthogonal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.snorm_sq_sum_orthogonal), [`MIPRE.StateModel.snorm_sq_sum_orthogonal'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.snorm_sq_sum_orthogonal'), [`MIPRE.StateModel.sum_snorm_sq_chain_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.sum_snorm_sq_chain_le), [`MIPRE.StateModel.snorm_sq_obs_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.snorm_sq_obs_sub_le), [`MIPRE.StateModel.abs_qform_sub_qform_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.abs_qform_sub_qform_le), [`MIPRE.StateModel.abs_qform_withState_sub_qform_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.abs_qform_withState_sub_qform_le), [`MIPRE.BipartiteModel.sum_stateSqNorm_sub_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_stateSqNorm_sub_le), [`MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four_of_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four_of_le), [`MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_stateSqNorm_sub_le_four).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2652](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2652)
