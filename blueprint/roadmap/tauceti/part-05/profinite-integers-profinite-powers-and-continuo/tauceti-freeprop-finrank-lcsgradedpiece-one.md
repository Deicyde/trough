---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.finrank_lcsGradedPiece_one
statement: formalized
proof: formalized
---

# TauCeti.freeProP.finrank\_lcsGradedPiece\_one

`gr_1` of the free pro-`p` group on `X` has rank `#X choose 2` over `ℤ_p`.

```lean
TauCeti.freeProP.finrank_lcsGradedPiece_one.{u} (p : ℕ) [Fact (Nat.Prime p)] (X : Type u)
  [Fintype X] :
  Module.finrank ℤ_[p] (TauCeti.lcsGradedPiece (TauCeti.freeProP p X) 1) = (Fintype.card X).choose 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [`gr_1` of a free pro-`p` group is the exterior square of `gr_0`](gr-1-of-a-free-pro-p-group-is-the-exterior-squar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.finrank_lcsGradedPiece_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.finrank_lcsGradedPiece_one).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.finrank_lcsGradedPiece_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.finrank_lcsGradedPiece_one)
- [Source of `TauCeti.freeProP.finrank_lcsGradedPiece_one` in TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean#L408)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
