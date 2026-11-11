---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceFun, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_memℓp_sliceFun, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceLinMap, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceLinMap_apply, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_tsum_normSq_slice_le, MathlibExt.Analysis.InnerProductSpace.HankelOperator.norm_hankelSliceLinMap_apply_le, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSlice, MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSlice_apply
statement: formalized
proof: formalized
---

# Hankel operators

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html).

## Anti-diagonal slice of a sequence

The `k`-th anti-diagonal slice function: reverse the first `k + 1`
coordinates, kill the rest.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceFun`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice-fun).

## Anti-diagonal slice of an ℓ² sequence lies in ℓ²

The slice of an `ℓ²` sequence is in `ℓ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_memℓp_sliceFun`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-mem-p-slice-fun).

## Anti-diagonal slice as a linear map

The `k`-th anti-diagonal slice as a linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice-lin-map).

## Pointwise action of the anti-diagonal slice map

Pointwise action of the slice linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSliceLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice-lin-map-apply).

## Anti-diagonal slice does not increase the sum of squared norms

The (squared) norms of a sliced sequence sum to at most the squared
norms of the original sequence: only the first `k + 1` coordinates survive,
in reverse order.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_tsum_normSq_slice_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-tsum-norm-sq-slice-le).

## Anti-diagonal slice map does not increase norms

A slice does not increase norms.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.norm_hankelSliceLinMap_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#norm-hankel-slice-lin-map-apply-le).

## Anti-diagonal slice operator

The `k`-th anti-diagonal slice as a bounded operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSlice`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice).

## Pointwise action of the anti-diagonal slice operator

Pointwise action of the slice operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSlice_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice-apply).

## Anti-diagonal slice operator has norm at most one

The operator norm of a slice is at most `1`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.norm_hankelSlice_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#norm-hankel-slice-le).

## Anti-diagonal slice is symmetric

A slice is symmetric for the inner product: the anti-diagonal symmetry
is a finite-sum reflection.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelSlice_inner_symm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-slice-inner-symm).

## Anti-diagonal slice operator is self-adjoint

A slice is self-adjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.adjoint_hankelSlice`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#adjoint-hankel-slice).

## Summability of weighted anti-diagonal slices

The slice operators weighted by `a` are summable in operator norm when
`a` is absolutely summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_summable_slices`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-summable-slices).

## Hankel operator with absolutely summable symbol

The Hankel operator with symbol `a`. Defined as the norm-convergent
series `∑' k, a k • hankelSlice k` over the anti-diagonal slices.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelOperator`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-operator).

## Hankel operator as the sum of its slices

The Hankel operator is the sum of its slices.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_hasSum_slices`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-has-sum-slices).

## Matrix entries of the Hankel operator

Pointwise action of the Hankel operator: `(Hₐ x) i = ∑' j, a (i + j) * x j`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-operator-apply).

## Hankel operator with zero symbol is zero

The zero symbol gives the zero operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankelOperator_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-operator-zero).

## Norm bound for the Hankel operator

Operator-norm bound: `‖Hₐ‖ ≤ ∑' k, ‖a k‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.norm_hankelOperator_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#norm-hankel-operator-le).

## Adjoint of a Hankel operator

Adjoint of a Hankel operator: `(Hₐ)† = H_{star a}`, by passing the
adjoint through the finite partial sums and taking the limit.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.adjoint_hankelOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#adjoint-hankel-operator).

## Hankel operator with real symbol is self-adjoint

A Hankel operator with a real-valued (`star`-fixed) symbol is
self-adjoint.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.isSelfAdjoint_hankelOperator_of_forall_star`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#is-self-adjoint-hankel-operator-of-foral).

## Partial sums of the Hankel slice series are compact

A finite partial sum of the slice series has finite-dimensional range,
hence is a compact operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.hankel_isCompactOperator_partialSum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#hankel-is-compact-operator-partial-sum).

## Hankel operator with absolutely summable symbol is compact

A Hankel operator with an absolutely summable symbol is compact:
it is the norm limit of its finite partial sums, each of which has
finite-dimensional range.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HankelOperator.isCompactOperator_hankelOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HankelOperator.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html#is-compact-operator-hankel-operator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hankel operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/shift-toeplitz-hankel/hankel-operators)
