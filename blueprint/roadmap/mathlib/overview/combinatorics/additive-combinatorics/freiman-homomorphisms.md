---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: IsAddFreimanHom
mathlib_file: Mathlib/Combinatorics/Additive/FreimanHom.lean
---

# Freiman homomorphisms

An additive `n`-Freiman homomorphism from a set `A` to a set `B` is a map which preserves sums
of `n` elements.

```lean
IsAddFreimanHom.{u_2, u_3} {α : Type u_2} {β : Type u_3} [AddCommMonoid α] [AddCommMonoid β] (n : ℕ)
  (A : Set α) (B : Set β) (f : α → β) : Prop
```

## Depends on

- [Multiset](../../data-structures/sets/multiset.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `IsAddFreimanHom`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/FreimanHom.html#IsAddFreimanHom)
- [Source of `IsAddFreimanHom` in Mathlib/Combinatorics/Additive/FreimanHom.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/FreimanHom.lean#L79)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L553)
