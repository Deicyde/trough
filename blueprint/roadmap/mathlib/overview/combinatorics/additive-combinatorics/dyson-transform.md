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
- [Source of `Finset.addDysonETransform` in Mathlib/Combinatorics/Additive/ETransform.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/Additive/ETransform.lean#L54)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L549)
