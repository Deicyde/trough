---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one
statement: formalized
proof: formalized
---

# Power-bounded elements of an affinoid algebra

For every complete ultrametric algebra
norm on an affinoid algebra, an element is power-bounded if and only if its supremum seminorm is
at most one.

```lean
TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A]
  (hA : TauCeti.IsAffinoidAlgebra K A) {f : A} :
  TauCeti.Huber.IsPowerBounded f ↔ TauCeti.supSeminorm K f ≤ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

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

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/PowerBounded.html#TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/PowerBounded.html#TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one)
- [Source of `TauCeti.IsAffinoidAlgebra.isPowerBounded_iff_supSeminorm_le_one` in TauCeti/RingTheory/Affinoid/PowerBounded.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/PowerBounded.lean#L166)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
