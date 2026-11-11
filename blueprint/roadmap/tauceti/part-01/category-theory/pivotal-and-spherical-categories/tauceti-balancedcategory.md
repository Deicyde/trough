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
- [Source of `TauCeti.BalancedCategory` in TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Braided/Balanced/Basic.lean#L49)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
