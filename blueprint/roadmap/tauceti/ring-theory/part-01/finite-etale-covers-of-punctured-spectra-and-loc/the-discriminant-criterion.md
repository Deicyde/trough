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

## Proof depends on

- [TauCeti.Algebra.etale_iff_traceForm_nondegenerate](tauceti-algebra-etale-iff-traceform-nondegenerat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_iff_isUnit_discr`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_isUnit_discr).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_iff_isUnit_discr`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Discriminant.html#TauCeti.Algebra.etale_iff_isUnit_discr)
- [Source of `TauCeti.Algebra.etale_iff_isUnit_discr` in TauCeti/RingTheory/Etale/Discriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Etale/Discriminant.lean#L116)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/LocalPurity/STATUS.md)
