---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_fan_separator_card_eq, Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths, TauCeti.exists_paths_arrowSeparator_card_eq, TauCeti.exists_paths_setArrowSeparator_card_eq, TauCeti.forall_exists_reachableWithout_iff_exists_paths, TauCeti.forall_reachableWithout_iff_exists_paths, Graph.exists_paths_setEdgeSeparator_card_eq, Graph.forall_exists_reachable_deleteEdges_iff_exists_paths, SimpleGraph.exists_paths_setEdgeSeparator_card_eq, SimpleGraph.forall_exists_reachable_deleteEdges_iff_exists_paths, Graph.exists_paths_edgeSeparator_card_eq, Graph.isEdgeReachable_iff_exists_paths, SimpleGraph.exists_paths_edgeSeparator_card_eq, SimpleGraph.isEdgeReachable_iff_exists_paths, SimpleGraph.forall_exists_walk_iff_exists_fan, TauCeti.exists_paths_vertexSeparator_card_eq, TauCeti.exists_paths_isMixedSeparator_card_eq, TauCeti.forall_not_isMixedSeparator_iff_exists_paths, TauCeti.forall_reachableAvoiding_iff_exists_paths, SimpleGraph.exists_paths_vertexSeparator_card_eq, SimpleGraph.exists_paths_vertexSeparator_card_add_one_eq, Graph.exists_paths_vertexSeparator_card_add_card_eq, Digraph.exists_paths_vertexSeparator_card_eq, Graph.exists_paths_vertexSeparator_card_eq, Graph.forall_reachable_deleteVerts_iff_exists_paths, SimpleGraph.forall_reachable_induce_iff_exists_paths, Graph.isVertexReachable_iff_exists_paths, Digraph.forall_reachableAvoiding_iff_exists_paths, SimpleGraph.isVertexReachable_iff_exists_paths, TauCeti.exists_paths_setSeparator_card_eq, TauCeti.forall_exists_reachableAvoiding_iff_exists_paths, SimpleGraph.exists_paths_setSeparator_card_eq, Graph.exists_paths_setSeparator_card_eq, Graph.forall_exists_reachable_deleteVerts_iff_exists_paths, SimpleGraph.forall_exists_walk_iff_exists_paths, TauCeti.isVertexStrong_iff_exists_paths
statement: formalized
proof: formalized
---

# Menger's theorem for fans

Let `x` be a vertex outside a set `U` of vertices of a simple
graph on a finite vertex type. Some family of `k` paths, the `i`-th from `x` to `u i ∈ U` with its
other vertices outside `U`, any two of which share only the vertex `x`, and some set of `k`
vertices other than `x` meeting every walk from `x` to a vertex of `U` exist. By
`SimpleGraph.card_le_card_of_fan`, the fan is then largest and the separator smallest.

```lean
SimpleGraph.exists_fan_separator_card_eq.{u} {V : Type u} {G : SimpleGraph V} {x : V} {U : Finset V}
  [Finite V] (hx : x ∉ U) :
  ∃ k u P X,
    Function.Injective u ∧
      (∀ (i : Fin k), u i ∈ U) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ u i → v ∉ U) ∧
            (Pairwise fun i j => ∀ v ∈ (P i).support, v ∈ (P j).support → v = x) ∧
              x ∉ X ∧ (∀ y ∈ U, ∀ (p : G.Walk x y), ∃ v ∈ p.support, v ∈ X) ∧ X.card = k
```

## Depends on

- [Graph.Walk](../finite-graph-connectivity-and-network-flows/graph-walk.md)

## Proof depends on

- [Max-flow/min-cut theorem](../finite-graph-connectivity-and-network-flows/max-flow-min-cut-theorem.md)
- [Max-flow/min-cut theorem between vertex sets](../finite-graph-connectivity-and-network-flows/max-flow-min-cut-theorem-between-vertex-sets.md)
- [Path–cycle decomposition](../finite-graph-connectivity-and-network-flows/path-cycle-decomposition.md)
- [TauCeti.AuxTerminalHom](../finite-graph-connectivity-and-network-flows/tauceti-auxterminalhom.md)
- [Vertex-capacitated Menger's theorem](vertex-capacitated-mengers-theorem.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_fan_separator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.html#SimpleGraph.exists_fan_separator_card_eq).

## Other forms

**Menger's theorem for adjacent vertices, predicate form.** Formalized in Tau Ceti as [`Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Adjacent.html#Graph.forall_reachable_deleteEdges_deleteVerts_iff_exists_paths).

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

**Menger's theorem for arrow-disjoint directed paths.** Formalized in Tau Ceti as [`TauCeti.exists_paths_arrowSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Edge.html#TauCeti.exists_paths_arrowSeparator_card_eq).

```lean
TauCeti.exists_paths_arrowSeparator_card_eq.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] [∀ (x y : V), Finite (Q x y)] (hst : s ≠ t) :
  ∃ k P F,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (Pairwise fun i j => (P i).arrows.Disjoint (P j).arrows) ∧
        ¬TauCeti.ReachableWithout (↑F) s t ∧ F.card = k
```

**Menger's theorem for arrow-disjoint directed paths between vertex sets.** Formalized in Tau Ceti as [`TauCeti.exists_paths_setArrowSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Edge.html#TauCeti.exists_paths_setArrowSeparator_card_eq).

```lean
TauCeti.exists_paths_setArrowSeparator_card_eq.{u, v} {V : Type u} {Q : V → V → Type v} [Finite V]
  [∀ (x y : V), Finite (Q x y)] {A B : Finset V} (hAB : Disjoint A B) :
  ∃ k a b P F,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).vertices, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (Pairwise fun i j => (P i).arrows.Disjoint (P j).arrows) ∧
              (∀ a ∈ A, ∀ b ∈ B, ¬TauCeti.ReachableWithout (↑F) a b) ∧ F.card = k
```

**Menger's theorem for arrow-disjoint directed paths between vertex sets, predicate form.** Formalized in Tau Ceti as [`TauCeti.forall_exists_reachableWithout_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Edge.html#TauCeti.forall_exists_reachableWithout_iff_exists_paths).

```lean
TauCeti.forall_exists_reachableWithout_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v}
  [Finite V] [∀ (x y : V), Finite (Q x y)] {A B : Finset V} (k : ℕ) :
  (∀ (F : Finset ((x : V) × (y : V) × Q x y)),
      F.card < k → ∃ a ∈ A, ∃ b ∈ B, TauCeti.ReachableWithout (↑F) a b) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).vertices, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
              Pairwise fun i j => (P i).arrows.Disjoint (P j).arrows
```

**Menger's theorem for arrow-disjoint directed paths, predicate form.** Formalized in Tau Ceti as [`TauCeti.forall_reachableWithout_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Edge.html#TauCeti.forall_reachableWithout_iff_exists_paths).

```lean
TauCeti.forall_reachableWithout_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] [∀ (x y : V), Finite (Q x y)] (k : ℕ) :
  (∀ (F : Finset ((x : V) × (y : V) × Q x y)), F.card < k → TauCeti.ReachableWithout (↑F) s t) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).arrows.Disjoint (P j).arrows
```

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

**Menger's theorem for fans, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.forall_exists_walk_iff_exists_fan`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.html#SimpleGraph.forall_exists_walk_iff_exists_fan).

```lean
SimpleGraph.forall_exists_walk_iff_exists_fan.{u} {V : Type u} {G : SimpleGraph V} {x : V}
  {U : Finset V} [Finite V] (hx : x ∉ U) (k : ℕ) :
  (∀ (X : Finset V), X.card < k → x ∉ X → ∃ y ∈ U, ∃ p, ∀ v ∈ p.support, v ∉ X) ↔
    ∃ u P,
      Function.Injective u ∧
        (∀ (i : Fin k), u i ∈ U) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ u i → v ∉ U) ∧
              Pairwise fun i j => ∀ v ∈ (P i).support, v ∈ (P j).support → v = x
```

**Menger's theorem for internally vertex-disjoint directed paths.** Formalized in Tau Ceti as [`TauCeti.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Vertex.html#TauCeti.exists_paths_vertexSeparator_card_eq).

```lean
TauCeti.exists_paths_vertexSeparator_card_eq.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : IsEmpty (Q s t)) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding Q (↑X) s t ∧ X.card = k
```

**Menger's theorem for internally vertex-disjoint directed paths between possibly adjacent terminals.** Formalized in Tau Ceti as [`TauCeti.exists_paths_isMixedSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Adjacent.html#TauCeti.exists_paths_isMixedSeparator_card_eq).

```lean
TauCeti.exists_paths_isMixedSeparator_card_eq.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] [Fintype (Q s t)] (hst : s ≠ t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k ⊕ Q s t), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          (∀ (e : Q s t), P (Sum.inr e) = (TauCeti.ArrowWalk.nil s).cons e) ∧
            TauCeti.IsMixedSeparator X (TauCeti.arrowFinset Q s t) s t ∧ X.card = k
```

**Menger's theorem for internally vertex-disjoint directed paths between possibly adjacent terminals, predicate form.** Formalized in Tau Ceti as [`TauCeti.forall_not_isMixedSeparator_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Adjacent.html#TauCeti.forall_not_isMixedSeparator_iff_exists_paths).

```lean
TauCeti.forall_not_isMixedSeparator_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v}
  {s t : V} [Finite V] [Fintype (Q s t)] (hst : s ≠ t) (k : ℕ) :
  (∀ (X : Finset V), X.card < k → ¬TauCeti.IsMixedSeparator X (TauCeti.arrowFinset Q s t) s t) ↔
    ∃ P,
      Function.Injective P ∧
        (∀ (i : Fin k ⊕ Q s t), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for internally vertex-disjoint directed paths, predicate form.** Formalized in Tau Ceti as [`TauCeti.forall_reachableAvoiding_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Vertex.html#TauCeti.forall_reachableAvoiding_iff_exists_paths).

```lean
TauCeti.forall_reachableAvoiding_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : IsEmpty (Q s t)) (k : ℕ) :
  (∀ (X : Finset V), s ∉ X → t ∉ X → X.card < k → TauCeti.ReachableAvoiding Q (↑X) s t) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for internally vertex-disjoint paths.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_card_eq).

```lean
SimpleGraph.exists_paths_vertexSeparator_card_eq.{u} {V : Type u} {G : SimpleGraph V} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : ¬G.Adj s t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          ∃ (hs : s ∉ X) (ht : t ∉ X),
            ¬(SimpleGraph.induce (↑X)ᶜ G).Reachable ⟨s, hs⟩ ⟨t, ht⟩ ∧ X.card = k
```

**Menger's theorem for internally vertex-disjoint paths between adjacent vertices.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_vertexSeparator_card_add_one_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_card_add_one_eq).

```lean
SimpleGraph.exists_paths_vertexSeparator_card_add_one_eq.{u} {V : Type u} {G : SimpleGraph V}
  {s t : V} [Finite V] (h : G.Adj s t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin (k + 1)), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          P (Fin.last k) = h.toWalk ∧
            ∃ (hs : s ∉ X) (ht : t ∉ X),
              ¬(SimpleGraph.induce (↑X)ᶜ (G.deleteEdges {s(s, t)})).Reachable ⟨s, hs⟩ ⟨t, ht⟩ ∧
                X.card = k
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

**Menger's theorem for internally vertex-disjoint paths in a digraph.** Formalized in Tau Ceti as [`Digraph.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.exists_paths_vertexSeparator_card_eq).

```lean
Digraph.exists_paths_vertexSeparator_card_eq.{u} {V : Type u} {D : Digraph V} {s t : V} [Finite V]
  (hst : s ≠ t) (hadj : ¬D.Adj s t) :
  ∃ k P X,
    Function.Injective P ∧
      (∀ (i : Fin k), (P i).IsPath) ∧
        (Pairwise fun i j => (P i).InternallyDisjoint (P j)) ∧
          s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding D.AdjHom (↑X) s t ∧ X.card = k
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

**Menger's theorem for internally vertex-disjoint paths, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.forall_reachable_induce_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.forall_reachable_induce_iff_exists_paths).

```lean
SimpleGraph.forall_reachable_induce_iff_exists_paths.{u} {V : Type u} {G : SimpleGraph V} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : ¬G.Adj s t) (k : ℕ) :
  (∀ (X : Finset V) (hs : s ∉ X) (ht : t ∉ X),
      X.card < k → (SimpleGraph.induce (↑X)ᶜ G).Reachable ⟨s, hs⟩ ⟨t, ht⟩) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for the vertex-reachability predicate.** Formalized in Tau Ceti as [`Graph.isVertexReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.isVertexReachable_iff_exists_paths).

```lean
Graph.isVertexReachable_iff_exists_paths.{u, v} {α : Type u} {β : Type v} {G : Graph α β}
  [Finite ↑G.vertexSet] {s t : ↑G.vertexSet} (hst : s ≠ t) (hadj : ¬G.Adj ↑s ↑t) (k : ℕ) :
  G.IsVertexReachable k s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for vertex deletion in a digraph, predicate form.** Formalized in Tau Ceti as [`Digraph.forall_reachableAvoiding_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.forall_reachableAvoiding_iff_exists_paths).

```lean
Digraph.forall_reachableAvoiding_iff_exists_paths.{u} {V : Type u} {D : Digraph V} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : ¬D.Adj s t) (k : ℕ) :
  (∀ (X : Finset V), s ∉ X → t ∉ X → X.card < k → TauCeti.ReachableAvoiding D.AdjHom (↑X) s t) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for vertex reachability.** Formalized in Tau Ceti as [`SimpleGraph.isVertexReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexReachable_iff_exists_paths).

```lean
SimpleGraph.isVertexReachable_iff_exists_paths.{u} {V : Type u} {G : SimpleGraph V} [Finite V]
  {s t : V} (hst : s ≠ t) (hadj : ¬G.Adj s t) (k : ℕ) :
  G.IsVertexReachable (↑k) s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for vertex-disjoint directed paths between vertex sets.** Formalized in Tau Ceti as [`TauCeti.exists_paths_setSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/SetToSet.html#TauCeti.exists_paths_setSeparator_card_eq).

```lean
TauCeti.exists_paths_setSeparator_card_eq.{u, v} {V : Type u} {Q : V → V → Type v} [Finite V]
  (A B : Finset V) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).vertices, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (Pairwise fun i j => (P i).vertices.Disjoint (P j).vertices) ∧
              (∀ a ∈ A, ∀ b ∈ B, ¬TauCeti.ReachableAvoiding Q (↑X) a b) ∧ X.card = k
```

**Menger's theorem for vertex-disjoint directed paths between vertex sets, predicate form.** Formalized in Tau Ceti as [`TauCeti.forall_exists_reachableAvoiding_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/SetToSet.html#TauCeti.forall_exists_reachableAvoiding_iff_exists_paths).

```lean
TauCeti.forall_exists_reachableAvoiding_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v}
  [Finite V] (A B : Finset V) (k : ℕ) :
  (∀ (X : Finset V), X.card < k → ∃ a ∈ A, ∃ b ∈ B, TauCeti.ReachableAvoiding Q (↑X) a b) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).vertices, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
              Pairwise fun i j => (P i).vertices.Disjoint (P j).vertices
```

**Menger's theorem for vertex-disjoint paths between vertex sets.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_setSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_setSeparator_card_eq).

```lean
SimpleGraph.exists_paths_setSeparator_card_eq.{u} {V : Type u} {G : SimpleGraph V} [Finite V]
  (A B : Finset V) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (Pairwise fun i j => (P i).support.Disjoint (P j).support) ∧
              (∀ a ∈ A, ∀ b ∈ B, ∀ (p : G.Walk a b), ∃ v ∈ p.support, v ∈ X) ∧ X.card = k
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

**Menger's theorem for vertex-disjoint paths between vertex sets, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.forall_exists_walk_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.forall_exists_walk_iff_exists_paths).

```lean
SimpleGraph.forall_exists_walk_iff_exists_paths.{u} {V : Type u} {G : SimpleGraph V} [Finite V]
  (A B : Finset V) (k : ℕ) :
  (∀ (X : Finset V), X.card < k → ∃ a ∈ A, ∃ b ∈ B, ∃ p, ∀ v ∈ p.support, v ∉ X) ↔
    ∃ a b P,
      (∀ (i : Fin k), a i ∈ A) ∧
        (∀ (i : Fin k), b i ∈ B) ∧
          (∀ (i : Fin k), (P i).IsPath) ∧
            (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
              Pairwise fun i j => (P i).support.Disjoint (P j).support
```

**Menger's theorem for vertex-strong arrow families.** Formalized in Tau Ceti as [`TauCeti.isVertexStrong_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.isVertexStrong_iff_exists_paths).

```lean
TauCeti.isVertexStrong_iff_exists_paths.{u, v} {V : Type u} {Q : V → V → Type v} {k : ℕ}
  [Finite V] :
  TauCeti.IsVertexStrong Q k ↔
    ↑k < ENat.card V ∧
      ∀ ⦃s t : V⦄,
        s ≠ t →
          ∃ P,
            Function.Injective P ∧
              (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_fan_separator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.html#SimpleGraph.exists_fan_separator_card_eq)
- [Source of `SimpleGraph.exists_fan_separator_card_eq` in TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.lean#L111)
