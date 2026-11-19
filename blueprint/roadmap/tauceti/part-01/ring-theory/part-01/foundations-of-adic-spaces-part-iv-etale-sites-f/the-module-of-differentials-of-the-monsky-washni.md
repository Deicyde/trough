---
declaration: def
origin: cited
lean: TauCeti.Dagger.Omega.washnitzerBasis
statement: formalized
---

# The module of differentials of the Monsky–Washnitzer algebra is free on the differentials `dX₁, …, dXₙ` of the variables

```lean
TauCeti.Dagger.Omega.washnitzerBasis.{u_1, u_2} (σ : Type u_1) (K : Type u_2) [Finite σ]
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] :
  Module.Basis σ (↥(TauCeti.Dagger.washnitzerAlgebra σ K))
    (TauCeti.Dagger.Omega K ↥(TauCeti.Dagger.washnitzerAlgebra σ K))
```

## Depends on

- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [TauCeti.Dagger.Omega](tauceti-dagger-omega.md)

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.Omega.washnitzerBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Omega/Basic.html#TauCeti.Dagger.Omega.washnitzerBasis).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.Omega.washnitzerBasis`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Omega/Basic.html#TauCeti.Dagger.Omega.washnitzerBasis)
- [Source of `TauCeti.Dagger.Omega.washnitzerBasis` in TauCeti/RingTheory/Dagger/Omega/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/Omega/Basic.lean#L222)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
