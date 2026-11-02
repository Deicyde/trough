---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Subring
mathlib_file: Mathlib/Algebra/Ring/Subring/Defs.lean
---

# Subring

`Subring R` is the type of subrings of `R`. A subring of `R` is a subset `s` that is a
multiplicative submonoid and an additive subgroup. Note in particular that it shares the
same 0 and 1 as R.

```lean
Subring.{u} (R : Type u) [NonAssocRing R] : Type u
```

## Depends on

- [Integer](../numbers/integer.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Subring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Subring/Defs.html#Subring)
- [Source of `Subring` in Mathlib/Algebra/Ring/Subring/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Ring/Subring/Defs.lean#L161)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L68)
- [Mathlib undergraduate list: Ring Theory › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L127)
