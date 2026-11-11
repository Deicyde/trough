---
declaration: def
origin: cited
lean: TauCeti.kInjectiveReplacement
statement: formalized
---

# TauCeti.kInjectiveReplacement

The K-injective replacement functor `D(C) ⥤ K(C)`. It sends an object of the derived category
to a K-injective complex representing it, viewed in the homotopy category. On morphisms it uses
that maps in the derived category into a K-injective complex are homotopy classes of chain
maps.

```lean
TauCeti.kInjectiveReplacement.{w, v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [TauCeti.HasKInjectiveResolutions C] [HasDerivedCategory C] :
  CategoryTheory.Functor (DerivedCategory C) (HomotopyCategory C (ComplexShape.up ℤ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.kInjectiveReplacement`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DerivedCategory/KInjective.html#TauCeti.kInjectiveReplacement).

## Sources

- [Tau Ceti documentation: `TauCeti.kInjectiveReplacement`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/DerivedCategory/KInjective.html#TauCeti.kInjectiveReplacement)
- [Source of `TauCeti.kInjectiveReplacement` in TauCeti/Algebra/Homology/DerivedCategory/KInjective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/DerivedCategory/KInjective.lean#L178)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
