---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective
statement: formalized
proof: formalized
---

# The Tate algebra and the Monsky–Washnitzer algebra have the same classical points

contraction of maximal ideals along `W → T` is a bijection of maximal spectra.

```lean
TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective.{u_1, u_2} {K : Type u_1}
  {σ : Type u_2} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite σ] :
  Function.Bijective (⋯.maximalSpectrumComap (TauCeti.Dagger.washnitzerAlgebra.toTate σ K))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/MaximalSpectrum.html#TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/MaximalSpectrum.html#TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective` in TauCeti/RingTheory/Dagger/MaximalSpectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/MaximalSpectrum.lean#L131)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
