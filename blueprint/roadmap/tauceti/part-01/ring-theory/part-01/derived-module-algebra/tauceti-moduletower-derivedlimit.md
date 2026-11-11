---
declaration: def
origin: cited
lean: TauCeti.ModuleTower.derivedLimit
statement: formalized
---

# TauCeti.ModuleTower.derivedLimit

The **derived limit** functor `Rlim : D(ℕᵒᵖ ⥤ ModuleCat R) ⥤ D(R)` on the derived category of
towers of `R`-modules, induced by the homotopy limit `Cone(δ)[-1]`
(`ModuleTower.derivedLimitFactors`).

```lean
TauCeti.ModuleTower.derivedLimit.{w, w', v, u} (R : Type u) [Ring R]
  [HasDerivedCategory (TauCeti.ModuleTower R)] [HasDerivedCategory (ModuleCat R)] :
  CategoryTheory.Functor (DerivedCategory (TauCeti.ModuleTower R)) (DerivedCategory (ModuleCat R))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.derivedLimit`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.html#TauCeti.ModuleTower.derivedLimit).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.derivedLimit`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.html#TauCeti.ModuleTower.derivedLimit)
- [Source of `TauCeti.ModuleTower.derivedLimit` in TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/Tower/DerivedLimit.lean#L312)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
