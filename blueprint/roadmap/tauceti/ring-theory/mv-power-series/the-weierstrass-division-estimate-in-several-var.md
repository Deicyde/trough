---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished, TauCeti.PowerSeries.IsDistinguished.gaussNorm_mul_add_eq_max, TauCeti.PowerSeries.IsMulDistinguished.gaussNorm_mul_add_eq_max
statement: formalized
proof: formalized
---

# The Weierstrass division estimate in several variables

Over an ultrametric normed
commutative ring, let the iterated series of `g` in the separated variable `X none` be
multiplicatively distinguished of degree `s`. If `r` has degree less than `s` in `X none`, then

```text
‖g * q + r‖ = max (‖g‖ * ‖q‖) ‖r‖
```

for the Gauss norms at the polyradii `c`. The norm of the coefficient ring need not be
multiplicative.

```lean
TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished.{u_1, u_2} {σ : Type u_1}
  {R : Type u_2} [NormedCommRing R] [IsUltrametricDist R] {c : Option σ → ℝ}
  [∀ (i : Option σ), Fact (0 < c i)] {s : ℕ} {g : ↥(MvPowerSeries.IsRestricted.subring c)}
  (hg : TauCeti.PowerSeries.IsMulDistinguished (c none) s ↑(MvPowerSeries.restrictedOptionEquiv g))
  (q : ↥(MvPowerSeries.IsRestricted.subring c)) {r : ↥(MvPowerSeries.IsRestricted.subring c)}
  (hr : ∀ (t : Option σ →₀ ℕ), s ≤ t none → (MvPowerSeries.coeff t) ↑r = 0) :
  ‖g * q + r‖ = max (‖g‖ * ‖q‖) ‖r‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass lower bound for the quotient](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-lower-bound-for-the-quotient.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.html#TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished).

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

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.html#TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished)
- [Source of `TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.lean#L87)
