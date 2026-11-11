---
declaration: theorem
origin: cited
lean: TauCeti.TerminalCut.exists_isCutTree
statement: formalized
proof: formalized
---

# Gomory–Hu theorem

Every symmetric submodular set function on a nonempty finite vertex
type has a cut tree: a weighted tree on the vertices in which the minimum cut value between any
two distinct vertices is the minimum weight on the tree path between them, and deleting any tree
edge leaves a minimum cut between its ends.

```lean
TauCeti.TerminalCut.exists_isCutTree.{u_1, u_2} {V : Type u_1} {K : Type u_2} [Fintype V]
  [DecidableEq V] [AddCommMonoid K] [LinearOrder K] [IsOrderedCancelAddMonoid K] {f : Finset V → K}
  [Nonempty V] (hf : TauCeti.IsSymmSubmodular f) : ∃ T w, TauCeti.TerminalCut.IsCutTree f T w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TerminalCut.exists_isCutTree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.html#TauCeti.TerminalCut.exists_isCutTree).

## Sources

- [Tau Ceti documentation: `TauCeti.TerminalCut.exists_isCutTree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.html#TauCeti.TerminalCut.exists_isCutTree)
- [Source of `TauCeti.TerminalCut.exists_isCutTree` in TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.lean#L410)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
