# Connected components

The connected component of a point is the maximal connected set
that contains this point.

```lean
connectedComponent.{u} {α : Type u} [TopologicalSpace α] (x : α) : Set α
```

## Depends on

- [Topological space](../../../overview/topology/general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `connectedComponent`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Connected/Basic.html#connectedComponent)
- [Source of `connectedComponent` in Mathlib/Topology/Connected/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Connected/Basic.lean#L493)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L415)
