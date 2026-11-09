# Closed map

A map `f : X → Y` is said to be a *closed map*,
if the image of any closed `U : Set X` is closed in `Y`.

```lean
IsClosedMap.{u, v} {X : Type u} {Y : Type v} [TopologicalSpace X] [TopologicalSpace Y] (f : X → Y) :
  Prop
```

## Depends on

- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `IsClosedMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html#IsClosedMap)
- [Source of `IsClosedMap` in Mathlib/Topology/Defs/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Topology/Defs/Basic.lean#L168)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L222)
