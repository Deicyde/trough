---
declaration: def
origin: cited
lean: TauCeti.AInfinityAlgebra.transfer
statement: formalized
---

# TauCeti.AInfinityAlgebra.transfer

The **transferred `A∞` structure** on the retract `H` of a special contraction of `(A, m₁)`:
its Taylor map is the letter component of the transferred bar differential.

```lean
TauCeti.AInfinityAlgebra.transfer.{uR, uA, uH} {R : Type uR} {A : Type uA} {H : Type uH}
  [CommRing R] [AddCommGroup A] [_root_.Module R A] [AddCommGroup H] [_root_.Module R H]
  (𝒜 : TauCeti.AInfinityAlgebra R A) {GH : TauCeti.InternalGrading R H ℤ} {dH : Module.End R H}
  (c : TauCeti.LinearSpecialContraction 𝒜.differential dH)
  (hh : TauCeti.LinearMap.IsHomogeneous c.homotopy (𝒜.grading.piece ℤ) (𝒜.grading.piece ℤ) (-1))
  (hincl : TauCeti.LinearMap.IsHomogeneous c.incl (GH.piece ℤ) (𝒜.grading.piece ℤ) 0)
  (hproj : TauCeti.LinearMap.IsHomogeneous c.proj (𝒜.grading.piece ℤ) (GH.piece ℤ) 0) :
  TauCeti.AInfinityAlgebra R H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Basic.html#TauCeti.AInfinityAlgebra.transfer).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Basic.html#TauCeti.AInfinityAlgebra.transfer)
- [Source of `TauCeti.AInfinityAlgebra.transfer` in TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/AInfinity/Algebra/Transfer/Basic.lean#L300)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)
