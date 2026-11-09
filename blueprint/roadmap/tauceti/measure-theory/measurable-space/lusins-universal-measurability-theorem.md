---
declaration: theorem
origin: cited
lean: TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet
statement: formalized
proof: formalized
---

# Lusin's universal-measurability theorem

An analytic subset of a metrizable space is
null-measurable with respect to every s-finite measure on a measurable space containing the Borel
sets, equivalently measurable in the completion of that measure.

```lean
TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet.{u_1} {X : Type u_1} [TopologicalSpace X]
  [TopologicalSpace.MetrizableSpace X] [MeasurableSpace X] [OpensMeasurableSpace X] {S : Set X}
  (hS : MeasureTheory.AnalyticSet S) (μ : MeasureTheory.Measure X) [MeasureTheory.SFinite μ] :
  MeasureTheory.NullMeasurableSet S μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Analytic.html#TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet).

## Sources

- [Tau Ceti documentation: `TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Analytic.html#TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet)
- [Source of `TauCeti.MeasureTheory.AnalyticSet.nullMeasurableSet` in TauCeti/MeasureTheory/MeasurableSpace/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/MeasurableSpace/Analytic.lean#L309)
