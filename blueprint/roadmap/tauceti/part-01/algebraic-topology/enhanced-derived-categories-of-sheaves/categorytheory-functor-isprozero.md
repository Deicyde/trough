---
declaration: def
origin: cited
lean: CategoryTheory.Functor.IsProZero
statement: formalized
---

# CategoryTheory.Functor.IsProZero

A diagram `F : J ⥤ C` is *pro-zero* if every object `F j` is killed by some map of the diagram:
for every `j` there is `f : i ⟶ j` with `F.map f = 0`. For towers `ℕᵒᵖ ⥤ C` this says that every
term is killed by some later composite transition (`isProZero_iff_forall_exists_le`).

```lean
CategoryTheory.Functor.IsProZero.{v₁, v₂, u₁, u₂} {J : Type u₁} [CategoryTheory.Category.{v₁, u₁} J]
  {C : Type u₂} [CategoryTheory.Category.{v₂, u₂} C] [CategoryTheory.Limits.HasZeroMorphisms C]
  (F : CategoryTheory.Functor J C) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.IsProZero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Functor/ProZero.html#CategoryTheory.Functor.IsProZero).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.IsProZero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Functor/ProZero.html#CategoryTheory.Functor.IsProZero)
- [Source of `CategoryTheory.Functor.IsProZero` in TauCeti/CategoryTheory/Functor/ProZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Functor/ProZero.lean#L64)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
