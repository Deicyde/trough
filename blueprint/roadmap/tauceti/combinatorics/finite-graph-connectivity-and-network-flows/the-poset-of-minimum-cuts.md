---
declaration: def
origin: cited
lean: TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso
statement: formalized
---

# The poset of minimum cuts

For a maximum bounded `s`–`t` assignment `f` between distinct
terminals, the minimum cuts, ordered by inclusion, are order isomorphic to the upper sets of the
poset of free residual components, ordered by inclusion. A minimum cut corresponds to the free
components contained in it, and an upper set to the vertices of its components together with the
vertices forced onto the source side.

```lean
TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso.{u, v, w} {V : Type u} {Q : V → V → Type v}
  {K : Type w} [Fintype V] [DecidableEq V] [(v w : V) → Fintype (Q v w)] [AddCommGroup K]
  [LinearOrder K] [IsOrderedAddMonoid K] {lo hi : TauCeti.Assignment Q K} {s t : V}
  {f : TauCeti.BoundedFlow lo hi s t} (hst : s ≠ t) (hf : f.IsMaximum) :
  ↥(TauCeti.TerminalCut.minimizers ⋯ {s} {t}) ≃o (UpperSet f.FreeComponent)ᵒᵈ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Poset.html#TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso).

## Sources

- [Tau Ceti documentation: `TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Poset.html#TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso)
- [Source of `TauCeti.BoundedFlow.IsMaximum.minimizersOrderIso` in TauCeti/Combinatorics/Network/MinimumCut/Poset.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/MinimumCut/Poset.lean#L215)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
