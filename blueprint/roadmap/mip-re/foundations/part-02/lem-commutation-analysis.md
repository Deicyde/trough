---
declaration: lemma
origin: cited
lean: MIPRE.qform_nonneg_of_nonneg, MIPRE.qform_le_of_le, MIPRE.sum_snorm_sq_mul_le, MIPRE.sum_snorm_sq_triangle', MIPRE.sum_snorm_sq_triangle3, MIPRE.sum_weighted_snorm_sq_triangle3, MIPRE.POVM.sum_mats_map_prod, MIPRE.POVM.sum_mats_map_prod', MIPRE.sum_xSqNorm_le_of_two_step, MIPRE.aOp_mono, MIPRE.bOp_mono, MIPRE.bOp_sum, MIPRE.sum_aOp_conjTranspose_mul_self_le_one, MIPRE.sum_bOp_conjTranspose_mul_self_le_one, MIPRE.sum_bOp_conjTranspose_mul_self_of_isPVM, MIPRE.IsPVM.marg_mul_marg, MIPRE.IsPVM.marg_mul_marg', MIPRE.IsPVM.sum_marg_left, MIPRE.IsPVM.sum_marg_right, MIPRE.IsPVM.marg_left, MIPRE.IsPVM.marg_right, MIPRE.sum_prod_snorm_sq_mul_le_fst, MIPRE.sum_prod_snorm_sq_mul_le_snd, MIPRE.commutation_analysis_abstract, MIPRE.commutation_analysis, MIPRE.commutation_analysis_aOp, MIPRE.obs2_commutator_eq
statement: formalized
proof: formalized
---

# Commutation analysis

Let $\{A_b\}$ and $\{C_c\}$ be POVMs on $\mathbb{C}^{d_\textsc{A}}$ and let $\{B_{b,c}\}$ be a *projective* measurement on $\mathbb{C}^{d_\textsc{B}}$ with outcomes the pairs, with marginals $B_b = \sum_c B_{b,c}$ and $B_c = \sum_b B_{b,c}$. If

$$
A_b \otimes {I} \simeq_\delta {I} \otimes B_b \qquad\text{and}\qquad
C_c \otimes {I} \simeq_\delta {I} \otimes B_c\;,
$$

then Alice's two POVMs approximately commute on the state:

$$
\sum_{b, c} \left\| {\bigl( [A_b, C_c] \otimes {I} \bigr) |\psi\rangle} \right\|^2 \;\leq\; 16\, \delta\;.\qquad\text{(4)}
$$

## Depends on

- [Cross-party state-dependent distance](def-cross-distance.md)
- [Nonlocal game](../part-01/def-game.md)

## Proof

Both products reach the *same* operator on Bob's factor, ${I} \otimes B_{b,c}$. For $A_b C_c \otimes {I}$: put $A_b \otimes {I}$ in front of $C$'s relation, and put ${I} \otimes B_c$ in front of $A$'s; the two meet at $A_b \otimes B_c$, and the second step lands on ${I} \otimes B_c B_b = {I} \otimes B_{b,c}$ — which is where projectivity is used, and the only place (`IsPVM.marg_mul_marg`). For $C_c A_b \otimes {I}$, the same two steps in the other order, using $B_b B_c = B_{b,c}$. Each side is therefore within $4\delta$ after one triangle inequality, and (4) is one more.

Putting an operator in front costs nothing and *adds* its index to the sum, which is the paper's `fact:add-a-proj`: if $\sum_i F_i^\dagger F_i \leq {I}$ then $\sum_i \left\| {F_i v} \right\|^2 \leq \left\| {v} \right\|^2$. For a POVM that hypothesis is $A_b^2 \leq A_b$ with $\sum_b A_b = {I}$, so it needs no projectivity of Alice's measurements (`sum_aOp_conjTranspose_mul_self_le_one`).

## Lean

Formalized as [`MIPRE.qform_nonneg_of_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.qform_nonneg_of_nonneg), [`MIPRE.qform_le_of_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.qform_le_of_le), [`MIPRE.sum_snorm_sq_mul_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_mul_le), [`MIPRE.sum_snorm_sq_triangle'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_triangle'), [`MIPRE.sum_snorm_sq_triangle3`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_triangle3), [`MIPRE.sum_weighted_snorm_sq_triangle3`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_weighted_snorm_sq_triangle3), [`MIPRE.POVM.sum_mats_map_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.sum_mats_map_prod), [`MIPRE.POVM.sum_mats_map_prod'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVM.sum_mats_map_prod'), [`MIPRE.sum_xSqNorm_le_of_two_step`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_le_of_two_step), [`MIPRE.aOp_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.aOp_mono), [`MIPRE.bOp_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.bOp_mono), [`MIPRE.bOp_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.bOp_sum), [`MIPRE.sum_aOp_conjTranspose_mul_self_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_aOp_conjTranspose_mul_self_le_one), [`MIPRE.sum_bOp_conjTranspose_mul_self_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bOp_conjTranspose_mul_self_le_one), [`MIPRE.sum_bOp_conjTranspose_mul_self_of_isPVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bOp_conjTranspose_mul_self_of_isPVM), [`MIPRE.IsPVM.marg_mul_marg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.marg_mul_marg), [`MIPRE.IsPVM.marg_mul_marg'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.marg_mul_marg'), [`MIPRE.IsPVM.sum_marg_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.sum_marg_left), [`MIPRE.IsPVM.sum_marg_right`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.sum_marg_right), [`MIPRE.IsPVM.marg_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.marg_left), [`MIPRE.IsPVM.marg_right`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.marg_right), [`MIPRE.sum_prod_snorm_sq_mul_le_fst`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_snorm_sq_mul_le_fst), [`MIPRE.sum_prod_snorm_sq_mul_le_snd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_snorm_sq_mul_le_snd), [`MIPRE.commutation_analysis_abstract`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutation_analysis_abstract), [`MIPRE.commutation_analysis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutation_analysis), [`MIPRE.commutation_analysis_aOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutation_analysis_aOp), [`MIPRE.obs2_commutator_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.obs2_commutator_eq).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 753](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L753)
