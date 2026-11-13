---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceFun, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitz_memℓp_sliceFun, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceLinMap, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceLinMap_apply, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.norm_toeplitzSliceLinMap_apply_le, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice_apply, MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice_eq_shiftCLM_pow_or_backwardCLM_pow
statement: formalized
proof: formalized
---

# Toeplitz operators

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html).

## Diagonal slice function of a Toeplitz matrix

The `k`-th diagonal slice function: shift coordinates by `k`, killing
the coordinates that fall off the end. For `k ≥ 0` this is the `k`-fold
forward shift; for `k < 0` it is the `(-k)`-fold backward shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-fun).

## Diagonal slices preserve square-summability

The slice of an `ℓ²` sequence is in `ℓ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitz_memℓp_sliceFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-mem-p-slice-fun).

## Diagonal slice as a linear map

The `k`-th diagonal slice as a linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-lin-map).

## Pointwise action of the diagonal slice linear map

Pointwise action of the slice linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSliceLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-lin-map-apply).

## Diagonal slices do not increase norms

A slice does not increase norms.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.norm_toeplitzSliceLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#norm-toeplitz-slice-lin-map-apply-le).

## Diagonal slice as a bounded operator

The `k`-th diagonal slice as a bounded operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice).

## Pointwise action of the diagonal slice operator

Pointwise action of the slice operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-apply).

## Diagonal slices are powers of the forward or backward shift

Every nonnegative Toeplitz slice is the corresponding power of the
canonical unilateral shift, and every negative slice is the corresponding
power of the canonical backward shift.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice_eq_shiftCLM_pow_or_backwardCLM_pow`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-eq-shift-clm-pow-or-backw).

## Operator norm of a diagonal slice is at most one

The operator norm of a slice is at most `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.norm_toeplitzSlice_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#norm-toeplitz-slice-le).

## Inner product symmetry of opposite diagonal slices

A slice is adjoint to the slice at the negated index: the diagonal
symmetry exchanges the two sides of the inner product.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzSlice_inner_symm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-slice-inner-symm).

## Adjoint of a diagonal slice is the opposite slice

A slice is adjoint to the slice at the negated index.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.adjoint_toeplitzSlice`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#adjoint-toeplitz-slice).

## Summability of weighted diagonal slices

The slice operators weighted by `a` are summable in operator norm when
`a` is absolutely summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitz_summable_slices`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-summable-slices).

## Toeplitz operator with absolutely summable symbol

The Toeplitz operator with symbol `a`. Defined as the norm-convergent
series `∑' k, a k • toeplitzSlice k` over the diagonal slices.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzOperator`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-operator).

## Toeplitz operator as the sum of its diagonal slices

The Toeplitz operator is the sum of its slices.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitz_hasSum_slices`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-has-sum-slices).

## Pointwise action of a Toeplitz operator

Pointwise action of the Toeplitz operator:
`(Tₐ x) i = ∑' j, a (i - j) * x j`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-operator-apply).

## Toeplitz operator of the zero symbol

The zero symbol gives the zero operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzOperator_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-operator-zero).

## Operator norm bound for a Toeplitz operator

Operator-norm bound: `‖Tₐ‖ ≤ ∑' k, ‖a k‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.norm_toeplitzOperator_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#norm-toeplitz-operator-le).

## Adjoint symbol of a Toeplitz operator

The adjoint symbol: `a* k = star (a (-k))`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzAdjointSymbol`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 512](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L512). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-adjoint-symbol).

## Absolute summability of the adjoint symbol

The adjoint symbol of an absolutely summable symbol is absolutely
summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.summable_norm_toeplitzAdjointSymbol`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#summable-norm-toeplitz-adjoint-symbol).

## Adjoint of a Toeplitz operator

Adjoint of a Toeplitz operator: `(Tₐ)† = T_{a*}`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.adjoint_toeplitzOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 522](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L522). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#adjoint-toeplitz-operator).

## Toeplitz operator applied to a standard basis vector

The Toeplitz operator applied to a standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzOperator_apply_single`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 550](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L550). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-operator-apply-single).

## Characterization of self-adjoint Toeplitz operators

Self-adjointness of a Toeplitz operator iff the symbol satisfies
`star (a (-k)) = a k` for all `k`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.isSelfAdjoint_toeplitzOperator_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 559](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L559). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#is-self-adjoint-toeplitz-operator-iff).

## Toeplitz operators with self-adjoint symbol are self-adjoint

A Toeplitz operator with a `star`-fixed adjoint symbol is self-adjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.isSelfAdjoint_toeplitzOperator_of_forall_star`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#is-self-adjoint-toeplitz-operator-of-for).

## Toeplitz operators with nonzero symbol are not compact

A Toeplitz operator with a nonzero symbol is not compact: the images
of the standard basis vectors converge coordinatewise to `0` but keep a
nonzero coordinate.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.not_isCompactOperator_toeplitzOperator_of_ne`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#not-is-compact-operator-toeplitz-operato).

## A Toeplitz operator is compact iff its symbol is zero

A Toeplitz operator is compact iff its symbol is zero.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.isCompactOperator_toeplitzOperator_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#is-compact-operator-toeplitz-operator-if).

## Delta symbol for Toeplitz operators

The delta symbol at `m` with value `c`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzDelta`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-delta).

## Absolute summability of a delta symbol

A delta symbol is absolutely summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.summable_norm_toeplitzDelta`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#summable-norm-toeplitz-delta).

## Toeplitz operator of a delta symbol is a scaled slice

A Toeplitz operator with a delta symbol is the corresponding scalar
multiple of its diagonal slice.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.toeplitzOperator_delta_eq_smul_slice`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#toeplitz-operator-delta-eq-smul-slice).

## $\ell^1$ norm of a delta symbol

The `ℓ¹` norm of a delta symbol is `‖c‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.tsum_norm_toeplitzDelta`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#tsum-norm-toeplitz-delta).

## Operator norm of a Toeplitz operator with delta symbol

The operator norm of a Toeplitz operator with a delta symbol is `‖c‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzOperator.norm_toeplitzOperator_delta`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean, line 775](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzOperator.lean#L775). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html#norm-toeplitz-operator-delta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Toeplitz operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/toeplitz-operators)
