---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup
statement: formalized
proof: formalized
---

# Linear groups are equationally Noetherian

Over a commutative Noetherian ring `R`, the
general linear group `GL n R` is equationally Noetherian over any coefficients: every system of
equations in finitely many variables has a finite subsystem with the same solutions in
`GL n R`.

```lean
TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup.{u_1, u_4, u_5} {G : Type u_1}
  [Group G] {R : Type u_4} {n : Type u_5} [CommRing R] [IsNoetherianRing R] [Fintype n]
  [DecidableEq n] (ι : G →* GL n R) : TauCeti.GroupAlgGeom.IsEquationallyNoetherian ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Linear.html#TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Linear.html#TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup)
- [Source of `TauCeti.GroupAlgGeom.isEquationallyNoetherian_generalLinearGroup` in TauCeti/GroupTheory/GroupAlgGeom/Linear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/GroupAlgGeom/Linear.lean#L188)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
