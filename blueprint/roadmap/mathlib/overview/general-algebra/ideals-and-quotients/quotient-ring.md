---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Ideal.Quotient.ring
mathlib_file: Mathlib/RingTheory/Ideal/Quotient/Defs.lean
---

# Quotient ring

**Quotient ring**: the quotient of a ring by a two-sided ideal is a ring.

```lean
Ideal.Quotient.ring.{u} {R : Type u} [Ring R] (I : Ideal R) [I.IsTwoSided] : Ring (R ⧸ I)
```

## Depends on

- [Ideal of a commutative ring](ideal-of-a-commutative-ring.md)
- [Quotient space](../../linear-algebra/fundamentals/quotient-space.md)

## Sources

- [Mathlib documentation: `Ideal.Quotient.ring`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Defs.html#Ideal.Quotient.ring)
- [Source of `Ideal.Quotient.ring` in Mathlib/RingTheory/Ideal/Quotient/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/Quotient/Defs.lean#L63)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L76)
- [Mathlib undergraduate list: Ring Theory › Ideals and Quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L133)
