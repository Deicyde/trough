---
declaration: theorem
origin: cited
lean: Graph.exists_orientation_indegree_mem_Icc_iff
statement: formalized
proof: formalized
---

# Bounded-indegree orientations

For vertex bounds `a ≤ b`, a finite multigraph has an
orientation with every indegree between `a` and `b` exactly when every vertex set `S` has at most
`b(S)` internal edges and at least `a(S)` incident edges.

```lean
Graph.exists_orientation_indegree_mem_Icc_iff.{u, v} {V : Type u} {E : Type v} {G : Graph V E}
  [Fintype ↑G.edgeSet] [Finite ↑G.vertexSet] {a b : ↑G.vertexSet → ℕ} (hab : a ≤ b) :
  (∃ o, ∀ (x : ↑G.vertexSet), o.indegree x ∈ Set.Icc (a x) (b x)) ↔
    (∀ (S : Finset ↑G.vertexSet), (G.internalEdges S).card ≤ ∑ x ∈ S, b x) ∧
      ∀ (S : Finset ↑G.vertexSet), ∑ x ∈ S, a x ≤ (G.incidentEdges S).card
```

## Depends on

- [Graph.Orientation](graph-orientation.md)

## Proof depends on

- [Hoffman's circulation theorem](hoffmans-circulation-theorem.md)
- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_orientation_indegree_mem_Icc_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_mem_Icc_iff).

## Sources

- [Tau Ceti documentation: `Graph.exists_orientation_indegree_mem_Icc_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_mem_Icc_iff)
- [Source of `Graph.exists_orientation_indegree_mem_Icc_iff` in TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean#L499)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
