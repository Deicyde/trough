# Well-ordering theorem

The **well-ordering theorem** (or **Zermelo's theorem**): every type can be well-ordered.

```lean
exists_wellFoundedLT.{u} (α : Type u) : ∃ x, WellFoundedLT α
```

## Depends on

Its statement uses no other concept on these lists.

## Proof depends on

- [Cardinal](../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)

## Sources

- [Mathlib documentation: `exists_wellFoundedLT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Order.html#exists_wellFoundedLT)
- [Source of `exists_wellFoundedLT` in Mathlib/SetTheory/Cardinal/Order.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/SetTheory/Cardinal/Order.lean#L531)
- [1000+ theorems list: Q1457052](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L1707)
- [1000+ theorems project: Q1457052](https://1000-plus.github.io/all.html?length=-1#Q1457052)
- [Wikipedia: Well-ordering theorem](https://en.wikipedia.org/wiki/Well-ordering_theorem)
- [Wikidata: Q1457052](https://www.wikidata.org/wiki/Q1457052)
