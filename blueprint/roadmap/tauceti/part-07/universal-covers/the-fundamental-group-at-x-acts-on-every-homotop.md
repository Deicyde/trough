---
declaration: instance
origin: cited
lean: TauCeti.homotopyGroupMulAction
statement: formalized
---

# The fundamental group at `x` acts on every homotopy group based at `x`

, an element of
`π₁(X, x)` acting by transport around the loop it represents.

The action is a left action: transport composes covariantly and `FundamentalGroup.mul_def`
reverses the order of concatenation, so the two reversals cancel.

```lean
TauCeti.homotopyGroupMulAction.{u_1, u_2} {N : Type u_1} [Fintype N] {X : Type u_2}
  [TopologicalSpace X] {x : X} : MulAction (FundamentalGroup X x) (HomotopyGroup N X x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.homotopyGroupMulAction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.html#TauCeti.homotopyGroupMulAction).

## Sources

- [Tau Ceti documentation: `TauCeti.homotopyGroupMulAction`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.html#TauCeti.homotopyGroupMulAction)
- [Source of `TauCeti.homotopyGroupMulAction` in TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean#L131)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
