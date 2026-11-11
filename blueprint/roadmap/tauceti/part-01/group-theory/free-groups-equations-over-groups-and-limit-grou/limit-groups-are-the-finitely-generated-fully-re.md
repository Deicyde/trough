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

- [TauCeti.LimitGroup.MarkedGroup](tauceti-limitgroup-markedgroup.md)

## Proof depends on

- [Free groups of countable rank are equationally Noetherian](free-groups-of-countable-rank-are-equationally-n.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/Characterization.html#TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree).

## Sources

- [Tau Ceti documentation: `TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/Characterization.html#TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree)
- [Source of `TauCeti.LimitGroup.isLimitGroup_iff_isFullyResiduallyFree` in TauCeti/GroupTheory/LimitGroup/Characterization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/LimitGroup/Characterization.lean#L169)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
