---
declaration: def
origin: cited
lean: TauCeti.universalGSpaceStandardHomotopyEquiv
statement: formalized
---

# Milnor's join resolution is homotopy equivalent to the standard resolution, by a homotopy equivalence whose forward map is the explicit join-to-standard chain map

Its homotopy inverse is
the lift of the identity of the trivial representation from the standard resolution to the join
resolution.

```lean
TauCeti.universalGSpaceStandardHomotopyEquiv.{u} (k : Type u) [CommRing k] (G : Type u) [Group G] :
  HomotopyEquiv (TauCeti.universalGSpaceChainComplex k G) (Rep.standardComplex k G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.universalGSpaceStandardHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/StandardResolution.html#TauCeti.universalGSpaceStandardHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.universalGSpaceStandardHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/StandardResolution.html#TauCeti.universalGSpaceStandardHomotopyEquiv)
- [Source of `TauCeti.universalGSpaceStandardHomotopyEquiv` in TauCeti/AlgebraicTopology/ClassifyingSpace/StandardResolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/StandardResolution.lean#L172)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
