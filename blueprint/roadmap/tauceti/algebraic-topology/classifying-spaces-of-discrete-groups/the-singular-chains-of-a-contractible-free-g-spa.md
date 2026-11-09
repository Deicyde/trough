---
declaration: def
origin: cited
lean: TauCeti.singularChainsResolution
statement: formalized
---

# The singular chains of a contractible free `G`-space are a projective resolution of the trivial representation of `G` over `k`

`G` acts freely on singular simplices, so the terms are
free over the group ring, and the augmented singular chain complex of a contractible space is
exact.

```lean
TauCeti.singularChainsResolution.{u} (k : Type u) [CommRing k] (E : TopCat) (G : Type u) [Group G]
  [MulAction G ↑E] [ContinuousConstSMul G ↑E] [IsCancelSMul G ↑E] [ContractibleSpace ↑E] :
  CategoryTheory.ProjectiveResolution (Rep.trivial k G k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.singularChainsResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/ModuleChains/Resolution.html#TauCeti.singularChainsResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.singularChainsResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/ModuleChains/Resolution.html#TauCeti.singularChainsResolution)
- [Source of `TauCeti.singularChainsResolution` in TauCeti/AlgebraicTopology/Singular/ModuleChains/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/ModuleChains/Resolution.lean#L249)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
