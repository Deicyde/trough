---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential
statement: formalized
proof: formalized
---

# The commutation map is a chain map

Over a commutative semiring of characteristic two,
counting empty pentagons turning on either side of the replaced grid line intertwines the unblocked
differentials of a grid diagram and of the diagram with the two columns of the turn exchanged.
This holds at every column turn: the two marking segments need not be non-interleaving.

```lean
TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential.{u_1} {n : ℕ}
  (G : TauCeti.GridDiagram n) (C : TauCeti.GridDiagram.ColumnTurn n) (R : Type u_1) [CommSemiring R]
  [CharP R 2] :
  G.commutationMap R C ∘ₛₗ G.unblockedDifferential R =
    (TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).unblockedDifferential
        R ∘ₛₗ
      G.commutationMap R C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Commutation/InitialPentagon/Overlap/Residual/Assembly.html#TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Commutation/InitialPentagon/Overlap/Residual/Assembly.html#TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential)
- [Source of `TauCeti.GridDiagram.commutationMap_comp_unblockedDifferential` in TauCeti/KnotTheory/Grid/Commutation/InitialPentagon/Overlap/Residual/Assembly.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Commutation/InitialPentagon/Overlap/Residual/Assembly.lean#L106)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
