---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: IsFractionRing
mathlib_file: Mathlib/RingTheory/Localization/FractionRing.lean
---

# Field of fractions of an integral domain

`IsFractionRing R K` states `K` is the ring of fractions of a commutative ring `R`.

```lean
IsFractionRing.{u_6, u_7} (R : Type u_6) [CommSemiring R] (K : Type u_7) [CommSemiring K]
  [Algebra R K] : Prop
```

## Depends on

- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `IsFractionRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/FractionRing.html#IsFractionRing)
- [Source of `IsFractionRing` in Mathlib/RingTheory/Localization/FractionRing.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Localization/FractionRing.lean#L51)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L129)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L181)
