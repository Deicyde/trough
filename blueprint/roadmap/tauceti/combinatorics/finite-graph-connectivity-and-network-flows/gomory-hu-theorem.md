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

## Proof depends on

- [Multi-cut non-crossing lemma](multi-cut-non-crossing-lemma.md)
- [Ultrametric inequality for minimum cut values](ultrametric-inequality-for-minimum-cut-values.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TerminalCut.exists_isCutTree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.html#TauCeti.TerminalCut.exists_isCutTree).

## Sources

- [Tau Ceti documentation: `TauCeti.TerminalCut.exists_isCutTree`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.html#TauCeti.TerminalCut.exists_isCutTree)
- [Source of `TauCeti.TerminalCut.exists_isCutTree` in TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/MinimumCut/GomoryHu.lean#L385)
