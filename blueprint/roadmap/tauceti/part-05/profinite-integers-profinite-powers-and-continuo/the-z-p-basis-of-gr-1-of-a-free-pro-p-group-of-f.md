---
declaration: def
origin: cited
lean: TauCeti.freeProP.lcsDegreeOneBasis
statement: formalized
---

# The `ℤ_p`-basis of `gr_1` of a free pro-`p` group of finite rank

, formed by the brackets
`[x_i, x_j]` of the generator classes for `i < j`
(`TauCeti.lcsGradedPiece_one_freeProP_bijective`).

```lean
TauCeti.freeProP.lcsDegreeOneBasis.{u} (p : ℕ) [Fact (Nat.Prime p)] (X : Type u) [Fintype X]
  [LinearOrder X] :
  Module.Basis { ij // ij.1 < ij.2 } ℤ_[p] (TauCeti.lcsGradedPiece (TauCeti.freeProP p X) 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.lcsDegreeOneBasis`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.lcsDegreeOneBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.lcsDegreeOneBasis`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.html#TauCeti.freeProP.lcsDegreeOneBasis)
- [Source of `TauCeti.freeProP.lcsDegreeOneBasis` in TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Free/LowerCentralSeries.lean#L335)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
