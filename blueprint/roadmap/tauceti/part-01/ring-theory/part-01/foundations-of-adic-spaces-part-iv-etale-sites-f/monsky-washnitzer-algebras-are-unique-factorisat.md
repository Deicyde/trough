---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid
statement: formalized
proof: formalized
---

# Monsky–Washnitzer algebras are unique factorisation domains

Over a complete ultrametric
normed field `K`, the algebra `K⟨X⟩†` of overconvergent power series in finitely many variables
is a unique factorisation domain.

```lean
TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid.{u_1, u_2} {σ : Type u_1} {K : Type u_2}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite σ] :
  UniqueFactorizationMonoid ↥(TauCeti.Dagger.washnitzerAlgebra σ K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [Weierstrass preparation](../../part-02/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/UniqueFactorization.html#TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/UniqueFactorization.html#TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid` in TauCeti/RingTheory/Dagger/UniqueFactorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/UniqueFactorization.lean#L81)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
