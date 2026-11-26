---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.mapMatrix_constantCoeff_star, SpaceTimeAlgebra.coeff_sum_X_smul_map_pderiv, SpaceTimeAlgebra.coeff_mul_apply_congr_left, SpaceTimeAlgebra.coeff_mul_apply_congr_right, SpaceTimeAlgebra.matrix_eq_zero_of_euler_eq_mul_add_mul, SpaceTimeAlgebra.eulerStep, SpaceTimeAlgebra.coeff_eulerStep_apply, SpaceTimeAlgebra.exists_matrix_eulerTransport
statement: formalized
proof: formalized
---

# Matrices over the jet ring

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Matrix`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean): 38 declarations, 36 with a docstring.

> Matrices of jets, their derivatives and Taylor coefficients, and the Euler (radial) transport.

## i. Overview

> A gauge transformation near a point is a matrix with entries in `SpaceTimeAlgebra`, the jets at
> that point. This file collects what is needed to work with such matrices entrywise.
>
> The central construction is the Euler (radial) transport. The Euler operator
> `E = ∑_ρ x_ρ ∂_ρ` multiplies a Taylor coefficient of degree `n` by `n`. Hence a matrix of jets
> `W` vanishing at the base point with `E W = A W + W B`, for `A` and `B` vanishing at the base
> point, is zero, since each of its coefficients is a multiple of coefficients of lower degree.
> The same recursion, run forwards, solves the radial system `E U = R U` with `U = 1` at the base
> point. This fundamental solution is unitary when `R` is anti-hermitian and has determinant one
> when `R` is traceless, and its Maurer–Cartan matrix `(∂_μ U) U⁻¹` solves a linear radial system.
> This is how a Lie algebra jet is integrated radially into a gauge jet, in
> `GlobalGaugeGroup.exists_sum_X_smul_maurerCartan_eq`.
>
> The remaining sections give the Leibniz rule for the Taylor coefficients of a product of
> matrices of jets, the derivatives of conjugates and inverses in terms of Maurer–Cartan
> matrices, and the invertible matrices of jets.

## ii. Key results

> - `SpaceTimeAlgebra.matrix_eq_zero_of_euler_eq_mul_add_mul` : the vanishing principle for the
>   Euler operator.
> - `SpaceTimeAlgebra.exists_matrix_eulerTransport` : the Euler transport of a matrix of jets
>   vanishing at the base point.
> - `SpaceTimeAlgebra.eulerTransport_mul_star`, `SpaceTimeAlgebra.eulerTransport_det` : the Euler
>   transport of an anti-hermitian, traceless matrix is unitary of determinant one.
> - `SpaceTimeAlgebra.euler_map_pderiv_mul_inv_of_eulerTransport` : the radial system solved by
>   the Maurer–Cartan matrix of an Euler transport.
> - `SpaceTimeAlgebra.map_coeff_mul` : the Taylor coefficients of a product of matrices of jets.
> - `SpaceTimeAlgebra.map_pderiv_conj_of_mul_eq_one` : the derivative of the conjugate of a
>   matrix of jets by an invertible one, in terms of its Maurer–Cartan matrix.
> - `SpaceTimeAlgebra.unitsEval`, `SpaceTimeAlgebra.unitsOfConstant` : evaluation at the base
>   point and the inclusion of constants, for invertible matrices.

## iv. References

> * None.

## A. The Euler operator and the Euler transport

**`SpaceTimeAlgebra.mapMatrix_constantCoeff_star`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L80).

> Entrywise evaluation at the base point commutes with the conjugate transpose.

```lean
lemma mapMatrix_constantCoeff_star {n : Type} [Fintype n] [DecidableEq n]
    (A : Matrix n n SpaceTimeAlgebra) :
    (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (star A) =
      star ((constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A)
```

**`SpaceTimeAlgebra.coeff_sum_X_smul_map_pderiv`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L89).

> The Euler operator on matrices of jets acts entrywise on Taylor coefficients as
> multiplication by the total degree.

```lean
lemma coeff_sum_X_smul_map_pderiv {κ : Type}
    (M : Matrix κ κ SpaceTimeAlgebra) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) (i j : κ) :
    coeff p ((∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ)) i j) =
      ((Finsupp.degree p : ℕ) : ℂ) * coeff p (M i j)
```

**`SpaceTimeAlgebra.coeff_mul_apply_congr_left`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L102).

> Multiplying on the left by a matrix of jets vanishing at the base point raises degrees, so
> the Taylor coefficient of `R M` in degree `|p|` only depends on the coefficients of `M` of
> lower degree.

```lean
lemma coeff_mul_apply_congr_left {κ : Type} [Fintype κ] {R : Matrix κ κ SpaceTimeAlgebra}
    (hR0 : ∀ i j, constantCoeff (R i j) = 0) (M N : Matrix κ κ SpaceTimeAlgebra)
    (p : (Fin 1 ⊕ Fin 3) →₀ ℕ)
    (h : ∀ (i j : κ) (q : (Fin 1 ⊕ Fin 3) →₀ ℕ), Finsupp.degree q < Finsupp.degree p →
      coeff q (M i j) = coeff q (N i j)) (i j : κ) :
    coeff p ((R * M) i j) = coeff p ((R * N) i j)
```

**`SpaceTimeAlgebra.coeff_mul_apply_congr_right`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L119).

> Multiplying on the right by a matrix of jets vanishing at the base point raises degrees.
> The transpose of `coeff_mul_apply_congr_left`.

```lean
lemma coeff_mul_apply_congr_right {κ : Type} [Fintype κ] {B : Matrix κ κ SpaceTimeAlgebra}
    (hB0 : ∀ i j, constantCoeff (B i j) = 0) (M N : Matrix κ κ SpaceTimeAlgebra)
    (p : (Fin 1 ⊕ Fin 3) →₀ ℕ)
    (h : ∀ (i j : κ) (q : (Fin 1 ⊕ Fin 3) →₀ ℕ), Finsupp.degree q < Finsupp.degree p →
      coeff q (M i j) = coeff q (N i j)) (i j : κ) :
    coeff p ((M * B) i j) = coeff p ((N * B) i j)
```

**`SpaceTimeAlgebra.matrix_eq_zero_of_euler_eq_mul_add_mul`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L133).

> The vanishing principle for the Euler operator. A matrix of jets vanishing at the
> base point and satisfying `E W = A W + W B` with `A`, `B` vanishing at the base point
> is zero. Each Taylor coefficient of `W` is a multiple of coefficients of strictly
> smaller degree, so all vanish by strong induction on the degree.

```lean
lemma matrix_eq_zero_of_euler_eq_mul_add_mul {κ : Type} [Fintype κ]
    {W : Matrix κ κ SpaceTimeAlgebra} (A B : Matrix κ κ SpaceTimeAlgebra)
    (hA : ∀ i j, constantCoeff (A i j) = 0) (hB : ∀ i j, constantCoeff (B i j) = 0)
    (h0 : ∀ i j, constantCoeff (W i j) = 0)
    (hW : ∑ ρ, (X ρ : SpaceTimeAlgebra) • W.map (pderiv ρ) = A * W + W * B) :
    W = 0
```

**`SpaceTimeAlgebra.eulerStep`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L176).

> One step of the Euler recursion for the radial system `E U = R U`. It is the identity
> plus `R M` with each Taylor coefficient of degree `n > 0` divided by `n`, and the Euler
> transport of `R` is its fixed point, reached degree by degree.

```lean
noncomputable def eulerStep {κ : Type} [Fintype κ] [DecidableEq κ]
    (R M : Matrix κ κ SpaceTimeAlgebra) : Matrix κ κ SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.coeff_eulerStep_apply`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L182).

> The Taylor coefficients of one step of the Euler recursion.

```lean
lemma coeff_eulerStep_apply {κ : Type} [Fintype κ] [DecidableEq κ]
    (R M : Matrix κ κ SpaceTimeAlgebra) (i j : κ) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    coeff p (eulerStep R M i j) = coeff p ((1 : Matrix κ κ SpaceTimeAlgebra) i j) +
      if p = 0 then 0 else ((Finsupp.degree p : ℕ) : ℂ)⁻¹ * coeff p ((R * M) i j)
```

**`SpaceTimeAlgebra.exists_matrix_eulerTransport`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L192).

> The Euler (radial) transport of a jet matrix `R` vanishing at the base point,
> a fundamental solution of the radial system `E U = R U` based at the identity,
> built order-by-order by the Euler recursion.

```lean
lemma exists_matrix_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    (R : Matrix κ κ SpaceTimeAlgebra) (hR0 : ∀ i j, constantCoeff (R i j) = 0) :
    ∃ U : Matrix κ κ SpaceTimeAlgebra, (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U = 1 ∧
      ∑ ρ, (X ρ : SpaceTimeAlgebra) • U.map (pderiv ρ) = R * U
```

**`SpaceTimeAlgebra.map_pderiv_sum_X_smul_map_pderiv`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L239).

> The formal derivative `∂_μ` and the Euler operator `E` on matrices of jets commute up to
> `∂_μ` itself, `∂_μ (E M) = E (∂_μ M) + ∂_μ M`, since `∂_μ x_ρ = δ_{μρ}`.

```lean
lemma map_pderiv_sum_X_smul_map_pderiv {κ : Type} (μ : Fin 1 ⊕ Fin 3)
    (M : Matrix κ κ SpaceTimeAlgebra) :
    (∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ)).map (pderiv μ) =
      ∑ ρ, (X ρ : SpaceTimeAlgebra) • (M.map (pderiv μ)).map (pderiv ρ) + M.map (pderiv μ)
```

## B. The Euler vanishing principle by degree on matrices

**`SpaceTimeAlgebra.coeff_entry_eq_zero_of_map_pderiv_eq_mul`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L260).

> The matrix form of `coeff_eq_zero_of_pderiv_eq_mul`. The entries of a matrix of power
> series satisfying `∂_ρ A = X_ρ A`, with the `X_ρ` vanishing below degree `n`, have no
> coefficients in nonzero degree up to `n`.

```lean
lemma coeff_entry_eq_zero_of_map_pderiv_eq_mul {κ : Type} [Fintype κ] {n : ℕ}
    {A : Matrix κ κ SpaceTimeAlgebra} {X : (Fin 1 ⊕ Fin 3) → Matrix κ κ SpaceTimeAlgebra}
    (hd : ∀ ρ, A.map (pderiv ρ) = X ρ * A)
    (hX : ∀ (ρ : Fin 1 ⊕ Fin 3) (q : (Fin 1 ⊕ Fin 3) →₀ ℕ), Finsupp.degree q < n →
      ∀ i j, coeff q (X ρ i j) = 0)
    (i j : κ) {p : (Fin 1 ⊕ Fin 3) →₀ ℕ} (hp : p ≠ 0) (hpn : Finsupp.degree p ≤ n) :
    coeff p (A i j) = 0
```

**`SpaceTimeAlgebra.matrix_map_truncation_eq_one`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L274).

> A matrix of power series with identity value and no coefficients in nonzero degree up
> to `n` truncates to the identity.

```lean
lemma matrix_map_truncation_eq_one {κ : Type} [Fintype κ] [DecidableEq κ] {n : ℕ}
    {A : Matrix κ κ SpaceTimeAlgebra}
        (h0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A = 1)
    (hA : ∀ (i j : κ) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ), p ≠ 0 → Finsupp.degree p ≤ n →
      coeff p (A i j) = 0) :
    A.map (SpaceTimeAlgebra.truncation n) = (1 : Matrix κ κ SpaceTimeAlgebra).map
        (SpaceTimeAlgebra.truncation n)
```

## C. Unitarity, determinant and Maurer–Cartan matrix of the Euler transport

**`SpaceTimeAlgebra.matrix_map_pderiv_mul`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L304).

> The entrywise Leibniz rule for matrix products of jets.

```lean
lemma matrix_map_pderiv_mul {κ : Type} [Fintype κ] (ρ : Fin 1 ⊕ Fin 3)
    (M N : Matrix κ κ SpaceTimeAlgebra) :
    (M * N).map (pderiv ρ) = M.map (pderiv ρ) * N + M * N.map (pderiv ρ)
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_mul`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L313).

> The Euler operator on matrices of jets is a derivation.

```lean
lemma sum_X_smul_map_pderiv_mul {κ : Type} [Fintype κ]
    (M N : Matrix κ κ SpaceTimeAlgebra) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (M * N).map (pderiv ρ) =
      (∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ)) * N +
        M * ∑ ρ, (X ρ : SpaceTimeAlgebra) • N.map (pderiv ρ)
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_star`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L323).

> The Euler operator commutes with the conjugate transpose.

```lean
lemma sum_X_smul_map_pderiv_star {κ : Type}
    (M : Matrix κ κ SpaceTimeAlgebra) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (star M).map (pderiv ρ) =
      star (∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ))
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_one`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L332).

> The Euler operator kills the identity matrix.

```lean
lemma sum_X_smul_map_pderiv_one {κ : Type} [DecidableEq κ] :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (1 : Matrix κ κ SpaceTimeAlgebra).map (pderiv ρ) = 0
```

**`SpaceTimeAlgebra.eulerTransport_mul_star`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L341).

> A fundamental solution of the radial system `E U = R U` based at the identity is
> unitary when `R` is anti-hermitian. `U U† − 1` vanishes at the base point and
> satisfies a homogeneous linear radial system, so it vanishes identically.

```lean
lemma eulerTransport_mul_star {κ : Type} [Fintype κ] [DecidableEq κ]
    {R U : Matrix κ κ SpaceTimeAlgebra} (hRstar : star R = -R)
    (hR0 : ∀ i j, constantCoeff (R i j) = 0)
    (hU0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U = 1)
    (hEU : ∑ ρ, (X ρ : SpaceTimeAlgebra) • U.map (pderiv ρ) = R * U) :
    U * star U = 1
```

**`SpaceTimeAlgebra.sum_X_smul_mcMatrix_of_eulerTransport`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L368).

> The radial Maurer–Cartan component of a unitary fundamental solution of the radial
> system `E V = −i P V` is `P`, `∑_μ x_μ · i (∂_μ V) V† = P`.

```lean
lemma sum_X_smul_mcMatrix_of_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    {P V : Matrix κ κ SpaceTimeAlgebra} (hVu : V * star V = 1)
    (hEV : ∑ μ, (X μ : SpaceTimeAlgebra) • V.map (pderiv μ) = ((-Complex.I) • P) * V) :
    ∑ μ, (X μ : SpaceTimeAlgebra) • (Complex.I • (V.map (pderiv μ) * star V)) = P
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_mul_inv_of_eulerTransport`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L383).

> The radial component of the Maurer–Cartan matrix of an invertible solution `V` of the
> radial system `E V = R V` is `R`, `∑_μ x_μ (∂_μ V) V⁻¹ = R`.

```lean
lemma sum_X_smul_map_pderiv_mul_inv_of_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    {R V W : Matrix κ κ SpaceTimeAlgebra} (hVW : V * W = 1)
    (hEV : ∑ μ, (X μ : SpaceTimeAlgebra) • V.map (pderiv μ) = R * V) :
    ∑ μ, (X μ : SpaceTimeAlgebra) • (V.map (pderiv μ) * W) = R
```

**`SpaceTimeAlgebra.euler_map_pderiv_mul_inv_of_eulerTransport`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L393).

> The Maurer–Cartan matrix `ω = (∂_μ V) V⁻¹` of an invertible solution `V` of the radial
> system `E V = R V` solves the linear radial system `E ω + ω = ∂_μ R + R ω − ω R`. This is
> `∂_μ` of the radial system, with `∂_μ E = E ∂_μ + ∂_μ` and `E V⁻¹ = −V⁻¹ R`.

```lean
lemma euler_map_pderiv_mul_inv_of_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    (μ : Fin 1 ⊕ Fin 3) {R V W : Matrix κ κ SpaceTimeAlgebra} (hVW : V * W = 1)
    (hWV : W * V = 1)
    (hEV : ∑ ρ, (X ρ : SpaceTimeAlgebra) • V.map (pderiv ρ) = R * V) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (V.map (pderiv μ) * W).map (pderiv ρ) +
        V.map (pderiv μ) * W =
      R.map (pderiv μ) + (R * (V.map (pderiv μ) * W) - V.map (pderiv μ) * W * R)
```

**`SpaceTimeAlgebra.eulerTransport_det`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L422).

> A fundamental solution of the radial system `E U = R U` based at the identity has
> determinant one when `R` is traceless. By Jacobi's formula the determinant is killed
> by the Euler operator, so it is the constant `1`.

```lean
lemma eulerTransport_det {κ : Type} [Fintype κ] [DecidableEq κ]
    {R U : Matrix κ κ SpaceTimeAlgebra}
    (hjac : ∀ (M : Matrix κ κ SpaceTimeAlgebra) (μ : Fin 1 ⊕ Fin 3),
      pderiv μ M.det = (M.map (pderiv μ) * M.adjugate).trace)
    (hRtr : R.trace = 0)
    (hU0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U = 1)
    (hEU : ∑ ρ, (X ρ : SpaceTimeAlgebra) • U.map (pderiv ρ) = R * U) :
    U.det = 1
```

## D. The Leibniz rule at the base point for matrices of power series

**`SpaceTimeAlgebra.matrix_multiset_sum_apply`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L458).

> The entry of a multiset sum of matrices is the multiset sum of the entries.

```lean
lemma matrix_multiset_sum_apply {κ α : Type*} [AddCommMonoid α]
    (m : Multiset (Matrix κ κ α)) (i j : κ) :
    m.sum i j = (m.map fun A => A i j).sum
```

**`SpaceTimeAlgebra.matrix_constantCoeff_iteratedPDeriv_mul`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L469).

> The matrix Leibniz rule at the base point. The base-point Taylor coefficients of a
> product of matrices of jets are the antidiagonal convolution of the base-point
> coefficients of the factors.

```lean
lemma matrix_constantCoeff_iteratedPDeriv_mul {κ : Type} [Fintype κ]
    (s : Multiset (Fin 1 ⊕ Fin 3)) (M N : Matrix κ κ SpaceTimeAlgebra) :
    ((M * N).map fun f => constantCoeff (iteratedPDeriv s f))
      = (s.antidiagonal.map fun p =>
          (M.map fun f => constantCoeff (iteratedPDeriv p.1 f)) *
            (N.map fun f => constantCoeff (iteratedPDeriv p.2 f))).sum
```

**`SpaceTimeAlgebra.map_coeff_mul`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L485).

> The Taylor coefficients of a product of matrices of jets are the antidiagonal
> convolution of the Taylor coefficients of the factors.

```lean
lemma map_coeff_mul {κ : Type} [Fintype κ] (M N : Matrix κ κ SpaceTimeAlgebra)
    (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) :
    (M * N).map (coeff p) =
      ∑ x ∈ Finset.antidiagonal p, M.map (coeff x.1) * N.map (coeff x.2)
```

**`SpaceTimeAlgebra.matrix_constantCoeff_iteratedPDeriv_commutator`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L495).

> The matrix Leibniz rule at the base point for a commutator. The base-point Taylor
> coefficients of `M N − N M` are sums of commutators of base-point Taylor coefficients.

```lean
lemma matrix_constantCoeff_iteratedPDeriv_commutator {κ : Type} [Fintype κ]
    (s : Multiset (Fin 1 ⊕ Fin 3)) (M N : Matrix κ κ SpaceTimeAlgebra) :
    ((M * N - N * M).map fun f => constantCoeff (iteratedPDeriv s f))
      = (s.antidiagonal.map fun p =>
          (M.map fun f => constantCoeff (iteratedPDeriv p.1 f)) *
            (N.map fun f => constantCoeff (iteratedPDeriv p.2 f)) -
          (N.map fun f => constantCoeff (iteratedPDeriv p.2 f)) *
            (M.map fun f => constantCoeff (iteratedPDeriv p.1 f))).sum
```

## E. Conjugation and derivatives of matrices of jets

**`SpaceTimeAlgebra.star_map_pderiv`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L525).

> The entrywise derivative commutes with the conjugate transpose.

```lean
lemma star_map_pderiv (μ : Fin 1 ⊕ Fin 3) (A : Matrix κ κ SpaceTimeAlgebra) :
    star (A.map (pderiv μ)) = (star A).map (pderiv μ)
```

**`SpaceTimeAlgebra.map_pderiv_sub`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L532).

> The entrywise derivative of a difference.

```lean
lemma map_pderiv_sub (μ : Fin 1 ⊕ Fin 3) (M N : Matrix κ κ SpaceTimeAlgebra) :
    (M - N).map (pderiv μ) = M.map (pderiv μ) - N.map (pderiv μ)
```

**`SpaceTimeAlgebra.map_pderiv_of_mul_eq_one`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L539).

> The entrywise derivative of the inverse `V` of a matrix of jets `U`, through the
> differentiated relation `U V = 1`, `∂_μ V = −V (∂_μ U) V`.

```lean
lemma map_pderiv_of_mul_eq_one [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U V : Matrix κ κ SpaceTimeAlgebra} (hUV : U * V = 1) (hVU : V * U = 1) :
    V.map (pderiv μ) = -(V * U.map (pderiv μ) * V)
```

**`SpaceTimeAlgebra.map_pderiv_star_of_unitary`**, a lemma, [line 554](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L554).

> The entrywise derivative of the conjugate transpose of a unitary matrix, through the
> differentiated unitarity relation.

```lean
lemma map_pderiv_star_of_unitary [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U : Matrix κ κ SpaceTimeAlgebra}
    (hU : U * star U = 1) (hU' : star U * U = 1) :
    (star U).map (pderiv μ) = -(star U * U.map (pderiv μ) * star U)
```

**`SpaceTimeAlgebra.map_pderiv_conj_of_mul_eq_one`**, a lemma, [line 563](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L563).

> The derivative of the conjugate `V A U` of a matrix of jets by an invertible matrix of
> jets `U` with inverse `V`, in terms of the Maurer–Cartan matrix `ω = (∂_μ U) V`,
> `∂_μ (V A U) = V (∂_μ A − (ω A − A ω)) U`.

```lean
lemma map_pderiv_conj_of_mul_eq_one [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U V : Matrix κ κ SpaceTimeAlgebra} (hUV : U * V = 1) (hVU : V * U = 1)
    (A : Matrix κ κ SpaceTimeAlgebra) :
    (V * A * U).map (pderiv μ) = V * (A.map (pderiv μ) -
      (U.map (pderiv μ) * V * A - A * (U.map (pderiv μ) * V))) * U
```

**`SpaceTimeAlgebra.map_pderiv_mul_mul_mul`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L574).

> The cocycle law of Maurer–Cartan matrices, for invertible matrices of jets `U₁`, `U₂`
> with inverses `V₁`, `V₂`, `∂_μ (U₁ U₂) (V₂ V₁) = (∂_μ U₁) V₁ + U₁ ((∂_μ U₂) V₂) V₁`.

```lean
lemma map_pderiv_mul_mul_mul [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U₁ U₂ V₁ V₂ : Matrix κ κ SpaceTimeAlgebra} (h : U₂ * V₂ = 1) :
    (U₁ * U₂).map (pderiv μ) * (V₂ * V₁) =
      U₁.map (pderiv μ) * V₁ + U₁ * (U₂.map (pderiv μ) * V₂) * V₁
```

**`SpaceTimeAlgebra.map_pderiv_commutator`**, a lemma, [line 584](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L584).

> The derivative of a commutator of matrices of jets.

```lean
lemma map_pderiv_commutator [Fintype κ] (μ : Fin 1 ⊕ Fin 3) (A B : Matrix κ κ SpaceTimeAlgebra) :
    (A * B - B * A).map (pderiv μ) = (A.map (pderiv μ) * B - B * A.map (pderiv μ))
      + (A * B.map (pderiv μ) - B.map (pderiv μ) * A)
```

**`SpaceTimeAlgebra.map_pderiv_mapMatrix_C`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L591).

> A constant matrix of jets has vanishing derivatives.

```lean
lemma map_pderiv_mapMatrix_C [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    (A : Matrix κ κ ℂ) : ((C : ℂ →+* SpaceTimeAlgebra).mapMatrix A).map (pderiv μ) = 0
```

**`SpaceTimeAlgebra.star_mcMatrix`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L597).

> The Maurer–Cartan matrix `i (∂_μ U) U†` of a unitary matrix of jets is hermitian.

```lean
lemma star_mcMatrix [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U : Matrix κ κ SpaceTimeAlgebra}
    (hU : U * star U = 1) (hU' : star U * U = 1) :
    star (Complex.I • (U.map (pderiv μ) * star U)) = Complex.I • (U.map (pderiv μ) * star U)
```

## F. Invertible matrices of jets

**`SpaceTimeAlgebra.unitsEval`**, a def, [line 618](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L618).

> Evaluation of an invertible matrix of jets at the base point, entrywise.

```lean
noncomputable def unitsEval : (Matrix κ κ SpaceTimeAlgebra)ˣ →* (Matrix κ κ ℂ)ˣ
```

**`SpaceTimeAlgebra.unitsEval_val`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L622).

```lean
lemma unitsEval_val (U : (Matrix κ κ SpaceTimeAlgebra)ˣ) :
    (unitsEval U : Matrix κ κ ℂ) = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U
```

**`SpaceTimeAlgebra.unitsOfConstant`**, a def, [line 626](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L626).

> An invertible matrix as a constant invertible matrix of jets, entrywise.

```lean
noncomputable def unitsOfConstant : (Matrix κ κ ℂ)ˣ →* (Matrix κ κ SpaceTimeAlgebra)ˣ
```

**`SpaceTimeAlgebra.unitsOfConstant_val`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L630).

```lean
lemma unitsOfConstant_val (g : (Matrix κ κ ℂ)ˣ) :
    (unitsOfConstant g : Matrix κ κ SpaceTimeAlgebra) =
      (C : ℂ →+* SpaceTimeAlgebra).mapMatrix g
```

**`SpaceTimeAlgebra.unitsEval_unitsOfConstant`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L635).

> A constant invertible matrix of jets evaluates to itself at the base point.

```lean
lemma unitsEval_unitsOfConstant (g : (Matrix κ κ ℂ)ˣ) : unitsEval (unitsOfConstant g) = g
```

## Depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](spacetimealgebra-basic.md)

## Proof depends on

- [Sums over the antidiagonal of a multiset](../../mathematics/part-01/multisetantidiagonal.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean)
