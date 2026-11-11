---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_paths_vertexSeparator_card_eq, SimpleGraph.exists_fan_separator_card_eq, SimpleGraph.forall_exists_walk_iff_exists_fan, SimpleGraph.exists_paths_vertexSeparator_card_add_one_eq, SimpleGraph.forall_reachable_induce_iff_exists_paths, SimpleGraph.isVertexReachable_iff_exists_paths, SimpleGraph.exists_paths_setSeparator_card_eq, SimpleGraph.forall_exists_walk_iff_exists_paths
statement: formalized
proof: formalized
---

# Menger's theorem for internally vertex-disjoint paths

Let `s` and `t` be distinct
nonadjacent vertices of a simple graph on a finite vertex type. Some family of `k` distinct paths
from `s` to `t`, pairwise sharing no vertex other than `s` and `t`, and some set of `k` vertices
other than `s` and `t`, whose deletion separates `s` from `t`, exist. By
`SimpleGraph.card_le_card_of_not_reachable_induce`, the family is then largest and the separator
smallest.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for vertex-strong arrow families](../../network/mengers-theorem-for-vertex-strong-arrow-families.md)
- [Vertex-capacitated Menger's theorem](vertex-capacitated-mengers-theorem.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_card_eq).

## Other forms

**Menger's theorem for fans.** Formalized in Tau Ceti as [`SimpleGraph.exists_fan_separator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Fan.html#SimpleGraph.exists_fan_separator_card_eq).

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

**Menger's theorem for internally vertex-disjoint paths, predicate form.** Formalized in Tau Ceti as [`SimpleGraph.forall_reachable_induce_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.forall_reachable_induce_iff_exists_paths).

```lean
SimpleGraph.forall_reachable_induce_iff_exists_paths.{u} {V : Type u} {G : SimpleGraph V} {s t : V}
  [Finite V] (k : ℕ) :
  (∀ (X : Finset V) (hs : s ∉ X) (ht : t ∉ X),
      X.card < k → (SimpleGraph.induce (↑X)ᶜ G).Reachable ⟨s, hs⟩ ⟨t, ht⟩) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

**Menger's theorem for vertex reachability.** Formalized in Tau Ceti as [`SimpleGraph.isVertexReachable_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexReachable_iff_exists_paths).

```lean
SimpleGraph.isVertexReachable_iff_exists_paths.{u} {V : Type u} {G : SimpleGraph V} [Finite V]
  {s t : V} (k : ℕ) :
  G.IsVertexReachable (↑k) s t ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
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

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_paths_vertexSeparator_card_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_card_eq)
- [Source of `SimpleGraph.exists_paths_vertexSeparator_card_eq` in TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean#L224)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
