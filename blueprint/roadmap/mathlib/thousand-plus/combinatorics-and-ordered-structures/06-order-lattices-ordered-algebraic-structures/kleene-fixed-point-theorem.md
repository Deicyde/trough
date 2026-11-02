---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: fixedPoints.lfp_eq_sSup_iterate
mathlib_file: Mathlib/Order/FixedPoints.lean
---

# Kleene fixed-point theorem

**Kleene's fixed point Theorem**: The least fixed point in a complete lattice is
the supremum of iterating a function on bottom arbitrary often.

```lean
fixedPoints.lfp_eq_sSup_iterate.{u} {α : Type u} [CompleteLattice α] (f : α →o α)
  (h : OmegaCompletePartialOrder.ωScottContinuous ⇑f) : OrderHom.lfp f = ⨆ n, (⇑f)^[n] ⊥
```

## Depends on

- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Proof depends on

- [Fixed points](../../../overview/dynamics/general-theory/fixed-points.md)

## Sources

- [Mathlib documentation: `fixedPoints.lfp_eq_sSup_iterate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/FixedPoints.html#fixedPoints.lfp_eq_sSup_iterate)
- [Source of `fixedPoints.lfp_eq_sSup_iterate` in Mathlib/Order/FixedPoints.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Order/FixedPoints.lean#L270)
- [1000+ theorems list: Q3527263](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2592)
- [1000+ theorems project: Q3527263](https://1000-plus.github.io/?length=-1#Q3527263)
- [Wikipedia: Kleene fixed-point theorem](https://en.wikipedia.org/wiki/Kleene_fixed-point_theorem)
- [Wikidata: Q3527263](https://www.wikidata.org/wiki/Q3527263)
