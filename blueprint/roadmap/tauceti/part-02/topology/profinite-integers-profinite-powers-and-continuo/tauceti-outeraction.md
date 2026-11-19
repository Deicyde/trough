---
declaration: def
origin: cited
lean: TauCeti.outerAction
statement: formalized
---

# TauCeti.outerAction

The **outer action** of `E ⧸ N` on a normal subgroup `N`: the class of `e` acts by the outer
class of conjugation by `e` (`outerAction_mk`). It is well defined because conjugation by an
element of `N` is inner.

```lean
TauCeti.outerAction.{u_1} {E : Type u_1} [Group E] [TopologicalSpace E] (N : Subgroup E) [N.Normal]
  [SeparatelyContinuousMul E] : E ⧸ N →* TauCeti.ContinuousOut ↥N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.outerAction`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.html#TauCeti.outerAction).

## Sources

- [Tau Ceti documentation: `TauCeti.outerAction`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.html#TauCeti.outerAction)
- [Source of `TauCeti.outerAction` in TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.lean#L63)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteArithmetic/STATUS.md)
