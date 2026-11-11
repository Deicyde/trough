---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.eLpNorm_decreasingRearrangement
statement: formalized
proof: formalized
---

# MeasureTheory.Measure.eLpNorm_decreasingRearrangement

The decreasing rearrangement has the same `Lᵖ` seminorm on `(0, ∞)` as `f`, for every
exponent `p ∈ [0, ∞]`.

```lean
MeasureTheory.Measure.eLpNorm_decreasingRearrangement.{u_1} {α : Type u_1} [MeasurableSpace α]
  (μ : MeasureTheory.Measure α) {f : α → ENNReal} (hf : AEMeasurable f μ) (p : ENNReal) :
  MeasureTheory.eLpNorm (μ.decreasingRearrangement f) p
      (MeasureTheory.volume.restrict (Set.Ioi 0)) =
    MeasureTheory.eLpNorm f p μ
```

## Depends on

- [MeasureTheory.Measure.decreasingRearrangement](measuretheory-measure-decreasingrearrangement.md)

## Proof depends on

- [Equimeasurability](equimeasurability.md)

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.eLpNorm_decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.eLpNorm_decreasingRearrangement).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.eLpNorm_decreasingRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/DecreasingRearrangement.html#MeasureTheory.Measure.eLpNorm_decreasingRearrangement)
- [Source of `MeasureTheory.Measure.eLpNorm_decreasingRearrangement` in TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/DecreasingRearrangement.lean#L334)
- [Tau Ceti roadmap status: Noncommutative integration and martingale inequalities](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeIntegration/STATUS.md)
