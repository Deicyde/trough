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
- [Source of `TauCeti.AInfinityAlgebra.minimalModel` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean#L228)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
