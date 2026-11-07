---
declaration: theorem
origin: cited
lean: TauCeti.isWeakHomotopyEquivalence_cwApproximationMap
statement: formalized
proof: formalized
---

# CW approximation

(Hatcher, Proposition 4.13). For a path-connected space `X`, the map
`TauCeti.cwApproximationMap X x` from the CW complex `TauCeti.cwApproximation X x` to `X` is a weak
homotopy equivalence.

```lean
TauCeti.isWeakHomotopyEquivalence_cwApproximationMap.{u} (X : TopCat) (x : ↑X)
  [PathConnectedSpace ↑X] :
  (TopCat.Hom.hom (TauCeti.cwApproximationMap X x)).IsWeakHomotopyEquivalence
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isWeakHomotopyEquivalence_cwApproximationMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Basic.html#TauCeti.isWeakHomotopyEquivalence_cwApproximationMap).

## Sources

- [Tau Ceti documentation: `TauCeti.isWeakHomotopyEquivalence_cwApproximationMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Basic.html#TauCeti.isWeakHomotopyEquivalence_cwApproximationMap)
- [Source of `TauCeti.isWeakHomotopyEquivalence_cwApproximationMap` in TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Homotopy/CWApproximation/Basic.lean#L363)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)
