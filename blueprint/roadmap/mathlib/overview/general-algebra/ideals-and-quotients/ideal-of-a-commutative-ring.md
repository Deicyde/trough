---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: Ideal
mathlib_file: Mathlib/RingTheory/Ideal/Defs.lean
---

# Ideal of a commutative ring

A (left) ideal in a semiring `R` is an additive submonoid `s` such that
`a * b ∈ s` whenever `b ∈ s`. If `R` is a ring, then `s` is an additive subgroup.

```lean
Ideal.{u} (R : Type u) [Semiring R] : Type u
```

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)

## Sources

- [Mathlib documentation: `Ideal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Defs.html#Ideal)
- [Source of `Ideal` in Mathlib/RingTheory/Ideal/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/Defs.lean#L38)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L75)
- [Mathlib undergraduate list: Ring Theory › Ideals and Quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L132)
