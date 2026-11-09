---
declaration: theorem
origin: cited
lean: Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq
statement: formalized
proof: formalized
---

# Kőnig's theorem for multiset capacitated matchings

Let `L` and `R` form a bipartition of a
multigraph with finitely many actual edges, and let `b v : ℕ` be a capacity on every actual vertex.
Some multiset capacitated matching `x` and some vertex cover `C` satisfy
`∑ e, x e = ∑ v ∈ C, b v`. By `Graph.IsCapacitatedMatching.sum_le_sum_of_isVertexCover`, the
matching is then largest and the cover of least weight.

```lean
Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq.{u, v} {α : Type u}
  {β : Type v} {G : Graph α β} [Fintype ↑G.edgeSet] {L R : Finset ↑G.vertexSet}
  (hLR : G.IsBipartition L R) (b : ↑G.vertexSet → ℕ) :
  ∃ x C, G.IsCapacitatedMatching b x ∧ G.IsVertexCover ↑C ∧ ∑ e, x e = ∑ v ∈ C, b v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vertex-capacitated Menger's theorem for directed paths](../network/vertex-capacitated-mengers-theorem-for-directed.md)

## Lean

Formalized in Tau Ceti as [`Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/Capacitated.html#Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq).

## Sources

- [Tau Ceti documentation: `Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/Capacitated.html#Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq)
- [Source of `Graph.IsBipartition.exists_isCapacitatedMatching_isVertexCover_sum_eq` in TauCeti/Combinatorics/Graph/Matching/Capacitated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Matching/Capacitated.lean#L122)
