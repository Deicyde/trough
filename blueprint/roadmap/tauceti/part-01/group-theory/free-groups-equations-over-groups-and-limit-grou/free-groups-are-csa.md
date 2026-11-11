---
declaration: theorem
origin: cited
lean: IsFreeGroup.isCSA
statement: formalized
proof: formalized
---

# Free groups are CSA

every maximal abelian subgroup of a free group is malnormal.

```lean
IsFreeGroup.isCSA.{u_1} {G : Type u_1} [Group G] [IsFreeGroup G] : Group.IsCSA G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsFreeGroup.isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/CSA.html#IsFreeGroup.isCSA).

## Sources

- [Tau Ceti documentation: `IsFreeGroup.isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/CSA.html#IsFreeGroup.isCSA)
- [Source of `IsFreeGroup.isCSA` in TauCeti/GroupTheory/FreeGroup/CSA.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/FreeGroup/CSA.lean#L159)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
