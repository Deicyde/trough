---
declaration: theorem
origin: cited
lean: TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential
statement: formalized
proof: formalized
---

# The Hochschild differential squares to zero

`[m, [m, F]] = 0` for every cochain `F` of
degree `q`.

```lean
TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential.{uR, uA} {R : Type uR}
  {A : Type uA} [CommRing R] [AddCommGroup A] [_root_.Module R A] (𝒜 : TauCeti.AInfinityAlgebra R A)
  {q : ℤ} {F : TauCeti.ReducedTensorWords R A →ₗ[R] A}
  (hF :
    TauCeti.LinearMap.IsHomogeneous F (TauCeti.ReducedTensorWords.gradedPiece (𝒜.grading.shift 1))
      ((𝒜.grading.shift 1).piece ℤ) q) :
  𝒜.hochschildDifferential (1 + q) (𝒜.hochschildDifferential q F) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Basic.html#TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Basic.html#TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential)
- [Source of `TauCeti.AInfinityAlgebra.hochschildDifferential_hochschildDifferential` in TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Algebra/Hochschild/Basic.lean#L145)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
