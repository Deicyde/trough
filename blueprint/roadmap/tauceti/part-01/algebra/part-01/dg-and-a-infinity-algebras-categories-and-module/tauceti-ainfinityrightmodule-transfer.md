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
  (hh : TauCeti.LinearMap.IsHomogeneous c.homotopy MM.grading.piece MM.grading.piece (-1))
  (hincl : TauCeti.LinearMap.IsHomogeneous c.incl GN.piece MM.grading.piece 0)
  (hproj : TauCeti.LinearMap.IsHomogeneous c.proj MM.grading.piece GN.piece 0) :
  TauCeti.AInfinityRightModule AA N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityRightModule.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.html#TauCeti.AInfinityRightModule.transfer).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityRightModule.transfer`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.html#TauCeti.AInfinityRightModule.transfer)
- [Source of `TauCeti.AInfinityRightModule.transfer` in TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/AInfinity/Module/Right/Transfer.lean#L564)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGAInfinity/STATUS.md)
