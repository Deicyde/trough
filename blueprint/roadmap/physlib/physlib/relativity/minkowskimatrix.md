---
declaration: module
origin: cited
lean: minkowskiMatrix, minkowskiMatrix.as_diagonal, minkowskiMatrix.as_block, minkowskiMatrix.inl_0_inl_0, minkowskiMatrix.inr_i_inr_i, minkowskiMatrix.off_diag_zero, minkowskiMatrix.η_diag_ne_zero, minkowskiMatrix.vecMul_apply
statement: formalized
proof: formalized
---

# The Minkowski matrix

The module `Physlib.Relativity.MinkowskiMatrix`, [Physlib/Relativity/MinkowskiMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean): 27 declarations, 24 with a docstring.

## i. Overview

> The aim of this module is to define the Minkowski matrix `η` in `d+1` dimensions, and
> prove properties thereof.
>
> The Minkowski matrix is the real matrix of the form `diag(1, -1, -1, -1, ...)`,
> It is related to the Minkowski metric on `ℝ^(d+1)`.
>
> Related to the Minkowski matrix is the notion of the dual of a matrix with respect to
> the Minkowski metric. This is defined as `η * Λᵀ * η`, where `Λ` is a real matrix.
> This will be used to help define the Lorentz group in later files.

## ii. Key results

> - `minkowskiMatrix` : The Minkowski matrix in `d+1` dimensions.
> - `minkowskiMatrix.dual` : The dual of a matrix with respect to the Minkowski metric,
>   defined to be `η * Λᵀ * η`.

## iv. References

> * None.

## A. The Minkowski Matrix

> We first define the Minkowski matrix in `d+1` dimensions, and prove some basic properties.

**`minkowskiMatrix`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L70).

> The `d.succ`-dimensional real matrix of the form `diag(1, -1, -1, -1, ...)`.

```lean
def minkowskiMatrix {d : ℕ} : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

### A.1. Basic equalities

> We show some basic equalities for the Minkowski matrix.
> In particular, we show it can be expressed as a block matrix.

**`minkowskiMatrix.as_diagonal`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L86).

> The Minkowski matrix as a diagonal matrix.

```lean
lemma as_diagonal : @minkowskiMatrix d = diagonal (Sum.elim 1 (-1))
```

**`minkowskiMatrix.as_block`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L90).

> The Minkowski matrix as a block matrix.

```lean
lemma as_block : minkowskiMatrix =
    Matrix.fromBlocks (1 : Matrix (Fin 1) (Fin 1) ℝ) 0 0 (-1 : Matrix (Fin d) (Fin d) ℝ)
```

### A.2. Notation for the Minkowski matrix

> We define the notation `η` for the Minkowski matrix, which can be used when the namespace
> `minkowskiMatrix` is opened.

### A.3. Components of the Minkowski matrix

> We prove some simple properties related to the components of the Minkowski matrix.

**`minkowskiMatrix.inl_0_inl_0`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L116).

> The `time-time` component of the Minkowski matrix is `1`.

```lean
lemma inl_0_inl_0 : @minkowskiMatrix d (Sum.inl 0) (Sum.inl 0) = 1
```

**`minkowskiMatrix.inr_i_inr_i`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L121).

> The space diagonal components of the Minkowski matrix are `-1`.

```lean
lemma inr_i_inr_i (i : Fin d) : @minkowskiMatrix d (Sum.inr i) (Sum.inr i) = -1
```

**`minkowskiMatrix.off_diag_zero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L126).

> The off diagonal elements of the Minkowski matrix are zero.

```lean
lemma off_diag_zero {μ ν : Fin 1 ⊕ Fin d} (h : μ ≠ ν) : η μ ν = 0
```

**`minkowskiMatrix.η_diag_ne_zero`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L129).

```lean
lemma η_diag_ne_zero {μ : Fin 1 ⊕ Fin d} : η μ μ ≠ 0
```

**`minkowskiMatrix.vecMul_apply`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L134).

> Right multiplication of a row vector by the Minkowski matrix multiplies each component by
> the corresponding diagonal sign.

```lean
lemma vecMul_apply (v : (Fin 1 ⊕ Fin d) → ℝ) (μ : Fin 1 ⊕ Fin d) :
    (v ᵥ* minkowskiMatrix) μ = v μ * minkowskiMatrix μ μ
```

### A.4. Squaring the Minkowski matrix

> we show that the Minkowski matrix is self-inverting, i.e. `η * η = 1`,
> as well as other properties related to squaring the Minkowski matrix.

**`minkowskiMatrix.sq`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L150).

> The Minkowski matrix is self-inverting.

```lean
lemma sq : @minkowskiMatrix d * minkowskiMatrix = 1
```

**`minkowskiMatrix.η_apply_mul_η_apply_diag`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L155).

> Multiplying any element on the diagonal of the Minkowski matrix by itself gives `1`.

```lean
lemma η_apply_mul_η_apply_diag (μ : Fin 1 ⊕ Fin d) : η μ μ * η μ μ = 1
```

**`minkowskiMatrix.η_apply_sq_eq_one`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L159).

```lean
lemma η_apply_sq_eq_one (μ : Fin 1 ⊕ Fin d) : η μ μ ^ 2 = 1
```

### A.5. Symmetry properties of the Minkowski matrix

> The Minkowski matrix is symmetric, due to it being diagonal.

**`minkowskiMatrix.eq_transpose`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L172).

> The Minkowski matrix is symmetric.

```lean
lemma eq_transpose : minkowskiMatrixᵀ = @minkowskiMatrix d
```

### A.6. Determinant of the Minkowski matrix

> We show the determinant of the Minkowski matrix is equal to `(-1)^d` where
> `d` is the number of spatial dimensions.

**`minkowskiMatrix.det_eq_neg_one_pow_d`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L187).

> The determinant of the Minkowski matrix is equal to `-1` to the power
> of the number of spatial dimensions.

```lean
lemma det_eq_neg_one_pow_d : (@minkowskiMatrix d).det = (- 1) ^ d
```

**`minkowskiMatrix.prod_diagonal`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L191).

> The product of all diagonal entries of the Minkowski matrix is `(-1) ^ d`.

```lean
lemma prod_diagonal : ∏ μ : Fin 1 ⊕ Fin d, minkowskiMatrix μ μ = (-1) ^ d
```

**`minkowskiMatrix.prod_diagonal_comp_of_injective`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L198).

> Reindexing all diagonal entries injectively does not change their product.

```lean
lemma prod_diagonal_comp_of_injective {v : Fin (d + 1) → Fin 1 ⊕ Fin d}
    (hv : Function.Injective v) :
    ∏ i, minkowskiMatrix (v i) (v i) = (-1) ^ d
```

### A.7. Injective properties of multiplying diagonal components

> If `x` and `y` are reals then since `η μ μ` is non-zero for any `μ`, the equation
> `η μ μ * x = η μ μ * y` implies `x = y`. We prove this as a lemma.
> This is a useful part of the API but is not used often.

**`minkowskiMatrix.mul_η_diag_eq_iff`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L219).

```lean
lemma mul_η_diag_eq_iff {μ : Fin 1 ⊕ Fin d} {x y : ℝ} :
    η μ μ * x = η μ μ * y ↔ x = y
```

### A.8. Action of the Minkowski matrix on vectors

> We show properties of the action of the Minkowski matrix on vectors.

**`minkowskiMatrix.mulVec_inl_0`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L233).

> The time components of a vector acted on by the Minkowski matrix remains unchanged.

```lean
lemma mulVec_inl_0 (v : (Fin 1 ⊕ Fin d) → ℝ) :
    (η *ᵥ v) (Sum.inl 0) = v (Sum.inl 0)
```

**`minkowskiMatrix.mulVec_inr_i`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L239).

> The space components of a vector acted on by the Minkowski matrix swaps sign.

```lean
lemma mulVec_inr_i (v : (Fin 1 ⊕ Fin d) → ℝ) (i : Fin d) :
    (η *ᵥ v) (Sum.inr i) = - v (Sum.inr i)
```

## B. The Minkowski dual

> Given a real matrix `Λ`, we define the dual of `Λ` with respect to the Minkowski metric
> to be `η * Λᵀ * η`.
>
> The ultimate idea is that for the Minkowski inner product
> `⟪Λ x, y⟫ = ⟪x, dual Λ y⟫` for all vectors `x` and `y`.
>
> An element `Λ` is in the Lorentz group if and only if `dual Λ = Λ⁻¹`. This will not be
> shown in this module.
>
> This notion of a dual is not quite a homomorphism because it reverses the order of multiplication.

**`minkowskiMatrix.dual`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L263).

> The dual of a matrix with respect to the Minkowski metric.
> A suitable name for this construction is the Minkowski dual.

```lean
def dual : Matrix (Fin 1 ⊕ Fin d) (Fin 1 ⊕ Fin d) ℝ
```

### B.1. The dual on the identity

> We show that the dual of the identity matrix is the identity matrix.

**`minkowskiMatrix.dual_id`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L275).

> The Minkowski dual of the identity is the identity.

```lean
lemma dual_id : @dual d 1 = 1
```

### B.2. The dual swaps multiplication

> We show that the dual swaps multiplication, i.e. `dual (Λ * Λ') = dual Λ' * dual Λ`.

**`minkowskiMatrix.dual_mul`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L288).

> The Minkowski dual swaps multiplications (acts contravariantly).

```lean
lemma dual_mul : dual (Λ * Λ') = dual Λ' * dual Λ
```

### B.3. The dual is an involution

> We show that the dual is an involution, i.e. `dual (dual Λ) = Λ`.

**`minkowskiMatrix.dual_dual`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L301).

> The Minkowski dual is involutive (i.e. `dual (dual Λ)) = Λ`).

```lean
lemma dual_dual : Function.Involutive (@dual d)
```

### B.4. The dual commutes with the transpose

**`minkowskiMatrix.dual_transpose`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L314).

> The Minkowski dual commutes with the transpose.

```lean
lemma dual_transpose : dual Λᵀ = (dual Λ)ᵀ
```

### B.5. The dual preserves the Minkowski matrix

**`minkowskiMatrix.dual_eta`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L325).

> The Minkowski dual preserves the Minkowski matrix.

```lean
lemma dual_eta : @dual d η = η
```

### B.6. The dual preserves the determinants

**`minkowskiMatrix.det_dual`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L336).

> The Minkowski dual preserves determinants.

```lean
lemma det_dual : (dual Λ).det = Λ.det
```

### B.7. Components of the dual

> We show a number of properties related to the components of the duals.

**`minkowskiMatrix.dual_apply`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L352).

> Expansion of the components of the Minkowski dual in terms of the components
> of the original matrix.

```lean
lemma dual_apply (μ ν : Fin 1 ⊕ Fin d) :
    dual Λ μ ν = η μ μ * Λ ν μ * η ν ν
```

**`minkowskiMatrix.dual_apply_minkowskiMatrix`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean#L358).

> The components of the Minkowski dual of a matrix multiplied by the Minkowski matrix
> in terms of the original matrix.

```lean
lemma dual_apply_minkowskiMatrix (μ ν : Fin 1 ⊕ Fin d) :
    dual Λ μ ν * η ν ν = η μ μ * Λ ν μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/MinkowskiMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/MinkowskiMatrix.lean)
