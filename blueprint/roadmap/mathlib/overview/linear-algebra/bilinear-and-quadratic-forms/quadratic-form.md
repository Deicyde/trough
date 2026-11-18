# Quadratic form

A quadratic form on a module.

```lean
QuadraticForm.{u, v} (R : Type u) (M : Type v) [CommSemiring R] [AddCommMonoid M]
  [_root_.Module R M] : Type (max u v)
```

## Depends on

- [Linear map](../fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `QuadraticForm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#QuadraticForm)
- [Source of `QuadraticForm` in Mathlib/LinearAlgebra/QuadraticForm/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/QuadraticForm/Basic.lean#L159)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L207)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Quadratic forms](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L204)
