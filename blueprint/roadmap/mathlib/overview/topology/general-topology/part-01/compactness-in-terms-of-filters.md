---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: IsCompact
mathlib_file: Mathlib/Topology/Defs/Filter.lean
---

# Compactness in terms of filters

A set `s` is compact if for every nontrivial filter `f` that contains `s`,
there exists `a ∈ s` such that every set of `f` meets every neighborhood of `a`.

```lean
IsCompact.{u_1} {X : Type u_1} [TopologicalSpace X] (s : Set X) : Prop
```

## Depends on

- [Cluster point](cluster-point.md)

## Sources

- [Mathlib documentation: `IsCompact`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Filter.html#IsCompact)
- [Source of `IsCompact` in Mathlib/Topology/Defs/Filter.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Defs/Filter.lean#L292)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L228)
