---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: IsOrderedRing
mathlib_file: Mathlib/Algebra/Order/Ring/Defs.lean
---

# Ordered ring

An ordered semiring is a semiring with a partial order such that addition is monotone and
multiplication by a nonnegative number is monotone.

```lean
IsOrderedRing.{u_1} (R : Type u_1) [Semiring R] [PartialOrder R] : Prop
```

## Depends on

- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `IsOrderedRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Ring/Defs.html#IsOrderedRing)
- [Source of `IsOrderedRing` in Mathlib/Algebra/Order/Ring/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Order/Ring/Defs.lean#L62)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L72)
