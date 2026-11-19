---
declaration: theorem
origin: cited
lean: TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree
statement: formalized
proof: formalized
---

# Limit groups are the finitely generated fully residually free groups (Champetier and Guirardel, Theorem 1.1)

```lean
TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree.{u_1} {G : Type u_1} [Group G] :
  TauCeti.LimitGroup.IsLimitGroup G ↔ Group.FG G ∧ TauCeti.LimitGroup.IsFullyResiduallyFree G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/Characterization.html#TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree).

## Sources

- [Tau Ceti documentation: `TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/Characterization.html#TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree)
- [Source of `TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree` in TauCeti/GroupTheory/LimitGroup/Characterization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/LimitGroup/Characterization.lean#L169)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
