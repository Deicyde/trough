---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal
statement: formalized
proof: formalized
---

# TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal

Over a two-dimensional regular local ring, every pair generating the maximal ideal is
regular on any finite injective normal local algebra, considered as a module over the base.

```lean
TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal.{u_1, u_2} {A : Type u_1} {B : Type u_2}
  [CommRing A] [CommRing B] [Algebra A B] [IsRegularLocalRing A] [IsLocalRing B] [IsDomain B]
  [IsIntegrallyClosed B] [Module.Finite A B] [IsLocalHom (algebraMap A B)]
  (hinj : Function.Injective ⇑(algebraMap A B)) (hdim : ringKrullDim A = 2) {x y : A}
  (hxy : Ideal.span {x, y} = IsLocalRing.maximalIdeal A) : RingTheory.Sequence.IsRegular B [x, y]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/FiniteNormal.html#TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/FiniteNormal.html#TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal)
- [Source of `TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal` in TauCeti/RingTheory/RegularLocalRing/FiniteNormal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/FiniteNormal.lean#L48)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalPurity/STATUS.md)
