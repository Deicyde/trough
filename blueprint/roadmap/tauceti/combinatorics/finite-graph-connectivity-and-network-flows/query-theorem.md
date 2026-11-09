---
declaration: theorem
origin: cited
lean: TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges
statement: formalized
proof: formalized
---

# Query theorem

If `s(u, v)` has minimum weight on the tree path from `s` to `t`, and `s`
lies on the side of `u`, then that side is a minimum `s`–`t` cut. Since the two sides of a tree
edge cover the vertices, one of the orientations `(u, v)` and `(v, u)` applies.

```lean
TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges.{u_1, u_2} {V : Type u_1}
  {K : Type u_2} [Fintype V] [Zero K] [LinearOrder K] {f : Finset V → K} {T : SimpleGraph V}
  {w : Sym2 V → K} (hT : TauCeti.TerminalCut.IsCutTree f T w) {s t u v : V} {p : T.Walk s t}
  (hp : p.IsPath) (huv : s(u, v) ∈ p.edges) (hmin : ∀ e ∈ p.edges, w s(u, v) ≤ w e)
  (hs : s ∈ T.edgeSide u v) : TauCeti.TerminalCut.IsMinimum f {s} {t} (T.edgeSide u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/CutTree.html#TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges).

## Sources

- [Tau Ceti documentation: `TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/CutTree.html#TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges)
- [Source of `TauCeti.TerminalCut.IsCutTree.isMinimum_edgeSide_of_mem_edges` in TauCeti/Combinatorics/Network/MinimumCut/CutTree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/MinimumCut/CutTree.lean#L189)
