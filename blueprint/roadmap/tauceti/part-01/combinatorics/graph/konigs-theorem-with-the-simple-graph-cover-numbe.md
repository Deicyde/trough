---
declaration: theorem
origin: cited
lean: Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum
statement: formalized
proof: formalized
---

# Kőnig's theorem with the simple-graph cover number

A multigraph with finitely many
actual edges and a finite covering bipartition has a unit-capacity matching whose size is the
vertex cover number of its simplification.

```lean
Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum.{u, v} {α : Type u}
  {β : Type v} {G : Graph α β} [Fintype ↑G.edgeSet] {L R : Finset ↑G.vertexSet}
  (hLR : G.IsBipartition L R) :
  ∃ x, G.IsCapacitatedMatching (fun x => 1) x ∧ ↑(∑ e, x e) = G.toSimpleGraph.vertexCoverNum
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kőnig's theorem for multiset capacitated matchings](konigs-theorem-for-multiset-capacitated-matching.md)

## Lean

Formalized in Tau Ceti as [`Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/VertexCover.html#Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum).

## Sources

- [Tau Ceti documentation: `Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/VertexCover.html#Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum)
- [Source of `Graph.IsBipartition.exists_isCapacitatedMatching_sum_eq_vertexCoverNum` in TauCeti/Combinatorics/Graph/Matching/VertexCover.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Matching/VertexCover.lean#L51)
