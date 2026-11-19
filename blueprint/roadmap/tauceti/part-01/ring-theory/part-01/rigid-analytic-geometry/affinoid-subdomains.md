---
declaration: structure
origin: cited
lean: TauCeti.IsAffinoidSubdomainMap
statement: formalized
---

# Affinoid subdomains

The `K`-algebra map `φ : A → B` represents the set `U` of classical
points of `A` as an affinoid subdomain: `B` is affinoid, every classical point of `B` lies over a
point of `U`, and every `K`-algebra map `ψ : A → C` into an affinoid algebra whose classical points
all lie over `U` factors uniquely through `φ`. The test algebras `C` carry no chosen norm and range
over the universe of `A` and `B`.

```lean
TauCeti.IsAffinoidSubdomainMap.{u, u_1} {K : Type u_1} [NormedField K] [IsUltrametricDist K]
  [CompleteSpace K] {A B : Type u} [CommRing A] [Algebra K A] [CommRing B] [Algebra K B]
  (φ : A →ₐ[K] B) (U : Set (MaximalSpectrum A)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidSubdomainMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Subdomain/Basic.html#TauCeti.IsAffinoidSubdomainMap).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidSubdomainMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Subdomain/Basic.html#TauCeti.IsAffinoidSubdomainMap)
- [Source of `TauCeti.IsAffinoidSubdomainMap` in TauCeti/RingTheory/Affinoid/Subdomain/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/Subdomain/Basic.lean#L65)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
