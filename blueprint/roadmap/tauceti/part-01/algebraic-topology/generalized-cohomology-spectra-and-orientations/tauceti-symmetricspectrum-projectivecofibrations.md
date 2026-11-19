---
declaration: theorem
origin: cited
lean: TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions
statement: formalized
proof: formalized
---

# TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions

Projective cofibrations are the retracts of relative cell complexes built from free cells on
the boundary inclusions.

```lean
TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions :
  TauCeti.SymmetricSpectrum.projectiveCofibrations =
    (CategoryTheory.MorphismProperty.transfiniteCompositions.{0, 0, 1}
        (CategoryTheory.MorphismProperty.coproducts.{0, 0, 1}
            (TauCeti.SymmetricSpectrum.freeCells SSet.modelCategoryQuillen.I)).pushouts).retracts
```

## Depends on

- [TauCeti.SymmetricSpectrum](tauceti-symmetricspectrum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/LevelFactorization.html#TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/LevelFactorization.html#TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions)
- [Source of `TauCeti.SymmetricSpectrum.projectiveCofibrations_eq_retracts_transfiniteCompositions` in TauCeti/AlgebraicTopology/Spectra/LevelFactorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Spectra/LevelFactorization.lean#L312)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
