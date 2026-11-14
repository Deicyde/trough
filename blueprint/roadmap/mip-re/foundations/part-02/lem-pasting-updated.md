---
declaration: lemma
origin: cited
lean: MIPRE.fibSum, MIPRE.isPVM_fibSum, MIPRE.sum_fiber, MIPRE.abs_sum_sum_le_sqrt, MIPRE.sum_comm4, MIPRE.sum_prod_eq, MIPRE.sum_prod_uniform, MIPRE.sum_prod_uniform_one, MIPRE.sum_weighted_add, MIPRE.sum_weighted_div, MIPRE.sum_weighted_const_mul, MIPRE.IsPVM.comp_equiv, MIPRE.qform_conjTranspose, MIPRE.sum_sq_le_one_of_sum_eq_one, MIPRE.sum_snorm_sq_orth_le_one, MIPRE.sum_snorm_sq_povm_le_one, MIPRE.sum_snorm_sq_prod_le_one, MIPRE.sum_bornProb_le_fibSum, MIPRE.sum_xSqNorm_fibSum_le, MIPRE.sum_snorm_sq_comm_eq, MIPRE.pasteJ, MIPRE.sandOp_posSemidef, MIPRE.sum_sandOp, MIPRE.sum_snorm_sq_sandOp_le_one, MIPRE.sandOpG_posSemidef, MIPRE.sum_sandOpG, MIPRE.pasteJ_posSemidef, MIPRE.sum_pasteJ, MIPRE.abs_sigma_sub_cloud_le, MIPRE.abs_sand_sub_ord_le, MIPRE.sum_bornProb_ord_ge, MIPRE.sum_snorm_sq_comm_coarse_le, MIPRE.collisionTerm, MIPRE.collisionTerm_nonneg, MIPRE.strife_sub_cloud_eq, MIPRE.sum_snorm_sq_comm_fine_le, MIPRE.one_sub_sum_bornProb_pasteJ_le', MIPRE.one_sub_sum_bornProb_pasteJ_le, MIPRE.sum_xSqNorm_pasteJ_le, MIPRE.sum_collisionTerm_le
statement: formalized
proof: formalized
---

# Pasting, the two-measurement case

Let $\mu$ be a distribution on questions, $|\psi\rangle$ a unit vector, and suppose given, for each question:

- a *projective* measurement $\{A_{b,a}\}$ on $\mathbb{C}^{d_\textsc{A}}$ with outcomes pairs in ${\mathcal{A}} \times {\mathcal{B}}$;
- a *projective* measurement $\{R_b\}_{b \in {\mathcal{A}}}$ on $\mathbb{C}^{d_\textsc{B}}$ — in the application already the coarse-graining of the first family along its own outcome map, which is why only its projectivity appears;
- a *projective* measurement $\{G_g\}_{g \in {\mathcal{C}}}$ on $\mathbb{C}^{d_\textsc{B}}$, a copy $\{G'_g\}$ of it on $\mathbb{C}^{d_\textsc{A}}$, and an outcome map $e : {\mathcal{C}} \to {\mathcal{B}}$.

Write $J_{b, a} = \sum_{g \,:\, e(g) = a} G_g R_b G_g$ for the pasted family, which is a POVM. Suppose that

$$
\bigl(\sum_a A_{b,a}\bigr) \otimes {I} \simeq_\delta {I} \otimes R_b\;, \qquad
\bigl(\sum_b A_{b,a}\bigr) \otimes {I} \simeq_\delta
{I} \otimes \sum_{g \,:\, e(g) = a} G_g\;, \qquad
G'_g \otimes {I} \simeq_\eta {I} \otimes G_g\;,\qquad\text{(7)}
$$

and that the *collision term* $\mathop{\mathbb{E}} \sum_b \sum_{g \neq g' \,:\, e(g) = e(g')} \langle\psi| G'_{g'} \otimes G_g R_b G_g |\psi\rangle$ is at most $\varepsilon$. Then

$$
1 - \mathop{\mathbb{E}} \sum_{b, a} \langle\psi| A_{b,a} \otimes J_{b,a} |\psi\rangle
\;\leq\; \frac{\delta}{2} + \sqrt{\frac{\delta}{2}}
+ \sqrt{32 \delta + 4\sqrt{\eta} + 2 \varepsilon}\;,\qquad\text{(8)}
$$

and hence $A_{b,a} \otimes {I} \simeq_{\delta_{\mathrm{pasting}}} {I} \otimes J_{b,a}$ with $\delta_{\mathrm{pasting}}$ twice the right-hand side of (8).

Finally, if the question is a pair $(z, y)$ with $y$ uniform and independent of $z$, every family above depending on $z$ alone and only $e$ on $y$, and if any two distinct $g, g'$ satisfy $e_z(y)(g) = e_z(y)(g')$ for at most an $\varepsilon(z)$ fraction of the probes $y$, then the collision term is at most the average of $\varepsilon(z)$. The dependence on $z$ is what the consumer needs: for a *degenerate* line — a direction that is zero, which the seeded test's diagonal branch does sample — the outcome map separates nothing at all, and what makes the average small is that such lines are rare, not that the bound holds at every question.

## Depends on

- [Cross-party state-dependent distance](def-cross-distance.md)
- [Commutation analysis](lem-commutation-analysis.md)

## Proof depends on

- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)

## Proof

The target is the agreement of $A$ with the sandwich. Two steps reach it. The ordered product $G_g R_b$ carries all but $\delta/2 + \sqrt{\delta/2}$: its outer factor sums away against Alice's second marginal by the second hypothesis, and what is left is Alice's first marginal against ${I} - R_b$, whose Cauchy–Schwarz costs the square root of the first hypothesis. Passing from the ordered product to the sandwich costs one more Cauchy–Schwarz against Bob's commutator $[R_b, G_g]$, the front factor $A_{b, e(g)} \otimes G_g$ being a mutually orthogonal family and so a contraction.

So everything reduces to the *fine-grained* commutator $\sum_{b, g} \left\| {[R_b, G_g] |\psi\rangle} \right\|^2$. Its coarse-grained counterpart, with $G$ replaced by its fibre sums, is at most $16(\delta + \delta)$ by Lemma [Commutation analysis](lem-commutation-analysis.md) — read in the mirror, with both families on Bob's factor and Alice's joint measurement supplying the operator both products reach. Expanding either commutator, the two diagonal terms are *exactly one* because $R$ and $G$ are projective, so each equals $2 - 2\Sigma$ for its own overlap $\Sigma$, and the two off-diagonal terms are complex conjugates. Comparing the two overlaps is the only remaining work, and it passes through the paper's cloud and strife: replacing Bob's outer factor by Alice's copy of it costs $\sqrt\eta$ on each side — and nothing depending on $|{\mathcal{C}}|$, because one factor $R_b$ stays in front of the deviation, so the sum over $b$ is absorbed — while the cloud and the strife differ by exactly the collision term.

For the last part, the Born probabilities do not depend on the probe, so the probe average acts on the collision indicator alone; what multiplies it is a POVM's total mass, which is one.

## Lean

Formalized as [`MIPRE.fibSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fibSum), [`MIPRE.isPVM_fibSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isPVM_fibSum), [`MIPRE.sum_fiber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_fiber), [`MIPRE.abs_sum_sum_le_sqrt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.abs_sum_sum_le_sqrt), [`MIPRE.sum_comm4`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_comm4), [`MIPRE.sum_prod_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_eq), [`MIPRE.sum_prod_uniform`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_uniform), [`MIPRE.sum_prod_uniform_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_prod_uniform_one), [`MIPRE.sum_weighted_add`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_weighted_add), [`MIPRE.sum_weighted_div`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_weighted_div), [`MIPRE.sum_weighted_const_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_weighted_const_mul), [`MIPRE.IsPVM.comp_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.comp_equiv), [`MIPRE.qform_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.qform_conjTranspose), [`MIPRE.sum_sq_le_one_of_sum_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sq_le_one_of_sum_eq_one), [`MIPRE.sum_snorm_sq_orth_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_orth_le_one), [`MIPRE.sum_snorm_sq_povm_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_povm_le_one), [`MIPRE.sum_snorm_sq_prod_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_prod_le_one), [`MIPRE.sum_bornProb_le_fibSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bornProb_le_fibSum), [`MIPRE.sum_xSqNorm_fibSum_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_fibSum_le), [`MIPRE.sum_snorm_sq_comm_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_comm_eq), [`MIPRE.pasteJ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.pasteJ), [`MIPRE.sandOp_posSemidef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandOp_posSemidef), [`MIPRE.sum_sandOp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sandOp), [`MIPRE.sum_snorm_sq_sandOp_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_sandOp_le_one), [`MIPRE.sandOpG_posSemidef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandOpG_posSemidef), [`MIPRE.sum_sandOpG`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sandOpG), [`MIPRE.pasteJ_posSemidef`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.pasteJ_posSemidef), [`MIPRE.sum_pasteJ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_pasteJ), [`MIPRE.abs_sigma_sub_cloud_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.abs_sigma_sub_cloud_le), [`MIPRE.abs_sand_sub_ord_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.abs_sand_sub_ord_le), [`MIPRE.sum_bornProb_ord_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bornProb_ord_ge), [`MIPRE.sum_snorm_sq_comm_coarse_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_comm_coarse_le), [`MIPRE.collisionTerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.collisionTerm), [`MIPRE.collisionTerm_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.collisionTerm_nonneg), [`MIPRE.strife_sub_cloud_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.strife_sub_cloud_eq), [`MIPRE.sum_snorm_sq_comm_fine_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_comm_fine_le), [`MIPRE.one_sub_sum_bornProb_pasteJ_le'`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_sum_bornProb_pasteJ_le'), [`MIPRE.one_sub_sum_bornProb_pasteJ_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_sum_bornProb_pasteJ_le), [`MIPRE.sum_xSqNorm_pasteJ_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_xSqNorm_pasteJ_le), [`MIPRE.sum_collisionTerm_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_collisionTerm_le).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 874](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L874)
