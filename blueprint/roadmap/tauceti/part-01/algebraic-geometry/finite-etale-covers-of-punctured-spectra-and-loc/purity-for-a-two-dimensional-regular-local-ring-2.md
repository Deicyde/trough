---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two
statement: formalized
proof: formalized
---

# Purity for a two-dimensional regular local ring (`TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two`)

A finite torsion-free algebra over a
two-dimensional regular local ring whose localizations at maximal ideals are normal domains is
étale, provided it is unramified at every prime not lying over the closed point.

```lean
TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two.{u_1, u_2} {A : Type u_1}
  {B : Type u_2} [CommRing A] [CommRing B] [Algebra A B] [IsRegularLocalRing A] [Module.Finite A B]
  [Module.IsTorsionFree A B] (hdim : ringKrullDim A = 2)
  (hnormal :
    ∀ (𝔮 : Ideal B) [inst : 𝔮.IsMaximal],
      IsDomain (Localization.AtPrime 𝔮) ∧ IsIntegrallyClosed (Localization.AtPrime 𝔮))
  (hunram :
    ∀ (q : Ideal B) [inst : q.IsPrime],
      Ideal.under A q ≠ IsLocalRing.maximalIdeal A → Algebra.IsUnramifiedAt A q) :
  Algebra.Etale A B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The discriminant criterion](the-discriminant-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Purity.html#TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Purity.html#TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two)
- [Source of `TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two` in TauCeti/RingTheory/RegularLocalRing/Purity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/RegularLocalRing/Purity.lean#L71)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
