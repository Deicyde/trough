---
declaration: def
origin: cited
lean: TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne
statement: formalized
---

# `gr_1` of a free pro-`p` group is the exterior square of `gr_0`

For the free pro-`p` group
`F` on a finite type, the graded bracket induces an isomorphism of `ℤ_p`-modules
`⋀²gr_0(F) ≃ gr_1(F)`, `x ∧ y ↦ [x, y]` (`exteriorSquareEquivLcsGradedPieceOne_ιMulti`).

```lean
TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne.{u} (p : ℕ) [Fact (Nat.Prime p)] (X : Type u)
  [Fintype X] :
  ↥(⋀[ℤ_[p]]^2 (TauCeti.lcsGradedPiece (TauCeti.freeProP p X) 0)) ≃ₗ[ℤ_[p]]
    TauCeti.lcsGradedPiece (TauCeti.freeProP p X) 1
```

## Depends on

- [The `ℤ_p`-basis of `gr_1` of a free pro-`p` group of finite rank](the-z-p-basis-of-gr-1-of-a-free-pro-p-group-of-f.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne)
- [Source of `TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne` in TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean#L379)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
