---
declaration: theorem
origin: cited
lean: SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support
statement: formalized
proof: formalized
---

# Dirac's theorem

For `2 ≤ k`, every set of at most `k` vertices of a `k`-vertex-connected
simple graph on a finite vertex type lies on a common cycle.

```lean
SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support.{u} {V : Type u} {G : SimpleGraph V}
  [Finite V] {k : ℕ} (hk : 2 ≤ k) (h : G.IsVertexConnected ↑k) {S : Finset V} (hS : S.card ≤ k) :
  ∃ u c, c.IsCycle ∧ ∀ v ∈ S, v ∈ c.support
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for internally vertex-disjoint paths](mengers-theorem-for-internally-vertex-disjoint-p.md)
- [Whitney's inequality](../part-02/whitneys-inequality.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/PrescribedCycle.html#SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support).

## Sources

- [Tau Ceti documentation: `SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/PrescribedCycle.html#SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support)
- [Source of `SimpleGraph.IsVertexConnected.exists_isCycle_forall_mem_support` in TauCeti/Combinatorics/SimpleGraph/Connectivity/PrescribedCycle.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/PrescribedCycle.lean#L117)
