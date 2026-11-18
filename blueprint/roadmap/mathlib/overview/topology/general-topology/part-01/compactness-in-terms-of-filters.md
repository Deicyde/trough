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
- [Source of `IsCompact` in Mathlib/Topology/Defs/Filter.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Defs/Filter.lean#L292)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L228)
