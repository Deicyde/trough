---
declaration: instance
origin: cited
lean: CategoryTheory.Mod.symmetricCategory
statement: formalized
---

# CategoryTheory.Mod.symmetricCategory

Modules over a commutative monoid object in a symmetric monoidal category form a symmetric
monoidal category under the balanced tensor product, with braiding induced by that of `C`.

```lean
CategoryTheory.Mod.symmetricCategory.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.SymmetricCategory C]
  [CategoryTheory.Limits.HasCoequalizers C]
  [∀ (X : C),
      CategoryTheory.Limits.PreservesColimitsOfSize.{0, 0, v, v, u, u}
        (CategoryTheory.MonoidalCategory.tensorLeft X)]
  [∀ (X : C),
      CategoryTheory.Limits.PreservesColimitsOfSize.{0, 0, v, v, u, u}
        (CategoryTheory.MonoidalCategory.tensorRight X)]
  {A : C} [CategoryTheory.MonObj A] [CategoryTheory.IsCommMonObj A] :
  CategoryTheory.SymmetricCategory (CategoryTheory.Mod C A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Mod.symmetricCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Mod/Symmetric.html#CategoryTheory.Mod.symmetricCategory).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Mod.symmetricCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Mod/Symmetric.html#CategoryTheory.Mod.symmetricCategory)
- [Source of `CategoryTheory.Mod.symmetricCategory` in TauCeti/CategoryTheory/Monoidal/Mod/Symmetric.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Mod/Symmetric.lean#L97)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
