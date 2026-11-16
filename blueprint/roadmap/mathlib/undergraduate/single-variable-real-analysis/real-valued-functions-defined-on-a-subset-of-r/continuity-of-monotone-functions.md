# Continuity of monotone functions

Mathlib states this as `OrderIso.continuous`.

```lean
OrderIso.continuous.{u_1, u_2} {α : Type u_1} {β : Type u_2} [Preorder α] [Preorder β]
  [TopologicalSpace α] [TopologicalSpace β] [OrderTopology α] [OrderTopology β] (e : α ≃o β) :
  Continuous ⇑e
```

## Depends on

- [Continuous function](../../../overview/topology/general-topology/part-01/continuous-function.md)
- [Order topology](../../../overview/topology/topological-algebra/order-topology.md)

## Sources

- [Mathlib documentation: `OrderIso.continuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Order/MonotoneContinuity.html#OrderIso.continuous)
- [Source of `OrderIso.continuous` in Mathlib/Topology/Order/MonotoneContinuity.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Order/MonotoneContinuity.lean#L281)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L311)
