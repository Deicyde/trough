---
declaration: theorem
origin: cited
lean: LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det
statement: formalized
proof: formalized
---

# Hermite's inequality

A symmetric positive definite integral bilinear form `B` on a free
`ℤ`-module of rank `n ≥ 1` takes on some nonzero vector `x` a value with
`3 ^ (n choose 2) · B(x, x) ^ n ≤ 4 ^ (n choose 2) · det B`, where `det B` is the Gram determinant
of `B` in any basis. Equivalently `B(x, x) ≤ (4 / 3) ^ ((n - 1) / 2) · (det B) ^ (1 / n)`.

```lean
LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det.{u_1, u_2} {M : Type u_1}
  [AddCommGroup M] [Nontrivial M] {ι : Type u_2} [Fintype ι] [DecidableEq ι]
  (B : LinearMap.BilinForm ℤ M) (hB : B.IsSymm)
  (hpos : (LinearMap.BilinMap.toQuadraticMap B).PosDef) (b : Module.Basis ι ℤ M) :
  ∃ x,
    x ≠ 0 ∧
      3 ^ (Fintype.card ι).choose 2 * (B x) x ^ Fintype.card ι ≤
        4 ^ (Fintype.card ι).choose 2 * ((LinearMap.BilinForm.toMatrix b) B).det
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Hermite.html#LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/Hermite.html#LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det)
- [Source of `LinearMap.BilinForm.exists_ne_zero_three_pow_mul_pow_le_four_pow_mul_det` in TauCeti/LinearAlgebra/BilinearForm/Hermite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/BilinearForm/Hermite.lean#L198)
