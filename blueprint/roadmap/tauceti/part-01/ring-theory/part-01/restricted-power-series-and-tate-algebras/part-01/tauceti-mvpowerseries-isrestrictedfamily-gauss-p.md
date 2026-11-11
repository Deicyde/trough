---
declaration: def
origin: cited
lean: TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv
statement: formalized
---

# TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv

Restricted series with finite free coefficients identify isometrically with a finite free
module over the scalar restricted-series ring.

```lean
TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv.{u_1, u_2, u_3}
  {σ : Type u_1} {ι : Type u_2} (R : Type u_3) [Fintype ι] (c : σ → ℝ) [∀ (i : σ), Fact (0 < c i)]
  [NormedRing R] [IsUltrametricDist R] :
  TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss c
      (ι → R) ≃ₗᵢ[↥(MvPowerSeries.IsRestricted.subring c)]
    ι → ↥(MvPowerSeries.IsRestricted.subring c)
```

## Depends on

- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Pi/Norm.html#TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Pi/Norm.html#TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv)
- [Source of `TauCeti.MvPowerSeries.IsRestrictedFamily.Gauss.piRingLinearIsometryEquiv` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Pi/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Module/Pi/Norm.lean#L169)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
