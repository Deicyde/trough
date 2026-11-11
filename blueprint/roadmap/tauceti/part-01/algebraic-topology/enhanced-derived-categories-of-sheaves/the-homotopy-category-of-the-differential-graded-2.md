---
declaration: def
origin: cited
lean: TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv
statement: formalized
---

# The homotopy category of the differential graded nerve of K-injective complexes is the derived category

When every complex has a K-injective resolution, the quasicategory
`dgNerve R (KInjectiveDGCategory C)` enhances `DerivedCategory C`. The functor is the inverse
`TauCeti.dgNerve.fromHomotopyCategory` of the identification of the homotopy category of the nerve
with `H⁰`, followed by the comparison functor `TauCeti.KInjectiveDGCategory.toDerivedCategory`.

```lean
TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv.{w, v, u} (R : Type v) [CommRing R]
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.Linear R C] [HasDerivedCategory C] [TauCeti.HasKInjectiveResolutions C] :
  (TauCeti.dgNerve R (TauCeti.KInjectiveDGCategory C)).HomotopyCategory ≌ DerivedCategory C
```

## Depends on

- [The homotopy category of the differential graded nerve](the-homotopy-category-of-the-differential-graded.md)

## Proof depends on

- [TauCeti.kInjectiveReplacement](../../ring-theory/part-01/derived-module-algebra/tauceti-kinjectivereplacement.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/CochainComplex/KInjective.html#TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/CochainComplex/KInjective.html#TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv)
- [Source of `TauCeti.KInjectiveDGCategory.dgNerveHomotopyCategoryEquiv` in TauCeti/CategoryTheory/DG/CochainComplex/KInjective.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/DG/CochainComplex/KInjective.lean#L188)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
