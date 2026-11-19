---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_iff_isUnit_discr
statement: formalized
proof: formalized
---

# The discriminant criterion

A finite free algebra is étale iff the discriminant of a basis
is a unit. Stacks, Lemma 49.3.1 (0BJF), affine form.

```lean
TauCeti.Algebra.etale_iff_isUnit_discr.{u_1, u_2, u_3} {A : Type u_1} {B : Type u_2} {ι : Type u_3}
  [CommRing A] [CommRing B] [Algebra A B] [Fintype ι] [DecidableEq ι] (b : Module.Basis ι A B) :
  Algebra.Etale A B ↔ IsUnit (Algebra.discr A ⇑b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_iff_isUnit_discr`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_isUnit_discr).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_iff_isUnit_discr`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_isUnit_discr)
- [Source of `TauCeti.Algebra.etale_iff_isUnit_discr` in TauCeti/RingTheory/Etale/Discriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Etale/Discriminant.lean#L117)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
