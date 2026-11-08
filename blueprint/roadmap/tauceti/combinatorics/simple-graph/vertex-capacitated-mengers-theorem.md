---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_paths_vertexSeparator_sum_eq, SimpleGraph.exists_paths_setSeparator_sum_eq, Graph.exists_paths_setSeparator_sum_eq, Digraph.exists_paths_vertexSeparator_sum_eq, TauCeti.exists_paths_vertexSeparator_sum_eq, TauCeti.exists_paths_setSeparator_sum_eq, Graph.exists_paths_vertexSeparator_sum_eq
statement: formalized
proof: formalized
---

# Vertex-capacitated Menger's theorem

Let `s` and `t` be distinct nonadjacent vertices of a
simple graph on a finite vertex type, and let `c v` be a capacity on every vertex. Some family of
`k` paths from `s` to `t`, in which every vertex `v` other than `s` and `t` lies on at most `c v`
members, and some set `X` of vertices other than `s` and `t`, whose deletion separates `s` from
`t`, satisfy `∑ v ∈ X, c v = k`. By `SimpleGraph.card_le_sum_of_not_reachable_induce`, the family is
then largest and the separator of least weight.

```lean
SimpleGraph.exists_paths_vertexSeparator_sum_eq.{u} {V : Type u} {G : SimpleGraph V} {s t : V}
  [Finite V] [DecidableEq V] (c : V → ℕ) (hst : s ≠ t) (hadj : ¬G.Adj s t) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : V), v ≠ s → v ≠ t → {i | v ∈ (P i).support}.card ≤ c v) ∧
        ∃ (hs : s ∉ X) (ht : t ∉ X),
          ¬(SimpleGraph.induce (↑X)ᶜ G).Reachable ⟨s, hs⟩ ⟨t, ht⟩ ∧ ∑ v ∈ X, c v = k
```

## Depends on

- [Graph.Walk](../finite-graph-connectivity-and-network-flows/graph-walk.md)

## Proof depends on

- [Integrality of maximum flows](../finite-graph-connectivity-and-network-flows/integrality-of-maximum-flows.md)
- [Path–cycle decomposition](../finite-graph-connectivity-and-network-flows/path-cycle-decomposition.md)
- [TauCeti.AuxTerminalHom](../finite-graph-connectivity-and-network-flows/tauceti-auxterminalhom.md)
- [TauCeti.residualUpdate](../finite-graph-connectivity-and-network-flows/tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_sum_eq).

## Other forms

**Vertex-capacitated Menger's theorem between vertex sets.** Formalized in Tau Ceti as [`SimpleGraph.exists_paths_setSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_setSeparator_sum_eq).

```lean
SimpleGraph.exists_paths_setSeparator_sum_eq.{u} {V : Type u} {G : SimpleGraph V} [Finite V]
  [DecidableEq V] (c : V → ℕ) (A B : Finset V) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).support, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (∀ (v : V), {i | v ∈ (P i).support}.card ≤ c v) ∧
              (∀ a ∈ A, ∀ b ∈ B, ∀ (p : G.Walk a b), ∃ v ∈ p.support, v ∈ X) ∧ ∑ v ∈ X, c v = k
```

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

**Vertex-capacitated Menger's theorem for a digraph.** Formalized in Tau Ceti as [`Digraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.exists_paths_vertexSeparator_sum_eq).

```lean
Digraph.exists_paths_vertexSeparator_sum_eq.{u} {V : Type u} {D : Digraph V} {s t : V} [Finite V]
  [DecidableEq V] (c : V → ℕ) (hst : s ≠ t) (hadj : ¬D.Adj s t) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : V), v ≠ s → v ≠ t → {i | v ∈ (P i).vertices}.card ≤ c v) ∧
        s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding D.AdjHom (↑X) s t ∧ ∑ v ∈ X, c v = k
```

**Vertex-capacitated Menger's theorem for directed paths.** Formalized in Tau Ceti as [`TauCeti.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Vertex.html#TauCeti.exists_paths_vertexSeparator_sum_eq).

```lean
TauCeti.exists_paths_vertexSeparator_sum_eq.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] [DecidableEq V] (c : V → ℕ) (hst : s ≠ t) (hadj : IsEmpty (Q s t)) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : V), v ≠ s → v ≠ t → {i | v ∈ (P i).vertices}.card ≤ c v) ∧
        s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding Q (↑X) s t ∧ ∑ v ∈ X, c v = k
```

**Vertex-capacitated Menger's theorem for directed paths between vertex sets.** Formalized in Tau Ceti as [`TauCeti.exists_paths_setSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/SetToSet.html#TauCeti.exists_paths_setSeparator_sum_eq).

```lean
TauCeti.exists_paths_setSeparator_sum_eq.{u, v} {V : Type u} {Q : V → V → Type v} [Finite V]
  [DecidableEq V] (c : V → ℕ) (A B : Finset V) :
  ∃ k a b P X,
    (∀ (i : Fin k), a i ∈ A) ∧
      (∀ (i : Fin k), b i ∈ B) ∧
        (∀ (i : Fin k), (P i).IsPath) ∧
          (∀ (i : Fin k), ∀ v ∈ (P i).vertices, v ≠ a i → v ≠ b i → v ∉ A ∧ v ∉ B) ∧
            (∀ (v : V), {i | v ∈ (P i).vertices}.card ≤ c v) ∧
              (∀ a ∈ A, ∀ b ∈ B, ¬TauCeti.ReachableAvoiding Q (↑X) a b) ∧ ∑ v ∈ X, c v = k
```

**Vertex-capacitated Menger's theorem for multigraphs.** Formalized in Tau Ceti as [`Graph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Menger/Vertex.html#Graph.exists_paths_vertexSeparator_sum_eq).

```lean
Graph.exists_paths_vertexSeparator_sum_eq.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {s t : α}
  [Finite ↑G.vertexSet] [DecidableEq α] (c : α → ℕ) (hst : s ≠ t) (hadj : ¬G.Adj s t) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : α), v ≠ s → v ≠ t → {i | v ∈ (P i).support}.card ≤ c v) ∧
        ↑X ⊆ G.vertexSet ∧ s ∉ X ∧ t ∉ X ∧ ¬(G.deleteVerts ↑X).Reachable s t ∧ ∑ v ∈ X, c v = k
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_sum_eq)
- [Source of `SimpleGraph.exists_paths_vertexSeparator_sum_eq` in TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean#L196)
