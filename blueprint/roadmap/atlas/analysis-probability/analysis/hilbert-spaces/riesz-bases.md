---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis, MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.linearIndependent, MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.dense_span, MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.exists_dual, MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.normSeq, MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.normSeqLp, MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.norm_normSeqLp, MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.summable_norm_synthesis
statement: formalized
proof: formalized
---

# Riesz bases

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html).

## Riesz basis of a Hilbert space

A family `f : ι → E` is a **Riesz basis** (with respect to the Hilbert basis
`b`) if it is the image of `b` under a bounded invertible operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#is-riesz-basis).

## Riesz bases are linearly independent

A Riesz basis is linearly independent.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.linearIndependent`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#linear-independent).

## Riesz bases have dense span

A Riesz basis has dense span.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.dense_span`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#dense-span).

## Biorthogonal dual of a Riesz basis

A Riesz basis admits a biorthogonal dual family with a reconstruction
formula: there is `g : ι → E` with `⟪f i, g j⟫ = if i = j then 1 else 0` and
`x = ∑' i, ⟪g i, x⟫ • f i` for every `x`. The dual is `g j = (T⁻¹)† (b j)`
for the operator `T` witnessing that `f` is a Riesz basis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasis.IsRieszBasis.exists_dual`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasis.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#exists-dual).

## Norm sequence of a square-summable family

The sequence of norms of a square-summable family, as an element of
`ℓ²(ι, ℝ)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.normSeq`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#norm-seq).

## Norm sequence of an $\ell^2$ coefficient sequence

The sequence of norms of an `ℓ²` coefficient sequence, as an element of
`ℓ²(ι, ℝ)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.normSeqLp`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#norm-seq-lp).

## $\ell^2$ norm of the norm sequence

The `ℓ²` norm of the norms of a coefficient sequence is the norm of the
sequence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.norm_normSeqLp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#norm-norm-seq-lp).

## Absolute summability of a synthesis series

The norms of the terms of a synthesis series are summable when the
coefficient sequence is in `ℓ²` and the synthesized family is square-summable:
this is Cauchy–Schwarz for `ℓ²`, via `lp.tsum_mul_le_mul_norm` applied to the
two real `ℓ²` sequences of norms.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.summable_norm_synthesis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#summable-norm-synthesis).

## Summability of a synthesis series

The terms of a synthesis series are summable when the coefficient sequence
is in `ℓ²` and the synthesized family is square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.summable_synthesis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#summable-synthesis).

## Norm bound for a synthesis series

Norm bound for a synthesis series, by Cauchy–Schwarz for `ℓ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.norm_tsum_smul_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#norm-tsum-smul-le).

## Linear map underlying the synthesis operator

The linear map underlying the synthesis operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.synthesisLinearMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#synthesis-linear-map).

## Synthesis operator of a square-summable family

The **synthesis operator**: for a square-summable family `d : ι → E`, the
bounded operator `ℓ²(ι, 𝕜) →L[𝕜] E` sending `c` to `∑' i, c i • d i`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.synthesisCLM`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#synthesis-clm).

## Operator norm bound for the synthesis operator

The operator norm of the synthesis operator is at most
`√(∑' i, ‖d i‖ ^ 2)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.norm_synthesisCLM_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#norm-synthesis-clm-le).

## Synthesis operator on a basis vector

The synthesis operator at a basis vector picks out one term of the
family.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.synthesisCLM_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#synthesis-clm-single).

## Paley–Wiener stability theorem

If `b` is a Hilbert basis and
`∑' i, ‖f i - b i‖ ^ 2 < 1`, then `f` is a Riesz basis.

Formalized by `MathlibExt.Analysis.InnerProductSpace.RieszBasisStability.isRieszBasis_of_tsum_norm_sq_lt_one`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/RieszBasisStability.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html#is-riesz-basis-of-tsum-norm-sq-lt-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riesz bases](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/riesz-bases/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/riesz-bases)
