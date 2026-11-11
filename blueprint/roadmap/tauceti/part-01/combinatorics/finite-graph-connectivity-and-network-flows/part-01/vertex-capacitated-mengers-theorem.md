---
declaration: theorem
origin: cited
lean: SimpleGraph.exists_paths_vertexSeparator_sum_eq, SimpleGraph.exists_paths_setSeparator_sum_eq
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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vertex-capacitated Menger's theorem for directed paths](../../network/vertex-capacitated-mengers-theorem-for-directed.md)

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

## Sources

- [Tau Ceti documentation: `SimpleGraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.html#SimpleGraph.exists_paths_vertexSeparator_sum_eq)
- [Source of `SimpleGraph.exists_paths_vertexSeparator_sum_eq` in TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/Menger.lean#L196)
