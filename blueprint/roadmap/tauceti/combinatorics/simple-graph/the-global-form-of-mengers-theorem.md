---
declaration: theorem
origin: cited
lean: SimpleGraph.isVertexConnected_iff_forall_exists_paths
statement: formalized
proof: formalized
---

# The global form of Menger's theorem

A simple graph on a finite vertex type with more than
`k` vertices is `k`-vertex-connected exactly when every two distinct vertices `s` and `t`,
adjacent or not, are joined by `k` distinct paths pairwise sharing no vertex other than `s` and
`t`.

```lean
SimpleGraph.isVertexConnected_iff_forall_exists_paths.{u} {V : Type u} {G : SimpleGraph V}
  [Finite V] {k : ℕ} (hk : k < Nat.card V) :
  G.IsVertexConnected ↑k ↔
    ∀ (s t : V),
      s ≠ t →
        ∃ P,
          Function.Injective P ∧
            (∀ (i : Fin k), (P i).IsPath) ∧ Pairwise fun i j => (P i).InternallyDisjoint (P j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for fans](mengers-theorem-for-fans.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexConnected_iff_forall_exists_paths).

## Sources

- [Tau Ceti documentation: `SimpleGraph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexConnected_iff_forall_exists_paths)
- [Source of `SimpleGraph.isVertexConnected_iff_forall_exists_paths` in TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean#L558)
