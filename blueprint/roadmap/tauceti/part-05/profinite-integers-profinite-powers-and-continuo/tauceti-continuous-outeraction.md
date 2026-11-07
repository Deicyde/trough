---
declaration: theorem
origin: cited
lean: TauCeti.continuous_outerAction
statement: formalized
proof: formalized
---

# TauCeti.continuous\_outerAction

For compact `N`, the outer action `E ⧸ N → ContinuousOut N` is continuous for the quotient
topologies.

```lean
TauCeti.continuous_outerAction.{u_1} {E : Type u_1} [Group E] [TopologicalSpace E] {N : Subgroup E}
  [N.Normal] [IsTopologicalGroup E] [CompactSpace ↥N] : Continuous ⇑(TauCeti.outerAction N)
```

## Depends on

- [TauCeti.outerAction](tauceti-outeraction.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.continuous_outerAction`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.html#TauCeti.continuous_outerAction).

## Sources

- [Tau Ceti documentation: `TauCeti.continuous_outerAction`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.html#TauCeti.continuous_outerAction)
- [Source of `TauCeti.continuous_outerAction` in TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/ContinuousAut/OuterAction.lean#L141)
- [Tau Ceti roadmap status: Profinite integers, profinite powers, and continuous automorphisms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteArithmetic/STATUS.md)
