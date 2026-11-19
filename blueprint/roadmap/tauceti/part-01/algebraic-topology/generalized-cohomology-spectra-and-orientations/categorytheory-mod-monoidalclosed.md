---
declaration: instance
origin: cited
lean: CategoryTheory.Mod.monoidalClosed
statement: formalized
---

# CategoryTheory.Mod.monoidalClosed

Modules over a commutative monoid in a braided closed monoidal category form a closed
monoidal category under balanced tensor, with the equalizer internal hom.

```lean
CategoryTheory.Mod.monoidalClosed.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
  [CategoryTheory.MonoidalClosed C] [CategoryTheory.Limits.HasEqualizers C] {A : C}
  [CategoryTheory.MonObj A] [CategoryTheory.IsCommMonObj A]
  [CategoryTheory.Limits.HasCoequalizers C]
  [∀ (X : C),
      CategoryTheory.Limits.PreservesColimitsOfSize.{0, 0, v, v, u, u}
        (CategoryTheory.MonoidalCategory.tensorLeft X)]
  [∀ (X : C),
      CategoryTheory.Limits.PreservesColimitsOfSize.{0, 0, v, v, u, u}
        (CategoryTheory.MonoidalCategory.tensorRight X)] :
  CategoryTheory.MonoidalClosed (CategoryTheory.Mod C A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Mod.monoidalClosed`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Mod/Closed.html#CategoryTheory.Mod.monoidalClosed).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Mod.monoidalClosed`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Mod/Closed.html#CategoryTheory.Mod.monoidalClosed)
- [Source of `CategoryTheory.Mod.monoidalClosed` in TauCeti/CategoryTheory/Monoidal/Mod/Closed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Mod/Closed.lean#L155)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
