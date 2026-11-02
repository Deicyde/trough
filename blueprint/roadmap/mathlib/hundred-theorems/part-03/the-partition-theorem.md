---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.Partition.card_odds_eq_card_distincts
mathlib_file: Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean
---

# The Partition Theorem

Mathlib states this as `Nat.Partition.card_odds_eq_card_distincts`.

```lean
Nat.Partition.card_odds_eq_card_distincts (n : ℕ) :
  (Nat.Partition.odds n).card = (Nat.Partition.distincts n).card
```

## Depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../overview/data-structures/sets/set.md)

## Proof depends on

- [Glaisher's theorem](../../thousand-plus/number-theory/part-03/glaishers-theorem.md)

## Sources

- [Mathlib documentation: `Nat.Partition.card_odds_eq_card_distincts`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Partition/Glaisher.html#Nat.Partition.card_odds_eq_card_distincts)
- [Source of `Nat.Partition.card_odds_eq_card_distincts` in Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean#L159)
- [Freek Wiedijk's 100 theorems, no. 45](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L239)
- [1000+ theorems list: Q1082910](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1340)
- [1000+ theorems project: Q1082910](https://1000-plus.github.io/all.html?length=-1#Q1082910)
- [Wikipedia: Integer partition § Odd parts and distinct parts](https://en.wikipedia.org/wiki/Integer_partition#Odd_parts_and_distinct_parts)
- [Wikidata: Q1082910](https://www.wikidata.org/wiki/Q1082910)
