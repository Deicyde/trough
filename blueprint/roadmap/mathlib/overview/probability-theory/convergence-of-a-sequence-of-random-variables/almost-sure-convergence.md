---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.ae
mathlib_file: Mathlib/MeasureTheory/OuterMeasure/AE.lean
---

# Almost sure convergence

The “almost everywhere” filter of co-null sets.

```lean
MeasureTheory.ae.{u_1, u_3} {α : Type u_1} {F : Type u_3} [FunLike F (Set α) ENNReal]
  [MeasureTheory.OuterMeasureClass F α] (μ : F) : Filter α
```

## Depends on

- [Infinite sum](../../topology/topological-algebra/infinite-sum.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Real number](../../general-algebra/numbers/real-number.md)

## Sources

- [Mathlib documentation: `MeasureTheory.ae`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/OuterMeasure/AE.html#MeasureTheory.ae)
- [Source of `MeasureTheory.ae` in Mathlib/MeasureTheory/OuterMeasure/AE.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/OuterMeasure/AE.lean#L46)
- [Mathlib overview: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L416)
- [Mathlib undergraduate list: Probability Theory › Convergence of a sequence of random variables](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L579)
