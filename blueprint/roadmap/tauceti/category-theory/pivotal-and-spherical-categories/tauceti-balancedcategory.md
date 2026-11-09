---
declaration: class
origin: cited
lean: TauCeti.BalancedCategory
statement: formalized
---

# TauCeti.BalancedCategory

A *balanced* structure on a braided monoidal category: a twist `θ : 𝟭 C ≅ 𝟭 C`, a natural
automorphism of the identity functor, satisfying the balancing axiom
`θ_{X ⊗ Y} = (θ_X ⊗ θ_Y) ≫ β_{X,Y} ≫ β_{Y,X}`.

```lean
TauCeti.BalancedCategory.{v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] : Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BalancedCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.html#TauCeti.BalancedCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.BalancedCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.html#TauCeti.BalancedCategory)
- [Source of `TauCeti.BalancedCategory` in TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.lean#L49)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
