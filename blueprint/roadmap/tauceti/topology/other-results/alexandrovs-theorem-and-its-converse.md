---
declaration: theorem
origin: cited
lean: TauCeti.isGδ_iff_isCompletelyMetrizableSpace
statement: formalized
proof: formalized
---

# Alexandrov's theorem and its converse

a subset of a completely metrizable space is
completely metrizable in the subspace topology if and only if it is a Gδ set.

```lean
TauCeti.isGδ_iff_isCompletelyMetrizableSpace.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.IsCompletelyMetrizableSpace X] {s : Set X} :
  IsGδ s ↔ TopologicalSpace.IsCompletelyMetrizableSpace ↑s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isGδ_iff_isCompletelyMetrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Polish/GDelta.html#TauCeti.isG%CE%B4_iff_isCompletelyMetrizableSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.isGδ_iff_isCompletelyMetrizableSpace`](https://taucetiproject.org/docs/TauCeti/Topology/MetricSpace/Polish/GDelta.html#TauCeti.isG%CE%B4_iff_isCompletelyMetrizableSpace)
- [Source of `TauCeti.isGδ_iff_isCompletelyMetrizableSpace` in TauCeti/Topology/MetricSpace/Polish/GDelta.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/MetricSpace/Polish/GDelta.lean#L92)
