---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: ClusterPt
mathlib_file: Mathlib/Topology/Defs/Filter.lean
---

# Cluster point

A point `x` is a cluster point of a filter `F` if `𝓝 x ⊓ F ≠ ⊥`.
Also known as an accumulation point or a limit point, but beware that terminology varies.
This is *not* the same as asking `𝓝[≠] x ⊓ F ≠ ⊥`, which is called `AccPt` in Mathlib.
See `mem_closure_iff_clusterPt` in particular.

```lean
ClusterPt.{u_1} {X : Type u_1} [TopologicalSpace X] (x : X) (F : Filter X) : Prop
```

## Depends on

- [Array](../../../data-structures/list-like-structures/array.md)
- [Filter](filter.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Topological space](topological-space.md)

## Sources

- [Mathlib documentation: `ClusterPt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Filter.html#ClusterPt)
- [Source of `ClusterPt` in Mathlib/Topology/Defs/Filter.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Defs/Filter.lean#L275)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L224)
- [Mathlib undergraduate list: Topology › Topology and Metric Spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L409)
