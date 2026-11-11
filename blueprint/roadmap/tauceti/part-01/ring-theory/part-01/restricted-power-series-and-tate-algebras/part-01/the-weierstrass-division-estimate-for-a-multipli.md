---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max, TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max
statement: formalized
proof: formalized
---

# The Weierstrass division estimate for a multiplicatively distinguished divisor

Over an
ultrametric normed commutative ring, if `g` is multiplicatively distinguished of degree `s` at the
radius `c`, `q` is restricted, and `r` vanishes in every degree `≥ s`, then

```text
‖g * q + r‖ = max (‖g‖ * ‖q‖) ‖r‖
```

for the Gauss norm at `c`. The norm of the coefficient ring need not be multiplicative. In a
Weierstrass division `f = g * q + r` it bounds the quotient by `‖f‖ / ‖g‖` and the remainder by
`‖f‖`.

```lean
TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ} {g q r : PowerSeries R}
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s g) (hc : 0 < c)
  (hq : PowerSeries.IsRestricted c q) (hr : ∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) r = 0) :
  PowerSeries.gaussNorm norm c (g * q + r) =
    max (PowerSeries.gaussNorm norm c g * PowerSeries.gaussNorm norm c q)
      (PowerSeries.gaussNorm norm c r)
```

## Depends on

- [TauCeti.PowerSeries.IsMulDistinguished](tauceti-powerseries-ismuldistinguished.md)

## Proof depends on

- [TauCeti.IsNormMulUnit](tauceti-isnormmulunit.md)
- [The Weierstrass lower bound for the quotient](../part-02/the-weierstrass-lower-bound-for-the-quotient.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max).

## Other forms

**The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2).** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max).

```lean
TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max.{u_1} {R : Type u_1} [NormedRing R]
  {c : ℝ} {s : ℕ} {f q r : PowerSeries R} [IsUltrametricDist R]
  (hf : TauCeti.PowerSeries.IsDistinguished c s f) (hc : 0 < c)
  (hmul : ∀ (x : R), ‖x * (PowerSeries.coeff s) f‖ = ‖x‖ * ‖(PowerSeries.coeff s) f‖)
  (hq : PowerSeries.IsRestricted c q) (hr : ∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) r = 0) :
  PowerSeries.gaussNorm norm c (q * f + r) =
    max (PowerSeries.gaussNorm norm c q * PowerSeries.gaussNorm norm c f)
      (PowerSeries.gaussNorm norm c r)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max)
- [Source of `TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max` in TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean#L228)
- [Tau Ceti roadmap status: Restricted power series and Tate algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RestrictedPowerSeries/STATUS.md)
