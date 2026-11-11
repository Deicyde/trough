---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.uniqueFactorizationMonoid
statement: formalized
proof: formalized
---

# Tate algebras are unique factorisation domains

Over a complete nonarchimedean field `K`,
the Tate algebra `K⟨X₁, …, Xₙ⟩` in finitely many variables is a unique factorisation domain.

```lean
TauCeti.MvPowerSeries.uniqueFactorizationMonoid.{u_1, u_2} {K : Type u_1} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {σ : Type u_2} [Finite σ] :
  UniqueFactorizationMonoid ↥(MvPowerSeries.IsRestricted.subring fun x => 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)
- [Weierstrass preparation](../../power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.html#TauCeti.MvPowerSeries.uniqueFactorizationMonoid).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.html#TauCeti.MvPowerSeries.uniqueFactorizationMonoid)
- [Source of `TauCeti.MvPowerSeries.uniqueFactorizationMonoid` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.lean#L54)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
