---
declaration: theorem
origin: cited
lean: SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon
statement: formalized
proof: formalized
---

# Finite partition energy is graphon partition energy

For a graph `G` on `Fin m` with
`0 < m` and a partition `P` of its vertices, the size-weighted energy of `P` is the partition
energy of the graphon of `G` over the partition of the unit interval grouping the vertex cells by
the parts of `P`.

```lean
SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon {m : ℕ} [NeZero m] (G : SimpleGraph (Fin m))
  [DecidableRel G.Adj] (P : Finpartition Finset.univ) :
  TauCeti.DenseGraphLimits.graphonPartitionEnergy MeasureTheory.volume P.cellPartition ⋯
      (TauCeti.DenseGraphLimits.finiteGraphGraphon G) =
    G.weightedEnergy P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graphon/Energy.html#SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon).

## Sources

- [Tau Ceti documentation: `SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graphon/Energy.html#SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon)
- [Source of `SimpleGraph.graphonPartitionEnergy_finiteGraphGraphon` in TauCeti/Combinatorics/Regularity/Graphon/Energy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Regularity/Graphon/Energy.lean#L102)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Regularity/STATUS.md)
