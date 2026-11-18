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

- [Hoffman's circulation theorem](../network/hoffmans-circulation-theorem.md)
- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff).

## Sources

- [Tau Ceti documentation: `Graph.exists_orientation_indegree_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Orientation/Hakimi.html#Graph.exists_orientation_indegree_eq_iff)
- [Source of `Graph.exists_orientation_indegree_eq_iff` in TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Graph/Orientation/Hakimi.lean#L550)
