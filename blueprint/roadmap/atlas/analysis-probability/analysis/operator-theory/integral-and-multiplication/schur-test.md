---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_pointwise_sq_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_norm_sq_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_apply_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_toEuclideanLin_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_toEuclideanCLM_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_matrix_l2_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_single_le, MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_sum_finset
statement: formalized
proof: formalized
---

# Schur test

36 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html).

## Per-row estimate in Schur's test

The per-row estimate in Schur's test: the `i`-th coordinate of `A x`
satisfies `‖(A x) i‖² ≤ R * ∑ j, ‖A i j‖ * ‖x j‖²` when every row sum of
`‖A i j‖` is at most `R`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_pointwise_sq_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-pointwise-sq-le).

## Squared-norm estimate in Schur's test

The squared-norm estimate in Schur's test: `‖A x‖² ≤ R * C * ‖x‖²`
when every row sum of `‖A i j‖` is at most `R` and every column sum is at
most `C`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_norm_sq_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-norm-sq-le).

## Norm estimate in Schur's test

The unsquared estimate in Schur's test: `‖A x‖ ≤ √(R * C) * ‖x‖`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.schur_apply_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-apply-le).

## Schur's test for rectangular Euclidean matrix operators

Schur's test for the canonical rectangular Euclidean matrix operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_toEuclideanLin_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-to-euclidean-lin-le).

## Schur's test for square Euclidean continuous linear maps

Schur's test for Mathlib's square Euclidean continuous linear map.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_toEuclideanCLM_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-to-euclidean-clm-le).

## Schur's test for the $L^2$ operator norm of a matrix

Schur's test for the actual scoped L2 operator norm of a matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTest.norm_matrix_l2_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTest.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-matrix-l2-le).

## Entries of a Schur matrix are bounded by the row bound

A single entry of a Schur matrix is bounded by the row bound.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_single_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-single-le).

## Summability of a finite sum of summable sequences

Summability of a finite sum of summable sequences.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_sum_finset`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-sum-finset).

## Interchange of an infinite sum with a finite sum

Swapping a `tsum` with a finite sum.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.tsum_sum_finset`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#tsum-sum-finset).

## Row bound of a Schur matrix is nonnegative

A single row bound: the row bound `R` is nonnegative.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_nonneg_of_row`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-nonneg-of-row).

## Weighted Cauchy–Schwarz for one row of a Schur matrix

Finite weighted Cauchy–Schwarz for one row.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_finset_cs`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-finset-cs).

## Summability of the weighted row series in Schur's test

Weighted summability for one row: `∑' j, ‖a i j‖ * ‖x j‖²` converges.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_weighted`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-weighted).

## Partial sums of the weighted row series in Schur's test

A finite partial sum of the weighted series is bounded by `R * ‖x‖²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.sum_range_schurInf_weighted_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#sum-range-schur-inf-weighted-le).

## Absolute summability of rows of a Schur matrix

Summability of the row series of absolute values.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_norm`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-norm).

## Summability of the row series defining a Schur coordinate

Summability of the row series defining one coordinate of the operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_coord`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-coord).

## Per-row estimate in Schur's test on $\ell^2$

The per-row estimate: `‖(T x) i‖² ≤ R * ∑' j, ‖a i j‖ * ‖x j‖²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_pointwise_sq_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-pointwise-sq-le).

## Summability of the double weighted series in Schur's test

Summability of the double weighted series `∑' i, ∑' j, ‖a i j‖ * ‖x j‖²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_weighted_tsum`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-weighted-tsum).

## Bound on the double weighted series in Schur's test

The double weighted series is bounded by `C * ‖x‖²`, via the `tsum` interchange.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_tsum_weighted_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-tsum-weighted-le).

## Squared coordinates of a Schur image are summable

Summability of the squared coordinates of a Schur image.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_coordSq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-coord-sq).

## Coordinates of a Schur image lie in $\ell^2$

The coordinates of a Schur image are in `ℓ²`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.memℓp_schurInfCoord`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#mem-p-schur-inf-coord).

## Schur operator of an infinite matrix as a linear map

The Schur operator of a matrix, as a linear map.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInfLinMap`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-lin-map).

## Pointwise action of the Schur linear map

Pointwise action of the Schur linear map.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInfLinMap_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-lin-map-apply).

## Norm bound for the Schur linear map

The Schur operator is bounded by `√(R * C)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.norm_schurInfLinMap_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-schur-inf-lin-map-le).

## Schur operator on $\ell^2(\mathbb{N})$

The Schur operator of a matrix, as a bounded operator on `ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInfOperator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 404](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L404). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-operator).

## Pointwise action of the Schur operator

Pointwise action of the Schur operator.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInfOperator_apply`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-operator-apply).

## Schur's test

The operator norm is at most `√(R * C)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.norm_schurInfOperator_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-schur-inf-operator-le).

## Schur's test with a single row and column bound

The single-bound form: if all row and column sums are at most `B`,
then the operator norm is at most `B`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.norm_schurInfOperator_le_of_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#norm-schur-inf-operator-le-of-le).

## Schur operator depends only on the matrix

The Schur operator depends only on the matrix, not on the bounds or proofs.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInfOperator_congr`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-operator-congr).

## Weighted partial sums grouped by the first index

A finite partial sum of the weighted series, grouped by the first index.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.sum_finset_schurInf_weighted_fst_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#sum-finset-schur-inf-weighted-fst-le).

## Weighted partial sums grouped by the second index

A finite partial sum of the weighted series, grouped by the second index.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.sum_finset_schurInf_weighted_snd_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#sum-finset-schur-inf-weighted-snd-le).

## Product summability for the Schur bilinear form

Product summability for the bilinear form of a Schur matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_prod`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-prod).

## Row summability of the conjugate-transpose Schur matrix

Row summability for the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_transposeStar_row`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-transpose-star-row).

## Row bounds for the conjugate-transpose Schur matrix

Row bounds for the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_transposeStar_row_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-transpose-star-row-le).

## Column summability for the conjugate-transpose matrix in Schur's test

Column summability for the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.summable_schurInf_transposeStar_col`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#summable-schur-inf-transpose-star-col).

## Column bounds for the conjugate-transpose matrix in Schur's test

Column bounds for the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.schurInf_transposeStar_col_le`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 601](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#schur-inf-transpose-star-col-le).

## Schur's test, adjoint form

The adjoint of a Schur operator is the
Schur operator of the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.SchurTestInfinite.adjoint_schurInfOperator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/SchurTestInfinite.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html#adjoint-schur-inf-operator).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur test](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/schur-test)
