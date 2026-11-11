---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished
statement: formalized
proof: formalized
---

# Weierstrass preparation in several variables over a Banach ring, in its unique-existence form

over a complete ultrametric normed commutative ring, if the iterated series of `g` in the
separated variable `X none` is multiplicatively distinguished of degree `s` at the radius
`c none`, then `g` is in exactly one way a multiplicative unit of the ring of restricted series at
`c` times a polynomial in `X none`, with coefficients restricted in the remaining variables, monic
of degree `s` and of Gauss norm `c none ^ s`.

```lean
TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished.{u_1,
    u_2}
  {σ : Type u_1} {R : Type u_2} [NormedCommRing R] [IsUltrametricDist R] {c : Option σ → ℝ}
  [∀ (i : Option σ), Fact (0 < c i)] {s : ℕ} [CompleteSpace R]
  {g : ↥(MvPowerSeries.IsRestricted.subring c)}
  (hg :
    TauCeti.PowerSeries.IsMulDistinguished (c none) s ↑(MvPowerSeries.restrictedOptionEquiv g)) :
  ∃! p,
    TauCeti.IsNormMulUnit p.1 ∧
      p.2.IsMonicOfDegree s ∧
        ‖MvPowerSeries.restrictedOptionEquiv.symm
                ((TauCeti.PowerSeries.polynomialToRestricted (c none)) p.2)‖ =
            c none ^ s ∧
          p.1 *
              MvPowerSeries.restrictedOptionEquiv.symm
                ((TauCeti.PowerSeries.polynomialToRestricted (c none)) p.2) =
            g
```

## Depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.MvPowerSeries.IsRestrictedFamily](tauceti-mvpowerseries-isrestrictedfamily.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Preparation.html#TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Preparation.html#TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished)
- [Source of `TauCeti.MvPowerSeries.existsUnique_isNormMulUnit_isMonicOfDegree_mul_eq_of_isMulDistinguished` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Preparation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Preparation.lean#L133)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
