# 0-manifolds are discrete spaces

A charted space over a discrete space is discrete.

```lean
ChartedSpace.discreteTopology.{u, u_2} (H : Type u) (M : Type u_2) [TopologicalSpace H]
  [TopologicalSpace M] [ChartedSpace H M] [DiscreteTopology H] : DiscreteTopology M
```

## Depends on

- [Limit of a map with respect to filters](../../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)
- [Topological space](../../../topology/general-topology/part-01/topological-space.md)

## Sources

- [Mathlib documentation: `ChartedSpace.discreteTopology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/ChartedSpace.html#ChartedSpace.discreteTopology)
- [Source of `ChartedSpace.discreteTopology` in Mathlib/Geometry/Manifold/ChartedSpace.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/ChartedSpace.lean#L318)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L464)
