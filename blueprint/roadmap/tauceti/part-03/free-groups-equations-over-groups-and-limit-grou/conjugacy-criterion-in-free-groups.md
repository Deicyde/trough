---
declaration: theorem
origin: cited
lean: FreeGroup.isConj_iff_isRotated_reduceCyclically
statement: formalized
proof: formalized
---

# Conjugacy criterion in free groups

Two elements of a free group are conjugate exactly
when the cyclic reductions of their reduced words are cyclic rotations of each other.

```lean
FreeGroup.isConj_iff_isRotated_reduceCyclically.{u_1} {α : Type u_1} [DecidableEq α]
  {x y : FreeGroup α} :
  IsConj x y ↔ FreeGroup.reduceCyclically x.toWord ~r FreeGroup.reduceCyclically y.toWord
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FreeGroup.isConj_iff_isRotated_reduceCyclically`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Conjugacy/Basic.html#FreeGroup.isConj_iff_isRotated_reduceCyclically).

## Sources

- [Tau Ceti documentation: `FreeGroup.isConj_iff_isRotated_reduceCyclically`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Conjugacy/Basic.html#FreeGroup.isConj_iff_isRotated_reduceCyclically)
- [Source of `FreeGroup.isConj_iff_isRotated_reduceCyclically` in TauCeti/GroupTheory/FreeGroup/Conjugacy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FreeGroup/Conjugacy/Basic.lean#L219)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
