---
declaration: def
origin: cited
lean: TauCeti.AInfinityAlgebra.minimalModel
statement: formalized
---

# TauCeti.AInfinityAlgebra.minimalModel

The minimal `A∞` model on cohomology obtained by homogeneous transfer.

```lean
TauCeti.AInfinityAlgebra.minimalModel.{uK, uA} {K : Type uK} {A : Type uA} [Field K]
  [AddCommGroup A] [_root_.Module K A] (𝒜 : TauCeti.AInfinityAlgebra K A) :
  TauCeti.AInfinityAlgebra K 𝒜.Cohomology
```

## Depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.html#TauCeti.AInfinityAlgebra.minimalModel).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.html#TauCeti.AInfinityAlgebra.minimalModel)
- [Source of `TauCeti.AInfinityAlgebra.minimalModel` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean#L228)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
