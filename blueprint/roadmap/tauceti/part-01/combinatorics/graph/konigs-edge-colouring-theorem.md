---
declaration: theorem
origin: cited
lean: Graph.IsBipartition.nonempty_edgeColoring_fin_iff, Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le
statement: formalized
proof: formalized
---

# Kőnig's edge-colouring theorem

A finite bipartite multigraph has a proper
edge-colouring by `k` colours if and only if every actual vertex is incident with at most `k`
actual edges. Parallel edges are counted separately.

```lean
Graph.IsBipartition.nonempty_edgeColoring_fin_iff.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  {L R : Finset ↑G.vertexSet} {k : ℕ} [Finite ↑G.edgeSet] (hLR : G.IsBipartition L R) :
  Nonempty (G.EdgeColoring (Fin k)) ↔ ∀ x ∈ G.vertexSet, G.incidenceCount x ≤ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hall's theorem for finite bipartite multigraphs](halls-theorem-for-finite-bipartite-multigraphs.md)

## Lean

Formalized in Tau Ceti as [`Graph.IsBipartition.nonempty_edgeColoring_fin_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/BipartiteColoring.html#Graph.IsBipartition.nonempty_edgeColoring_fin_iff).

## Other forms

**Kőnig's edge-colouring theorem.** Formalized in Tau Ceti as [`Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/EdgeColoring.html#Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le).

```lean
Graph.IsBipartition.nonempty_edgeColoring_iff_forall_incidenceCount_le.{u, v} {α : Type u}
  {β : Type v} {G : Graph α β} {L R : Finset ↑G.vertexSet} {k : ℕ} [Finite ↑G.edgeSet]
  (hLR : G.IsBipartition L R) :
  Nonempty (G.EdgeColoring (Fin k)) ↔ ∀ x ∈ G.vertexSet, G.incidenceCount x ≤ k
```

## Sources

- [Tau Ceti documentation: `Graph.IsBipartition.nonempty_edgeColoring_fin_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Matching/BipartiteColoring.html#Graph.IsBipartition.nonempty_edgeColoring_fin_iff)
- [Source of `Graph.IsBipartition.nonempty_edgeColoring_fin_iff` in TauCeti/Combinatorics/Graph/Matching/BipartiteColoring.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Matching/BipartiteColoring.lean#L48)
