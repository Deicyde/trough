---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.decreasingRearrangement_add_le
statement: formalized
proof: formalized
---

# Shifted subadditivity `(f + g)* (s + t) ≤ f* s + g* t`

```lean
MeasureTheory.Measure.decreasingRearrangement_add_le.{u_1} {α : Type u_1} [MeasurableSpace α]
  (μ : MeasureTheory.Measure α) {s t : ℝ} (f g : α → ENNReal) (hs : 0 ≤ s) (ht : 0 ≤ t) :
  μ.decreasingRearrangement (f + g) (s + t) ≤
    μ.decreasingRearrangement f s + μ.decreasingRearrangement g t
```

## Depends on

- [MeasureTheory.Measure.decreasingRearrangement](measuretheory-measure-decreasingrearrangement.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.decreasingRearrangement_add_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.decreasingRearrangement_add_le).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.decreasingRearrangement_add_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.decreasingRearrangement_add_le)
- [Source of `MeasureTheory.Measure.decreasingRearrangement_add_le` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L253)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
