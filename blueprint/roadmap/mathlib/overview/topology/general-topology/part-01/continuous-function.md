# Continuous function

A function between topological spaces is continuous if the preimage
of every open set is open. Registered as a structure to make sure it is not unfolded by Lean.

```lean
Continuous.{u, v} {X : Type u} {Y : Type v} [TopologicalSpace X] [TopologicalSpace Y] (f : X → Y) :
  Prop
```

## Depends on

- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `Continuous`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Basic.html#Continuous)
- [Source of `Continuous` in Mathlib/Topology/Defs/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Defs/Basic.lean#L155)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L218)
- [Mathlib undergraduate list: Single Variable Real Analysis › Real-valued functions defined on a subset of $\R$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L307)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L410)
