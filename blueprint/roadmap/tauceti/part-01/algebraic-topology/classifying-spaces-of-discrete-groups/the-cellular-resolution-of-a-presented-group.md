---
declaration: def
origin: cited
lean: TauCeti.cellularClassifyingSpaceResolution
statement: formalized
---

# The cellular resolution of a presented group

the cellular chains of the universal cover of
the cellular classifying space of `⟨S | R⟩`, with its lifted CW structure, form a projective
resolution of the trivial representation of `PresentedGroup R` over `k`. In degree `n` they are
free over `k[PresentedGroup R]` with one generator for each `n`-cell of the cellular classifying
space (`TauCeti.cellularChainRepIsoFree`). The group acts by the deck transformations of
`isQuotientCoveringMap_cellularClassifyingSpace_universalCover`. This is
`TauCeti.cellularResolutionOfIsAspherical` for the cellular classifying space.

```lean
TauCeti.cellularClassifyingSpaceResolution.{u} {S : Type u} (R : Set (FreeGroup S)) (k : Type u)
  [CommRing k] : CategoryTheory.ProjectiveResolution (Rep.trivial k (PresentedGroup R) k)
```

## Depends on

- [The cellular chains of a contractible free cover are a projective resolution of the trivial representation of `G` over `R`](the-cellular-chains-of-a-contractible-free-cover.md)

## Proof depends on

- [A CW structure lifts along a covering map](a-cw-structure-lifts-along-a-covering-map.md)
- [The cellular and the simplicial classifying spaces agree](the-cellular-and-the-simplicial-classifying-spac.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Seifert--van Kampen theorem for a family with a common pairwise intersection](../fundamental-group/the-seifert-van-kampen-theorem-for-a-family-with.md)
- [Whitehead's theorem (Hatcher, Theorem 4.5)](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem-hatcher-theorem-4-5.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cellularClassifyingSpaceResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/PresentedGroupResolution.html#TauCeti.cellularClassifyingSpaceResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.cellularClassifyingSpaceResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/PresentedGroupResolution.html#TauCeti.cellularClassifyingSpaceResolution)
- [Source of `TauCeti.cellularClassifyingSpaceResolution` in TauCeti/AlgebraicTopology/ClassifyingSpace/PresentedGroupResolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/PresentedGroupResolution.lean#L98)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
