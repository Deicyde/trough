---
declaration: theorem
origin: cited
lean: TauCeti.exists_injective_freeGroup_SL
statement: formalized
proof: formalized
---

# Free groups of countable rank are linear over `ℤ`

Every free group on a countable basis
embeds in `SL(2, ℤ)`.

```lean
TauCeti.exists_injective_freeGroup_SL.{u_2} (ι : Type u_2) [Countable ι] :
  ∃ f, Function.Injective ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_injective_freeGroup_SL`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.exists_injective_freeGroup_SL).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_injective_freeGroup_SL`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Linear.html#TauCeti.exists_injective_freeGroup_SL)
- [Source of `TauCeti.exists_injective_freeGroup_SL` in TauCeti/GroupTheory/FreeGroup/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/FreeGroup/Linear.lean#L141)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
