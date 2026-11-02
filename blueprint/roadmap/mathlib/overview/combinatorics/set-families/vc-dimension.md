---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Finset.vcDim
mathlib_file: Mathlib/Combinatorics/SetFamily/Shatter.lean
---

# VC dimension

The Vapnik-Chervonenkis dimension of a set family is the maximal size of a set it shatters.

```lean
Finset.vcDim.{u_1} {α : Type u_1} [DecidableEq α] (𝒜 : Finset (Finset α)) : ℕ
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Finset.vcDim`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SetFamily/Shatter.html#Finset.vcDim)
- [Source of `Finset.vcDim` in Mathlib/Combinatorics/SetFamily/Shatter.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/SetFamily/Shatter.lean#L185)
- [Mathlib overview: Combinatorics › Set families](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L519)
