---
declaration: theorem
origin: cited
lean: Digraph.exists_paths_vertexSeparator_sum_eq
statement: formalized
proof: formalized
---

# Vertex-capacitated Menger's theorem for a digraph

Let `s` and `t` be distinct vertices
with no arrow from `s` to `t`, and let `c v` be the capacity of vertex `v`. Some family of `k`
directed `s`-to-`t` paths respects every nonterminal vertex capacity, and some terminal-excluding
vertex separator has total capacity `k`.

```lean
Digraph.exists_paths_vertexSeparator_sum_eq.{u} {V : Type u} {D : Digraph V} {s t : V} [Finite V]
  [DecidableEq V] (c : V → ℕ) (hst : s ≠ t) (hadj : ¬D.Adj s t) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : V), v ≠ s → v ≠ t → {i | v ∈ (P i).vertices}.card ≤ c v) ∧
        s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding D.AdjHom (↑X) s t ∧ ∑ v ∈ X, c v = k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vertex-capacitated Menger's theorem for directed paths](../network/vertex-capacitated-mengers-theorem-for-directed.md)

## Lean

Formalized in Tau Ceti as [`Digraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.exists_paths_vertexSeparator_sum_eq).

## Sources

- [Tau Ceti documentation: `Digraph.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Digraph/Menger.html#Digraph.exists_paths_vertexSeparator_sum_eq)
- [Source of `Digraph.exists_paths_vertexSeparator_sum_eq` in TauCeti/Combinatorics/Digraph/Menger.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Digraph/Menger.lean#L55)
