---
declaration: theorem
origin: cited
lean: TauCeti.isVertexStrong_iff_exists_paths, TauCeti.exists_paths_arrowSeparator_card_eq, TauCeti.exists_paths_setArrowSeparator_card_eq, TauCeti.forall_exists_reachableWithout_iff_exists_paths, TauCeti.forall_reachableWithout_iff_exists_paths, TauCeti.exists_paths_vertexSeparator_card_eq, TauCeti.exists_paths_isMixedSeparator_card_eq, TauCeti.forall_not_isMixedSeparator_iff_exists_paths, TauCeti.forall_reachableAvoiding_iff_exists_paths, TauCeti.exists_paths_setSeparator_card_eq, TauCeti.forall_exists_reachableAvoiding_iff_exists_paths
statement: formalized
proof: formalized
---

# Menger's theorem for vertex-strong arrow families

An arrow family on a finite vertex type
is `k`-vertex-strong exactly when it has more than `k` vertices and any two distinct vertices `s`
and `t` are joined by `k` distinct directed paths pairwise sharing no vertex other than `s` and
`t`. When there are arrows from `s` to `t`, one of these paths may be a single arrow.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Max-flow/min-cut theorem](../finite-graph-connectivity-and-network-flows/part-01/max-flow-min-cut-theorem.md)
- [Max-flow/min-cut theorem between vertex sets](max-flow-min-cut-theorem-between-vertex-sets.md)
- [Vertex-capacitated Menger's theorem for directed paths](vertex-capacitated-mengers-theorem-for-directed.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isVertexStrong_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.isVertexStrong_iff_exists_paths).

## Other forms

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
  [Finite V] (k : ℕ) :
  (∀ (X : Finset V), s ∉ X → t ∉ X → X.card < k → TauCeti.ReachableAvoiding Q (↑X) s t) ↔
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

## Sources

- [Tau Ceti documentation: `TauCeti.isVertexStrong_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Connectivity/Basic.html#TauCeti.isVertexStrong_iff_exists_paths)
- [Source of `TauCeti.isVertexStrong_iff_exists_paths` in TauCeti/Combinatorics/Network/Connectivity/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/Connectivity/Basic.lean#L285)
