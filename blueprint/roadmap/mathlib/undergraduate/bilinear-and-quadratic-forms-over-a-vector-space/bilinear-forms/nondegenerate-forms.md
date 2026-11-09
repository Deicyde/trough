# Nondegenerate forms

A nondegenerate bilinear form is a bilinear form that is both left-separating and
right-separating, i.e. if `B x y = 0` for all `y` then `x = 0`, and if `B x y = 0` for all `x` then
`y = 0`.

Note that these conditions are independent of each other in general, but in the common case of
finite-dimensional vector spaces (or, more generally, finite free modules over an integral
domain), either of these conditions implies the other; see
`LinearMap.BilinForm.Nondegenerate.ofSeparatingLeft` and
`LinearMap.BilinForm.nondegenerate_iff_ker_eq_bot`, proved in a later file.

```lean
LinearMap.BilinForm.Nondegenerate.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [AddCommMonoid M] [_root_.Module R M] (B : LinearMap.BilinForm R M) : Prop
```

## Depends on

- [Bilinear form](../../../overview/linear-algebra/bilinear-and-quadratic-forms/bilinear-form.md)

## Sources

- [Mathlib documentation: `LinearMap.BilinForm.Nondegenerate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearForm/Properties.html#LinearMap.BilinForm.Nondegenerate)
- [Source of `LinearMap.BilinForm.Nondegenerate` in Mathlib/LinearAlgebra/BilinearForm/Properties.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/BilinearForm/Properties.lean#L280)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Bilinear forms](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L199)
