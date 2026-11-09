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

## Proof depends on

- [IsFreeGroup.maximal_isMulCommutative_iff](isfreegroup-maximal-ismulcommutative-iff.md)

## Lean

Formalized in Tau Ceti as [`IsFreeGroup.isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/CSA.html#IsFreeGroup.isCSA).

## Sources

- [Tau Ceti documentation: `IsFreeGroup.isCSA`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/CSA.html#IsFreeGroup.isCSA)
- [Source of `IsFreeGroup.isCSA` in TauCeti/GroupTheory/FreeGroup/CSA.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FreeGroup/CSA.lean#L159)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
