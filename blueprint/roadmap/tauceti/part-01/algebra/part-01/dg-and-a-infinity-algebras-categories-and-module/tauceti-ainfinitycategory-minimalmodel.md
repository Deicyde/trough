---
declaration: def
origin: cited
lean: TauCeti.AInfinityCategory.minimalModel
statement: formalized
---

# TauCeti.AInfinityCategory.minimalModel

The **minimal model** of an `A∞` category over a field: the `A∞` category on the quiver of Hom
cohomologies transferred along the cohomology contraction.  Its differential vanishes
(`homDifferential_minimalModel`), its composition is the composition induced on cohomology
(`comp_minimalModel_cohomologyClass`), and its higher operations are the transferred ones.

```lean
TauCeti.AInfinityCategory.minimalModel.{u, v, w} {K : Type w} [Field K] {C : Type u}
  [TauCeti.GradedLinearQuiver K C] (𝒞 : TauCeti.AInfinityCategory K C) :
  TauCeti.AInfinityCategory K 𝒞.CohomologyQuiver
```

## Depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityCategory.minimalModel`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Transfer/Cohomology.html#TauCeti.AInfinityCategory.minimalModel).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityCategory.minimalModel`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/AInfinity/Transfer/Cohomology.html#TauCeti.AInfinityCategory.minimalModel)
- [Source of `TauCeti.AInfinityCategory.minimalModel` in TauCeti/CategoryTheory/AInfinity/Transfer/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/AInfinity/Transfer/Cohomology.lean#L245)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
