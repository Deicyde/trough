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
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [Weierstrass preparation](../power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/UniqueFactorization.html#TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/UniqueFactorization.html#TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.uniqueFactorizationMonoid` in TauCeti/RingTheory/Dagger/UniqueFactorization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/UniqueFactorization.lean#L93)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
