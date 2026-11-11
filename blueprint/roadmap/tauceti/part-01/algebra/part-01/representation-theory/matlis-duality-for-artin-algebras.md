---
declaration: def
origin: cited
lean: TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality
statement: formalized
---

# Matlis duality for Artin algebras

For an injective hull `E` of `R ⧸ J(R)`, the dual
`D_R = Hom_R(-, E)` is an anti-equivalence between the finitely generated left and the finitely
generated right modules over an Artin `R`-algebra `A`.

```lean
TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality.{u, v, t} {R : Type u} [CommRing R]
  [IsArtinianRing R] {E : Type v} [AddCommGroup E] [_root_.Module R E] [Small.{v, u} R]
  {f : R ⧸ Ring.jacobson R →ₗ[R] E} {A : Type t} [Ring A] [Algebra R A] [Module.Finite R A]
  (hf : TauCeti.IsInjectiveEnvelope f) : (FGModuleCat A)ᵒᵖ ≌ FGModuleCat Aᵐᵒᵖ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/MatlisDuality.html#TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality).

## Sources

- [Tau Ceti documentation: `TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/FGModuleCat/MatlisDuality.html#TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality)
- [Source of `TauCeti.IsInjectiveEnvelope.fgModuleCatMatlisDuality` in TauCeti/Algebra/Category/FGModuleCat/MatlisDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/FGModuleCat/MatlisDuality.lean#L94)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)
