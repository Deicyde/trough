---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_variance_eq, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_bhatia_davis, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_popoviciu, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_kantorovich, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.apply_eigenvectorBasis_real, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.eigenvalue_mem_Icc_of_rayleigh_bounds, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.sum_weights_eq_norm_sq, MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.rayleigh_eq_weighted_sum
statement: formalized
proof: formalized
---

# Kantorovich, Bhatia–Davis and Popoviciu inequalities

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html).

## Scalar

## Weighted variance as weighted squared deviation from the mean

The weighted variance equals the weighted squared deviation from the
weighted mean.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_variance_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#weighted-variance-eq).

## Bhatia–Davis inequality

**Bhatia–Davis inequality**, scalar weighted form: if the weights are
nonnegative, sum to `1`, and every `λ i` lies in `[m, M]`, then the weighted
variance is at most `(M - μ) * (μ - m)`, where `μ` is the weighted mean.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_bhatia_davis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#weighted-bhatia-davis).

## Popoviciu's inequality

**Popoviciu's inequality**, scalar weighted form: the weighted variance
is at most `((M - m) / 2)²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_popoviciu`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#weighted-popoviciu).

## Kantorovich's inequality

**Kantorovich's inequality**, scalar weighted form: if the weights are
nonnegative, sum to `1`, every `λ i` lies in `[m, M]`, and `0 < m`, then
`(∑ w i * λ i) * (∑ w i / λ i) ≤ (M + m)² / (4 * m * M)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.weighted_kantorovich`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#weighted-kantorovich).

## Eigenvector basis equation with real eigenvalues

Real-valued form of `LinearMap.IsSymmetric.apply_eigenvectorBasis`: the
eigenvalue is a plain real scalar, with no `ℝ → 𝕜` coercion.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.apply_eigenvectorBasis_real`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#apply-eigenvector-basis-real).

## Eigenvalues lie within the Rayleigh quotient bounds

The eigenvalues of a symmetric operator lie in `[m, M]` whenever its
Rayleigh quotients do.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.eigenvalue_mem_Icc_of_rayleigh_bounds`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#eigenvalue-mem-icc-of-rayleigh-bounds).

## Eigenbasis weights sum to the squared norm

The eigenbasis weights sum to `‖x‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.sum_weights_eq_norm_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#sum-weights-eq-norm-sq).

## Rayleigh quotient as a weighted average of eigenvalues

The Rayleigh quotient is the weighted average of the eigenvalues, with
weights `((eigenvectorBasis).repr x i)²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.rayleigh_eq_weighted_sum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#rayleigh-eq-weighted-sum).

## Second moment as a weighted average of squared eigenvalues

The second-moment quadratic form is the weighted average of the squared
eigenvalues.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.second_moment_eq_weighted_sum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#second-moment-eq-weighted-sum).

## Inverse quadratic form as a weighted average of reciprocal eigenvalues

The quadratic form of a two-sided inverse is the weighted average of the
reciprocal eigenvalues.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.inv_rayleigh_eq_weighted_sum_div`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#inv-rayleigh-eq-weighted-sum-div).

## Operator variance as weighted squared deviation of eigenvalues

The variance of `T` at a unit vector is the weighted squared deviation
of the eigenvalues from the Rayleigh quotient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.variance_eq_weighted_sum_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#variance-eq-weighted-sum-sq).

## Bhatia–Davis inequality

**Bhatia–Davis inequality** for a symmetric operator: the variance of `T`
at a unit vector is at most `(M - μ) * (μ - m)`, where `μ` is the Rayleigh
quotient.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.bhatia_davis_inequality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#bhatia-davis-inequality).

## Popoviciu's inequality

**Popoviciu's inequality** for a symmetric operator: the variance of `T`
at a unit vector is at most `((M - m) / 2)²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.popoviciu_inequality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#popoviciu-inequality).

## Kantorovich's inequality

**Kantorovich's inequality** for a symmetric operator: for a unit vector
`x`, the product of the Rayleigh quotient of `T` and the Rayleigh quotient
of its two-sided inverse `S` is at most `(M + m)² / (4 * m * M)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.KantorovichInequality.kantorovich_inequality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/KantorovichInequality.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html#kantorovich-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kantorovich, Bhatia–Davis and Popoviciu inequalities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/inequalities/kantorovich-bhatia-davis-and-popoviciu-inequalit)
