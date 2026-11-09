# Orthogonal elements

A set of vectors `v` is orthogonal with respect to some bilinear form `B` if and only
if for all `i ≠ j`, `B (v i) (v j) = 0`.

```lean
LinearMap.BilinForm.iIsOrtho.{w, u_1, u_2} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] {n : Type w} (B : LinearMap.BilinForm R M) (v : n → M) :
  Prop
```

## Depends on

- [Bilinear form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/bilinear-form.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.iIsOrtho`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearForm/Orthogonal.html#LinearMap.BilinForm.iIsOrtho)
- [Source of `LinearMap.BilinForm.iIsOrtho` in Mathlib/LinearAlgebra/BilinearForm/Orthogonal.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/BilinearForm/Orthogonal.lean#L63)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Orthogonality](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L207)
