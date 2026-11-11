---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain
statement: formalized
proof: formalized
---

# Heights of maximal ideals of affinoid domains

Every maximal ideal of an affinoid domain
`A` has height `dim A`.

```lean
TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain.{u_1, u_2} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A] [Algebra K A]
  [IsDomain A] (hA : TauCeti.IsAffinoidAlgebra K A) (m : Ideal A) [m.IsMaximal] :
  ↑m.height = ringKrullDim A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/part-01/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/KrullDimension.html#TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain)
- [Source of `TauCeti.IsAffinoidAlgebra.height_eq_ringKrullDim_of_isDomain` in TauCeti/RingTheory/Affinoid/KrullDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/KrullDimension.lean#L96)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
