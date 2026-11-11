---
declaration: def
origin: cited
lean: CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory
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

- [Chen's theorem, fullness](chens-theorem-fullness.md)
- [TauCeti.SingularityCategory](tauceti-singularitycategory.md)

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory).

## Sources

- [Tau Ceti documentation: `CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.html#CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory)
- [Source of `CategoryTheory.GorensteinProjective.fullyFaithfulToSingularityCategory` in TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/TotallyAcyclic/Abelian/Singularity.lean#L467)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
