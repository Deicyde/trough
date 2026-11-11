---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton
statement: formalized
proof: formalized
---

# Sierpiński's theorem

An atomless measure on a standard Borel space takes every value
between `0` and `μ s` on measurable subsets of a measurable set `s` of finite measure.

```lean
MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton.{u_1} {X : Type u_1}
  [MeasurableSpace X] [StandardBorelSpace X] (μ : MeasureTheory.Measure X)
  [MeasureTheory.NullSingletonClass μ] {s : Set X} (hs : MeasurableSet s) (hμs : μ s ≠ ⊤)
  {a : ENNReal} (ha : a ≤ μ s) : ∃ t ⊆ s, MeasurableSet t ∧ μ t = a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/AtomlessStandardBorel/Transport.html#MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/AtomlessStandardBorel/Transport.html#MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton)
- [Source of `MeasureTheory.Measure.exists_subset_measure_eq_of_nullSingleton` in TauCeti/MeasureTheory/Measure/AtomlessStandardBorel/Transport.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/AtomlessStandardBorel/Transport.lean#L113)
