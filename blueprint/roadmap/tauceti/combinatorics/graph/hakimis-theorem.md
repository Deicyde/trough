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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hoffman's circulation theorem](../finite-graph-connectivity-and-network-flows/hoffmans-circulation-theorem.md)
- [Integrality of maximum flows](../finite-graph-connectivity-and-network-flows/integrality-of-maximum-flows.md)
- [TauCeti.AuxTerminalHom](../finite-graph-connectivity-and-network-flows/tauceti-auxterminalhom.md)
- [TauCeti.residualUpdate](../finite-graph-connectivity-and-network-flows/tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff).

## Sources

- [Tau Ceti documentation: `Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff)
- [Source of `Graph.exists_orientation_indegree_eq_iff` in TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean#L550)
