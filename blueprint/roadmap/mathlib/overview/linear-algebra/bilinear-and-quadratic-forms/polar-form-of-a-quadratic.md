# Polar form of a quadratic

Up to a factor 2, `Q.polar` is the associated bilinear map for a quadratic map `Q`.

Source of this name: https://en.wikipedia.org/wiki/Quadratic_form#Generalization

```lean
QuadraticMap.polar.{u_4, u_5} {M : Type u_4} {N : Type u_5} [AddCommGroup M] [AddCommGroup N]
  (f : M → N) (x y : M) : N
```

## Depends on

- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `QuadraticMap.polar`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#QuadraticMap.polar)
- [Source of `QuadraticMap.polar` in Mathlib/LinearAlgebra/QuadraticForm/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/QuadraticForm/Basic.lean#L92)
- [Mathlib overview: Linear algebra › Bilinear and quadratic forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L208)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Quadratic forms](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L205)
