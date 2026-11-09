# Topological fiber bundle

A (topological) fiber bundle with fiber `F` over a base `B` is a space projecting on `B`
for which the fibers are all homeomorphic to `F`, such that the local situation around each point
is a direct product.

```lean
FiberBundle.{u_2, u_3, u_5} {B : Type u_2} (F : Type u_3) [TopologicalSpace B] [TopologicalSpace F]
  (E : B → Type u_5) [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → TopologicalSpace (E b)] :
  Type (max (max u_2 u_3) u_5)
```

## Depends on

- [Induced topology](induced-topology.md)
- [Limit of a map with respect to filters](limit-of-a-map-with-respect-to-filters.md)

## Sources

- [Mathlib documentation: `FiberBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/FiberBundle/Basic.html#FiberBundle)
- [Source of `FiberBundle` in Mathlib/Topology/FiberBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/FiberBundle/Basic.lean#L184)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L233)
- [Mathlib overview: Geometry › Smooth vector and fiber bundles](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L467)
