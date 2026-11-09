---
declaration: theorem
origin: cited
lean: MeasureTheory.AnalyticSet.measurable_of_graph
statement: formalized
proof: formalized
---

# Souslin's theorem for graphs

A map from a Hausdorff space with its Borel sets measurable
to a Polish space, whose graph is analytic, is measurable.

```lean
MeasureTheory.AnalyticSet.measurable_of_graph.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [T2Space X] [MeasurableSpace X] [OpensMeasurableSpace X] [TopologicalSpace Y]
  [PolishSpace Y] [MeasurableSpace Y] [BorelSpace Y] {f : X → Y}
  (hf : MeasureTheory.AnalyticSet (Function.graph f)) : Measurable f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.AnalyticSet.measurable_of_graph`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#MeasureTheory.AnalyticSet.measurable_of_graph).

## Sources

- [Tau Ceti documentation: `MeasureTheory.AnalyticSet.measurable_of_graph`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#MeasureTheory.AnalyticSet.measurable_of_graph)
- [Source of `MeasureTheory.AnalyticSet.measurable_of_graph` in TauCeti/MeasureTheory/Constructions/Polish/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Constructions/Polish/Graph.lean#L172)
