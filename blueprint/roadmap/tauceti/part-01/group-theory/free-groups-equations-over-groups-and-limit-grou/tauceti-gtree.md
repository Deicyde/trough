---
declaration: structure
origin: cited
lean: TauCeti.GTree
statement: formalized
---

# TauCeti.GTree

A `G`-tree: a Serre tree with an action of `G` by graph automorphisms without inversions.

```lean
TauCeti.GTree.{u, v, w} (G : Type w) [Group G] : Type (max (max (u + 1) (v + 1)) w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GTree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/Basic.html#TauCeti.GTree).

## Sources

- [Tau Ceti documentation: `TauCeti.GTree`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/Basic.html#TauCeti.GTree)
- [Source of `TauCeti.GTree` in TauCeti/GroupTheory/GTree/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GTree/Basic.lean#L81)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
