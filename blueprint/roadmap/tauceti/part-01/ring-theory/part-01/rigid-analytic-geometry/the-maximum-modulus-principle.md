---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm
statement: formalized
proof: formalized
---

# The maximum modulus principle

On a nonzero affinoid algebra the supremum seminorm is
attained at a classical point: for every `f : A` there is a maximal ideal `x` of `A` with
`|f(x)| = |f|sup`.

```lean
TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A]
  [Algebra K A] [Nontrivial A] (hA : TauCeti.IsAffinoidAlgebra K A) (f : A) :
  ∃ x, TauCeti.pointNorm K x f = TauCeti.supSeminorm K f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Maximum modulus principle for Tate algebras](../restricted-power-series-and-tate-algebras/maximum-modulus-principle-for-tate-algebras.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L157)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
