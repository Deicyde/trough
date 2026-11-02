---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Ideal.IsPrime
mathlib_file: Mathlib/RingTheory/Ideal/Prime.lean
---

# Prime ideal

An ideal `P` of a ring `R` is prime if `P ≠ R` and `xy ∈ P → x ∈ P ∨ y ∈ P`

```lean
Ideal.IsPrime.{u} {α : Type u} [Semiring α] (I : Ideal α) : Prop
```

## Depends on

- [Ideal of a commutative ring](ideal-of-a-commutative-ring.md)

## Sources

- [Mathlib documentation: `Ideal.IsPrime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime)
- [Source of `Ideal.IsPrime` in Mathlib/RingTheory/Ideal/Prime.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/Prime.lean#L39)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L77)
- [Mathlib undergraduate list: Ring Theory › Ideals and Quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L134)
