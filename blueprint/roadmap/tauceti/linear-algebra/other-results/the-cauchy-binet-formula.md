---
declaration: theorem
origin: cited
lean: TauCeti.det_mul_transpose_eq_sum_plucker_mul, Matrix.det_mul_transpose_eq_sum_plucker_sq, TauCeti.det_mul_conjTranspose_eq_sum_plucker_mul_star
statement: formalized
proof: formalized
---

# The Cauchy–Binet formula

The determinant of the `p × p` matrix of pairwise products
`∑ₖ x i k * y j k` is the sum over the `p`-element subsets `s` of `ι` of the products of the
Plücker coordinates of `x` and `y` at `s`. For `p > #ι` both sides vanish.

```lean
TauCeti.det_mul_transpose_eq_sum_plucker_mul.{u_1, u_3} {R : Type u_1} {ι : Type u_3} [CommRing R]
  [LinearOrder ι] {p : ℕ} [Fintype ι] (x y : Fin p → ι → R) :
  (Matrix.of x * (Matrix.of y).transpose).det = ∑ s, TauCeti.plucker x s * TauCeti.plucker y s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.det_mul_transpose_eq_sum_plucker_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/Plucker.html#TauCeti.det_mul_transpose_eq_sum_plucker_mul).

## Other forms

**The Cauchy–Binet formula for a Gram determinant.** Formalized in Tau Ceti as [`Matrix.det_mul_transpose_eq_sum_plucker_sq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/Plucker.html#Matrix.det_mul_transpose_eq_sum_plucker_sq).

```lean
Matrix.det_mul_transpose_eq_sum_plucker_sq.{u_1, u_3} {R : Type u_1} {ι : Type u_3} [CommRing R]
  [LinearOrder ι] {p : ℕ} [Fintype ι] (A : Matrix (Fin p) ι R) :
  (A * A.transpose).det = ∑ s, TauCeti.plucker A.row s ^ 2
```

**The Cauchy–Binet formula, Hermitian form.** Formalized in Tau Ceti as [`TauCeti.det_mul_conjTranspose_eq_sum_plucker_mul_star`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/Plucker.html#TauCeti.det_mul_conjTranspose_eq_sum_plucker_mul_star).

```lean
TauCeti.det_mul_conjTranspose_eq_sum_plucker_mul_star.{u_1, u_3} {R : Type u_1} {ι : Type u_3}
  [CommRing R] [LinearOrder ι] {p : ℕ} [StarRing R] [Fintype ι] (x : Fin p → ι → R) :
  (Matrix.of x * (Matrix.of x).conjTranspose).det =
    ∑ s, TauCeti.plucker x s * star (TauCeti.plucker x s)
```

## Sources

- [Tau Ceti documentation: `TauCeti.det_mul_transpose_eq_sum_plucker_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/ExteriorPower/Plucker.html#TauCeti.det_mul_transpose_eq_sum_plucker_mul)
- [Source of `TauCeti.det_mul_transpose_eq_sum_plucker_mul` in TauCeti/LinearAlgebra/ExteriorPower/Plucker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/ExteriorPower/Plucker.lean#L241)
