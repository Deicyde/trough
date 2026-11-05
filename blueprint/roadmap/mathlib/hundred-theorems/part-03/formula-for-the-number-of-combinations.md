---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.card_powersetCard, Finset.mem_powersetCard
mathlib_file: Mathlib/Data/Finset/Powerset.lean
---

# Formula for the Number of Combinations

Mathlib records this with 2 declarations.

`Finset.card_powersetCard`: **Formula for the Number of Combinations**

```lean
Finset.card_powersetCard.{u_1} {α : Type u_1} (n : ℕ) (s : Finset α) :
  (Finset.powersetCard n s).card = s.card.choose n
```

`Finset.mem_powersetCard`.

```lean
Finset.mem_powersetCard.{u_1} {α : Type u_1} {n : ℕ} {s t : Finset α} :
  s ∈ Finset.powersetCard n t ↔ s ⊆ t ∧ s.card = n
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.card_powersetCard`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Powerset.html#Finset.card_powersetCard)
- [Source of `Finset.card_powersetCard` in Mathlib/Data/Finset/Powerset.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Finset/Powerset.lean#L209)
- [Mathlib documentation: `Finset.mem_powersetCard`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Powerset.html#Finset.mem_powersetCard)
- [Source of `Finset.mem_powersetCard` in Mathlib/Data/Finset/Powerset.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Finset/Powerset.lean#L201)
- [Freek Wiedijk's 100 theorems, no. 58](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L297)
