---
declaration: theorem
origin: cited
lean: Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion
statement: formalized
proof: formalized
---

# The Nullstellensatz for the completed Tate algebra

Over a complete nonarchimedean field
`K`, the residue field of every maximal ideal of `K⟨X₁, …, Xₙ⟩` is a finite extension of `K`.

```lean
Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion.{u_1} {K : Type u_1}
  [NormedField K] [IsUltrametricDist K] [NonarchimedeanRing K] [CompleteSpace K] {n : ℕ}
  (m : Ideal (TauCeti.Huber.restrictedMvPowerSeriesCompletion n K)) [m.IsMaximal] :
  Module.Finite K (TauCeti.Huber.restrictedMvPowerSeriesCompletion n K ⧸ m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Restricted/TateAlgebra.html#Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion).

## Sources

- [Tau Ceti documentation: `Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/Restricted/TateAlgebra.html#Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion)
- [Source of `Ideal.finite_quotient_of_isMaximal_restrictedMvPowerSeriesCompletion` in TauCeti/RingTheory/Huber/Restricted/TateAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/Restricted/TateAlgebra.lean#L125)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
