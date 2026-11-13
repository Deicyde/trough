---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.mapMatrix_constantCoeff_star, SpaceTimeAlgebra.coeff_sum_X_smul_map_pderiv, SpaceTimeAlgebra.matrix_eq_zero_of_euler_eq_mul_add_mul, SpaceTimeAlgebra.exists_matrix_eulerTransport, SpaceTimeAlgebra.coeff_entry_eq_zero_of_map_pderiv_eq_mul, SpaceTimeAlgebra.matrix_map_truncation_eq_one, SpaceTimeAlgebra.matrix_map_pderiv_mul, SpaceTimeAlgebra.sum_X_smul_map_pderiv_mul
statement: formalized
proof: formalized
---

# Matrices over the jet ring

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Matrix`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean): 23 declarations, 23 with a docstring.

## i. Overview

> Results about matrices with entries in `SpaceTimeAlgebra`, chiefly the Euler (radial) transport: a
> matrix of jets vanishing at the base point is the radial logarithmic derivative of a formal
> fundamental solution.

## ii. Key results

> - `mapMatrix_constantCoeff_star` : entrywise evaluation at the base point commutes with the
>   conjugate transpose
> - `coeff_sum_X_smul_map_pderiv` : the Euler operator on matrices of jets acts entrywise on Taylor
>   coefficients as multiplication by the total degree
> - `matrix_eq_zero_of_euler_eq_mul_add_mul` : the vanishing principle for the Euler operator: a
>   matrix of jets vanishing at the base point and satisfying `E W = A W + W B` with `A`, `B`
>   vanishing at the base point is zero
> - `exists_matrix_eulerTransport` : the Euler (radial) transport of a jet matrix `R` vanishing at the
>   base point: a fundamental solution of the radial system `E U = R U` based at the identity, built
>   order-by-order by the Euler recursion

## iv. References

> * None.

## A. The Euler operator toolkit on matrices

**`SpaceTimeAlgebra.mapMatrix_constantCoeff_star`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L61).

> Entrywise evaluation at the base point commutes with the conjugate transpose.

```lean
lemma mapMatrix_constantCoeff_star {n : Type} [Fintype n] [DecidableEq n]
    (A : Matrix n n SpaceTimeAlgebra) :
    (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (star A) =
      star ((constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A)
```

**`SpaceTimeAlgebra.coeff_sum_X_smul_map_pderiv`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L70).

> The Euler operator on matrices of jets acts entrywise on Taylor coefficients as
> multiplication by the total degree.

```lean
lemma coeff_sum_X_smul_map_pderiv {κ : Type}
    (M : Matrix κ κ SpaceTimeAlgebra) (p : (Fin 1 ⊕ Fin 3) →₀ ℕ) (i j : κ) :
    coeff p ((∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ)) i j) =
      ((Finsupp.degree p : ℕ) : ℂ) * coeff p (M i j)
```

**`SpaceTimeAlgebra.matrix_eq_zero_of_euler_eq_mul_add_mul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L84).

> The vanishing principle for the Euler operator: a matrix of jets vanishing at the
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

**`SpaceTimeAlgebra.exists_matrix_eulerTransport`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L145).

> The Euler (radial) transport of a jet matrix `R` vanishing at the base point:
> a fundamental solution of the radial system `E U = R U` based at the identity,
> built order-by-order by the Euler recursion.

```lean
lemma exists_matrix_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    (R : Matrix κ κ SpaceTimeAlgebra) (hR0 : ∀ i j, constantCoeff (R i j) = 0) :
    ∃ U : Matrix κ κ SpaceTimeAlgebra, (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U = 1 ∧
      ∑ ρ, (X ρ : SpaceTimeAlgebra) • U.map (pderiv ρ) = R * U
```

## B. The Euler vanishing principle by degree on matrices

**`SpaceTimeAlgebra.coeff_entry_eq_zero_of_map_pderiv_eq_mul`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L217).

> The matrix form of `coeff_eq_zero_of_pderiv_eq_mul`: the entries of a matrix of power
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

**`SpaceTimeAlgebra.matrix_map_truncation_eq_one`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L231).

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

## C. Unitarity and determinant of the Euler transport

**`SpaceTimeAlgebra.matrix_map_pderiv_mul`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L261).

> The entrywise Leibniz rule for matrix products of jets.

```lean
lemma matrix_map_pderiv_mul {κ : Type} [Fintype κ] (ρ : Fin 1 ⊕ Fin 3)
    (M N : Matrix κ κ SpaceTimeAlgebra) :
    (M * N).map (pderiv ρ) = M.map (pderiv ρ) * N + M * N.map (pderiv ρ)
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_mul`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L270).

> The Euler operator on matrices of jets is a derivation.

```lean
lemma sum_X_smul_map_pderiv_mul {κ : Type} [Fintype κ]
    (M N : Matrix κ κ SpaceTimeAlgebra) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (M * N).map (pderiv ρ) =
      (∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ)) * N +
        M * ∑ ρ, (X ρ : SpaceTimeAlgebra) • N.map (pderiv ρ)
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_star`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L280).

> The Euler operator commutes with the conjugate transpose.

```lean
lemma sum_X_smul_map_pderiv_star {κ : Type}
    (M : Matrix κ κ SpaceTimeAlgebra) :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (star M).map (pderiv ρ) =
      star (∑ ρ, (X ρ : SpaceTimeAlgebra) • M.map (pderiv ρ))
```

**`SpaceTimeAlgebra.sum_X_smul_map_pderiv_one`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L289).

> The Euler operator kills the identity matrix.

```lean
lemma sum_X_smul_map_pderiv_one {κ : Type} [DecidableEq κ] :
    ∑ ρ, (X ρ : SpaceTimeAlgebra) • (1 : Matrix κ κ SpaceTimeAlgebra).map (pderiv ρ) = 0
```

**`SpaceTimeAlgebra.eulerTransport_mul_star`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L298).

> A fundamental solution of the radial system `E U = R U` based at the identity is
> unitary when `R` is anti-hermitian: `U U† − 1` vanishes at the base point and
> satisfies a homogeneous linear radial system, so it vanishes identically.

```lean
lemma eulerTransport_mul_star {κ : Type} [Fintype κ] [DecidableEq κ]
    {R U : Matrix κ κ SpaceTimeAlgebra} (hRstar : star R = -R)
    (hR0 : ∀ i j, constantCoeff (R i j) = 0)
    (hU0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U = 1)
    (hEU : ∑ ρ, (X ρ : SpaceTimeAlgebra) • U.map (pderiv ρ) = R * U) :
    U * star U = 1
```

**`SpaceTimeAlgebra.sum_X_smul_mcMatrix_of_eulerTransport`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L325).

> The radial Maurer–Cartan component of a unitary fundamental solution of the radial
> system `E V = −i P V` is `P`: `∑_μ x_μ · i (∂_μ V) V† = P`.

```lean
lemma sum_X_smul_mcMatrix_of_eulerTransport {κ : Type} [Fintype κ] [DecidableEq κ]
    {P V : Matrix κ κ SpaceTimeAlgebra} (hVu : V * star V = 1)
    (hEV : ∑ μ, (X μ : SpaceTimeAlgebra) • V.map (pderiv μ) = ((-Complex.I) • P) * V) :
    ∑ μ, (X μ : SpaceTimeAlgebra) • (Complex.I • (V.map (pderiv μ) * star V)) = P
```

**`SpaceTimeAlgebra.eulerTransport_det`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L341).

> A fundamental solution of the radial system `E U = R U` based at the identity has
> determinant one when `R` is traceless: by Jacobi's formula the determinant is killed
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

**`SpaceTimeAlgebra.matrix_multiset_sum_apply`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L377).

> The entry of a multiset sum of matrices is the multiset sum of the entries.

```lean
lemma matrix_multiset_sum_apply {κ α : Type*} [AddCommMonoid α]
    (m : Multiset (Matrix κ κ α)) (i j : κ) :
    m.sum i j = (m.map fun A => A i j).sum
```

**`SpaceTimeAlgebra.matrix_constantCoeff_iteratedPDeriv_mul`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L388).

> The matrix Leibniz rule at the base point: the base-point Taylor coefficients of a
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

## E. Conjugation, scalars and derivatives of matrices of jets

**`SpaceTimeAlgebra.mapMatrix_C_star`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L413).

> Entrywise inclusion of constants commutes with the conjugate transpose.

```lean
lemma mapMatrix_C_star [Fintype κ] [DecidableEq κ] (A : Matrix κ κ ℂ) :
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix (star A) = star
        ((C : ℂ →+* SpaceTimeAlgebra).mapMatrix A)
```

**`SpaceTimeAlgebra.mapMatrix_C_smul`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L420).

> Entrywise inclusion of constants commutes with complex scalars.

```lean
lemma mapMatrix_C_smul [Fintype κ] [DecidableEq κ] (c : ℂ) (M : Matrix κ κ ℂ) :
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix (c • M) = c •
        (C : ℂ →+* SpaceTimeAlgebra).mapMatrix M
```

**`SpaceTimeAlgebra.mapMatrix_constantCoeff_smul`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L428).

> The entrywise constant coefficient commutes with complex scalars.

```lean
lemma mapMatrix_constantCoeff_smul [Fintype κ] [DecidableEq κ] (c : ℂ)
    (M : Matrix κ κ SpaceTimeAlgebra) :
    (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix (c • M)
      = c • (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix M
```

**`SpaceTimeAlgebra.star_map_pderiv`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L436).

> The entrywise derivative commutes with the conjugate transpose.

```lean
lemma star_map_pderiv (μ : Fin 1 ⊕ Fin 3) (A : Matrix κ κ SpaceTimeAlgebra) :
    star (A.map (pderiv μ)) = (star A).map (pderiv μ)
```

**`SpaceTimeAlgebra.map_pderiv_smul`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L443).

> Pulling a complex scalar out of the entrywise derivative.

```lean
lemma map_pderiv_smul (μ : Fin 1 ⊕ Fin 3) (c : ℂ) (M : Matrix κ κ SpaceTimeAlgebra) :
    (c • M).map (pderiv μ) = c • M.map (pderiv μ)
```

**`SpaceTimeAlgebra.map_pderiv_sub`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L448).

> The entrywise derivative of a difference.

```lean
lemma map_pderiv_sub (μ : Fin 1 ⊕ Fin 3) (M N : Matrix κ κ SpaceTimeAlgebra) :
    (M - N).map (pderiv μ) = M.map (pderiv μ) - N.map (pderiv μ)
```

**`SpaceTimeAlgebra.map_pderiv_star_of_unitary`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L455).

> The entrywise derivative of the conjugate transpose of a unitary matrix, through the
> differentiated unitarity relation.

```lean
lemma map_pderiv_star_of_unitary [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U : Matrix κ κ SpaceTimeAlgebra}
    (hU : U * star U = 1) (hU' : star U * U = 1) :
    (star U).map (pderiv μ) = -(star U * U.map (pderiv μ) * star U)
```

**`SpaceTimeAlgebra.star_mcMatrix`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean#L470).

> The Maurer–Cartan matrix `i (∂_μ U) U†` of a unitary matrix of jets is hermitian.

```lean
lemma star_mcMatrix [Fintype κ] [DecidableEq κ] (μ : Fin 1 ⊕ Fin 3)
    {U : Matrix κ κ SpaceTimeAlgebra}
    (hU : U * star U = 1) (hU' : star U * U = 1) :
    star (Complex.I • (U.map (pderiv μ) * star U)) = Complex.I • (U.map (pderiv μ) * star U)
```

## Depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](spacetimealgebra-basic.md)

## Proof depends on

- [Sums over the antidiagonal of a multiset](../../mathematics/part-01/multisetantidiagonal.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Matrix.lean)
