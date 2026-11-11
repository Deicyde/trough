---
declaration: theorem
origin: cited
lean: TauCeti.measurableSet_graph_iff_measurable, TauCeti.measurableSet_graphOn_iff, TauCeti.analyticSet_graph_iff_measurable
statement: formalized
proof: formalized
---

# The Borel graph theorem

A map between standard Borel spaces is measurable if and only if
its graph is measurable.

```lean
TauCeti.measurableSet_graph_iff_measurable.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [MeasurableSpace X] [StandardBorelSpace X] [MeasurableSpace Y] [StandardBorelSpace Y]
  {f : X → Y} : MeasurableSet (Function.graph f) ↔ Measurable f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lusin–Souslin for vertical sections](lusin-souslin-for-vertical-sections.md)
- [Souslin's theorem for graphs](souslins-theorem-for-graphs.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.measurableSet_graph_iff_measurable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#TauCeti.measurableSet_graph_iff_measurable).

## Other forms

**The Borel graph theorem for partial maps.** Formalized in Tau Ceti as [`TauCeti.measurableSet_graphOn_iff`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#TauCeti.measurableSet_graphOn_iff).

```lean
TauCeti.measurableSet_graphOn_iff.{u_1, u_2} {X : Type u_1} {Y : Type u_2} [MeasurableSpace X]
  [StandardBorelSpace X] [MeasurableSpace Y] [StandardBorelSpace Y] {s : Set X} {f : X → Y} :
  MeasurableSet (Set.graphOn f s) ↔ MeasurableSet s ∧ Measurable (s.domRestrict f)
```

**The Borel graph theorem, analytic form.** Formalized in Tau Ceti as [`TauCeti.analyticSet_graph_iff_measurable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#TauCeti.analyticSet_graph_iff_measurable).

```lean
TauCeti.analyticSet_graph_iff_measurable.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [PolishSpace X] [MeasurableSpace X] [BorelSpace X] [TopologicalSpace Y]
  [PolishSpace Y] [MeasurableSpace Y] [BorelSpace Y] {f : X → Y} :
  MeasureTheory.AnalyticSet (Function.graph f) ↔ Measurable f
```

## Sources

- [Tau Ceti documentation: `TauCeti.measurableSet_graph_iff_measurable`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#TauCeti.measurableSet_graph_iff_measurable)
- [Source of `TauCeti.measurableSet_graph_iff_measurable` in TauCeti/MeasureTheory/Constructions/Polish/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Constructions/Polish/Graph.lean#L158)
