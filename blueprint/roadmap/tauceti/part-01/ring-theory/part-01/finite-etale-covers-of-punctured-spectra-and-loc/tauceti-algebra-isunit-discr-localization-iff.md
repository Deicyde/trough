---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.isUnit_discr_localization_iff
statement: formalized
proof: formalized
---

# TauCeti.Algebra.isUnit_discr_localization_iff

The discriminant of a basis of a finite free algebra is a unit at a prime `𝔭` iff the base
change to the localization `A_𝔭` is étale over `A_𝔭`.

```lean
TauCeti.Algebra.isUnit_discr_localization_iff.{u_1, u_2, u_3} {A : Type u_1} {B : Type u_2}
  {ι : Type u_3} [CommRing A] [CommRing B] [Algebra A B] [Fintype ι] [DecidableEq ι]
  (b : Module.Basis ι A B) (p : Ideal A) [p.IsPrime] :
  IsUnit ((algebraMap A (Localization.AtPrime p)) (Algebra.discr A ⇑b)) ↔
    Algebra.Etale (Localization.AtPrime p) (TensorProduct A (Localization.AtPrime p) B)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The discriminant criterion](the-discriminant-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.isUnit_discr_localization_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.isUnit_discr_localization_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.isUnit_discr_localization_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.isUnit_discr_localization_iff)
- [Source of `TauCeti.Algebra.isUnit_discr_localization_iff` in TauCeti/RingTheory/Etale/Discriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Etale/Discriminant.lean#L140)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalPurity/STATUS.md)
