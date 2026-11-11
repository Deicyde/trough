---
declaration: def
origin: cited
lean: TauCeti.MulAction.germKernel
statement: formalized
---

# TauCeti.MulAction.germKernel

The germ kernel of the action of `G` at `x`: the subgroup of the elements of `G` that act as
the identity on a neighbourhood of `x`.

```lean
TauCeti.MulAction.germKernel.{u_1, u_2} (G : Type u_1) {X : Type u_2} [Group G] [MulAction G X]
  [TopologicalSpace X] (x : X) : Subgroup G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MulAction.germKernel`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/GermKernel.html#TauCeti.MulAction.germKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.MulAction.germKernel`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/GroupAction/GermKernel.html#TauCeti.MulAction.germKernel)
- [Source of `TauCeti.MulAction.germKernel` in TauCeti/Topology/Algebra/GroupAction/GermKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/GroupAction/GermKernel.lean#L72)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Orbifolds/STATUS.md)
