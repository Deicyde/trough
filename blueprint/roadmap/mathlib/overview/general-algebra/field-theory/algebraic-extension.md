---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Algebra.IsAlgebraic
mathlib_file: Mathlib/RingTheory/Algebraic/Defs.lean
---

# Algebraic extension

An algebra is algebraic if all its elements are algebraic.

```lean
Algebra.IsAlgebraic.{u, v} (R : Type u) (A : Type v) [CommRing R] [Ring A] [Algebra R A] : Prop
```

## Depends on

- [Algebraic elements](../../../undergraduate/ring-theory/field-theory/part-01/algebraic-elements.md)

## Sources

- [Mathlib documentation: `Algebra.IsAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Algebra.IsAlgebraic)
- [Source of `Algebra.IsAlgebraic` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Algebraic/Defs.lean#L66)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L130)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L184)
