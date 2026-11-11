---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard
statement: formalized
proof: formalized
---

# Krull dimension of the Monsky–Washnitzer algebra

The overconvergent algebra over a
complete ultrametric normed field has dimension equal to its number of variables.

```lean
TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard.{u_1, u_2} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {σ : Type u_2} [Finite σ] :
  ringKrullDim ↥(TauCeti.Dagger.washnitzerAlgebra σ K) = ↑(Nat.card σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/KrullDimension.html#TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/KrullDimension.html#TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.ringKrullDim_eq_natCard` in TauCeti/RingTheory/Dagger/KrullDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/KrullDimension.lean#L97)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
