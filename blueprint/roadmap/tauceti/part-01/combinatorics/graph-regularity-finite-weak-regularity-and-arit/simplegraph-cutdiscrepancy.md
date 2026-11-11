---
declaration: def
origin: cited
lean: SimpleGraph.cutDiscrepancy
statement: formalized
---

# SimpleGraph.cutDiscrepancy

The cut discrepancy of `G` with respect to `P`: the largest deviation, over all rectangles
`(A, B)`, between the number of edges from `A` to `B` and its stepped prediction. It is
count-scaled, so it lies between `0` and `(card V) ^ 2`.

```lean
SimpleGraph.cutDiscrepancy.{u_1} {V : Type u_1} [Fintype V] [DecidableEq V] (G : SimpleGraph V)
  [DecidableRel G.Adj] (P : Finpartition Finset.univ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.cutDiscrepancy`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/CutDiscrepancy.html#SimpleGraph.cutDiscrepancy).

## Sources

- [Tau Ceti documentation: `SimpleGraph.cutDiscrepancy`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/CutDiscrepancy.html#SimpleGraph.cutDiscrepancy)
- [Source of `SimpleGraph.cutDiscrepancy` in TauCeti/Combinatorics/Regularity/Graph/CutDiscrepancy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Regularity/Graph/CutDiscrepancy.lean#L197)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Regularity/STATUS.md)
