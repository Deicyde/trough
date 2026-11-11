---
declaration: def
origin: cited
lean: TauCeti.derivedHom
statement: formalized
---

# TauCeti.derivedHom

The derived Hom complex `RHom(L, M)` of objects `L` and `M` of the derived category of `C`,
an object of the derived category of `R`-modules. It is the `R`-linear Hom complex between the
K-injective replacements of `L` and `M`.

```lean
TauCeti.derivedHom.{t, w', w, v, u} (R : Type w) [Ring R] (C : Type u)
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.Linear R C]
  [TauCeti.HasKInjectiveResolutions C] [HasDerivedCategory C] [HasDerivedCategory (ModuleCat R)] :
  CategoryTheory.Functor (DerivedCategory C)ᵒᵖ
    (CategoryTheory.Functor (DerivedCategory C) (DerivedCategory (ModuleCat R)))
```

## Depends on

- [TauCeti.kInjectiveReplacement](tauceti-kinjectivereplacement.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.derivedHom`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.html#TauCeti.derivedHom).

## Sources

- [Tau Ceti documentation: `TauCeti.derivedHom`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.html#TauCeti.derivedHom)
- [Source of `TauCeti.derivedHom` in TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.lean#L64)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
