---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq
statement: formalized
proof: formalized
---

# TauCeti.GridDiagram.unblockedDifferential\_commutationHomotopy\_add\_eq

The homotopy equation `∂ ∘ H + H ∘ ∂ = 1 + Ψ ∘ Φ` of a column commutation, over any
commutative semiring of characteristic two: the hexagon-counting map `H` is a chain homotopy
between the identity of `GC⁻(G)` and the round trip through the commuted diagram.

```lean
TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq.{u_1} {n : ℕ}
  (G : TauCeti.GridDiagram n) (C : G.ColumnCommutationData) (R : Type u_1) [CommSemiring R]
  [CharP R 2] (c : TauCeti.GridChainMinus R n) :
  (G.unblockedDifferential R) ((G.commutationHomotopy R C) c) +
      (G.commutationHomotopy R C) ((G.unblockedDifferential R) c) =
    c +
      ((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).commutationMap R
          C.reverse.toColumnTurn)
        ((G.commutationMap R C.toColumnTurn) c)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Commutation/Homotopy/Equation.html#TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Commutation/Homotopy/Equation.html#TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq)
- [Source of `TauCeti.GridDiagram.unblockedDifferential_commutationHomotopy_add_eq` in TauCeti/KnotTheory/Grid/Commutation/Homotopy/Equation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Commutation/Homotopy/Equation.lean#L93)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
