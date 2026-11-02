---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Finset.addDysonETransform
mathlib_file: Mathlib/Combinatorics/Additive/ETransform.lean
---

# Dyson transform

The **Dyson e-transform**.
Turns `(s, t)` into `(s ∪ e +ᵥ t, t ∩ -e +ᵥ s)`. This reduces the sum of the two sets.

```lean
Finset.addDysonETransform.{u_1} {α : Type u_1} [DecidableEq α] [AddCommGroup α] (e : α)
  (x : Finset α × Finset α) : Finset α × Finset α
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Finset.addDysonETransform`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/ETransform.html#Finset.addDysonETransform)
- [Source of `Finset.addDysonETransform` in Mathlib/Combinatorics/Additive/ETransform.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/ETransform.lean#L54)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L549)
