---
declaration: def
origin: cited
lean: TauCeti.AInfinityAlgebra.transferHomotopy
statement: formalized
---

# TauCeti.AInfinityAlgebra.transferHomotopy

The homotopy from the identity of an A-infinity algebra to its transferred inclusion composed
with its transferred projection. On bar constructions this is `K - K X K`, where `K` is the
tensor-trick homotopy and `X` the perturbation operator.

```lean
TauCeti.AInfinityAlgebra.transferHomotopy.{uR, uA, uH} {R : Type uR} {A : Type uA} {H : Type uH}
  [CommRing R] [AddCommGroup A] [_root_.Module R A] [AddCommGroup H] [_root_.Module R H]
  (𝒜 : TauCeti.AInfinityAlgebra R A) {GH : TauCeti.InternalGrading R H ℤ} {dH : Module.End R H}
  (c : TauCeti.LinearSpecialContraction 𝒜.differential dH)
  (hh : TauCeti.LinearMap.IsHomogeneous c.homotopy (𝒜.grading.piece ℤ) (𝒜.grading.piece ℤ) (-1))
  (hincl : TauCeti.LinearMap.IsHomogeneous c.incl (GH.piece ℤ) (𝒜.grading.piece ℤ) 0)
  (hproj : TauCeti.LinearMap.IsHomogeneous c.proj (𝒜.grading.piece ℤ) (GH.piece ℤ) 0) :
  (TauCeti.AInfinityHom.id 𝒜).Homotopy
    ((𝒜.transferInclusion c hh hincl hproj).comp (𝒜.transferProjection c hh hincl hproj))
```

## Depends on

- [TauCeti.AInfinityAlgebra.transfer](tauceti-ainfinityalgebra-transfer.md)

## Proof depends on

- [The suspended Stasheff identity free of the structural coefficient holds exactly when the unsuspended one does](../homology/the-suspended-stasheff-identity-free-of-the-stru.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.transferHomotopy`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Homotopy.html#TauCeti.AInfinityAlgebra.transferHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.transferHomotopy`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Homotopy.html#TauCeti.AInfinityAlgebra.transferHomotopy)
- [Source of `TauCeti.AInfinityAlgebra.transferHomotopy` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Homotopy.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Homotopy.lean#L47)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
