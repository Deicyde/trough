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
- [Source of `MeasureTheory.Measure.volume_restrict_setOf_lt_decreasingRearrangement` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L293)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
