---
declaration: def
origin: cited
lean: Subgroup.quotientConjugationAction
statement: formalized
---

# Subgroup.quotientConjugationAction

Conjugation on an abelian normal subgroup, viewed as an action of the quotient group.
Use `letI := N.quotientConjugationAction` to install the action locally.

```lean
Subgroup.quotientConjugationAction.{u_1} {G : Type u_1} [Group G] (N : Subgroup G) [N.Normal]
  [IsMulCommutative ↥N] : MulDistribMulAction (G ⧸ N) ↥N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.quotientConjugationAction`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Action.html#Subgroup.quotientConjugationAction).

## Sources

- [Tau Ceti documentation: `Subgroup.quotientConjugationAction`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupExtension/Quotient/Action.html#Subgroup.quotientConjugationAction)
- [Source of `Subgroup.quotientConjugationAction` in TauCeti/GroupTheory/GroupExtension/Quotient/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GroupExtension/Quotient/Action.lean#L30)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
