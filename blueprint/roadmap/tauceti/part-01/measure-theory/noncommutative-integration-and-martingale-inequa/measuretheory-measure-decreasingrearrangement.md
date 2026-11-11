---
declaration: def
origin: cited
lean: MeasureTheory.Measure.decreasingRearrangement
statement: formalized
---

# MeasureTheory.Measure.decreasingRearrangement

The **decreasing rearrangement** `f* s = sup {c | s < μ {f > c}}` of `f : α → ℝ≥0∞` with
respect to `μ`. It is the nonincreasing right-continuous function on `(0, ∞)` with the same
distribution as `f`, and equals `inf {c | μ {f > c} ≤ s}` (`decreasingRearrangement_le_iff`).
For `s ≤ 0` its value is the essential supremum of `f`.

```lean
MeasureTheory.Measure.decreasingRearrangement.{u_1} {α : Type u_1} [MeasurableSpace α]
  (μ : MeasureTheory.Measure α) (f : α → ENNReal) (s : ℝ) : ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.decreasingRearrangement).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.decreasingRearrangement)
- [Source of `MeasureTheory.Measure.decreasingRearrangement` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L99)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
