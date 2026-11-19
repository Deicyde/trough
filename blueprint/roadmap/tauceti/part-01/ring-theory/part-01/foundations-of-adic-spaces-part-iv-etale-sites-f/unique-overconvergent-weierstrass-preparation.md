---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq
statement: formalized
proof: formalized
---

# Unique overconvergent Weierstrass preparation

An overconvergent series `g` distinguished
of degree `s` at unit radius in the separated variable, with unit coefficient in degree `s`, is
uniquely `e * ω(Y)` with `e` a unit of `K⟨X, Y⟩†` and `ω` a monic polynomial of degree `s` over
`K⟨X⟩†`. Existence is `exists_isUnit_isMonicOfDegree_mul_eq` and uniqueness is
`eq_and_eq_of_isUnit_isMonicOfDegree_mul_eq`.

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
      p.2.IsMonicOfDegree s ∧ p.1 * TauCeti.Dagger.washnitzerAlgebra.polynomialToOption p.2 = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [Weierstrass preparation](../../part-02/power-series/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Preparation.html#TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Preparation.html#TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.existsUnique_isUnit_isMonicOfDegree_mul_eq` in TauCeti/RingTheory/Dagger/Preparation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/Preparation.lean#L212)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
