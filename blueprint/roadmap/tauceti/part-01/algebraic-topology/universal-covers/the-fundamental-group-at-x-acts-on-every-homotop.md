---
declaration: instance
origin: cited
lean: TauCeti.homotopyGroupMulAction
statement: formalized
---

# The fundamental group at `x` acts on every homotopy group based at `x`

**The fundamental group at `x` acts on every homotopy group based at `x`**, an element of
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
- [Source of `TauCeti.homotopyGroupMulAction` in TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean#L131)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/UniversalCovers/STATUS.md)
