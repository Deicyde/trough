---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq
statement: formalized
proof: formalized
---

# TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq

Unique multivariable Weierstrass preparation in the Monsky–Washnitzer algebra.
The series is distinguished of degree `s` at unit radius in the separated variable,
with unit coefficient in degree `s`.
Both the unit and every coefficient of the monic polynomial are overconvergent.

```lean
TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq.{u_1, u_2}
  {σ : Type u_1} {K : Type u_2} [NormedField K] [IsUltrametricDist K] [CompleteSpace K]
  {g : ↥(TauCeti.Dagger.washnitzerAlgebra (Option σ) K)} {s : ℕ}
  (hg :
    TauCeti.PowerSeries.IsDistinguished 1 s
      ↑(MvPowerSeries.restrictedOptionEquiv
          ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g)))
  (hu :
    IsUnit
      ((PowerSeries.coeff s)
        ↑(MvPowerSeries.restrictedOptionEquiv
            ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g)))) :
  ∃! p,
    IsUnit p.1 ∧
      p.2.IsMonicOfDegree s ∧
        ↑(MvPowerSeries.restrictedOptionEquiv
                ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) p.1)) *
            ↑(Polynomial.map (TauCeti.Dagger.washnitzerAlgebra.toTate σ K).toRingHom p.2) =
          ↑(MvPowerSeries.restrictedOptionEquiv
              ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K) g))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [Weierstrass preparation](../power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Preparation.html#TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Preparation.html#TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq` in TauCeti/RingTheory/Dagger/Preparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/Preparation.lean#L198)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
