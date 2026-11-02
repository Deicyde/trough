---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Nat.Partition.card_restricted_eq_card_countRestricted
mathlib_file: Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean
---

# Glaisher's theorem

Mathlib states this as `Nat.Partition.card_restricted_eq_card_countRestricted`.

```lean
Nat.Partition.card_restricted_eq_card_countRestricted (n : ℕ) {m : ℕ} (hm : 0 < m) :
  (Nat.Partition.restricted n fun x => ¬m ∣ x).card = (Nat.Partition.countRestricted n m).card
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Proof depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../overview/topology/general-topology/part-01/closure.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Infinite sum](../../../overview/topology/topological-algebra/infinite-sum.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Power series](../../../overview/general-algebra/polynomials-and-power-series/power-series.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `Nat.Partition.card_restricted_eq_card_countRestricted`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Enumerative/Partition/Glaisher.html#Nat.Partition.card_restricted_eq_card_countRestricted)
- [Source of `Nat.Partition.card_restricted_eq_card_countRestricted` in Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Enumerative/Partition/Glaisher.lean#L154)
- [1000+ theorems list: Q5566491](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3272)
- [1000+ theorems project: Q5566491](https://1000-plus.github.io/?length=-1#Q5566491)
- [Wikipedia: Glaisher's theorem](https://en.wikipedia.org/wiki/Glaisher's_theorem)
- [Wikidata: Q5566491](https://www.wikidata.org/wiki/Q5566491)
