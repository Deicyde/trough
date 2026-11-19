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
- [Source of `TauCeti.kInjectiveReplacement` in TauCeti/Algebra/Homology/DerivedCategory/KInjective.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/DerivedCategory/KInjective.lean#L178)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
