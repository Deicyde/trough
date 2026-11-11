---
declaration: theorem
origin: cited
lean: TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal
statement: formalized
proof: formalized
---

# TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal

A group is a limit group if and only if it is finitely generated and satisfies every universal
sentence of the group language that holds in the free group of rank two.

```lean
TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal.{u_1} {G : Type u_1} [Group G] :
  TauCeti.LimitGroup.IsLimitGroup G ↔
    Group.FG G ∧
      ∀ (σ : FirstOrder.Language.group.Sentence),
        FirstOrder.Language.BoundedFormula.IsUniversal σ → FreeGroup (Fin 2) ⊨ σ → G ⊨ σ
```

## Depends on

- [TauCeti.LimitGroup.MarkedGroup](tauceti-limitgroup-markedgroup.md)

## Proof depends on

- [Free groups of countable rank are equationally Noetherian](free-groups-of-countable-rank-are-equationally-n.md)
- [Limit groups are the finitely generated fully residually free groups (Champetier and Guirardel, Theorem 1.1)](limit-groups-are-the-finitely-generated-fully-re.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/UniversalTheory.html#TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal).

## Sources

- [Tau Ceti documentation: `TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal`](https://taucetiproject.org/docs/TauCeti/GroupTheory/LimitGroup/UniversalTheory.html#TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal)
- [Source of `TauCeti.LimitGroup.isLimitGroup_iff_forall_isUniversal` in TauCeti/GroupTheory/LimitGroup/UniversalTheory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/LimitGroup/UniversalTheory.lean#L123)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
