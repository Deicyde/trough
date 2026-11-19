---
declaration: theorem
origin: cited
lean: TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace
statement: formalized
proof: formalized
---

# Every group has a cellular classifying space

**Every group has a cellular classifying space**, satisfying the standing hypotheses of
covering-space theory: for every group `G` there is a set `R` of relators on the generators `G`
such that the cellular classifying space of `⟨G | R⟩` is a locally path-connected, semilocally
simply connected `K(G, 1)`. Take the tautological presentation, whose relators are the kernel of
the evaluation map `FreeGroup G →* G`. No hypothesis on the group is needed. This is the cellular
counterpart of `TauCeti.exists_isEilenbergMacLaneSpaceOne`.

```lean
TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace.{u} (G : Type u) [Group G] :
  ∃ R,
    LocallyPathConnectedSpace ↑(TauCeti.cellularClassifyingSpace R) ∧
      TauCeti.SemilocallySimplyConnectedSpace ↑(TauCeti.cellularClassifyingSpace R) ∧
        TauCeti.IsEilenbergMacLaneSpaceOne G (↑(TauCeti.cellularClassifyingSpace R))
          (TauCeti.cellularClassifyingSpaceBasepoint R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cellular and the simplicial classifying spaces agree](the-cellular-and-the-simplicial-classifying-spac.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The Seifert--van Kampen theorem for a family with a common pairwise intersection](../fundamental-group/the-seifert-van-kampen-theorem-for-a-family-with.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.html#TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.html#TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace)
- [Source of `TauCeti.exists_isEilenbergMacLaneSpaceOne_cellularClassifyingSpace` in TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.lean#L281)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
