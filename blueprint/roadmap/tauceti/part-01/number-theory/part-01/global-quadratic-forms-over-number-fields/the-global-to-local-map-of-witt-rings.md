---
declaration: def
origin: cited
lean: TauCeti.WittRing.globalToLocal
statement: formalized
---

# The global-to-local map of Witt rings

**The global-to-local map of Witt rings** `W(K) → ∏_v W(K_v) × ∏_w W(ℝ)` of a number field
`K`, with one component for each finite place `v` and one for each real place `w`, each given by
scalar extension.

```lean
TauCeti.WittRing.globalToLocal.{u} (K : Type u) [Field K] [NumberField K] :
  TauCeti.WittRing K →+*
    ((v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) →
        TauCeti.WittRing (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)) ×
      ({ w // w.IsReal } → TauCeti.WittRing ℝ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WittRing.globalToLocal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.html#TauCeti.WittRing.globalToLocal).

## Sources

- [Tau Ceti documentation: `TauCeti.WittRing.globalToLocal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.html#TauCeti.WittRing.globalToLocal)
- [Source of `TauCeti.WittRing.globalToLocal` in TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/WittLocalization.lean#L164)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
