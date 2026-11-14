---
declaration: lemma
origin: cited
lean: MIPRE.one_sub_sum_bornProb_ldSandwich_le, MIPRE.sandK, MIPRE.sandK_zero, MIPRE.sandK_succ, MIPRE.sandK_snoc, MIPRE.sandK_nonneg, MIPRE.sum_sandK, MIPRE.sqrt_sum_xSqNorm_sandK_le, MIPRE.sqrt_sum_xSqNorm_sandStep_le, MIPRE.sum_snorm_sq_sandStep_le, MIPRE.snorm_sandStep_le, MIPRE.sandStep_identity, MIPRE.snorm_add3_le, MIPRE.sqrt_sum_weighted_sq_add_le, MIPRE.sqrt_sum_weighted_sq_le_add3, MIPRE.sum_mul_sum_eq_sum_prod, MIPRE.sqrt_wsum_le_add3, MIPRE.IsPVM.le_one, MIPRE.IsPVM.aOp_contraction, MIPRE.IsPVM.bOp_contraction, MIPRE.sum_bOp_conjTranspose_mul_self_le_one_of_nonneg, MIPRE.fibSum_comp_equiv, MIPRE.fibSum_marg_left, MIPRE.fibSum_snd, MIPRE.fibSum_fibSum, MIPRE.sum_sum_bornProb_eq_one, MIPRE.one_sub_sum_bornProb_le_sqrt, MIPRE.sum_bornProb_le_fibSum_of_nonneg, MIPRE.one_sub_sum_bornProb_le_eval
statement: formalized
proof: formalized
---

# Low-degree sandwich support

Let $k\geq 0$. Let $x$ be drawn from a distribution $\mu$ on a finite set ${\mathcal{X}}$ and, independently of $x$, let $y$ be drawn from a distribution $\nu$ on a finite set $Y$ (uniform in the source). For each $i\leq k$ let $\mathcal{G}_i$ be a finite family of functions on $Y$, any two distinct elements of which agree at $y\sim\nu$ with probability at most $\varepsilon$. Let $|\psi\rangle\in \mathbb{C}^{d_\textsc{A}}\otimes\mathbb{C}^{d_\textsc{B}}$ be a unit vector, let $\{A^x_{g_1,\ldots,g_k}\}$ be a projective measurement on $\mathbb{C}^{d_\textsc{A}}$ with outcomes in $\mathcal{G}_1\times\ldots\times\mathcal{G}_k$, and for each $i$ let $\{G^{i,x}_g\}_{g\in\mathcal{G}_i}$ be a projective measurement on $\mathbb{C}^{d_\textsc{B}}$. Suppose that for every $i$ the evaluated $i$th coordinate of $A$ and the evaluated $G^{i,x}$ disagree with probability at most $\delta$:

$$
1 - \mathop{\mathbb{E}}_{x,y} \sum_{a} \langle\psi| A^x_{[g_i(y)=a]} \otimes G^{i,x}_{[g(y)=a]} |\psi\rangle
\;\leq\; \delta\;.
$$

Define the POVM $C^x_{g_1,\ldots,g_k}=G^{k,x}_{g_k}\ldots G^{2,x}_{g_2}G^{1,x}_{g_1} G^{2,x}_{g_2}\ldots G^{k,x}_{g_k}$, the last index outermost. Then the evaluated tuples disagree with probability at most $2\sqrt{2}\,k\,(\delta+\varepsilon)^{1/2}$:

$$
1 - \mathop{\mathbb{E}}_{x,y} \sum_{a_1,\ldots,a_k} \langle\psi|
A^x_{[(g_1(y),\ldots,g_k(y))=(a_1,\ldots,a_k)]} \otimes
C^x_{[(g_1(y),\ldots,g_k(y))=(a_1,\ldots,a_k)]} |\psi\rangle
\;\leq\; 2\sqrt{2}\,k\,(\delta+\varepsilon)^{1/2}\;.
$$

Combined with [(1)](../../foundations/part-02/def-cross-distance.md), the evaluated tuples are $4\sqrt{2}\,k\,(\delta+\varepsilon)^{1/2}$-close across the parties in the sense of Definition [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md).

## Depends on

- [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md)
- [Cool closeness fact, and the marginal step](../../foundations/part-02/lem-cool-closeness-fact.md)
- [Pasting, the two-measurement case](../../foundations/part-02/lem-pasting-updated.md)

## Proof depends on

- [Commutation analysis](../../foundations/part-02/lem-commutation-analysis.md)
- [Combined $XZ$ point measurements](../../background-results/part-02/lem-qld-combined-points.md)

## Proof

Three steps, of which only the middle one is about sandwiches.

*From evaluations to outcomes.* Fix $i$ and write $\eta$ for the probability that the $i$th coordinate of $A$ and $G^{i,x}$ return different functions. The Born probabilities do not depend on $y$, and two different functions are separated at $y$ with probability at least $1-\varepsilon$, so the evaluated disagreement is at least $(1-\varepsilon)\eta$; since $\eta\leq 1$ this gives $\eta\leq\delta+\varepsilon$ with no case split. Both measurements are projective, so their squared distance across the parties is exactly $2\eta$.

*One layer at a time.* Split the outcome as $(o, g)$ with $g$ the last coordinate. Alice's element is the palindrome $A_g A_o A_g$ of her two marginals, and three replacements move it to Bob's $G_g C_o G_g$: the right $A_g$, then $A_o$, then the left $A_g$. Each multiplies a known deviation by a family $F$ with $\sum F^\dagger F\leq{I}$ — the joint projections, the product of the contraction $A_g$ with the projective $G_g$, and $G_g C_o$ with $\sum_o C_o^2\leq{I}$ — so each costs exactly the deviation it multiplies (the paper's `fact:add-a-proj`). The three costs are added as square roots, by Minkowski's inequality in $\ell^2$ over the index and the outcomes: each layer adds twice the square root of its coordinate's squared distance, and by induction on $k$ the square root of the outcome-level squared distance between $A$ and $C$ is at most $2\sum_i (2(\delta+\varepsilon))^{1/2}$. The cruder $(a+b+c)^2\leq 3(a^2+b^2+c^2)$ would lose a factor $3$ at every layer, exponential in $k$.

*Back to agreement, then evaluation.* Against a projective measurement, $1-\sum_g\langle\psi|A_g\otimes C_g|\psi\rangle$ is a sum of cross terms against the deviations and is at most the square root of the squared distance, whatever $C$ is; Jensen moves the average over $x$ inside the root. Evaluating both sides at $y$ merges outcomes, and since every Born probability involved is nonnegative, merging can only add agreement.

## Lean

Formalized as [`MIPRE.one_sub_sum_bornProb_ldSandwich_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_sum_bornProb_ldSandwich_le), [`MIPRE.sandK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandK), [`MIPRE.sandK_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandK_zero), [`MIPRE.sandK_succ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandK_succ), [`MIPRE.sandK_snoc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandK_snoc), [`MIPRE.sandK_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandK_nonneg), [`MIPRE.sum_sandK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sandK), [`MIPRE.sqrt_sum_xSqNorm_sandK_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sqrt_sum_xSqNorm_sandK_le), [`MIPRE.sqrt_sum_xSqNorm_sandStep_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sqrt_sum_xSqNorm_sandStep_le), [`MIPRE.sum_snorm_sq_sandStep_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_snorm_sq_sandStep_le), [`MIPRE.snorm_sandStep_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_sandStep_le), [`MIPRE.sandStep_identity`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sandStep_identity), [`MIPRE.snorm_add3_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.snorm_add3_le), [`MIPRE.sqrt_sum_weighted_sq_add_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sqrt_sum_weighted_sq_add_le), [`MIPRE.sqrt_sum_weighted_sq_le_add3`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sqrt_sum_weighted_sq_le_add3), [`MIPRE.sum_mul_sum_eq_sum_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_mul_sum_eq_sum_prod), [`MIPRE.sqrt_wsum_le_add3`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sqrt_wsum_le_add3), [`MIPRE.IsPVM.le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.le_one), [`MIPRE.IsPVM.aOp_contraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.aOp_contraction), [`MIPRE.IsPVM.bOp_contraction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVM.bOp_contraction), [`MIPRE.sum_bOp_conjTranspose_mul_self_le_one_of_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bOp_conjTranspose_mul_self_le_one_of_nonneg), [`MIPRE.fibSum_comp_equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fibSum_comp_equiv), [`MIPRE.fibSum_marg_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fibSum_marg_left), [`MIPRE.fibSum_snd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fibSum_snd), [`MIPRE.fibSum_fibSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.fibSum_fibSum), [`MIPRE.sum_sum_bornProb_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sum_bornProb_eq_one), [`MIPRE.one_sub_sum_bornProb_le_sqrt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_sum_bornProb_le_sqrt), [`MIPRE.sum_bornProb_le_fibSum_of_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_bornProb_le_fibSum_of_nonneg), [`MIPRE.one_sub_sum_bornProb_le_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.one_sub_sum_bornProb_le_eval).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5263](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5263)
