---
declaration: theorem
origin: cited
lean: TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory, TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory_isTriangulated
statement: formalized
proof: formalized
---

# Buchweitz's theorem for self-injective algebras

the functor `stmod-A ⥤ D_sg(A)` is an
equivalence of categories.

```lean
TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory.{w, w', u} (k : Type w)
  [Field k] {A : Type u} [Ring A] [Algebra k A] [FiniteDimensional k A] [IsNoetherianRing Aᵐᵒᵖ]
  (hr : Module.Injective Aᵐᵒᵖ Aᵐᵒᵖ) (hl : Module.Injective Aᵐᵒᵖᵐᵒᵖ Aᵐᵒᵖ)
  [HasDerivedCategory (FGModuleCat Aᵐᵒᵖ)] :
  (TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory k hr hl).IsEquivalence
```

## Depends on

- [Happel's theorem](../../part-01/stable-periodic-and-curved-homological-algebra/happels-theorem.md)
- [The module-category Frobenius theorem](the-module-category-frobenius-theorem.md)
- [TauCeti.SingularityCategory](../../part-01/stable-periodic-and-curved-homological-algebra/tauceti-singularitycategory.md)

## Proof depends on

- [Buchweitz's theorem](../homology/buchweitzs-theorem.md)
- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/Stable/Singularity.html#TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory).

## Other forms

**Buchweitz's theorem for self-injective algebras, triangulated form.** Formalized in Tau Ceti as [`TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory_isTriangulated`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/Stable/Singularity.html#TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory_isTriangulated).

```lean
TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory_isTriangulated.{w, w', u} (k : Type w)
  [Field k] {A : Type u} [Ring A] [Algebra k A] [FiniteDimensional k A] [IsNoetherianRing Aᵐᵒᵖ]
  (hr : Module.Injective Aᵐᵒᵖ Aᵐᵒᵖ) (hl : Module.Injective Aᵐᵒᵖᵐᵒᵖ Aᵐᵒᵖ)
  [HasDerivedCategory (FGModuleCat Aᵐᵒᵖ)] :
  (TauCeti.FGModuleCat.stableModuleCategoryToSingularityCategory k hr hl).IsTriangulated
```

## Sources

- [Tau Ceti documentation: `TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/Stable/Singularity.html#TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory)
- [Source of `TauCeti.FGModuleCat.isEquivalence_stableModuleCategoryToSingularityCategory` in TauCeti/Algebra/Category/FGModuleCat/Stable/Singularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Category/FGModuleCat/Stable/Singularity.lean#L140)
