---
declaration: def
origin: cited
lean: TauCeti.steinerSymmetrization
statement: formalized
---

# TauCeti.steinerSymmetrization

Steiner symmetrization along the unit direction `e`, centered on its orthogonal hyperplane.
The section of length `ℓ` is the open centered interval of radius `ℓ / 2`; this includes
empty intervals for `ℓ = 0` and the whole line for `ℓ = ∞`.

```lean
TauCeti.steinerSymmetrization.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  (e : E) (he : ‖e‖ = 1) (s : Set E) : Set E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.steinerSymmetrization`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Basic.html#TauCeti.steinerSymmetrization).

## Sources

- [Tau Ceti documentation: `TauCeti.steinerSymmetrization`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Basic.html#TauCeti.steinerSymmetrization)
- [Source of `TauCeti.steinerSymmetrization` in TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Basic.lean#L52)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Isoperimetry/STATUS.md)
