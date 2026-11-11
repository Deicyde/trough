---
declaration: theorem
origin: cited
lean: SimpleGraph.isVertexConnected_iff_forall_exists_paths
statement: formalized
proof: formalized
---

# The global form of Menger's theorem

A simple graph on a vertex type `V` with
`k < Nat.card V` (which forces `V` to be finite) is `k`-vertex-connected exactly when every two
distinct vertices `s` and `t`, adjacent or not, are joined by `k` distinct paths pairwise sharing
no vertex other than `s` and `t`.

```lean
SimpleGraph.isVertexConnected_iff_forall_exists_paths.{u} {V : Type u} {G : SimpleGraph V} {k : ℕ}
  (hk : k < Nat.card V) :
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

- [Menger's theorem for internally vertex-disjoint paths](mengers-theorem-for-internally-vertex-disjoint-p.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexConnected_iff_forall_exists_paths).

## Sources

- [Tau Ceti documentation: `SimpleGraph.isVertexConnected_iff_forall_exists_paths`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.html#SimpleGraph.isVertexConnected_iff_forall_exists_paths)
- [Source of `SimpleGraph.isVertexConnected_iff_forall_exists_paths` in TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/VertexConnectivity.lean#L591)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
