---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsLocalRing
mathlib_file: Mathlib/RingTheory/LocalRing/Defs.lean
---

# Local ring

A semiring is local if it is nontrivial and `a` or `b` is a unit whenever `a + b = 1`.
Note that `IsLocalRing` is a predicate.

```lean
IsLocalRing.{u_1} (R : Type u_1) [Semiring R] : Prop
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `IsLocalRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/LocalRing/Defs.html#IsLocalRing)
- [Source of `IsLocalRing` in Mathlib/RingTheory/LocalRing/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/LocalRing/Defs.lean#L27)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L70)
