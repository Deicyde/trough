---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.stabilizeXHomologyMap_bijective
statement: formalized
proof: formalized
---

# Stabilization invariance of `GH⁻`

The map `GH⁻(G') → GH⁻(G)` induced by the
stabilization chain map is bijective.

```lean
TauCeti.GridDiagram.stabilizeXHomologyMap_bijective.{u_1} {n : ℕ} (G : TauCeti.GridDiagram n)
  (s : Fin n) (R : Type u_1) [CommRing R] [CharP R 2] :
  Function.Bijective ⇑(G.stabilizeXHomologyMap s R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.stabilizeXHomologyMap_bijective`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Stabilization/Homology.html#TauCeti.GridDiagram.stabilizeXHomologyMap_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.stabilizeXHomologyMap_bijective`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Stabilization/Homology.html#TauCeti.GridDiagram.stabilizeXHomologyMap_bijective)
- [Source of `TauCeti.GridDiagram.stabilizeXHomologyMap_bijective` in TauCeti/KnotTheory/Grid/Stabilization/Homology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Stabilization/Homology.lean#L213)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
