---
declaration: theorem
origin: cited
lean: Graph.isVertexConnected_iff_forall_exists_paths
statement: formalized
proof: formalized
---

# The global form of Menger's theorem for multigraphs

A multigraph with finitely many
actual vertices, more than `k` of them, is `k`-vertex-connected exactly when every two distinct
actual vertices `s` and `t`, adjacent or not, are joined by `k` distinct paths pairwise sharing no
vertex other than `s` and `t`. The edge set may be infinite.

```lean
Graph.isVertexConnected_iff_forall_exists_paths.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] {k : ℕ} (hk : k < Nat.card ↑G.vertexSet) :
  G.IsVertexConnected k ↔
    ∀ (s t : ↑G.vertexSet),
      s ≠ t →
        ∃ P,
          Function.Injective P ∧
            (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global form of Menger's theorem](../finite-graph-connectivity-and-network-flows/part-01/the-global-form-of-mengers-theorem.md)

## Lean

Formalized in Tau Ceti as [`Graph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.isVertexConnected_iff_forall_exists_paths).

## Sources

- [Tau Ceti documentation: `Graph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.isVertexConnected_iff_forall_exists_paths)
- [Source of `Graph.isVertexConnected_iff_forall_exists_paths` in TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.lean#L253)
