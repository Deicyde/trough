---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm
statement: formalized
proof: formalized
---

# The spectral-radius formula

For every complete ultrametric algebra norm on an affinoid
algebra, `‖f ^ n‖ ^ (1 / n)` tends to the supremum seminorm `|f|sup`.

```lean
TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2}
  [NormedCommRing A] [NormedAlgebra K A] [IsUltrametricDist A] [CompleteSpace A]
  (hA : TauCeti.IsAffinoidAlgebra K A) (f : A) :
  Filter.Tendsto (fun n => ‖f ^ n‖ ^ (1 / ↑n)) Filter.atTop (nhds (TauCeti.supSeminorm K f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Power-bounded elements of an affinoid algebra](power-bounded-elements-of-an-affinoid-algebra.md)
- [TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm](tauceti-isaffinoidalgebra-exists-supseminorm-pow.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/SpectralRadius.html#TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/SpectralRadius.html#TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm)
- [Source of `TauCeti.IsAffinoidAlgebra.pow_norm_pow_one_div_tendsto_nhds_supSeminorm` in TauCeti/RingTheory/Affinoid/SpectralRadius.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/SpectralRadius.lean#L105)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
