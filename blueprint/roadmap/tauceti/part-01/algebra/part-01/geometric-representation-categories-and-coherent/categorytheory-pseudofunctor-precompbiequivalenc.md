---
declaration: def
origin: cited
lean: CategoryTheory.Pseudofunctor.precompBiequivalence
statement: formalized
---

# CategoryTheory.Pseudofunctor.precompBiequivalence

An equivalence `e : Γ ≌ Λ` induces a biequivalence between the bicategories of families
`LocallyDiscrete Γ ⥤ᵖ B` and `LocallyDiscrete Λ ⥤ᵖ B`, with pseudofunctors pulling back along
`e.inverse` and along `e.functor`. Its unit is the composite of `(precompIdEquiv B Γ).symm`,
the equivalence `precompNatIso B e.unitIso` and `precompCompEquiv B e.functor e.inverse`; its
counit is the composite of `(precompCompEquiv B e.inverse e.functor).symm`,
`precompNatIso B e.counitIso` and `precompIdEquiv B Λ`.

```lean
CategoryTheory.Pseudofunctor.precompBiequivalence.{w₃, v₃, u₃, v₂, u₂, v₁, u₁} (B : Type u₃)
  [CategoryTheory.Bicategory B] {Γ : Type u₁} [CategoryTheory.Category.{v₁, u₁} Γ] {Λ : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} Λ] (e : Γ ≌ Λ) :
  TauCeti.Biequivalence (CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete Γ) B)
    (CategoryTheory.Pseudofunctor (CategoryTheory.LocallyDiscrete Λ) B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Pseudofunctor.precompBiequivalence`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/FunctorBicategory/Biequivalence.html#CategoryTheory.Pseudofunctor.precompBiequivalence).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Pseudofunctor.precompBiequivalence`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Bicategory/FunctorBicategory/Biequivalence.html#CategoryTheory.Pseudofunctor.precompBiequivalence)
- [Source of `CategoryTheory.Pseudofunctor.precompBiequivalence` in TauCeti/CategoryTheory/Bicategory/FunctorBicategory/Biequivalence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Bicategory/FunctorBicategory/Biequivalence.lean#L416)
- [Tau Ceti roadmap status: Geometric representation categories and coherent local transport](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricRepresentationCategories/STATUS.md)
