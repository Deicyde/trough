---
declaration: theorem
origin: cited
lean: Subgroup.rank_sub_one_eq_index_mul_rank_sub_one, Subgroup.rank_add_index_eq_index_mul_natCard_add_one, Subgroup.rank_add_index_eq_index_mul_rank_add_one, Subgroup.rank_sub_one_eq_index_mul_natCard_sub_one
statement: formalized
proof: formalized
---

# Schreier's index formula (`Subgroup.rank_sub_one_eq_index_mul_rank_sub_one`)

a subgroup `H` of finite index `i` of a finitely generated free
group `G` satisfies `rank H - 1 = i * (rank G - 1)` as integers.

```lean
Subgroup.rank_sub_one_eq_index_mul_rank_sub_one.{u_1} {G : Type u_1} [Group G] [IsFreeGroup G]
  [Group.FG G] (H : Subgroup G) [H.FiniteIndex] :
  ↑(Group.rank ↥H) - 1 = ↑H.index * (↑(Group.rank G) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.rank_sub_one_eq_index_mul_rank_sub_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Schreier.html#Subgroup.rank_sub_one_eq_index_mul_rank_sub_one).

## Other forms

**Schreier's index formula.** Formalized in Tau Ceti as [`Subgroup.rank_add_index_eq_index_mul_natCard_add_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Schreier.html#Subgroup.rank_add_index_eq_index_mul_natCard_add_one).

```lean
Subgroup.rank_add_index_eq_index_mul_natCard_add_one.{u_1} {α : Type u_1}
  (H : Subgroup (FreeGroup α)) [Finite α] [H.FiniteIndex] :
  Group.rank ↥H + H.index = H.index * Nat.card α + 1
```

**Schreier's index formula.** Formalized in Tau Ceti as [`Subgroup.rank_add_index_eq_index_mul_rank_add_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Schreier.html#Subgroup.rank_add_index_eq_index_mul_rank_add_one).

```lean
Subgroup.rank_add_index_eq_index_mul_rank_add_one.{u_1} {G : Type u_1} [Group G] [IsFreeGroup G]
  [Group.FG G] (H : Subgroup G) [H.FiniteIndex] :
  Group.rank ↥H + H.index = H.index * Group.rank G + 1
```

**Schreier's index formula.** Formalized in Tau Ceti as [`Subgroup.rank_sub_one_eq_index_mul_natCard_sub_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Schreier.html#Subgroup.rank_sub_one_eq_index_mul_natCard_sub_one).

```lean
Subgroup.rank_sub_one_eq_index_mul_natCard_sub_one.{u_1} {α : Type u_1} (H : Subgroup (FreeGroup α))
  [Finite α] [H.FiniteIndex] : ↑(Group.rank ↥H) - 1 = ↑H.index * (↑(Nat.card α) - 1)
```

## Sources

- [Tau Ceti documentation: `Subgroup.rank_sub_one_eq_index_mul_rank_sub_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Schreier.html#Subgroup.rank_sub_one_eq_index_mul_rank_sub_one)
- [Source of `Subgroup.rank_sub_one_eq_index_mul_rank_sub_one` in TauCeti/GroupTheory/FreeGroup/Schreier.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/FreeGroup/Schreier.lean#L91)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
