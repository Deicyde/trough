---
declaration: def
origin: cited
lean: CategoryTheory.Limits.limitFiberwiseLimitIso
statement: formalized
---

# CategoryTheory.Limits.limitFiberwiseLimitIso

Taking the total limit agrees with first taking limits on fibers and then on the base.

```lean
CategoryTheory.Limits.limitFiberwiseLimitIso.{v, u, v', u', w, z} {D : Type u}
  [CategoryTheory.Category.{v, u} D] {C : CategoryTheory.Functor D CategoryTheory.Cat} {V : Type u'}
  [CategoryTheory.Category.{v', u'} V]
  (F : CategoryTheory.Functor (CategoryTheory.Grothendieck C) V)
  [∀ (d : D), CategoryTheory.Limits.HasLimit ((CategoryTheory.Grothendieck.ι C d).comp F)]
  [∀ {d e : D} (f : d ⟶ e),
      CategoryTheory.Limits.HasLimit
        ((C.map f).toFunctor.comp ((CategoryTheory.Grothendieck.ι C e).comp F))]
  [∀ {d e : D} (f : d ⟶ e),
      CategoryTheory.IsIso
        (CategoryTheory.Limits.limit.pre ((CategoryTheory.Grothendieck.ι C e).comp F)
          (C.map f).toFunctor)]
  [CategoryTheory.Limits.HasLimit F]
  [CategoryTheory.Limits.HasLimit (CategoryTheory.Limits.fiberwiseLimit F)] :
  CategoryTheory.Limits.limit F ≅
    CategoryTheory.Limits.limit (CategoryTheory.Limits.fiberwiseLimit F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Limits.limitFiberwiseLimitIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Limits/Shapes/Grothendieck.html#CategoryTheory.Limits.limitFiberwiseLimitIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Limits.limitFiberwiseLimitIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Limits/Shapes/Grothendieck.html#CategoryTheory.Limits.limitFiberwiseLimitIso)
- [Source of `CategoryTheory.Limits.limitFiberwiseLimitIso` in TauCeti/CategoryTheory/Limits/Shapes/Grothendieck.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Limits/Shapes/Grothendieck.lean#L286)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
