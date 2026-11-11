---
declaration: theorem
origin: cited
lean: Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths, Graph.exists_paths_setEdgeSeparator_card_eq, Graph.forall_exists_reachable_deleteEdges_iff_exists_paths, SimpleGraph.exists_paths_setEdgeSeparator_card_eq, SimpleGraph.forall_exists_reachable_deleteEdges_iff_exists_paths, Graph.exists_paths_edgeSeparator_card_eq, Graph.isEdgeReachable_iff_exists_paths, SimpleGraph.exists_paths_edgeSeparator_card_eq, SimpleGraph.isEdgeReachable_iff_exists_paths, Graph.exists_paths_vertexSeparator_card_add_card_eq, Graph.exists_paths_vertexSeparator_card_eq, Graph.forall_reachable_deleteVerts_iff_exists_paths, Graph.isVertexReachable_iff_exists_paths, Graph.exists_paths_setSeparator_card_eq, Graph.forall_exists_reachable_deleteVerts_iff_exists_paths
statement: formalized
proof: formalized
---

# Menger's theorem for adjacent vertices, predicate form

For distinct points,
after deleting every direct edge, every set of fewer than `k` nonterminal points leaves
the terminals reachable exactly when there are distinct internally disjoint paths indexed by
`Fin k ⊕ {e // G.IsLink e s t}`.

```lean
Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} {s t : α} [Finite ↑G.vertexSet] [Finite { e // G.IsLink e s t }] (hst : s ≠ t)
  (k : ℕ) :
  (∀ (X : Finset α),
      s ∉ X →
        t ∉ X → X.card < k → ((G.deleteEdges {e | G.IsLink e s t}).deleteVerts ↑X).Reachable s t) ↔
    ∃ P,
      Function.Injective P ∧
        (∀ (i : Fin k ⊕ { e // G.IsLink e s t }), (P i).IsPath) ∧
          Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Max-flow/min-cut theorem between vertex sets](../network/max-flow-min-cut-theorem-between-vertex-sets.md)
- [Menger's theorem for internally vertex-disjoint paths](../finite-graph-connectivity-and-network-flows/part-01/mengers-theorem-for-internally-vertex-disjoint-p.md)
- [Menger's theorem for vertex-strong arrow families](../network/mengers-theorem-for-vertex-strong-arrow-families.md)
- [Vertex-capacitated Menger's theorem for multigraphs](vertex-capacitated-mengers-theorem-for-multigrap.md)

## Lean

Formalized in Tau Ceti as [`Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.html#Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths).

## Other forms

**Menger's theorem for edge-disjoint paths between vertex sets in a multigraph.** Formalized in Tau Ceti as [`Graph.exists_paths_setEdgeSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#Graph.exists_paths_setEdgeSeparator_card_eq).

```lean
Graph.exists_paths_setEdgeSeparator_card_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] [Finite ↑G.edgeSet] {A B : Finset α} (hAB : Disjoint A B) :
  ∃ k a b P F,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (Pairwise fun i j => (P i).edges.Disjoint (P j).edges) ∧
              ↑F ⊆ G.edgeSet ∧ (∀ a ∈ A, ∀ b ∈ B, ¬(G.deleteEdges ↑F).Reachable a b) ∧ F.card = k
```

**Menger's theorem for edge-disjoint paths between vertex sets in a multigraph, predicate form.** Formalized in Tau Ceti as [`Graph.forall_exists_reachable_deleteEdges_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#Graph.forall_exists_reachable_deleteEdges_iff_exists_paths).

```lean
Graph.forall_exists_reachable_deleteEdges_iff_exists_paths.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} [Finite ↑G.vertexSet] [Finite ↑G.edgeSet] {A B : Finset α} (hAB : Disjoint A B)
  (k : ℕ) :
  (∀ (F : Finset β), F.card < k → ∃ a ∈ A, ∃ b ∈ B, (G.deleteEdges ↑F).Reachable a b) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
              Pairwise fun i j => (P i).edges.Disjoint (P j).edges
```

**Menger's theorem for edge-disjoint paths between vertex sets in a simple graph.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_setEdgeSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#SimpleGraph.exists_paths_setEdgeSeparator_card_eq).

```lean
SimpleGraph.exists_paths_setEdgeSeparator_card_eq.{u} {α : Type u} {G : SimpleGraph α} [Finite α]
  {A B : Finset α} (hAB : Disjoint A B) :
  ∃ k a b P F,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (Pairwise fun i j => (P i).edges.Disjoint (P j).edges) ∧
              ↑F ⊆ G.edgeSet ∧ (∀ a ∈ A, ∀ b ∈ B, ¬(G.deleteEdges ↑F).Reachable a b) ∧ F.card = k
```

**Menger's theorem for edge-disjoint paths between vertex sets in a simple graph, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.forall_exists_reachable_deleteEdges_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#SimpleGraph.forall_exists_reachable_deleteEdges_iff_exists_paths).

```lean
SimpleGraph.forall_exists_reachable_deleteEdges_iff_exists_paths.{u} {α : Type u}
  {G : SimpleGraph α} [Finite α] {A B : Finset α} (hAB : Disjoint A B) (k : ℕ) :
  (∀ (F : Finset (Sym2 α)), F.card < k → ∃ a ∈ A, ∃ b ∈ B, (G.deleteEdges ↑F).Reachable a b) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
              Pairwise fun i j => (P i).edges.Disjoint (P j).edges
```

**Menger's theorem for edge-disjoint paths in a multigraph.** Formalized in Tau Ceti as [`Graph.exists_paths_edgeSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#Graph.exists_paths_edgeSeparator_card_eq).

```lean
Graph.exists_paths_edgeSeparator_card_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {s t : α}
  [Finite ↑G.vertexSet] [Finite ↑G.edgeSet] (hst : s ≠ t) :
  ∃ k P F,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (Pairwise fun i j => (P i).edges.Disjoint (P j).edges) ∧
        ↑F ⊆ G.edgeSet ∧ ¬(G.deleteEdges ↑F).Reachable s t ∧ F.card = k
```

**Menger's theorem for edge-disjoint paths in a multigraph, predicate form.** Formalized in Tau Ceti as [`Graph.isEdgeReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#Graph.isEdgeReachable_iff_exists_paths).

```lean
Graph.isEdgeReachable_iff_exists_paths.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {s t : α}
  [Finite ↑G.vertexSet] [Finite ↑G.edgeSet] (hs : s ∈ G.vertexSet) (k : ℕ) :
  G.IsEdgeReachable k s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).edges.Disjoint (P j).edges
```

**Menger's theorem for edge-disjoint paths in a simple graph.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_edgeSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#SimpleGraph.exists_paths_edgeSeparator_card_eq).

```lean
SimpleGraph.exists_paths_edgeSeparator_card_eq.{u} {α : Type u} {G : SimpleGraph α} {s t : α}
  [Finite α] (hst : s ≠ t) :
  ∃ k P F,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (Pairwise fun i j => (P i).edges.Disjoint (P j).edges) ∧
        ↑F ⊆ G.edgeSet ∧ ¬(G.deleteEdges ↑F).Reachable s t ∧ F.card = k
```

**Menger's theorem for edge-disjoint paths in a simple graph, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.isEdgeReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Edge.html#SimpleGraph.isEdgeReachable_iff_exists_paths).

```lean
SimpleGraph.isEdgeReachable_iff_exists_paths.{u} {α : Type u} {G : SimpleGraph α} {s t : α}
  [Finite α] (k : ℕ) :
  G.IsEdgeReachable (↑k) s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).edges.Disjoint (P j).edges
```

**Menger's theorem for internally vertex-disjoint paths between possibly adjacent vertices.** Formalized in Tau Ceti as [`Graph.exists_paths_vertexSeparator_card_add_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.html#Graph.exists_paths_vertexSeparator_card_add_card_eq).

```lean
Graph.exists_paths_vertexSeparator_card_add_card_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  {s t : α} [Finite ↑G.vertexSet] [Finite { e // G.IsLink e s t }] (hst : s ≠ t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k ⊕ { e // G.IsLink e s t }), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          (∀ (e : { e // G.IsLink e s t }), P (Sum.inr e) = ⋯.toWalk) ∧
            ↑X ⊆ G.vertexSet ∧
              s ∉ X ∧
                t ∉ X ∧
                  ¬((G.deleteEdges {e | G.IsLink e s t}).deleteVerts ↑X).Reachable s t ∧ X.card = k
```

**Menger's theorem for internally vertex-disjoint paths in a multigraph.** Formalized in Tau Ceti as [`Graph.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.exists_paths_vertexSeparator_card_eq).

```lean
Graph.exists_paths_vertexSeparator_card_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  {s t : α} [Finite ↑G.vertexSet] (hst : s ≠ t) (hadj : ¬G.Adj s t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          ↑X ⊆ G.vertexSet ∧ s ∉ X ∧ t ∉ X ∧ ¬(G.deleteVerts ↑X).Reachable s t ∧ X.card = k
```

**Menger's theorem for internally vertex-disjoint paths in a multigraph, predicate form.** Formalized in Tau Ceti as [`Graph.forall_reachable_deleteVerts_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.forall_reachable_deleteVerts_iff_exists_paths).

```lean
Graph.forall_reachable_deleteVerts_iff_exists_paths.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  {s t : α} [Finite ↑G.vertexSet] (hst : s ≠ t) (hadj : ¬G.Adj s t) (k : ℕ) :
  (∀ (X : Finset α), s ∉ X → t ∉ X → X.card < k → (G.deleteVerts ↑X).Reachable s t) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for the vertex-reachability predicate.** Formalized in Tau Ceti as [`Graph.isVertexReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.isVertexReachable_iff_exists_paths).

```lean
Graph.isVertexReachable_iff_exists_paths.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] {s t : ↑G.vertexSet} (k : ℕ) :
  G.IsVertexReachable k s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for vertex-disjoint paths between vertex sets in a multigraph.** Formalized in Tau Ceti as [`Graph.exists_paths_setSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/SetToSet.html#Graph.exists_paths_setSeparator_card_eq).

```lean
Graph.exists_paths_setSeparator_card_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] (A B : Finset α) (hA : ↑A ⊆ G.vertexSet) (hB : ↑B ⊆ G.vertexSet) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ x ∈ (P i).support, x ≠ a i → x ≠ b i → x ∉ A ∧ x ∉ B) ∧
            (Pairwise fun i j => (P i).support.Disjoint (P j).support) ∧
              ↑X ⊆ G.vertexSet ∧ (∀ a ∈ A, ∀ b ∈ B, ¬(G.deleteVerts ↑X).Reachable a b) ∧ X.card = k
```

**Menger's theorem for vertex-disjoint paths between vertex sets in a multigraph, predicate form.** Formalized in Tau Ceti as [`Graph.forall_exists_reachable_deleteVerts_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/SetToSet.html#Graph.forall_exists_reachable_deleteVerts_iff_exists_paths).

```lean
Graph.forall_exists_reachable_deleteVerts_iff_exists_paths.{u, v} {α : Type u} {β : Type v}
  {G : Graph α β} [Finite ↑G.vertexSet] (A B : Finset α) (hA : ↑A ⊆ G.vertexSet)
  (hB : ↑B ⊆ G.vertexSet) (k : ℕ) :
  (∀ (X : Finset α), X.card < k → ∃ a ∈ A, ∃ b ∈ B, (G.deleteVerts ↑X).Reachable a b) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ x ∈ (P i).support, x ≠ a i → x ≠ b i → x ∉ A ∧ x ∉ B) ∧
              Pairwise fun i j => (P i).support.Disjoint (P j).support
```

## Sources

- [Tau Ceti documentation: `Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.html#Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths)
- [Source of `Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths` in TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.lean#L174)
