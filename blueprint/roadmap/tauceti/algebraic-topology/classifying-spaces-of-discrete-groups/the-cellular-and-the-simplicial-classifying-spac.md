---
declaration: def
origin: cited
lean: TauCeti.cellularHomotopyEquivClassifyingSpace
statement: formalized
---

# The cellular and the simplicial classifying spaces agree

For a presentation
`e : PresentedGroup R ≃* G` of `G`, this is a homotopy equivalence from the cellular classifying
space `cellularClassifyingSpace R` to Milnor's classifying space `classifyingSpace G`. Its forward
map is pointed, induces `e` under the identifications of both fundamental groups
(`TauCeti.classifyingSpaceFundamentalGroupMulEquiv_mapOfEq_cellularHomotopyEquivClassifyingSpace`),
and is unique up to pointed homotopy
(`TauCeti.homotopicRel_cellularHomotopyEquivClassifyingSpace_toFun`). Its homotopy inverse
induces `e⁻¹` up to a change of base point
(`TauCeti.exists_path_map_cellularHomotopyEquivClassifyingSpace_invFun`).

```lean
TauCeti.cellularHomotopyEquivClassifyingSpace.{u} {S : Type u} (R : Set (FreeGroup S)) {G : Type u}
  [Group G] (e : PresentedGroup R ≃* G) :
  ContinuousMap.HomotopyEquiv (↑(TauCeti.cellularClassifyingSpace R)) (TauCeti.classifyingSpace G)
```

## Depends on

- [Whitehead's theorem (Hatcher, Theorem 4.5)](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem-hatcher-theorem-4-5.md)

## Proof depends on

- [The cellular classifying space is a CW complex](the-cellular-classifying-space-is-a-cw-complex.md)
- [The fundamental group at `x` acts on every homotopy group based at `x`, an element of `π₁(X, x)` acting by transport around the loop it represents](../universal-covers/the-fundamental-group-at-x-acts-on-every-homotop.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The orbit space of a free cellular action is a CW complex](the-orbit-space-of-a-free-cellular-action-is-a-c.md)
- [The Seifert--van Kampen theorem for a family with a common pairwise intersection](../fundamental-group/the-seifert-van-kampen-theorem-for-a-family-with.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cellularHomotopyEquivClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.html#TauCeti.cellularHomotopyEquivClassifyingSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.cellularHomotopyEquivClassifyingSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.html#TauCeti.cellularHomotopyEquivClassifyingSpace)
- [Source of `TauCeti.cellularHomotopyEquivClassifyingSpace` in TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/Comparison.lean#L202)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
