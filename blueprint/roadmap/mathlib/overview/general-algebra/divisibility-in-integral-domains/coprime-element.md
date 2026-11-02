---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsCoprime
mathlib_file: Mathlib/RingTheory/Coprime/Basic.lean
---

# Coprime element

The proposition that `x` and `y` are coprime, defined to be the existence of `a` and `b` such
that `a * x + b * y = 1`. Note that elements with no common divisors are not necessarily coprime,
e.g., the multivariate polynomials `x₁` and `x₂` are not coprime.

```lean
IsCoprime.{u} {R : Type u} [CommSemiring R] (x y : R) : Prop
```

## Depends on

- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `IsCoprime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Coprime/Basic.html#IsCoprime)
- [Source of `IsCoprime` in Mathlib/RingTheory/Coprime/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Coprime/Basic.lean#L39)
- [Mathlib overview: General algebra › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L85)
- [Mathlib undergraduate list: Ring Theory › Divisibility in integral domains](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L143)
