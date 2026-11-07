---
declaration: def
origin: cited
lean: TauCeti.schwarzRearrangement
statement: formalized
---

# TauCeti.schwarzRearrangement

The **Schwarz rearrangement** of `f : E → ℝ≥0∞` with respect to `μ`: the radially
nonincreasing function whose superlevel set `{t < f*}` is `{x | μ (ball 0 ‖x‖) < μ {t < f}}`.
For an additive Haar measure on a nontrivial finite-dimensional real normed space, this is the
centered open ball of the same measure when `μ {t < f}` is finite, and the whole space when it is
infinite.

```lean
TauCeti.schwarzRearrangement.{u_1} {E : Type u_1} [NormedAddCommGroup E] [MeasurableSpace E]
  (μ : MeasureTheory.Measure E) (f : E → ENNReal) (x : E) : ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.schwarzRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/SchwarzRearrangement.html#TauCeti.schwarzRearrangement).

## Sources

- [Tau Ceti documentation: `TauCeti.schwarzRearrangement`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/SchwarzRearrangement.html#TauCeti.schwarzRearrangement)
- [Source of `TauCeti.schwarzRearrangement` in TauCeti/MeasureTheory/Function/SchwarzRearrangement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Function/SchwarzRearrangement.lean#L128)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
