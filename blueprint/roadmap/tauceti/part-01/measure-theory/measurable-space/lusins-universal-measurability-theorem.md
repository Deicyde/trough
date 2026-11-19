---
declaration: theorem
origin: cited
lean: MeasureTheory.AnalyticSet.nullMeasurableSet
statement: formalized
proof: formalized
---

# Lusin's universal-measurability theorem

An analytic subset of a Hausdorff space is
null-measurable with respect to every s-finite measure on a measurable space containing the Borel
sets, equivalently measurable in the completion of that measure.

```lean
MeasureTheory.AnalyticSet.nullMeasurableSet.{u_1} {X : Type u_1} [TopologicalSpace X] [T2Space X]
  [MeasurableSpace X] [OpensMeasurableSpace X] {S : Set X} (hS : MeasureTheory.AnalyticSet S)
  (μ : MeasureTheory.Measure X) [MeasureTheory.SFinite μ] : MeasureTheory.NullMeasurableSet S μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.AnalyticSet.nullMeasurableSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Analytic.html#MeasureTheory.AnalyticSet.nullMeasurableSet).

## Sources

- [Tau Ceti documentation: `MeasureTheory.AnalyticSet.nullMeasurableSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/MeasurableSpace/Analytic.html#MeasureTheory.AnalyticSet.nullMeasurableSet)
- [Source of `MeasureTheory.AnalyticSet.nullMeasurableSet` in TauCeti/MeasureTheory/MeasurableSpace/Analytic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/MeasurableSpace/Analytic.lean#L98)
