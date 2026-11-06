# Change of coordinates

Mathlib states this as `LinearMap.BilinForm.toMatrix_comp`.

```lean
LinearMap.BilinForm.toMatrix_comp.{u_1, u_2, u_5, u_6, u_7} {R₁ : Type u_1} {M₁ : Type u_2}
  [CommSemiring R₁] [AddCommMonoid M₁] [_root_.Module R₁ M₁] {n : Type u_5} {o : Type u_6}
  [Fintype n] [Fintype o] [DecidableEq n] (b : Module.Basis n R₁ M₁) {M₂' : Type u_7}
  [AddCommMonoid M₂'] [_root_.Module R₁ M₂'] (c : Module.Basis o R₁ M₂') [DecidableEq o]
  (B : LinearMap.BilinForm R₁ M₁) (l r : M₂' →ₗ[R₁] M₁) :
  (LinearMap.BilinForm.toMatrix c) (B.comp l r) =
    ((LinearMap.toMatrix c b) l).transpose * (LinearMap.BilinForm.toMatrix b) B *
      (LinearMap.toMatrix c b) r
```

## Depends on

- [Matrix representation](../../../overview/linear-algebra/bilinear-and-quadratic-forms/matrix-representation.md)
- [Matrix representation of a linear map](../../../overview/linear-algebra/matrices/matrix-representation-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.toMatrix_comp`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/BilinearForm.html#LinearMap.BilinForm.toMatrix_comp)
- [Source of `LinearMap.BilinForm.toMatrix_comp` in Mathlib/LinearAlgebra/Matrix/BilinearForm.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Matrix/BilinearForm.lean#L251)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Bilinear forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L201)
