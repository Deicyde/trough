---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: LinearMap.BilinForm.toMatrix
mathlib_file: Mathlib/LinearAlgebra/Matrix/BilinearForm.lean
---

# Matrix representation

`BilinForm.toMatrix b` is the equivalence between `R`-bilinear forms on `M` and
`n`-by-`n` matrices with entries in `R`, if `b` is an `R`-basis for `M`.

```lean
LinearMap.BilinForm.toMatrix.{u_1, u_2, u_5} {R₁ : Type u_1} {M₁ : Type u_2} [CommSemiring R₁]
  [AddCommMonoid M₁] [_root_.Module R₁ M₁] {n : Type u_5} [Fintype n] [DecidableEq n]
  (b : Module.Basis n R₁ M₁) : LinearMap.BilinForm R₁ M₁ ≃ₗ[R₁] Matrix n n R₁
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Bilinear form](bilinear-form.md)
- [Isomorphism with $K^n$](../finite-dimensional-vector-spaces/isomorphism-with-k-n.md)
- [Ring-valued matrix](../matrices/ring-valued-matrix.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.toMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/BilinearForm.html#LinearMap.BilinForm.toMatrix)
- [Source of `LinearMap.BilinForm.toMatrix` in Mathlib/LinearAlgebra/Matrix/BilinearForm.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/BilinearForm.lean#L185)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L206)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Bilinear forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L200)
