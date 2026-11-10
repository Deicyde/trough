---
declaration: def
origin: cited
lean: TauCeti.IsProP.gradedLieAlgebra
statement: formalized
---

# The `ℤ_ℓ`-Lie algebra of a pro-`ℓ` group

For a pro-`ℓ` group `G`, the graded Lie ring
`⨁ k, gr_k(G)` of the lower `p`-series is a Lie algebra over `ℤ_ℓ`, for the `ℤ_ℓ`-module structure
which in each degree is `TauCeti.IsProP.gradedPieceModule`: the graded bracket is `ℤ_ℓ`-bilinear.
For `p = 0` this is the `ℤ_ℓ`-Lie algebra of the closed lower central series.

```lean
TauCeti.IsProP.gradedLieAlgebra.{u} (p : ℕ) {G : Type u} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] {ℓ : ℕ} [Fact (Nat.Prime ℓ)] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hG : TauCeti.IsProP ℓ G) : LieAlgebra ℤ_[ℓ] (DirectSum ℕ fun k => TauCeti.gradedPiece p G k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobi identity](the-jacobi-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.gradedLieAlgebra`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.html#TauCeti.IsProP.gradedLieAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.gradedLieAlgebra`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.html#TauCeti.IsProP.gradedLieAlgebra)
- [Source of `TauCeti.IsProP.gradedLieAlgebra` in TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/LowerCentralSeries/Graded/LieRing.lean#L236)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
