---
declaration: abbrev
origin: cited
lean: TopCat.Hom.arbitraryBaseSerreSpectralSequence
statement: formalized
---

# The Serre spectral sequence over an arbitrary base

For `p : E ⟶ B`, the Serre spectral
sequence `TauCeti.TopCat.serreSpectralSequence` of the pullback `ΓB ×_B E ⟶ ΓB` of `p` to the CW
approximation `TauCeti.sigmaCWApproximation B` of `B`, with coefficients in `R`.

```lean
TopCat.Hom.arbitraryBaseSerreSpectralSequence.{u} {E B : TopCat} (p : E ⟶ B) (R : Type u) [Ring R] :
  CategoryTheory.SpectralSequence (ModuleCat R) (fun r => ComplexShape.up' (r, 1 - r)) 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.Hom.arbitraryBaseSerreSpectralSequence`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.html#TopCat.Hom.arbitraryBaseSerreSpectralSequence).

## Sources

- [Tau Ceti documentation: `TopCat.Hom.arbitraryBaseSerreSpectralSequence`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.html#TopCat.Hom.arbitraryBaseSerreSpectralSequence)
- [Source of `TopCat.Hom.arbitraryBaseSerreSpectralSequence` in TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.lean#L78)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
