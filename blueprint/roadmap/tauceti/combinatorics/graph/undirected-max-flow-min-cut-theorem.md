---
declaration: theorem
origin: cited
lean: Graph.exists_flow_val_eq_edgeCutCapacity, Graph.exists_flow_val_eq_edgeCutCapacity_mem
statement: formalized
proof: formalized
---

# Undirected max-flow/min-cut theorem

For nonnegative capacities on the edges of a
multigraph and distinct actual vertices `s` and `t`, some acyclic `s`–`t` flow has value equal to
the capacity of some set of actual vertices containing `s` but not `t`. By
`TauCeti.Flow.val_le_edgeCutCapacity` this flow is maximum and this cut is minimum.

```lean
Graph.exists_flow_val_eq_edgeCutCapacity.{u, v, w} {α : Type u} {β : Type v} {K : Type w}
  {G : Graph α β} [Fintype ↑G.vertexSet] [Fintype ↑G.edgeSet]
  [(x y : ↑G.vertexSet) → Fintype (G.BidirectedHom x y)] [AddCommGroup K] [LinearOrder K]
  [IsOrderedAddMonoid K] {c : ↑G.edgeSet → K} {s t : ↑G.vertexSet} (hst : s ≠ t) (hc : 0 ≤ c) :
  ∃ f, f.toFun.IsAcyclic ∧ ∃ S, s ∈ S ∧ t ∉ S ∧ f.val = G.edgeCutCapacity c S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Integrality of maximum flows](../finite-graph-connectivity-and-network-flows/integrality-of-maximum-flows.md)
- [TauCeti.residualUpdate](../finite-graph-connectivity-and-network-flows/tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_flow_val_eq_edgeCutCapacity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Flow.html#Graph.exists_flow_val_eq_edgeCutCapacity).

## Other forms

**Undirected max-flow/min-cut theorem with integrality.** Formalized in Tau Ceti as [`Graph.exists_flow_val_eq_edgeCutCapacity_mem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Flow.html#Graph.exists_flow_val_eq_edgeCutCapacity_mem).

```lean
Graph.exists_flow_val_eq_edgeCutCapacity_mem.{u, v, w} {α : Type u} {β : Type v} {K : Type w}
  {G : Graph α β} [Fintype ↑G.vertexSet] [Fintype ↑G.edgeSet]
  [(x y : ↑G.vertexSet) → Fintype (G.BidirectedHom x y)] [AddCommGroup K] [LinearOrder K]
  [IsOrderedAddMonoid K] {c : ↑G.edgeSet → K} {s t : ↑G.vertexSet} (hst : s ≠ t) (hc : 0 ≤ c)
  (H : AddSubgroup K) (hcH : ∀ (e : ↑G.edgeSet), c e ∈ H) :
  ∃ f,
    f.toFun.IsAcyclic ∧
      (∀ ⦃x y : ↑G.vertexSet⦄ (a : G.BidirectedHom x y), f.toFun a ∈ H) ∧
        ∃ S, s ∈ S ∧ t ∉ S ∧ f.val = G.edgeCutCapacity c S
```

## Sources

- [Tau Ceti documentation: `Graph.exists_flow_val_eq_edgeCutCapacity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Flow.html#Graph.exists_flow_val_eq_edgeCutCapacity)
- [Source of `Graph.exists_flow_val_eq_edgeCutCapacity` in TauCeti/Combinatorics/Graph/Connectivity/Flow.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Flow.lean#L197)
