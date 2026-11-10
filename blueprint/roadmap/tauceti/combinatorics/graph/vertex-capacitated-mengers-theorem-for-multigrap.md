---
declaration: theorem
origin: cited
lean: Graph.exists_paths_vertexSeparator_sum_eq, Graph.exists_paths_setSeparator_sum_eq
statement: formalized
proof: formalized
---

# Vertex-capacitated Menger's theorem for multigraphs

Let `s ≠ t` be points of a multigraph
with finitely many actual vertices, joined by no edge, and let `c v` be a capacity on every vertex.
Some family of `k` paths from `s` to `t`, in which every vertex `v` other than `s` and `t` lies on
at most `c v` members, and some set `X` of actual vertices avoiding `s` and `t`, whose deletion
leaves `s` and `t` unreachable, satisfy `∑ v ∈ X, c v = k`. By
`Graph.card_le_sum_of_not_reachable_deleteVerts`, the family is then largest and the separator of
least weight.

```lean
Graph.exists_paths_vertexSeparator_sum_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {s t : α}
  [Finite ↑G.vertexSet] [DecidableEq α] (c : α → ℕ) (hst : s ≠ t) (hadj : ¬G.Adj s t) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : α), v ≠ s → v ≠ t → {i | v ∈ (P i).support}.card ≤ c v) ∧
        ↑X ⊆ G.vertexSet ∧ s ∉ X ∧ t ∉ X ∧ ¬(G.deleteVerts ↑X).Reachable s t ∧ ∑ v ∈ X, c v = k
```

## Depends on

- [Graph.Walk](../finite-graph-connectivity-and-network-flows/graph-walk.md)

## Proof depends on

- [Vertex-capacitated Menger's theorem for directed paths](../network/vertex-capacitated-mengers-theorem-for-directed.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.exists_paths_vertexSeparator_sum_eq).

## Other forms

**Vertex-capacitated Menger's theorem between vertex sets in a multigraph.** Formalized in Tau Ceti as [`Graph.exists_paths_setSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/SetToSet.html#Graph.exists_paths_setSeparator_sum_eq).

```lean
Graph.exists_paths_setSeparator_sum_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] [DecidableEq α] (c : α → ℕ) (A B : Finset α) (hA : ↑A ⊆ G.vertexSet)
  (hB : ↑B ⊆ G.vertexSet) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ x ∈ (P i).support, x ≠ a i → x ≠ b i → x ∉ A ∧ x ∉ B) ∧
            (∀ (x : α), {i | x ∈ (P i).support}.card ≤ c x) ∧
              ↑X ⊆ G.vertexSet ∧
                (∀ a ∈ A, ∀ b ∈ B, ¬(G.deleteVerts ↑X).Reachable a b) ∧ ∑ x ∈ X, c x = k
```

## Sources

- [Tau Ceti documentation: `Graph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.exists_paths_vertexSeparator_sum_eq)
- [Source of `Graph.exists_paths_vertexSeparator_sum_eq` in TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.lean#L123)
