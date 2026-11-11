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
- [Source of `TauCeti.homotopyGroupMulAction` in TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Homotopy/HomotopyGroup/FundamentalGroupAction.lean#L131)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)
