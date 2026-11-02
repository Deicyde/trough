---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: exists_wellFoundedLT
mathlib_file: Mathlib/SetTheory/Cardinal/Order.lean
---

# Well-ordering theorem

The **well-ordering theorem** (or **Zermelo's theorem**): every type can be well-ordered.

```lean
exists_wellFoundedLT.{u} (α : Type u) : ∃ x, WellFoundedLT α
```

## Depends on

- [Array](../../../../overview/data-structures/list-like-structures/array.md)
- [Natural number](../../../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Cantor’s Theorem](../../../../hundred-theorems/part-04/cantors-theorem.md)
- [Cardinal](../../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Finite set](../../../../overview/data-structures/sets/finite-set.md)
- [Integer](../../../../overview/general-algebra/numbers/integer.md)
- [Schroeder-Bernstein Theorem](../../../../hundred-theorems/part-02/schroeder-bernstein-theorem.md)

## Sources

- [Mathlib documentation: `exists_wellFoundedLT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Order.html#exists_wellFoundedLT)
- [Source of `exists_wellFoundedLT` in Mathlib/SetTheory/Cardinal/Order.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/SetTheory/Cardinal/Order.lean#L534)
- [1000+ theorems list: Q1457052](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1704)
- [1000+ theorems project: Q1457052](https://1000-plus.github.io/?length=-1#Q1457052)
- [Wikipedia: Well-ordering theorem](https://en.wikipedia.org/wiki/Well-ordering_theorem)
- [Wikidata: Q1457052](https://www.wikidata.org/wiki/Q1457052)
