---
declaration: module
origin: cited
lean: ProbabilisticTheory.MonotoneCompleteOrder, ProbabilisticTheory.MonotoneCompleteOrder.directedSup, ProbabilisticTheory.MonotoneCompleteOrder.isLUB_directedSup, ProbabilisticTheory.MonotoneCompleteOrder.exists_isLUB_range, ProbabilisticTheory.MonotoneCompleteOrder.rangeSup, ProbabilisticTheory.MonotoneCompleteOrder.isLUB_rangeSup
statement: formalized
proof: formalized
---

# Monotone-complete ordered spaces

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.MonotoneComplete`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean): 6 declarations, 4 with a docstring.

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

**`ProbabilisticTheory.MonotoneCompleteOrder`**, a class, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L46).

> An order is monotone complete when every nonempty upward-directed bounded set has a supremum.
> No lattice operations are bundled: ordered vector spaces need not be lattices.

```lean
class MonotoneCompleteOrder (E : Type*) [Preorder E] : Prop where
  /-- Existence of the directed supremum. -/
  exists_isLUB (D : Set E) : D.Nonempty → DirectedOn (· ≤ ·) D → BddAbove D →
    ∃ x : E, IsLUB D x
```

## B. Chosen suprema

**`ProbabilisticTheory.MonotoneCompleteOrder.directedSup`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L58).

> A chosen supremum of a nonempty directed set that is bounded above.

```lean
noncomputable def directedSup (D : Set E) (hD : D.Nonempty)
    (hdir : DirectedOn (· ≤ ·) D) (hbdd : BddAbove D) : E
```

**`ProbabilisticTheory.MonotoneCompleteOrder.isLUB_directedSup`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L62).

```lean
lemma isLUB_directedSup (D : Set E) (hD : D.Nonempty)
    (hdir : DirectedOn (· ≤ ·) D) (hbdd : BddAbove D) :
    IsLUB D (directedSup D hD hdir hbdd)
```

**`ProbabilisticTheory.MonotoneCompleteOrder.exists_isLUB_range`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L68).

> A monotone sequence with a common upper bound has a least upper bound.

```lean
lemma exists_isLUB_range (x : ℕ → E) (hx : Monotone x) (hbounded : BddAbove (Set.range x)) :
    ∃ a : E, IsLUB (Set.range x) a
```

**`ProbabilisticTheory.MonotoneCompleteOrder.rangeSup`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L76).

> The chosen supremum of a bounded increasing sequence.

```lean
noncomputable def rangeSup (x : ℕ → E) (hx : Monotone x)
    (hbounded : BddAbove (Set.range x)) : E
```

**`ProbabilisticTheory.MonotoneCompleteOrder.isLUB_rangeSup`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean#L81).

```lean
lemma isLUB_rangeSup (x : ℕ → E) (hx : Monotone x)
    (hbounded : BddAbove (Set.range x)) :
    IsLUB (Set.range x) (rangeSup x hx hbounded)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/MonotoneComplete.lean)
