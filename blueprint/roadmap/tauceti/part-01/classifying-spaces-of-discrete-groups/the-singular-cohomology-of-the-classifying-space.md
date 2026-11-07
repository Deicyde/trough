---
declaration: def
origin: cited
lean: TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology
statement: formalized
---

# The singular cohomology of the classifying space is group cohomology

for every group
`G`, the singular cohomology `Hⁿ(BG; M)` of Milnor's classifying space with coefficients in a
module `M` over a commutative ring `k` is Mathlib's group cohomology `Hⁿ(G, M)` of the trivial
representation `M`. It comes from the free resolution of `k` by the singular chains of
`universalGSpace G`.

```lean
TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology.{u} (k : Type u) [CommRing k]
  (G : Type u) [Group G] (M : Type u) [AddCommGroup M] [_root_.Module k M] (n : ℕ) :
  TopCat.singularCohomology (↧k) k (↧M) (↧(TauCeti.classifyingSpace G)) n ≅
    groupCohomology (Rep.trivial k G M) n
```

## Depends on

- [TauCeti.singularChainsResolution](tauceti-singularchainsresolution.md)

## Proof depends on

- [ContinuousMap.IsWeakHomotopyEquivalence.homotopyEquiv](../algebraic-topology-of-spaces-and-manifolds/continuousmap-isweakhomotopyequivalence-homotopy.md)
- [TauCeti.homotopyGroupMulAction](../../part-07/universal-covers/tauceti-homotopygroupmulaction.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.html#TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.html#TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology)
- [Source of `TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology` in TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.lean#L84)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
