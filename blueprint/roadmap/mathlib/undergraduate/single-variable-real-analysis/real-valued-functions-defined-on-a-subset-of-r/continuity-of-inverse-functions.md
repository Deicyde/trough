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
- [Source of `OrderIso.toHomeomorph` in Mathlib/Topology/Order/MonotoneContinuity.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Order/MonotoneContinuity.lean#L293)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L312)
