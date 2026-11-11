---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq
statement: formalized
proof: formalized
---

# Weierstrass division over a Banach ring (Martin, Proposition 1.27), in its unique-existence form

over a complete ultrametric normed commutative ring, a restricted series
`g` multiplicatively distinguished of degree `s` at a positive radius divides every restricted
series `f` in exactly one way, with a restricted quotient and a remainder that is a polynomial
of degree less than `s`.

```lean
TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ} {f g : PowerSeries R} [CompleteSpace R]
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s g) (hc : 0 < c)
  (hgr : PowerSeries.IsRestricted c g) (hf : PowerSeries.IsRestricted c f) :
  ∃! p,
    PowerSeries.IsRestricted c p.1 ∧
      (∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) p.2 = 0) ∧ g * p.1 + p.2 = f
```

## Depends on

- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](the-weierstrass-division-estimate-for-a-multipli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.existsUnique_mul_add_eq` in TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean#L522)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
