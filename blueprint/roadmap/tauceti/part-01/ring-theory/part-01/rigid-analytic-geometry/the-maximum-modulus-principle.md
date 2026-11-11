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

- [TauCeti.supSeminorm](tauceti-supseminorm.md)

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Maximum modulus principle for Tate algebras](../restricted-power-series-and-tate-algebras/part-01/maximum-modulus-principle-for-tate-algebras.md)
- [The supremum seminorm is the spectral value of the minimal polynomial](the-supremum-seminorm-is-the-spectral-value-of-t.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/part-01/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.MvPowerSeries.supSeminorm_eq_norm](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-supseminorm-eq-norm.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/MaximumModulus.html#TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_pointNorm_eq_supSeminorm` in TauCeti/RingTheory/Affinoid/MaximumModulus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Affinoid/MaximumModulus.lean#L153)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
