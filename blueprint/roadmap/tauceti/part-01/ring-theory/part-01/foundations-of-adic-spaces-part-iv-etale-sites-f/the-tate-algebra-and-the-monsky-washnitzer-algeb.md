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

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/MaximalSpectrum.html#TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/MaximalSpectrum.html#TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.maximalSpectrumComap_toTate_bijective` in TauCeti/RingTheory/Dagger/MaximalSpectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/MaximalSpectrum.lean#L131)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
