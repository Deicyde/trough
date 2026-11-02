---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Perfection
mathlib_file: Mathlib/RingTheory/Perfection.lean
---

# Perfection of a ring

The perfection of a monoid `α`, defined to be the projective limit of `α` using the `p`-th
power maps `α → α` indexed by the natural numbers, implemented as
`{ f : ℕ → M | ∀ n, f (n + 1) ^ p = f n }`.

If `α` is a ring with characteristic `p` and `p` is prime, `Perfection α p` is also a ring.

```lean
Perfection.{u₁} (α : Type u₁) [Pow α ℕ] (p : ℕ) : Type u₁
```

## Depends on

- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Perfection`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Perfection.html#Perfection)
- [Source of `Perfection` in Mathlib/RingTheory/Perfection.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Perfection.lean#L35)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L152)
