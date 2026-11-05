---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsAlgebraic
mathlib_file: Mathlib/RingTheory/Algebraic/Defs.lean
---

# Algebraic elements

An element of an R-algebra is algebraic over R if it is a root of a nonzero polynomial
with coefficients in R.

```lean
IsAlgebraic.{u, v} (R : Type u) {A : Type v} [CommRing R] [Ring A] [Algebra R A] (x : A) : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Linear map](../../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Polynomial in one indeterminate](../../../../overview/general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `IsAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#IsAlgebraic)
- [Source of `IsAlgebraic` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Algebraic/Defs.lean#L42)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L182)
