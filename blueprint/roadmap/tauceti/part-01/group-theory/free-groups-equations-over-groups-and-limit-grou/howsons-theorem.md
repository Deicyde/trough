---
declaration: theorem
origin: cited
lean: Subgroup.FG.inf_of_isFreeGroup
statement: formalized
proof: formalized
---

# Howson's theorem

in a free group, the intersection of two finitely generated subgroups
is finitely generated.

```lean
Subgroup.FG.inf_of_isFreeGroup.{u_1} {G : Type u_1} [Group G] [IsFreeGroup G] {H K : Subgroup G}
  (hH : H.FG) (hK : K.FG) : (H ⊓ K).FG
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.StallingsGraph.stallingsGraph](tauceti-stallingsgraph-stallingsgraph.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.FG.inf_of_isFreeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Howson.html#Subgroup.FG.inf_of_isFreeGroup).

## Sources

- [Tau Ceti documentation: `Subgroup.FG.inf_of_isFreeGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Howson.html#Subgroup.FG.inf_of_isFreeGroup)
- [Source of `Subgroup.FG.inf_of_isFreeGroup` in TauCeti/GroupTheory/FreeGroup/Howson.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/FreeGroup/Howson.lean#L37)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
