---
declaration: theorem
origin: cited
lean: Graph.exists_isCutTree_edgeCutCapacity
statement: formalized
proof: formalized
---

# Graph.exists_isCutTree_edgeCutCapacity

Every finite weighted multigraph with nonnegative nonloop edge weights has a cut tree on its
actual vertices. Parallel edges retain their separate contributions, while loops are ignored by
the cut function.

```lean
Graph.exists_isCutTree_edgeCutCapacity.{u_1, u_2, u_3} {α : Type u_1} {β : Type u_2} {K : Type u_3}
  {G : Graph α β} [Fintype ↑G.vertexSet] [Nonempty ↑G.vertexSet] [Fintype ↑G.edgeSet]
  [AddCommMonoid K] [LinearOrder K] [IsOrderedCancelAddMonoid K] (c : ↑G.edgeSet → K)
  (hc : ∀ (e : ↑G.edgeSet), ¬(G.edgeEnds e).IsDiag → 0 ≤ c e) :
  ∃ T w, TauCeti.TerminalCut.IsCutTree (G.edgeCutCapacity c) T w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gomory–Hu theorem](gomory-hu-theorem.md)

## Lean

Formalized in Tau Ceti as [`Graph.exists_isCutTree_edgeCutCapacity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Graph.html#Graph.exists_isCutTree_edgeCutCapacity).

## Sources

- [Tau Ceti documentation: `Graph.exists_isCutTree_edgeCutCapacity`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Graph.html#Graph.exists_isCutTree_edgeCutCapacity)
- [Source of `Graph.exists_isCutTree_edgeCutCapacity` in TauCeti/Combinatorics/Network/MinimumCut/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/MinimumCut/Graph.lean#L63)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
