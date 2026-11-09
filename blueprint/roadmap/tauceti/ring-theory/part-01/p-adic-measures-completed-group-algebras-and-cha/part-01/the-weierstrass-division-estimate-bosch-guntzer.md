---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max, TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max
statement: formalized
proof: formalized
---

# The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)

If `f` is
distinguished of degree `s` at the radius `c`, right multiplication by its coefficient in degree
`s` scales norms exactly, `q` is restricted, and `r` vanishes in every degree `≥ s`, then

```text
‖q * f + r‖ = max (‖q‖ * ‖f‖) ‖r‖
```

for the Gauss norm at `c`. No cancellation occurs in a Weierstrass decomposition. The norm
condition on the distinguished coefficient holds whenever the norm of the coefficient ring is
multiplicative.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass lower bound for the quotient](the-weierstrass-lower-bound-for-the-quotient.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max).

## Other forms

**The Weierstrass division estimate for a multiplicatively distinguished divisor.** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max).

```lean
TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] {c : ℝ} {s : ℕ} {g q r : PowerSeries R}
  (hg : TauCeti.PowerSeries.IsMulDistinguished c s g) (hc : 0 < c)
  (hq : PowerSeries.IsRestricted c q) (hr : ∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) r = 0) :
  PowerSeries.gaussNorm norm c (g * q + r) =
    max (PowerSeries.gaussNorm norm c g * PowerSeries.gaussNorm norm c q)
      (PowerSeries.gaussNorm norm c r)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max)
- [Source of `TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max` in TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean#L161)
