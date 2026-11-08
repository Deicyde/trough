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

## Proof depends on

- [The suspended Stasheff identity free of the structural coefficient holds exactly when the unsuspended one does](../homology/the-suspended-stasheff-identity-free-of-the-stru.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.html#TauCeti.AInfinityAlgebra.minimalModel).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.minimalModel`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.html#TauCeti.AInfinityAlgebra.minimalModel)
- [Source of `TauCeti.AInfinityAlgebra.minimalModel` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Cohomology.lean#L228)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
