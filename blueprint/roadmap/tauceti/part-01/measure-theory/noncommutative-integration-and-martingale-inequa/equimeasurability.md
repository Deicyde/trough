---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement
statement: formalized
proof: formalized
---

# Equimeasurability

For Lebesgue measure on `(0, ∞)`, the superlevel sets of `f*` have the
same measures as those of `f`.

```lean
MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement.{u_1} {α : Type u_1}
  [MeasurableSpace α] (μ : MeasureTheory.Measure α) (f : α → ENNReal) (c : ENNReal) :
  (MeasureTheory.volume.restrict (Set.Ioi 0)) {s | c < μ.decreasingRearrangement f s} =
    μ {y | c < f y}
```

## Depends on

- [MeasureTheory.Measure.decreasingRearrangement](measuretheory-measure-decreasingrearrangement.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement)
- [Source of `MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L292)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
