---
declaration: theorem
origin: cited
lean: TauCeti.injective_freeGroup_lift_transvection_two
statement: formalized
proof: formalized
---

# Sanov's theorem

The matrices `[[1, 2], [0, 1]]` and `[[1, 0], [2, 1]]` freely generate
a free subgroup of rank two of `SL(2, ℤ)`. This is the case `R = ℤ`, `c = d = 2` of
`injective_freeGroup_lift_transvection_of_two_le_abs`.

```lean
TauCeti.injective_freeGroup_lift_transvection_two :
  Function.Injective
    ⇑(FreeGroup.lift
        ![Matrix.SpecialLinearGroup.transvection ⋯ 2, Matrix.SpecialLinearGroup.transvection ⋯ 2])
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.injective_freeGroup_lift_transvection_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.injective_freeGroup_lift_transvection_two).

## Sources

- [Tau Ceti documentation: `TauCeti.injective_freeGroup_lift_transvection_two`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.injective_freeGroup_lift_transvection_two)
- [Source of `TauCeti.injective_freeGroup_lift_transvection_two` in TauCeti/GroupTheory/FreeGroup/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FreeGroup/Linear.lean#L122)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
