---
declaration: theorem
origin: cited
lean: Graph.isBridge_iff_forall_cycle_notMem
statement: formalized
proof: formalized
---

# Graph.isBridge_iff_forall_cycle_notMem

An actual edge is a bridge exactly when it lies on no cycle.

```lean
Graph.isBridge_iff_forall_cycle_notMem.{u, v} {α : Type u} {β : Type v} {G : Graph α β} {e : β}
  (he : e ∈ G.edgeSet) : G.IsBridge e ↔ ∀ ⦃u : α⦄ (p : G.Walk u u), p.IsCycle → e ∉ p.edges
```

## Depends on

- [Graph.Walk](graph-walk.md)

## Lean

Formalized in Tau Ceti as [`Graph.isBridge_iff_forall_cycle_notMem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.html#Graph.isBridge_iff_forall_cycle_notMem).

## Sources

- [Tau Ceti documentation: `Graph.isBridge_iff_forall_cycle_notMem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.html#Graph.isBridge_iff_forall_cycle_notMem)
- [Source of `Graph.isBridge_iff_forall_cycle_notMem` in TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Graph/Connectivity/Bridge/Basic.lean#L287)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
