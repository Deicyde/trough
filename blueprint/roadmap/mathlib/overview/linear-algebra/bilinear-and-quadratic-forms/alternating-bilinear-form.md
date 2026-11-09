# Alternating bilinear form

The proposition that a bilinear form is alternating

```lean
LinearMap.BilinForm.IsAlt.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] (B : LinearMap.BilinForm R M) : Prop
```

## Depends on

- [Bilinear form](bilinear-form.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.IsAlt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearForm/Properties.html#LinearMap.BilinForm.IsAlt)
- [Source of `LinearMap.BilinForm.IsAlt` in Mathlib/LinearAlgebra/BilinearForm/Properties.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/BilinearForm/Properties.lean#L235)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L204)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Bilinear forms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L197)
