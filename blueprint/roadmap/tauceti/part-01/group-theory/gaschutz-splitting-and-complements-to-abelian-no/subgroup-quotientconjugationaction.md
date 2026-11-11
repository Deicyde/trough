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
- [Source of `Subgroup.quotientConjugationAction` in TauCeti/GroupTheory/GroupExtension/Quotient/Action.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupExtension/Quotient/Action.lean#L30)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
