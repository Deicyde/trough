---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow
statement: formalized
proof: formalized
---

# The supremum seminorm is the spectral value of the minimal polynomial

Let `B` be an
affinoid algebra which is integral and torsion-free over an integrally closed domain `A`. For
`f : B` with minimal polynomial `X ^ d + ∑_{i < d} aᵢ X ^ i` over `A`,
`|f|sup = max_{i < d} |aᵢ|sup ^ (1 / (d - i))`.

```lean
TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow.{u_1, u_2, u_3} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A]
  [Algebra K A] {B : Type u_3} [CommRing B] [Algebra K B] [Algebra A B] [IsScalarTower K A B]
  (hB : TauCeti.IsAffinoidAlgebra K B) [IsDomain A] [IsIntegrallyClosed A]
  [Module.IsTorsionFree A B] [Algebra.IsIntegral A B] (f : B) :
  TauCeti.supSeminorm K f =
    ⨆ i, TauCeti.supSeminorm K ((minpoly A f).coeff ↑i) ^ (1 / (↑(minpoly A f).natDegree - ↑↑i))
```

## Depends on

- [TauCeti.supSeminorm](tauceti-supseminorm.md)

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MinimalPolynomial.html#TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MinimalPolynomial.html#TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow)
- [Source of `TauCeti.IsAffinoidAlgebra.supSeminorm_eq_iSup_minpoly_coeff_rpow` in TauCeti/RingTheory/Affinoid/MinimalPolynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/MinimalPolynomial.lean#L200)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
