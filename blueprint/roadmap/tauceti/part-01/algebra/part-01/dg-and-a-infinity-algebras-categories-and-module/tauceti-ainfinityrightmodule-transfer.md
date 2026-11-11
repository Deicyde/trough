---
declaration: def
origin: cited
lean: TauCeti.AInfinityRightModule.transfer
statement: formalized
---

# TauCeti.AInfinityRightModule.transfer

The **transferred right `A∞` module** on the retract `N` of a special contraction of
`(M, m₁)`: its bar differential is the transferred bar differential.

```lean
TauCeti.AInfinityRightModule.transfer.{uR, uA, uM, uN} {R : Type uR} {A : Type uA} {M : Type uM}
  {N : Type uN} [CommRing R] [AddCommGroup A] [_root_.Module R A] [AddCommGroup M]
  [_root_.Module R M] [AddCommGroup N] [_root_.Module R N] {AA : TauCeti.AInfinityAlgebra R A}
  (MM : TauCeti.AInfinityRightModule AA M) {GN : TauCeti.InternalGrading R N ℤ}
  {dN : Module.End R N} (c : TauCeti.LinearSpecialContraction MM.differential dN)
  (hh : TauCeti.LinearMap.IsHomogeneous c.homotopy (MM.grading.piece ℤ) (MM.grading.piece ℤ) (-1))
  (hincl : TauCeti.LinearMap.IsHomogeneous c.incl (GN.piece ℤ) (MM.grading.piece ℤ) 0)
  (hproj : TauCeti.LinearMap.IsHomogeneous c.proj (MM.grading.piece ℤ) (GN.piece ℤ) 0) :
  TauCeti.AInfinityRightModule AA N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityRightModule.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.html#TauCeti.AInfinityRightModule.transfer).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityRightModule.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.html#TauCeti.AInfinityRightModule.transfer)
- [Source of `TauCeti.AInfinityRightModule.transfer` in TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.lean#L564)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
