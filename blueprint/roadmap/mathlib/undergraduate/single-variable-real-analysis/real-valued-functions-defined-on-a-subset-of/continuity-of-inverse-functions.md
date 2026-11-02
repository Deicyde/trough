---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: OrderIso.toHomeomorph
mathlib_file: Mathlib/Topology/Order/MonotoneContinuity.lean
---

# Continuity of inverse functions

An order isomorphism between two linear order `OrderTopology` spaces is a homeomorphism.

```lean
OrderIso.toHomeomorph.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Preorder α] [Preorder β]
  [TopologicalSpace α] [TopologicalSpace β] [OrderTopology α] [OrderTopology β] (e : α ≃o β) :
  α ≃ₜ β
```

## Depends on

- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `OrderIso.toHomeomorph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/MonotoneContinuity.html#OrderIso.toHomeomorph)
- [Source of `OrderIso.toHomeomorph` in Mathlib/Topology/Order/MonotoneContinuity.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Order/MonotoneContinuity.lean#L293)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L312)
