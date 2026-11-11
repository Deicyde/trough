---
declaration: section
origin: cited
lean: MathlibExt.Analysis.OperatorTheory.HilbertSchmidtNorm.hsNormSq, MathlibExt.Analysis.OperatorTheory.HilbertSchmidtNorm.hsENNNorm, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.norm_sq_lp_eq_tsum, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_norm_sq_of_memℓp, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.memℓp_of_summable_norm_sq, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.IsHilbertSchmidt, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsNormSq, MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_row_of_isHilbertSchmidt
statement: formalized
---

# Hilbert–Schmidt operators

63 results, 61 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html).

## Squared Hilbert–Schmidt norm in a family

Let $H$ be a real inner product space, let
$T : H \to H$ be a continuous linear operator and let $(u_n)_{n \in \mathbb{N}}$ be a sequence in
$H$. The squared Hilbert–Schmidt norm of $T$ in the family $(u_n)$ is the extended nonnegative
real $\sum_{n=0}^{\infty} \|T u_n\|^2$, the sum being taken in $[0, \infty]$. It is $\infty$
exactly when the real series $\sum_n \|T u_n\|^2$ diverges.

Formalized by `MathlibExt.Analysis.OperatorTheory.HilbertSchmidtNorm.hsNormSq`, a definition declared in [MathlibExt/Analysis/OperatorTheory/HilbertSchmidtNorm.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/OperatorTheory/HilbertSchmidtNorm.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-norm-sq-2).

## Extended Hilbert–Schmidt norm in a family

Let $H$ be a real inner product space, let
$T : H \to H$ be a continuous linear operator and let $(u_n)_{n \in \mathbb{N}}$ be a sequence in
$H$. The Hilbert–Schmidt norm of $T$ in the family $(u_n)$ is the square root, taken in
$[0, \infty]$ with $\sqrt{\infty} = \infty$, of the squared Hilbert–Schmidt norm
$\sum_{n=0}^{\infty} \|T u_n\|^2 \in [0, \infty]$.

In particular it is $\infty$, not $0$, when the series $\sum_n \|T u_n\|^2$ diverges, for example
for the identity operator when $(u_n)$ is an orthonormal basis of $H$ indexed by $\mathbb{N}$.

Formalized by `MathlibExt.Analysis.OperatorTheory.HilbertSchmidtNorm.hsENNNorm`, a definition declared in [MathlibExt/Analysis/OperatorTheory/HilbertSchmidtNorm.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/OperatorTheory/HilbertSchmidtNorm.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-ennnorm).

## Squared ℓ² norm as a sum of squared coordinates

Norm squared of an `ℓ²(ℕ, 𝕜)` vector is the sum of the squared coordinate norms.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.norm_sq_lp_eq_tsum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#norm-sq-lp-eq-tsum).

## Square-summability of coordinates of an ℓ² vector

Summability of squared coordinate norms from `Memℓp`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_norm_sq_of_memℓp`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-norm-sq-of-mem-p).

## Square-summable sequences lie in ℓ²

`Memℓp` at `2` from summability of squared norms.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.memℓp_of_summable_norm_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#mem-p-of-summable-norm-sq).

## Hilbert–Schmidt matrix

A matrix is Hilbert–Schmidt if the squared norms of its entries are summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.IsHilbertSchmidt`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt).

## Squared Hilbert–Schmidt norm of a matrix

The finite squared Hilbert–Schmidt norm: the sum of the squared entry norms.
The witness restricts this real quantity to summable matrices, avoiding the
zero default of a nonsummable real `tsum`. Divergent operators are handled
by the existing extended-valued operator norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsNormSq`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-norm-sq).

## Rows of a Hilbert–Schmidt matrix are square-summable

Fiber summability: each row of a Hilbert–Schmidt matrix is square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_row_of_isHilbertSchmidt`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-row-of-is-hilbert-schmidt).

## Row vector of a Hilbert–Schmidt matrix

The row vector of a Hilbert–Schmidt matrix, as an `ℓ²` element (conjugated).

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsRow`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-row).

## Summability of the Hilbert–Schmidt coordinate series

The coordinate series defining the Hilbert–Schmidt operator is summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_hsCoord`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-hs-coord).

## Hilbert–Schmidt coordinates as inner products with rows

The coordinate series is the inner product with the row vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsCoord_eq_inner`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-coord-eq-inner).

## Hilbert–Schmidt matrix maps ℓ² vectors into ℓ²

The coordinate series of a Hilbert–Schmidt matrix applied to an `ℓ²` vector is in `ℓ²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.memℓp_hsCoord`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#mem-p-hs-coord).

## Hilbert–Schmidt operator as a linear map

The Hilbert–Schmidt operator of a matrix, as a linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsLinMap`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-lin-map).

## Square-summability of a Hilbert–Schmidt image

The squared norms of the coordinates of a Hilbert–Schmidt image are summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_norm_sq_hsLinMap`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-norm-sq-hs-lin-map).

## Pointwise action of the Hilbert–Schmidt linear map

Pointwise action of the Hilbert–Schmidt linear map.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsLinMap_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-lin-map-apply).

## Norm bound for the Hilbert–Schmidt linear map

The Hilbert–Schmidt operator is bounded by the square root of `hsNormSq`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.norm_hsLinMap_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#norm-hs-lin-map-le).

## Hilbert–Schmidt operator on ℓ²

The Hilbert–Schmidt operator of a matrix, as a bounded operator on `ℓ²(ℕ, 𝕜)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator).

## Pointwise action of the Hilbert–Schmidt operator

Pointwise action of the Hilbert–Schmidt operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-apply).

## Operator norm is at most the Hilbert–Schmidt norm

The operator norm of a Hilbert–Schmidt operator is at most its Hilbert–Schmidt norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.norm_hsOperator_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#norm-hs-operator-le).

## Zero matrix is Hilbert–Schmidt

The zero matrix is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-zero).

## Hilbert–Schmidt operator of the zero matrix is zero

The Hilbert–Schmidt operator of the zero matrix is zero.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_zero`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-zero).

## Negation preserves the Hilbert–Schmidt property

The negative of a Hilbert–Schmidt matrix is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_neg`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-neg).

## Sum of Hilbert–Schmidt matrices is Hilbert–Schmidt

The sum of Hilbert–Schmidt matrices is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-add).

## Difference of Hilbert–Schmidt matrices is Hilbert–Schmidt

The difference of Hilbert–Schmidt matrices is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-sub).

## Scalar multiple of a Hilbert–Schmidt matrix is Hilbert–Schmidt

A scalar multiple of a Hilbert–Schmidt matrix is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_smul`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-smul).

## Additivity of the Hilbert–Schmidt operator

The Hilbert–Schmidt operator of a sum is the sum of the operators.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-add).

## Hilbert–Schmidt operator of a difference of matrices

The Hilbert–Schmidt operator of a difference is the difference of the operators.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-sub).

## Hilbert–Schmidt operator of a scalar multiple of a matrix

The Hilbert–Schmidt operator of a scalar multiple is the scalar multiple of the operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_smul`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-smul).

## Conjugate transpose of an infinite matrix

The conjugate transpose of a matrix: `(aᵀ*) i j = star (a j i)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsTransposeStar`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-transpose-star).

## Conjugate transpose of a Hilbert–Schmidt matrix is Hilbert–Schmidt

The conjugate transpose of a Hilbert–Schmidt matrix is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_transposeStar`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-transpose-star).

## Matrix of a bounded operator on $\ell^2$

The matrix of a bounded operator on `ℓ²(ℕ, 𝕜)`: entry `(i, j)` is the `i`-th
coordinate of the image of the `j`-th standard basis vector.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsMatrix`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-matrix).

## Operator with Hilbert–Schmidt matrix is the operator of its matrix

A bounded operator whose matrix is Hilbert–Schmidt is the Hilbert–Schmidt
operator of its matrix.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.eq_hsOperator_of_isHilbertSchmidt_matrix`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#eq-hs-operator-of-is-hilbert-schmidt-mat).

## Matrix of the Hilbert–Schmidt operator of a matrix

The matrix of a Hilbert–Schmidt operator is the matrix itself.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsMatrix_hsOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-matrix-hs-operator).

## Hilbert–Schmidt operator is independent of the summability proof

The Hilbert–Schmidt operator depends only on the matrix, not on the summability proof.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_congr`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-congr).

## Adjoint of a Hilbert–Schmidt operator

The adjoint of a Hilbert–Schmidt operator is the Hilbert–Schmidt operator
of the conjugate-transpose matrix.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.adjoint_hsOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#adjoint-hs-operator).

## Truncation of a matrix to its top-left block

The truncation of a matrix to the top-left `N × N` block.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsTrunc`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-trunc).

## Truncated matrices are Hilbert–Schmidt

A truncation of any matrix is Hilbert–Schmidt: it is supported on a finite set.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_hsTrunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-hs-trunc).

## Rank-one operators on $\ell^2$ are compact

A rank-one operator on `ℓ²` is compact: it factors through the one-dimensional space `𝕜`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isCompactOperator_rankOne`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-compact-operator-rank-one).

## Scaled rank-one operator on standard basis vectors

The action of a scaled rank-one operator on standard basis vectors, pointwise.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.rankOne_single_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#rank-one-single-apply).

## Truncated Hilbert–Schmidt operator as a sum of rank-one operators

A truncated Hilbert–Schmidt operator is a finite sum of rank-one operators.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_hsTrunc_eq_sum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-hs-trunc-eq-sum).

## Truncated Hilbert–Schmidt operators are compact

A truncated Hilbert–Schmidt operator is compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isCompactOperator_hsOperator_hsTrunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 486](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L486). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-compact-operator-hs-operator-hs-trunc).

## Hilbert–Schmidt norm of the truncation error as a tail sum

The squared Hilbert–Schmidt norm of the truncation error is the tail sum.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsNormSq_sub_hsTrunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-norm-sq-sub-hs-trunc).

## Square partial sums converge to the squared Hilbert–Schmidt norm

The partial sums of the squared norms over expanding squares converge to `hsNormSq`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.tendsto_hsTrunc_finset_sum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 553](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L553). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#tendsto-hs-trunc-finset-sum).

## Hilbert–Schmidt norm of the truncation error tends to zero

The squared Hilbert–Schmidt norm of the truncation error tends to zero.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.tendsto_hsNormSq_sub_hsTrunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#tendsto-hs-norm-sq-sub-hs-trunc).

## Truncated operators converge in norm to the Hilbert–Schmidt operator

The truncated operators converge in norm to the Hilbert–Schmidt operator.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.tendsto_hsOperator_hsTrunc`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#tendsto-hs-operator-hs-trunc).

## Hilbert–Schmidt operators on $\ell^2$ are compact

Every Hilbert–Schmidt operator on `ℓ²(ℕ, 𝕜)` is compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isCompactOperator_hsOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 609](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L609). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-compact-operator-hs-operator).

## Bounded operator with Hilbert–Schmidt matrix is compact

A bounded operator whose matrix is Hilbert–Schmidt is compact.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isCompactOperator_of_isHilbertSchmidt_matrix`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 615](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L615). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-compact-operator-of-is-hilbert-schmid).

## Operator norm bounded by the Hilbert–Schmidt norm

A bounded operator whose matrix is Hilbert–Schmidt has norm at most its
Hilbert–Schmidt norm.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.norm_le_of_isHilbertSchmidt_matrix`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#norm-le-of-is-hilbert-schmidt-matrix).

## Diagonal infinite matrix

The diagonal matrix with diagonal `d`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsDiagonal`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-diagonal).

## Rows of a diagonal matrix are square-summable

A row of a diagonal matrix is square-summable.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_hsDiagonal_row`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-hs-diagonal-row).

## Squared row norm of a diagonal matrix

The squared norms in a row of a diagonal matrix sum to the squared diagonal entry.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.tsum_hsDiagonal_row`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 645](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L645). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#tsum-hs-diagonal-row).

## Diagonal matrix with square-summable diagonal is Hilbert–Schmidt

A diagonal matrix with square-summable diagonal is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_hsDiagonal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-hs-diagonal).

## Hilbert–Schmidt norm of a diagonal matrix

The squared Hilbert–Schmidt norm of a diagonal matrix is the sum of the squared
diagonal entries.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsNormSq_hsDiagonal`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 666](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L666). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-norm-sq-hs-diagonal).

## Diagonal Hilbert–Schmidt operator acts by pointwise multiplication

A diagonal Hilbert–Schmidt operator acts by pointwise multiplication by the diagonal.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_hsDiagonal_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-hs-diagonal-apply).

## Rank-one infinite matrix

The rank-one matrix `u i * star (v j)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsRankOne`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-rank-one).

## Entries of a rank-one matrix are square-summable

The squared norms of the entries of a rank-one matrix are summable over the product.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.summable_hsRankOne_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 692](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L692). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#summable-hs-rank-one-sq).

## Rank-one matrix of $\ell^2$ vectors is Hilbert–Schmidt

A rank-one matrix with `ℓ²` vectors is Hilbert–Schmidt.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.isHilbertSchmidt_hsRankOne`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#is-hilbert-schmidt-hs-rank-one).

## Action of a rank-one Hilbert–Schmidt operator

A rank-one Hilbert–Schmidt operator acts as the inner product with `v` times `u`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsOperator_hsRankOne_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-operator-hs-rank-one-apply).

## Hilbert–Schmidt norm of a rank-one matrix

The squared Hilbert–Schmidt norm of a rank-one matrix is `‖u‖² * ‖v‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.hsNormSq_hsRankOne`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 721](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L721). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#hs-norm-sq-hs-rank-one).

## Canonical Hilbert–Schmidt norm equals the matrix norm

In the standard `ℓ²` basis, the existing extended operator squared norm
equals the finite matrix squared norm. This bridge is specialized to real
scalars because the canonical operator norm API is real-only.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.canonical_hsNormSq_eq_ofReal_matrix`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#canonical-hs-norm-sq-eq-of-real-matrix).

## Canonical Hilbert–Schmidt norm of the constructed operator

The constructed real Hilbert–Schmidt operator has the canonical extended
squared norm given by the finite squared norm of its matrix.

Formalized by `MathlibExt.Analysis.InnerProductSpace.HilbertSchmidt.canonical_hsNormSq_hsOperator`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/HilbertSchmidt.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#canonical-hs-norm-sq-hs-operator).

## The Hilbert–Schmidt norm of a finite-rank operator is controlled by its operator norm

There is a function $C$ from the natural numbers to the positive reals with the following
property. Let $H$ be an infinite-dimensional separable real Hilbert space, let
$(u_i)_{i \in \mathbb{N}}$ be a Hilbert basis of $H$, and let $T : H \to H$ be a bounded linear
operator such that the quotient $H/\ker T$ is finite-dimensional, of dimension $n$. Then the
Hilbert–Schmidt norm of $T$ computed in the basis $(u_i)$, taken in $[0,\infty]$, satisfies

$$\Big(\sum_{i \in \mathbb{N}} \|Tu_i\|^2\Big)^{1/2} \le C(n)\,\|T\|,$$

where $\|T\|$ is the operator norm of $T$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_98`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.HilbertSchmidtFiniteRankBoundWanted.exists_hsNorm_le_mul_opNorm_of_finiteDimensional_quotient_ker` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/HilbertSchmidtFiniteRankBoundWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/HilbertSchmidtFiniteRankBoundWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#exists-hs-norm-le-mul-op-norm-of-finite).

## The Hilbert–Schmidt norm bounds an operator on unit vectors

Let $H$ be a real Hilbert
space, let $T : H \to H$ be a bounded linear operator, and let $(u_n)_{n \in \mathbb{N}}$ be an
orthonormal basis of $H$ indexed by the natural numbers. Let
$\|T\|_{\mathrm{HS}} = \bigl(\sum_{n} \|T u_n\|^2\bigr)^{1/2} \in [0, \infty]$ be the
Hilbert–Schmidt norm of $T$ computed in this basis; it is $\infty$ when the series diverges.
Then $\|Tx\| \le \|T\|_{\mathrm{HS}}$ for every $x \in H$ with $\|x\| = 1$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; Special classes of linear operators), problem `ma_proofbench_l2_68`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.NormApplyLeHilbertSchmidtNormWanted.norm_apply_le_hsNorm_of_norm_eq_one` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/NormApplyLeHilbertSchmidtNormWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/OperatorTheory/NormApplyLeHilbertSchmidtNormWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html#norm-apply-le-hs-norm-of-norm-eq-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert–Schmidt operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/compact-and-fredholm/hilbert-schmidt-operators)
