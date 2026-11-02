---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: LinearMap.toMatrix
mathlib_file: Mathlib/LinearAlgebra/Matrix/ToLin.lean
---

# Matrix representation of a linear map

Given bases of two modules `M₁` and `M₂` over a commutative ring `R`, we get a linear
equivalence between linear maps `M₁ →ₗ M₂` and matrices over `R` indexed by the bases.

```lean
LinearMap.toMatrix.{u_1, u_3, u_4, u_5, u_6} {R : Type u_1} [CommSemiring R] {m : Type u_3}
  {n : Type u_4} [Fintype n] [Finite m] [DecidableEq n] {M₁ : Type u_5} {M₂ : Type u_6}
  [AddCommMonoid M₁] [AddCommMonoid M₂] [_root_.Module R M₁] [_root_.Module R M₂]
  (v₁ : Module.Basis n R M₁) (v₂ : Module.Basis m R M₂) : (M₁ →ₗ[R] M₂) ≃ₗ[R] Matrix m n R
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Isomorphism with $K^n$](../finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Ring-valued matrix](ring-valued-matrix.md)

## Sources

- [Mathlib documentation: `LinearMap.toMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ToLin.html#LinearMap.toMatrix)
- [Source of `LinearMap.toMatrix` in Mathlib/LinearAlgebra/Matrix/ToLin.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/ToLin.lean#L581)
- [Mathlib overview: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L191)
- [Mathlib undergraduate list: Linear algebra › Matrices](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L44)
