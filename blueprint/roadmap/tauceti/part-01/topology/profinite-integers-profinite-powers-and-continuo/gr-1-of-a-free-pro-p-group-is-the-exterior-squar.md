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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne)
- [Source of `TauCeti.freeProP.exteriorSquareEquivLcsGradedPieceOne` in TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean#L379)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteArithmetic/STATUS.md)
