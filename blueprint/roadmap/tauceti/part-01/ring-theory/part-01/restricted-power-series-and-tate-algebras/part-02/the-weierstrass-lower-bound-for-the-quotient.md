---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add, TauCeti.PowerSeries.IsDistinguished.gaussNorm_le_gaussNorm_mul_add
statement: formalized
proof: formalized
---

# The Weierstrass lower bound for the quotient

In a decomposition `q * f + r` by a
distinguished series `f` of degree `s`, with `r` vanishing in every degree `≥ s`, the Gauss norm of
the sum is at least the product of the Gauss norms of `q` and `f`, provided right multiplication by
the coefficient of `f` in degree `s` scales norms exactly.

```lean
TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add.{u_1} {R : Type u_1} [NormedRing R] {c : ℝ}
  {s : ℕ} {f q r : PowerSeries R} [IsUltrametricDist R]
  (hf : TauCeti.PowerSeries.IsDistinguished c s f) (hc : 0 < c)
  (hmul : ∀ (x : R), ‖x * (PowerSeries.coeff s) f‖ = ‖x‖ * ‖(PowerSeries.coeff s) f‖)
  (hq : PowerSeries.IsRestricted c q) (hr : ∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) r = 0) :
  PowerSeries.gaussNorm norm c q * PowerSeries.gaussNorm norm c f ≤
    PowerSeries.gaussNorm norm c (q * f + r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add).

## Other forms

**The Weierstrass lower bound for the remainder.** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.gaussNorm_le_gaussNorm_mul_add`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.gaussNorm_le_gaussNorm_mul_add).

```lean
TauCeti.PowerSeries.IsDistinguished.gaussNorm_le_gaussNorm_mul_add.{u_1} {R : Type u_1}
  [NormedRing R] {c : ℝ} {s : ℕ} {f q r : PowerSeries R} [IsUltrametricDist R]
  (hf : TauCeti.PowerSeries.IsDistinguished c s f) (hc : 0 < c)
  (hmul : ∀ (x : R), ‖x * (PowerSeries.coeff s) f‖ = ‖x‖ * ‖(PowerSeries.coeff s) f‖)
  (hq : PowerSeries.IsRestricted c q) (hr : ∀ (m : ℕ), s ≤ m → (PowerSeries.coeff m) r = 0) :
  PowerSeries.gaussNorm norm c r ≤ PowerSeries.gaussNorm norm c (q * f + r)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.html#TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add)
- [Source of `TauCeti.PowerSeries.IsDistinguished.le_gaussNorm_mul_add` in TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Weierstrass/Division.lean#L109)
