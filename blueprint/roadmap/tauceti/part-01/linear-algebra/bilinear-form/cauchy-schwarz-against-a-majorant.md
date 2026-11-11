---
declaration: theorem
origin: cited
lean: LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply
statement: formalized
proof: formalized
---

# Cauchy-Schwarz against a majorant

If `F` is a symmetric positive semidefinite bilinear
form and `F x x ≤ F x z`, then `F x v ^ 2 ≤ F z z * F v v` for every `v`.

```lean
LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] [AddCommGroup M] [_root_.Module R M]
  (F : LinearMap.BilinForm R M) (hnonneg : ∀ (x : M), 0 ≤ (F x) x) (hsymm : LinearMap.IsSymm F)
  {x z : M} (hle : (F x) x ≤ (F x) z) (v : M) : (F x) v ^ 2 ≤ (F z) z * (F v) v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/PosSemidef.html#LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/BilinearForm/PosSemidef.html#LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply)
- [Source of `LinearMap.BilinForm.apply_sq_le_mul_of_apply_le_apply` in TauCeti/LinearAlgebra/BilinearForm/PosSemidef.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/BilinearForm/PosSemidef.lean#L67)
