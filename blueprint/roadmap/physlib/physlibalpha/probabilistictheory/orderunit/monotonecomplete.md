---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder, PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.directedSup, PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.isLUB_directedSup, PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.exists_isLUB_range, PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.rangeSup, PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.isLUB_rangeSup
statement: formalized
proof: formalized
---

# Monotone-complete ordered spaces

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.MonotoneComplete`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean): 6 declarations, 4 with a docstring.

> Monotone-complete orders and chosen suprema of bounded directed sets and increasing sequences.

## i. Overview

> An ordered space is monotone complete when every nonempty directed set that is bounded above has a
> least upper bound.

## ii. Key results

> - `MonotoneCompleteOrder` : monotone-complete ordered spaces.
> - `MonotoneCompleteOrder.directedSup` : the supremum of a bounded directed set.
> - `MonotoneCompleteOrder.rangeSup` : the supremum of a bounded increasing sequence.

## iv. References

> * None.

## A. Monotone-complete orders

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder`**, a class, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L46).

> An order is monotone complete when every nonempty upward-directed bounded set has a supremum.
> No lattice operations are bundled: ordered vector spaces need not be lattices.

```lean
class MonotoneCompleteOrder (E : Type*) [Preorder E] : Prop where
  /-- Existence of the directed supremum. -/
  exists_isLUB (D : Set E) : D.Nonempty → DirectedOn (· ≤ ·) D → BddAbove D →
    ∃ x : E, IsLUB D x
```

## B. Chosen suprema

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.directedSup`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L58).

> A chosen supremum of a nonempty directed set that is bounded above.

```lean
noncomputable def directedSup (D : Set E) (hD : D.Nonempty)
    (hdir : DirectedOn (· ≤ ·) D) (hbdd : BddAbove D) : E
```

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.isLUB_directedSup`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L62).

```lean
lemma isLUB_directedSup (D : Set E) (hD : D.Nonempty)
    (hdir : DirectedOn (· ≤ ·) D) (hbdd : BddAbove D) :
    IsLUB D (directedSup D hD hdir hbdd)
```

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.exists_isLUB_range`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L68).

> A monotone sequence with a common upper bound has a least upper bound.

```lean
lemma exists_isLUB_range (x : ℕ → E) (hx : Monotone x) (hbounded : BddAbove (Set.range x)) :
    ∃ a : E, IsLUB (Set.range x) a
```

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.rangeSup`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L76).

> The chosen supremum of a bounded increasing sequence.

```lean
noncomputable def rangeSup (x : ℕ → E) (hx : Monotone x)
    (hbounded : BddAbove (Set.range x)) : E
```

**`PhyslibAlpha.ProbabilisticTheory.MonotoneCompleteOrder.isLUB_rangeSup`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L81).

```lean
lemma isLUB_rangeSup (x : ℕ → E) (hx : Monotone x)
    (hbounded : BddAbove (Set.range x)) :
    IsLUB (Set.range x) (rangeSup x hx hbounded)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean)
