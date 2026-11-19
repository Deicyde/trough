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

- [Rückert's factorial descent](ruckerts-factorial-descent.md)
- [Tate algebras satisfy the Rückert hypotheses](tate-algebras-satisfy-the-ruckert-hypotheses.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.html#TauCeti.MvPowerSeries.uniqueFactorizationMonoid).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.uniqueFactorizationMonoid`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.html#TauCeti.MvPowerSeries.uniqueFactorizationMonoid)
- [Source of `TauCeti.MvPowerSeries.uniqueFactorizationMonoid` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/UniqueFactorization.lean#L56)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
