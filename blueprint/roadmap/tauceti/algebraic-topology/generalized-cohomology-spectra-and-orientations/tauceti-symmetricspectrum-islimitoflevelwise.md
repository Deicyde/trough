---
declaration: def
origin: cited
lean: TauCeti.SymmetricSpectrum.isLimitOfLevelwise
statement: formalized
---

# TauCeti.SymmetricSpectrum.isLimitOfLevelwise

A cone of symmetric spectra is limiting if its cone of pointed simplicial sets is
limiting at every level. In particular, the limiting maps respect the sphere action.

```lean
TauCeti.SymmetricSpectrum.isLimitOfLevelwise.{v, w} {J : Type w} [CategoryTheory.Category.{v, w} J]
  {F : CategoryTheory.Functor J TauCeti.SymmetricSpectrum} (c : CategoryTheory.Limits.Cone F)
  (h :
    (n : ℕ) →
      CategoryTheory.Limits.IsLimit
        (((CategoryTheory.evaluation TauCeti.FiniteBijection TauCeti.PointedSSet).obj
              { len := n }).mapCone
          ((CategoryTheory.MonoidalCategory.DayFunctor.equiv TauCeti.FiniteBijection
                  TauCeti.PointedSSet).functor.mapCone
            ((CategoryTheory.Mod.forget TauCeti.SymmetricSequence.sphere).mapCone c)))) :
  CategoryTheory.Limits.IsLimit c
```

## Depends on

- [TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor](tauceti-pointedsset-instbraidedfinitebijectionsm.md)
- [TauCeti.PointedSSet.monoidalClosed](tauceti-pointedsset-monoidalclosed.md)
- [TauCeti.SymmetricSequence](tauceti-symmetricsequence.md)
- [TauCeti.SymmetricSpectrum](tauceti-symmetricspectrum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricSpectrum.isLimitOfLevelwise`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/Limits.html#TauCeti.SymmetricSpectrum.isLimitOfLevelwise).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricSpectrum.isLimitOfLevelwise`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/Limits.html#TauCeti.SymmetricSpectrum.isLimitOfLevelwise)
- [Source of `TauCeti.SymmetricSpectrum.isLimitOfLevelwise` in TauCeti/AlgebraicTopology/Spectra/Limits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Spectra/Limits.lean#L43)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
