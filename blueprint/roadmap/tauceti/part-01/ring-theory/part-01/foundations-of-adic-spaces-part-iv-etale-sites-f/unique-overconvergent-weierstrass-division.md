---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished
statement: formalized
proof: formalized
---

# Unique overconvergent Weierstrass division

**Unique overconvergent Weierstrass division**, with the quotient and polynomial remainder
bundled as a unique pair. No characteristic or nontrivial-norm assumption is required.

```lean
TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished.{u_1, u_2} {σ : Type u_1} {K : Type u_2}
  [NormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {g : ↥(TauCeti.Dagger.washnitzerAlgebra (Option σ) K)} {s : ℕ}
  (hg :
    TauCeti.PowerSeries.IsDistinguished 1 s
      ↑(MvPowerSeries.restrictedOptionEquiv
          ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g)))
  (hu :
    IsUnit
      ((PowerSeries.coeff s)
        ↑(MvPowerSeries.restrictedOptionEquiv
            ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g))))
  (f : ↥(TauCeti.Dagger.washnitzerAlgebra (Option σ) K)) :
  ∃! p,
    p.2.degree < ↑s ∧
      TauCeti.Dagger.washnitzerAlgebra.optionSeries p.1 *
            TauCeti.Dagger.washnitzerAlgebra.optionSeries g +
          ↑p.2 =
        TauCeti.Dagger.washnitzerAlgebra.optionSeries f
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

Formalized in Tau Ceti as [`TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Weierstrass.html#TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Weierstrass.html#TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished)
- [Source of `TauCeti.Dagger.existsUnique_mul_add_eq_of_isDistinguished` in TauCeti/RingTheory/Dagger/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/Weierstrass.lean#L282)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
