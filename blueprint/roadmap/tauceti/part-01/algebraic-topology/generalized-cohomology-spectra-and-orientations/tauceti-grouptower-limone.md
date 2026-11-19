---
declaration: abbrev
origin: cited
lean: TauCeti.GroupTower.limOne
statement: formalized
---

# TauCeti.GroupTower.limOne

The nonabelian `lim¹` of a tower of groups: the orbit set of the twisted action of `∏ₙ Gₙ`
on `∏ₙ Gₙ`. It is a pointed set, pointed by the orbit of the identity family.

```lean
TauCeti.GroupTower.limOne.{u} {G : ℕ → Type u} [(n : ℕ) → Group (G n)] (r : TauCeti.GroupTower G) :
  Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupTower.limOne`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Tower.html#TauCeti.GroupTower.limOne).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupTower.limOne`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Tower.html#TauCeti.GroupTower.limOne)
- [Source of `TauCeti.GroupTower.limOne` in TauCeti/Algebra/Group/Tower.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Group/Tower.lean#L116)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
