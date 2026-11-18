# The Number of Subsets of a Set

**Number of Subsets of a Set**

```lean
Finset.card_powerset.{u_1} {α : Type u_1} (s : Finset α) : s.powerset.card = 2 ^ s.card
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Finset.card_powerset`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finset/Powerset.html#Finset.card_powerset)
- [Source of `Finset.card_powerset` in Mathlib/Data/Finset/Powerset.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Finset/Powerset.lean#L100)
- [Freek Wiedijk's 100 theorems, no. 52](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L269)
