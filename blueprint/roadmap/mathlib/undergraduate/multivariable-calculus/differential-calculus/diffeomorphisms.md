# Diffeomorphisms

A `G`-diffeomorphism between two charted spaces is a homeomorphism which, when read in the
charts, belongs to `G`. We avoid the word diffeomorph as it is too related to the smooth category,
and use structomorph instead.

```lean
Structomorph.{u, u_5, u_6} {H : Type u} [TopologicalSpace H] (G : StructureGroupoid H)
  (M : Type u_5) (M' : Type u_6) [TopologicalSpace M] [TopologicalSpace M'] [ChartedSpace H M]
  [ChartedSpace H M'] : Type (max u_5 u_6)
```

## Depends on

- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Limit of a map with respect to filters](../../../overview/topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Sources

- [Mathlib documentation: `Structomorph`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/HasGroupoid.html#Structomorph)
- [Source of `Structomorph` in Mathlib/Geometry/Manifold/HasGroupoid.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Geometry/Manifold/HasGroupoid.lean#L361)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L472)
