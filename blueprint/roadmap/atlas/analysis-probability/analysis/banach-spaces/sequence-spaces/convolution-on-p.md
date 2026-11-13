---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.intConv, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.tsum_norm_l1, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.summable_intConv_term, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.memℓp_shift, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.shiftLp, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.shiftLp_apply, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_shiftLp, MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.summable_l1Conv_term
statement: formalized
proof: formalized
---

# Convolution on ℓ^p(ℤ)

31 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html).

## Convolution of sequences on the integers

Convolution of two complex sequences on `ℤ`, as a series. The series is
`0` when it does not converge; for `f ∈ ℓ¹` and `g ∈ ℓ^p` it always
converges (see `summable_intConv_term`).

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.intConv`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#int-conv).

## The $\ell^1$ norm as a sum of coordinate norms

The `ℓ¹` norm is the sum of the coordinate norms.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.tsum_norm_l1`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#tsum-norm-l1).

## Summability of convolution terms for $\ell^1$ and $\ell^p$ sequences

The terms of a convolution of an `ℓ¹` sequence with an `ℓ^p` sequence are
summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.summable_intConv_term`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#summable-int-conv-term).

## Translation preserves $\ell^p$ membership

Translating an `ℓ^p` sequence on `ℤ` preserves `ℓ^p` membership.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.memℓp_shift`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#mem-p-shift).

## Translation of an $\ell^p$ sequence on the integers

Translation of an `ℓ^p` sequence on `ℤ` by `m`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.shiftLp`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#shift-lp).

## Pointwise formula for translation of $\ell^p$ sequences

Pointwise action of a translation.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.shiftLp_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#shift-lp-apply).

## Translation is an isometry of $\ell^p(\mathbb{Z})$

Translation is an isometry of `ℓ^p(ℤ, ℂ)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_shiftLp`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#norm-shift-lp).

## Summability of the Banach-space series for $\ell^1$ convolution

The terms of the Banach-space series defining `l1Conv` are summable.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.summable_l1Conv_term`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#summable-l1-conv-term).

## Convolution of an $\ell^1$ sequence with an $\ell^p$ sequence

Convolution of an `ℓ¹` sequence with an `ℓ^p` sequence, as an element of
`ℓ^p(ℤ, ℂ)`: the Banach-space sum `∑' m, f m • shift m g`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv).

## Pointwise formula for $\ell^1$–$\ell^p$ convolution

Pointwise formula for convolution.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-apply).

## Young's inequality with one $\ell^1$ factor

Young's inequality for convolution with one `ℓ¹` factor.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_l1Conv_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#norm-l1-conv-le).

## Convolution is additive in the $\ell^1$ argument

Convolution is additive in the `ℓ¹` argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_add_left`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-add-left).

## Convolution is additive in the $\ell^p$ argument

Convolution is additive in the `ℓ^p` argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_add_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-add-right).

## Convolution is homogeneous in the $\ell^1$ argument

Convolution commutes with scalar multiplication in the `ℓ¹` argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_smul_left`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-smul-left).

## Convolution is homogeneous in the $\ell^p$ argument

Convolution commutes with scalar multiplication in the `ℓ^p` argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_smul_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-smul-right).

## Convolution with zero on the left

Convolution with `0` on the left is `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_zero_left`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-zero-left).

## Convolution with zero on the right

Convolution with `0` on the right is `0`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_zero_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-zero-right).

## Convolution by a fixed $\ell^1$ sequence as a bounded operator

For fixed `f ∈ ℓ¹`, convolution by `f` as a bounded operator on `ℓ^p`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1ConvCLMOf`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-clmof).

## Pointwise action of the convolution operator

Pointwise action of the convolution operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1ConvCLMOf_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-clmof-apply).

## Operator norm of convolution by $f$ is at most $\|f\|_1$

The operator norm of convolution by `f` is at most `‖f‖`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_l1ConvCLMOf_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#norm-l1-conv-clmof-le).

## Convolution action of $\ell^1$ on $\ell^p$ as a bounded bilinear map

The convolution action as a bounded linear map
`ℓ¹(ℤ, ℂ) →L[ℂ] (ℓ^p(ℤ, ℂ) →L[ℂ] ℓ^p(ℤ, ℂ))`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1ConvCLM`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-clm).

## Pointwise action of the bundled convolution action

Pointwise action of the convolution action.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1ConvCLM_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-clm-apply).

## Convolution action has operator norm at most 1

The convolution action has operator norm at most `1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_l1ConvCLM_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#norm-l1-conv-clm-le).

## Commutativity of $\ell^1$ convolution

Convolution of `ℓ¹` sequences is commutative.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_comm`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-comm).

## Associativity of $\ell^1$ convolution

Convolution of `ℓ¹` sequences is associative.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_assoc`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-assoc).

## Unit sequence in $\ell^1(\mathbb{Z})$

The unit sequence `δ` at `0` in `ℓ¹(ℤ, ℂ)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Delta`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-delta).

## Pointwise values of the unit sequence

Pointwise values of the unit sequence.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Delta_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-delta-apply).

## Norm of the unit sequence is 1

The norm of the unit sequence is `1`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.norm_l1Delta`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#norm-l1-delta).

## Unit sequence is a left identity for convolution

The unit sequence is a left unit for convolution.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_delta_left`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-delta-left).

## Unit sequence is a right identity for $\ell^1$ convolution

The unit sequence is a right unit for convolution on `ℓ¹`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_delta_right`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-delta-right).

## Convolution of coordinate vectors

Convolution of two coordinate vectors: positions add, coefficients
multiply.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.IntConvolution.l1Conv_single_single`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/IntConvolution.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html#l1-conv-single-single).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convolution on ℓ^p(ℤ)](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/convolution-on-p)
