---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Order.cof
mathlib_file: Mathlib/SetTheory/Cardinal/Cofinality/Basic.lean
---

# Cofinality

The cofinality of a preorder is the smallest cardinality of a cofinal subset.

```lean
Order.cof.{u} (α : Type u) [Preorder α] : Cardinal.{u}
```

## Depends on

- [Cardinal](cardinal.md)
- [Set](../../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Order.cof`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Cofinality/Basic.html#Order.cof)
- [Source of `Order.cof` in Mathlib/SetTheory/Cardinal/Cofinality/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/SetTheory/Cardinal/Cofinality/Basic.lean#L33)
- [Mathlib overview: Logic and computation › Set theory › Cardinals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L633)
