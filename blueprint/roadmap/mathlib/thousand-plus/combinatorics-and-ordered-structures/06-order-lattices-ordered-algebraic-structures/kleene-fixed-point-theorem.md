# Kleene fixed-point theorem

**Kleene's fixed point Theorem**: The least fixed point in a complete lattice is
the supremum of iterating a function on bottom arbitrary often.

```lean
fixedPoints.lfp_eq_sSup_iterate.{u} {α : Type u} [CompleteLattice α] (f : α →o α)
  (h : OmegaCompletePartialOrder.ωScottContinuous ⇑f) : OrderHom.lfp f = ⨆ n, (⇑f)^[n] ⊥
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Proof depends on

- [Fixed points](../../../overview/dynamics/general-theory/fixed-points.md)

## Sources

- [Mathlib documentation: `fixedPoints.lfp_eq_sSup_iterate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/FixedPoints.html#fixedPoints.lfp_eq_sSup_iterate)
- [Source of `fixedPoints.lfp_eq_sSup_iterate` in Mathlib/Order/FixedPoints.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Order/FixedPoints.lean#L270)
- [1000+ theorems list: Q3527263](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L2595)
- [1000+ theorems project: Q3527263](https://1000-plus.github.io/all.html?length=-1#Q3527263)
- [Wikipedia: Kleene fixed-point theorem](https://en.wikipedia.org/wiki/Kleene_fixed-point_theorem)
- [Wikidata: Q3527263](https://www.wikidata.org/wiki/Q3527263)
