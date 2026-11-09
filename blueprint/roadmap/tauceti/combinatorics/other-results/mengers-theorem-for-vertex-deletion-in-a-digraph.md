---
declaration: theorem
origin: cited
lean: Digraph.forall_reachableAvoiding_iff_exists_paths, Digraph.exists_paths_vertexSeparator_card_eq
statement: formalized
proof: formalized
---

# Menger's theorem for vertex deletion in a digraph, predicate form

Distinct nonadjacent
vertices remain joined after deleting any fewer than `k` other vertices exactly when there are
`k` pairwise internally vertex-disjoint directed paths between them.

```lean
Digraph.forall_reachableAvoiding_iff_exists_paths.{u} {V : Type u} {D : Digraph V} {s t : V}
  [Finite V] (hst : s ≠ t) (hadj : ¬D.Adj s t) (k : ℕ) :
  (∀ (X : Finset V), s ∉ X → t ∉ X → X.card < k → TauCeti.ReachableAvoiding D.AdjHom (↑X) s t) ↔
    ∃ P, (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for vertex-strong arrow families](../network/mengers-theorem-for-vertex-strong-arrow-families.md)

## Lean

Formalized in Tau Ceti as [`Digraph.forall_reachableAvoiding_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.forall_reachableAvoiding_iff_exists_paths).

## Other forms

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

## Sources

- [Tau Ceti documentation: `Digraph.forall_reachableAvoiding_iff_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.forall_reachableAvoiding_iff_exists_paths)
- [Source of `Digraph.forall_reachableAvoiding_iff_exists_paths` in TauCeti/Combinatorics/Digraph/Menger.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Digraph/Menger.lean#L77)
