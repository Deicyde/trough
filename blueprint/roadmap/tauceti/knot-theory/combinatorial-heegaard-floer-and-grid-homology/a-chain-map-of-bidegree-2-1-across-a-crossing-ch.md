---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc
statement: formalized
proof: formalized
---

# A chain map of bidegree `(-2, -1)` across a crossing change

If the segments of the two
columns of the column turn `C` interleave and the `O`-marking of the first column does not lie on
the arc of the second, then the commutation map turning in the row of the `X`-marking of the
first column has bidegree `(-2, -1)`, the bidegree of multiplication by `U`.

```lean
TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc {n : ℕ} {G : TauCeti.GridDiagram n}
  (C : TauCeti.GridDiagram.ColumnTurn n)
  (h : G.ColumnsInterleaving C.column ((finRotate n) C.column))
  (hO : G.O.toPerm C.column ∉ G.columnArc ((finRotate n) C.column))
  (hs : C.turnRow = G.X.toPerm C.column) : G.commutationBidegree C = (-2, -1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/CrossingChange/Grading.html#TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/CrossingChange/Grading.html#TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc)
- [Source of `TauCeti.GridDiagram.commutationBidegree_eq_of_notMem_columnArc` in TauCeti/KnotTheory/Grid/CrossingChange/Grading.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/CrossingChange/Grading.lean#L100)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
