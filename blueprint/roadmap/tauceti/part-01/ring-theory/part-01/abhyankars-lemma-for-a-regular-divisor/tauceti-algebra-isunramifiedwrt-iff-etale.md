---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.isUnramifiedWRT_iff_etale
statement: formalized
proof: formalized
---

# TauCeti.Algebra.isUnramifiedWRT_iff_etale

A finite separable extension `L` of the fraction field of a discrete valuation ring `A` is
unramified with respect to `A` iff the integral closure of `A` in `L` is étale over `A`.

```lean
TauCeti.Algebra.isUnramifiedWRT_iff_etale.{u_1, u_2, u_3} (A : Type u_1) (K : Type u_2)
  (L : Type u_3) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A] [Field K] [Algebra A K]
  [IsFractionRing A K] [Field L] [Algebra A L] [Algebra K L] [IsScalarTower A K L]
  [FiniteDimensional K L] [Algebra.IsSeparable K L] :
  TauCeti.Algebra.IsUnramifiedWRT A L ↔ Algebra.Etale A ↥(integralClosure A L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.isUnramifiedWRT_iff_etale`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.html#TauCeti.Algebra.isUnramifiedWRT_iff_etale).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.isUnramifiedWRT_iff_etale`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.html#TauCeti.Algebra.isUnramifiedWRT_iff_etale)
- [Source of `TauCeti.Algebra.isUnramifiedWRT_iff_etale` in TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.lean#L279)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
