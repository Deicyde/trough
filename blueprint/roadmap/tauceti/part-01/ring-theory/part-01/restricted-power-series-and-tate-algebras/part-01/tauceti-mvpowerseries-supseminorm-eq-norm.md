---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.supSeminorm_eq_norm
statement: formalized
proof: formalized
---

# TauCeti.MvPowerSeries.supSeminorm_eq_norm

On a Tate algebra the supremum seminorm is the Gauss norm: `|f|sup = ‖f‖`.

```lean
TauCeti.MvPowerSeries.supSeminorm_eq_norm.{u_1} {K : Type u_1} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {n : ℕ}
  (f : ↥(MvPowerSeries.IsRestricted.subring fun x => 1)) : TauCeti.supSeminorm K f = ‖f‖
```

## Depends on

- [TauCeti.supSeminorm](../../rigid-analytic-geometry/tauceti-supseminorm.md)

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Maximum modulus principle for Tate algebras](maximum-modulus-principle-for-tate-algebras.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](../../rigid-analytic-geometry/tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.supSeminorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.supSeminorm_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.supSeminorm_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.MvPowerSeries.supSeminorm_eq_norm)
- [Source of `TauCeti.MvPowerSeries.supSeminorm_eq_norm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L112)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
