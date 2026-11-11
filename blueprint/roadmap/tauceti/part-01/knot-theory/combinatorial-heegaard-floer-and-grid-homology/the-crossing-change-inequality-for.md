---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy
statement: formalized
proof: formalized
---

# The crossing change inequality for `τ`

Let the segments of the columns `a` and
`b = finRotate n a` of a knot grid `G` interleave with `O_a` on the arc of column `b`, and let `C`
turn in the row of `O_a`. Suppose that the crossing change maps, the commutation map `Φ` of `C`
and the commutation map `Ψ` of `G' = G.swapColumns a b` turning in the row of `X_b`, have
composites `ΨΦ` and `ΦΨ` chain homotopic to multiplication by `V_b` and `V_a`. Then
`τ(G) - 1 ≤ τ(G') ≤ τ(G)`.

```lean
TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy.{u_1} {n : ℕ}
  {G : TauCeti.GridDiagram n} (hG : G.IsKnot) {K : Type u_1} [CommRing K] [CharP K 2]
  {C : TauCeti.GridDiagram.ColumnTurn n}
  (h : G.ColumnsInterleaving C.column ((finRotate n) C.column))
  (hO : G.O.toPerm C.column ∈ G.columnArc ((finRotate n) C.column))
  (hs : C.turnRow = G.O.toPerm C.column)
  (hH :
    ∃ H,
      ∀ (c : TauCeti.GridChainMinus K n),
        (G.unblockedDifferential K) (H c) + H ((G.unblockedDifferential K) c) =
          MvPolynomial.X ((finRotate n) C.column) • c +
            ((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).commutationMap K
                (C.withTurnRow (G.X.toPerm ((finRotate n) C.column))))
              ((G.commutationMap K C) c))
  (hH' :
    ∃ H',
      ∀ (c : TauCeti.GridChainMinus K n),
        ((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).unblockedDifferential
                K)
              (H' c) +
            H'
              (((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column)
                      G).unblockedDifferential
                  K)
                c) =
          MvPolynomial.X C.column • c +
            ((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column)
                    (TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column)
                      G)).commutationMap
                K
                ((C.withTurnRow (G.X.toPerm ((finRotate n) C.column))).withTurnRow
                  (G.O.toPerm C.column)))
              (((TauCeti.GridDiagram.swapColumns C.column ((finRotate n) C.column) G).commutationMap
                  K (C.withTurnRow (G.X.toPerm ((finRotate n) C.column))))
                c)) :
  ⋯.tau K ∈ Set.Icc (hG.tau K - 1) (hG.tau K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/CrossingChange/Tau.html#TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/CrossingChange/Tau.html#TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy)
- [Source of `TauCeti.GridDiagram.IsKnot.tau_swapColumns_mem_Icc_of_homotopy` in TauCeti/KnotTheory/Grid/CrossingChange/Tau.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Grid/CrossingChange/Tau.lean#L98)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
