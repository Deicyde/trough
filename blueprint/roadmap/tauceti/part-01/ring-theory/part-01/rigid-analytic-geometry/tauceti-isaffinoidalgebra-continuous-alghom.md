---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.continuous_algHom
statement: formalized
proof: formalized
---

# TauCeti.IsAffinoidAlgebra.continuous_algHom

Every homomorphism from a noetherian ultrametric Banach algebra to a completely normed
affinoid algebra is continuous. The affinoid presentation is purely algebraic.

```lean
TauCeti.IsAffinoidAlgebra.continuous_algHom.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A]
  (hA : TauCeti.IsAffinoidAlgebra K A) {B : Type u_3} [NormedCommRing B] [NormedAlgebra K B]
  [IsUltrametricDist B] [CompleteSpace B] [IsNoetherianRing B] (f : B →ₐ[K] A) : Continuous ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.continuous_algHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Continuity.html#TauCeti.IsAffinoidAlgebra.continuous_algHom).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.continuous_algHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/Continuity.html#TauCeti.IsAffinoidAlgebra.continuous_algHom)
- [Source of `TauCeti.IsAffinoidAlgebra.continuous_algHom` in TauCeti/RingTheory/Affinoid/Continuity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/Continuity.lean#L51)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
