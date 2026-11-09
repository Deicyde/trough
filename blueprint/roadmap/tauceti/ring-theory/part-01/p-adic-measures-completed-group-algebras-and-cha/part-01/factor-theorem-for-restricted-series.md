---
declaration: theorem
origin: cited
lean: PowerSeries.IsRestricted.evalAt_eq_zero_iff
statement: formalized
proof: formalized
---

# Factor theorem for restricted series

Over a complete ultrametric normed commutative ring,
a series restricted at a radius `c > 0` vanishes at a point `a` of the closed disc of radius `c`
exactly when it is `X - a` times a series restricted at `c`.

```lean
PowerSeries.IsRestricted.evalAt_eq_zero_iff.{u_1} {R : Type u_1} [NormedCommRing R] [NormOneClass R]
  [IsUltrametricDist R] [CompleteSpace R] {c : ℝ} {f : PowerSeries R}
  (hf : PowerSeries.IsRestricted c f) (hc : 0 < c) {a : R} (ha : ‖a‖ ≤ c) :
  f.evalAt a = 0 ↔ ∃ q, PowerSeries.IsRestricted c q ∧ f = (PowerSeries.X - PowerSeries.C a) * q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`PowerSeries.IsRestricted.evalAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.evalAt_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `PowerSeries.IsRestricted.evalAt_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.html#PowerSeries.IsRestricted.evalAt_eq_zero_iff)
- [Source of `PowerSeries.IsRestricted.evalAt_eq_zero_iff` in TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Schwarz.lean#L72)
