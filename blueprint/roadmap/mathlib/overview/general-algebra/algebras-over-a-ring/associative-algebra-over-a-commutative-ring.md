---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Algebra
mathlib_file: Mathlib/Algebra/Algebra/Defs.lean
---

# Associative algebra over a commutative ring

An associative unital `R`-algebra is a semiring `A` equipped with a map into its center `R → A`.

See the implementation notes in this file for discussion of the details of this definition.

```lean
Algebra.{u, v} (R : Type u) (A : Type v) [CommSemiring R] [Semiring A] : Type (max u v)
```

## Depends on

- [Ring morphism](../rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `Algebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Algebra/Defs.html#Algebra)
- [Source of `Algebra` in Mathlib/Algebra/Algebra/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Algebra/Defs.lean#L91)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L110)
- [Mathlib undergraduate list: Ring Theory › Algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L139)
