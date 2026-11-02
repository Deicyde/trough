---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: RingHom.quotientKerEquivOfSurjective
mathlib_file: Mathlib/RingTheory/Ideal/Quotient/Operations.lean
---

# First isomorphism theorem for commutative rings

The **first isomorphism theorem** for commutative rings, surjective case.

```lean
RingHom.quotientKerEquivOfSurjective.{u, v} {R : Type u} {S : Type v} [Ring R] [Semiring S]
  {f : R →+* S} (hf : Function.Surjective ⇑f) : R ⧸ RingHom.ker f ≃+* S
```

## Depends on

- [Quotient ring](quotient-ring.md)
- [Ring morphism](../rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `RingHom.quotientKerEquivOfSurjective`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Operations.html#RingHom.quotientKerEquivOfSurjective)
- [Source of `RingHom.quotientKerEquivOfSurjective` in Mathlib/RingTheory/Ideal/Quotient/Operations.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/Quotient/Operations.lean#L88)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L81)
