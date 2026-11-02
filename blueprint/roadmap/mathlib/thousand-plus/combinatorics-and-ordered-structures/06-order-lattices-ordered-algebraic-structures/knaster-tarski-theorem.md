---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: fixedPoints.completeLattice
mathlib_file: Mathlib/Order/FixedPoints.lean
---

# Knaster–Tarski theorem

**Knaster-Tarski Theorem**: The fixed points of `f` form a complete lattice.

```lean
fixedPoints.completeLattice.{u} {α : Type u} [CompleteLattice α] (f : α →o α) :
  CompleteLattice ↑(Function.fixedPoints ⇑f)
```

## Depends on

- [Array](../../../overview/data-structures/list-like-structures/array.md)
- [Fixed points](../../../overview/dynamics/general-theory/fixed-points.md)
- [Natural number](../../../overview/general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `fixedPoints.completeLattice`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/FixedPoints.html#fixedPoints.completeLattice)
- [Source of `fixedPoints.completeLattice` in Mathlib/Order/FixedPoints.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Order/FixedPoints.lean#L252)
- [1000+ theorems list: Q609612](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L620)
- [1000+ theorems project: Q609612](https://1000-plus.github.io/?length=-1#Q609612)
- [Wikipedia: Knaster–Tarski theorem](https://en.wikipedia.org/wiki/Knaster%E2%80%93Tarski_theorem)
- [Wikidata: Q609612](https://www.wikidata.org/wiki/Q609612)
