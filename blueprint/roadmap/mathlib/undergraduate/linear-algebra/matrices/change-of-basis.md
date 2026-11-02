---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix
mathlib_file: Mathlib/LinearAlgebra/Matrix/Basis.lean
---

# Change of basis

Mathlib states this as `basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix`.

```lean
basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix.{u_1, u_2, u_3, u_4, u_5, u_6, u_9}
  {ι : Type u_1} {ι' : Type u_2} {κ : Type u_3} {κ' : Type u_4} {R : Type u_5} {M : Type u_6}
  [CommSemiring R] [AddCommMonoid M] [_root_.Module R M] {N : Type u_9} [AddCommMonoid N]
  [_root_.Module R N] (b : Module.Basis ι R M) (b' : Module.Basis ι' R M) (c : Module.Basis κ R N)
  (c' : Module.Basis κ' R N) (f : M →ₗ[R] N) [Fintype ι'] [Finite κ] [Fintype ι] [Fintype κ']
  [DecidableEq ι] [DecidableEq ι'] :
  c.toMatrix ⇑c' * (LinearMap.toMatrix b' c') f * b'.toMatrix ⇑b = (LinearMap.toMatrix b c) f
```

## Depends on

- [Matrix representation of a linear map](../../../overview/linear-algebra/matrices/matrix-representation-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Basis.html#basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix)
- [Source of `basis_toMatrix_mul_linearMap_toMatrix_mul_basis_toMatrix` in Mathlib/LinearAlgebra/Matrix/Basis.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/Basis.lean#L201)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L45)
