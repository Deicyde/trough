---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing
statement: formalized
proof: formalized
---

# Monsky–Washnitzer algebras are noetherian

Over a complete ultrametric normed field `K`,
the algebra `K⟨X⟩†` of overconvergent power series in finitely many variables is a noetherian
ring. No characteristic or nontrivial-norm assumption is needed.

```lean
TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing.{u_1, u_2} {σ : Type u_1} {K : Type u_2}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite σ] :
  IsNoetherianRing ↥(TauCeti.Dagger.washnitzerAlgebra σ K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Noetherian.html#TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Noetherian.html#TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.isNoetherianRing` in TauCeti/RingTheory/Dagger/Noetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/Noetherian.lean#L179)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
