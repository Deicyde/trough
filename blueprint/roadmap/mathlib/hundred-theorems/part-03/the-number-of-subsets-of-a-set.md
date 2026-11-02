---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Finset.card_powerset
mathlib_file: Mathlib/Data/Finset/Powerset.lean
---

# The Number of Subsets of a Set

**Number of Subsets of a Set**

```lean
Finset.card_powerset.{u_1} {α : Type u_1} (s : Finset α) : s.powerset.card = 2 ^ s.card
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Array](../../overview/data-structures/list-like-structures/array.md)
- [Integer](../../overview/general-algebra/numbers/integer.md)

## Sources

- [Mathlib documentation: `Finset.card_powerset`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Powerset.html#Finset.card_powerset)
- [Source of `Finset.card_powerset` in Mathlib/Data/Finset/Powerset.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/Finset/Powerset.lean#L100)
- [Freek Wiedijk's 100 theorems, no. 52](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L269)
