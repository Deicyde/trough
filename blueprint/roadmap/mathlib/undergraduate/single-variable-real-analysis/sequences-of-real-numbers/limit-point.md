# Limit point

A point `x` is a cluster point of a sequence `u` along a filter `F` if it is a cluster point
of `map u F`.

```lean
MapClusterPt.{u_1, u_3} {X : Type u_1} [TopologicalSpace X] {ι : Type u_3} (x : X) (F : Filter ι)
  (u : ι → X) : Prop
```

## Depends on

- [Cluster point](../../../overview/topology/general-topology/part-01/cluster-point.md)

## Sources

- [Mathlib documentation: `MapClusterPt`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Defs/Filter.html#MapClusterPt)
- [Source of `MapClusterPt` in Mathlib/Topology/Defs/Filter.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Topology/Defs/Filter.lean#L282)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L285)
