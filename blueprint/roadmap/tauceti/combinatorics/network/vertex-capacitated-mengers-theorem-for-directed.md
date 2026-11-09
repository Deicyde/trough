---
declaration: theorem
origin: cited
lean: TauCeti.exists_paths_vertexSeparator_sum_eq, TauCeti.exists_paths_setSeparator_sum_eq
statement: formalized
proof: formalized
---

# Vertex-capacitated Menger's theorem for directed paths

Let `s ≠ t` be vertices of an arrow
family on a finite vertex type, with no arrow from `s` to `t`, and let `c v` be a capacity on every
vertex. Some family of `k` directed `s`–`t` paths, in which every vertex `v` other than `s` and `t`
lies on at most `c v` members, and some set `X` of vertices avoiding `s` and `t`, whose deletion
leaves `t` unreachable from `s`, satisfy `∑ v ∈ X, c v = k`. By
`TauCeti.card_le_sum_of_not_reachableAvoiding`, the family is then largest and the separator of
least weight.

```lean
TauCeti.exists_paths_vertexSeparator_sum_eq.{u, v} {V : Type u} {Q : V → V → Type v} {s t : V}
  [Finite V] [DecidableEq V] (c : V → ℕ) (hst : s ≠ t) (hadj : IsEmpty (Q s t)) :
  ∃ k P X,
    (∀ (i : Fin k), (P i).IsPath) ∧
      (∀ (v : V), v ≠ s → v ≠ t → {i | v ∈ (P i).vertices}.card ≤ c v) ∧
        s ∉ X ∧ t ∉ X ∧ ¬TauCeti.ReachableAvoiding Q (↑X) s t ∧ ∑ v ∈ X, c v = k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Integrality of maximum flows](../finite-graph-connectivity-and-network-flows/integrality-of-maximum-flows.md)
- [Path–cycle decomposition](../finite-graph-connectivity-and-network-flows/path-cycle-decomposition.md)
- [TauCeti.AuxTerminalHom](../finite-graph-connectivity-and-network-flows/tauceti-auxterminalhom.md)
- [TauCeti.residualUpdate](../finite-graph-connectivity-and-network-flows/tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Vertex.html#TauCeti.exists_paths_vertexSeparator_sum_eq).

## Other forms

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

## Sources

- [Tau Ceti documentation: `TauCeti.exists_paths_vertexSeparator_sum_eq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Menger/Vertex.html#TauCeti.exists_paths_vertexSeparator_sum_eq)
- [Source of `TauCeti.exists_paths_vertexSeparator_sum_eq` in TauCeti/Combinatorics/Network/Menger/Vertex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/Menger/Vertex.lean#L138)
