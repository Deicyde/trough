# Induced topology

Given `f : X → Y` and a topology on `Y`,
the induced topology on `X` is the collection of sets
that are preimages of some open set in `Y`.
This is the coarsest topology that makes `f` continuous.

```lean
TopologicalSpace.induced.{u_1, u_2} {X : Type u_1} {Y : Type u_2} (f : X → Y)
  (t : TopologicalSpace Y) : TopologicalSpace X
```

## Depends on

- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `TopologicalSpace.induced`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Induced.html#TopologicalSpace.induced)
- [Source of `TopologicalSpace.induced` in Mathlib/Topology/Defs/Induced.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Defs/Induced.lean#L60)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L220)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L406)
