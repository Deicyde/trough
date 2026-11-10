---
declaration: def
origin: cited
lean: CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory, CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory, CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory
statement: formalized
---

# Chen's theorem

the functor from the stable category of Gorenstein-projective objects of an
abelian category to its singularity category is fully faithful.

```lean
CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory.{w, v, u} (C : Type u)
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [HasDerivedCategory C] :
  (CategoryTheory.GorensteinProjective.toSingularityCategory C).FullyFaithful
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory).

## Other forms

**Chen's theorem, faithfulness.** Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory).

```lean
CategoryTheory.GorensteinProjective.instFaithfulProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory.{w,
    v, u}
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [HasDerivedCategory C] : (CategoryTheory.GorensteinProjective.toSingularityCategory C).Faithful
```

**Chen's theorem, fullness.** Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory).

```lean
CategoryTheory.GorensteinProjective.instFullProjectiveStableCategoryExactStructureSingularityCategoryToSingularityCategory.{w,
    v, u}
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [HasDerivedCategory C] : (CategoryTheory.GorensteinProjective.toSingularityCategory C).Full
```

## Sources

- [Tau Ceti documentation: `CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory)
- [Source of `CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory` in TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean#L448)
