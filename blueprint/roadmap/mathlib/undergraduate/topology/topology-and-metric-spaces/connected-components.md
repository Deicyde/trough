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
- [Source of `connectedComponent` in Mathlib/Topology/Connected/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Connected/Basic.lean#L493)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L415)
