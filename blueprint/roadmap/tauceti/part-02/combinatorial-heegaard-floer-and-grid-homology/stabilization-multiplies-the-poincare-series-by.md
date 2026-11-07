---
declaration: theorem
origin: cited
lean: TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX
statement: formalized
proof: formalized
---

# Stabilization multiplies the Poincaré series by `W`

The Poincaré series of the fully
blocked homology of the stabilization splitting an `X`-marking is that of the original diagram
times the series `W` of the stabilization factor.

```lean
TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX {n : ℕ}
  (G : TauCeti.OddComponentGridDiagram n) (s : Fin n) :
  (G.stabilizeX s).bigradedFullyBlockedHomologyPoincareSeries =
    G.bigradedFullyBlockedHomologyPoincareSeries * TauCeti.Bigraded.W
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Stabilization/FullyBlocked/Homology.html#TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Stabilization/FullyBlocked/Homology.html#TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX)
- [Source of `TauCeti.OddComponentGridDiagram.bigradedFullyBlockedHomologyPoincareSeries_stabilizeX` in TauCeti/KnotTheory/Grid/Stabilization/FullyBlocked/Homology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Stabilization/FullyBlocked/Homology.lean#L179)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
