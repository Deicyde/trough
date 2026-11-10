---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished
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

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.html#TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished).

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.html#TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished)
- [Source of `TauCeti.MvPowerSeries.norm_mul_add_eq_max_of_isMulDistinguished` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Weierstrass/Division.lean#L87)
