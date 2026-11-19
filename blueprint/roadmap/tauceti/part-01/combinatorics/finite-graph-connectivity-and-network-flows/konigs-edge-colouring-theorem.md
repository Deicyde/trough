---
declaration: theorem
origin: cited
lean: Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le, SimpleGraph.IsBipartite.edgeColorable_iff_maxDegree_le
statement: formalized
proof: formalized
---

# Kőnig's edge-colouring theorem

A finite bipartite multigraph admits a proper
edge-colouring by `k` colours exactly when every actual vertex is incident with at most `k`
actual edges.

```lean
Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le.{u, v} {α : Type u}
  {β : Type v} {G : Graph α β} {L R : Finset ↑G.vertexSet} {k : ℕ} [Finite ↑G.edgeSet]
  (hLR : G.IsBipartition L R) :
  Nonempty (G.EdgeColoring (Fin k)) ↔ ∀ x ∈ G.vertexSet, G.incidenceCount x ≤ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hall's theorem for finite bipartite multigraphs](../graph/halls-theorem-for-finite-bipartite-multigraphs.md)
- [Kőnig's line-colouring theorem](konigs-line-colouring-theorem.md)

## Lean

Formalized in Tau Ceti as [`Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le).

## Other forms

**Kőnig's edge-colouring theorem.** Formalized in Tau Ceti as [`SimpleGraph.IsBipartite.edgeColorable_iff_maxDegree_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#SimpleGraph.IsBipartite.edgeColorable_iff_maxDegree_le).

```lean
SimpleGraph.IsBipartite.edgeColorable_iff_maxDegree_le.{u} {α : Type u} {k : ℕ} {H : SimpleGraph α}
  [Fintype α] [DecidableRel H.Adj] (hH : H.IsBipartite) : H.EdgeColorable k ↔ H.maxDegree ≤ k
```

## Sources

- [Tau Ceti documentation: `Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le)
- [Source of `Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le` in TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.lean#L44)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
