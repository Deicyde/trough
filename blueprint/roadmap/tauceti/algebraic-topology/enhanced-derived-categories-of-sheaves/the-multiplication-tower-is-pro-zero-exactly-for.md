---
declaration: theorem
origin: cited
lean: TauCeti.ModuleTower.isProZero_multiplicationTower_iff
statement: formalized
proof: formalized
---

# The multiplication tower is pro-zero exactly for nilpotent elements

```lean
TauCeti.ModuleTower.isProZero_multiplicationTower_iff.{u} {R : Type u} [Ring R] (a : R) :
  CategoryTheory.Functor.IsProZero (TauCeti.ModuleTower.multiplicationTower a) ↔ IsNilpotent a
```

## Depends on

- [CategoryTheory.Functor.IsProZero](categorytheory-functor-isprozero.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.isProZero_multiplicationTower_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/ProZero.html#TauCeti.ModuleTower.isProZero_multiplicationTower_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.isProZero_multiplicationTower_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/ProZero.html#TauCeti.ModuleTower.isProZero_multiplicationTower_iff)
- [Source of `TauCeti.ModuleTower.isProZero_multiplicationTower_iff` in TauCeti/Algebra/Category/ModuleCat/Tower/ProZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Tower/ProZero.lean#L188)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
