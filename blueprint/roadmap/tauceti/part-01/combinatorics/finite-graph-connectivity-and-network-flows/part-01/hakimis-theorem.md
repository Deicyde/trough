---
declaration: theorem
origin: cited
lean: Graph.exists_orientation_indegree_eq_iff
statement: formalized
proof: formalized
---

# Hakimi's theorem

A finite multigraph has an orientation with indegree `d` exactly when
`d` sums to the number of actual edges and every vertex set `S` has at most `d(S)` internal
edges.

```lean
Graph.exists_orientation_indegree_eq_iff.{u, v} {V : Type u} {E : Type v} {G : Graph V E}
  [Fintype ↑G.edgeSet] [Fintype ↑G.vertexSet] (d : ↑G.vertexSet → ℕ) :
  (∃ o, ∀ (x : ↑G.vertexSet), o.indegree x = d x) ↔
    ∑ x, d x = Fintype.card ↑G.edgeSet ∧
      ∀ (S : Finset ↑G.vertexSet), (G.internalEdges S).card ≤ ∑ x ∈ S, d x
```

## Depends on

- [Graph.Orientation](graph-orientation.md)

## Proof depends on

- [Bounded-indegree orientations](bounded-indegree-orientations.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff).

## Sources

- [Tau Ceti documentation: `Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff)
- [Source of `Graph.exists_orientation_indegree_eq_iff` in TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean#L550)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
