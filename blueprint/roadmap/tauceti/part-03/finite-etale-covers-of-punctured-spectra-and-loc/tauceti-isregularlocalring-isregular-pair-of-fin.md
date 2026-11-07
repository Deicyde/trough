---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal
statement: formalized
proof: formalized
---

# TauCeti.IsRegularLocalRing.isRegular\_pair\_of\_finite\_normal

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
- [Source of `TauCeti.IsRegularLocalRing.isRegular_pair_of_finite_normal` in TauCeti/RingTheory/RegularLocalRing/FiniteNormal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RegularLocalRing/FiniteNormal.lean#L48)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/LocalPurity/STATUS.md)
