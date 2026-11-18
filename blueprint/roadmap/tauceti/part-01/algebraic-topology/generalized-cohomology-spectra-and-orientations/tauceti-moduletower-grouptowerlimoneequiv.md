---
declaration: def
origin: cited
lean: TauCeti.ModuleTower.groupTowerLimOneEquiv
statement: formalized
---

# TauCeti.ModuleTower.groupTowerLimOneEquiv

The nonabelian `lim¹` of the tower of groups underlying a tower of modules is its `lim¹`, the
cokernel of the shift map: the orbit of a family under the twisted action is sent to its class
modulo the image of the shift map.

```lean
TauCeti.ModuleTower.groupTowerLimOneEquiv.{v, u} {R : Type u} [Ring R] (F : TauCeti.ModuleTower R) :
  F.toGroupTower.limOne ≃ F.limOne
```

## Depends on

- [TauCeti.GroupTower.limOne](tauceti-grouptower-limone.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.groupTowerLimOneEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/GroupTower.html#TauCeti.ModuleTower.groupTowerLimOneEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.groupTowerLimOneEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/GroupTower.html#TauCeti.ModuleTower.groupTowerLimOneEquiv)
- [Source of `TauCeti.ModuleTower.groupTowerLimOneEquiv` in TauCeti/Algebra/Category/ModuleCat/Tower/GroupTower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/ModuleCat/Tower/GroupTower.lean#L53)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
