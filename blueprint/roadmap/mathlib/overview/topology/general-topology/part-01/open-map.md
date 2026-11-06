# Open map

A map `f : X → Y` is said to be an *open map*,
if the image of any open `U : Set X` is open in `Y`.

```lean
IsOpenMap.{u, v} {X : Type u} {Y : Type v} [TopologicalSpace X] [TopologicalSpace Y] (f : X → Y) :
  Prop
```

## Depends on

- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `IsOpenMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html#IsOpenMap)
- [Source of `IsOpenMap` in Mathlib/Topology/Defs/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Defs/Basic.lean#L163)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L221)
