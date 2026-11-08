---
declaration: theorem
origin: cited
lean: Matrix.abv_det_le_prod_sum_abv, Matrix.abv_det_le_prod_sum_abv', Matrix.abs_det_le_prod_sum_abs', Matrix.abs_det_le_prod_sum_abs
statement: formalized
proof: formalized
---

# Hadamard's bound, `ℓ¹` row form

The absolute value of a determinant is at most the
product of the `ℓ¹` norms of the rows.

```lean
Matrix.abv_det_le_prod_sum_abv.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} [CommRing R]
  [Nontrivial R] [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {n : Type u_3} [Fintype n]
  [DecidableEq n] (A : Matrix n n R) (abv : AbsoluteValue R S) : abv A.det ≤ ∏ i, ∑ j, abv (A i j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.abv_det_le_prod_sum_abv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_sum_abv).

## Other forms

**Hadamard's bound, `ℓ¹` column form.** Formalized in Tau Ceti as [`Matrix.abv_det_le_prod_sum_abv'`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_sum_abv').

```lean
Matrix.abv_det_le_prod_sum_abv'.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} [CommRing R]
  [Nontrivial R] [CommRing S] [LinearOrder S] [IsStrictOrderedRing S] {n : Type u_3} [Fintype n]
  [DecidableEq n] (A : Matrix n n R) (abv : AbsoluteValue R S) : abv A.det ≤ ∏ j, ∑ i, abv (A i j)
```

**Hadamard's bound, `ℓ¹` column form, for `|·|`.** Formalized in Tau Ceti as [`Matrix.abs_det_le_prod_sum_abs'`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abs_det_le_prod_sum_abs').

```lean
Matrix.abs_det_le_prod_sum_abs'.{u_2, u_3} {S : Type u_2} [CommRing S] [LinearOrder S]
  [IsStrictOrderedRing S] {n : Type u_3} [Fintype n] [DecidableEq n] (A : Matrix n n S) :
  |A.det| ≤ ∏ j, ∑ i, |A i j|
```

**Hadamard's bound, `ℓ¹` row form, for `|·|`.** Formalized in Tau Ceti as [`Matrix.abs_det_le_prod_sum_abs`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abs_det_le_prod_sum_abs).

```lean
Matrix.abs_det_le_prod_sum_abs.{u_2, u_3} {S : Type u_2} [CommRing S] [LinearOrder S]
  [IsStrictOrderedRing S] {n : Type u_3} [Fintype n] [DecidableEq n] (A : Matrix n n S) :
  |A.det| ≤ ∏ i, ∑ j, |A i j|
```

## Sources

- [Tau Ceti documentation: `Matrix.abv_det_le_prod_sum_abv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.html#Matrix.abv_det_le_prod_sum_abv)
- [Source of `Matrix.abv_det_le_prod_sum_abv` in TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/AbsoluteValue.lean#L69)
