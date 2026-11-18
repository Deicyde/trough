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
- [Source of `TauCeti.derivedHom` in TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/DerivedCategory/DerivedHom.lean#L64)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
