---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass
statement: formalized
proof: formalized
---

# The commutation map on `GH⁻` preserves the class of the `X`-marking state

Under the
condition of `commutationMap_single_X`, the induced map on unblocked grid homology sends the
class of the `X`-marking state of `G` to that of the commuted diagram.

```lean
TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass.{u_1} {n : ℕ}
  (G : TauCeti.GridDiagram n) (R : Type u_1) [CommRing R] [CharP R 2] (C : G.ColumnCommutationData)
  (hs : C.turnRow ≠ G.X.toPerm ((finRotate n) C.column)) :
  (G.unblockedHomologyCommutationMap R C.toColumnTurn) (G.XMarkingClass R) =
    (TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).XMarkingClass R
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The commutation map is a chain map](the-commutation-map-is-a-chain-map.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Commutation/XMarking.html#TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Commutation/XMarking.html#TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass)
- [Source of `TauCeti.GridDiagram.unblockedHomologyCommutationMap_XMarkingClass` in TauCeti/KnotTheory/Grid/Homology/Commutation/XMarking.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Homology/Commutation/XMarking.lean#L190)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
