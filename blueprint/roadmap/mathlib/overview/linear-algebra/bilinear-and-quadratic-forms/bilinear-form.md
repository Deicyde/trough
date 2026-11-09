# Bilinear form

For convenience, a shorthand for the type of bilinear forms from `M` to `R`.

```lean
LinearMap.BilinForm.{u_2, u_5} (R : Type u_2) [CommSemiring R] (M : Type u_5) [AddCommMonoid M]
  [_root_.Module R M] : Type (max u_2 u_5)
```

## Depends on

- [Linear map](../fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearMap.html#LinearMap.BilinForm)
- [Source of `LinearMap.BilinForm` in Mathlib/LinearAlgebra/BilinearMap.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/BilinearMap.lean#L537)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L203)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Bilinear forms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L196)
