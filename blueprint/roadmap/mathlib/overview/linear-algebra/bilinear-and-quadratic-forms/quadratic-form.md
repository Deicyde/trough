---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: QuadraticForm
mathlib_file: Mathlib/LinearAlgebra/QuadraticForm/Basic.lean
---

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
- [Source of `QuadraticForm` in Mathlib/LinearAlgebra/QuadraticForm/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/QuadraticForm/Basic.lean#L159)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L207)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Quadratic forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L204)
