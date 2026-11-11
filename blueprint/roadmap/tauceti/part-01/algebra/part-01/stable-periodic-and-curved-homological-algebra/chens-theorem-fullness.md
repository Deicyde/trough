---
declaration: theorem
origin: cited
lean: CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory, CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory
statement: formalized
proof: formalized
---

# Chen's theorem, fullness

every morphism of the singularity category between
Gorenstein-projective objects comes from a morphism of `C`.

```lean
CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory.{w,
    v, u}
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [HasDerivedCategory C] : (CategoryTheory.GorensteinProjective.toSingularityCategory C).Full
```

## Depends on

- [TauCeti.SingularityCategory](tauceti-singularitycategory.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory).

## Other forms

**Chen's theorem, faithfulness.** Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory).

```lean
CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory.{w,
    v, u}
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [HasDerivedCategory C] : (CategoryTheory.GorensteinProjective.toSingularityCategory C).Faithful
```

## Sources

- [Tau Ceti documentation: `CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory)
- [Source of `CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory` in TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean#L439)
