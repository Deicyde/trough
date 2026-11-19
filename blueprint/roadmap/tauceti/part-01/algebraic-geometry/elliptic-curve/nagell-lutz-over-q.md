---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isInteger_or_order_two_of_torsion_rat, WeierstrassCurve.lutz_nagell, WeierstrassCurve.y_eq_zero_or_sq_dvd_Δ_of_torsion, WeierstrassCurve.isInteger_of_torsion
statement: formalized
proof: formalized
---

# Nagell–Lutz over `ℚ`

for an integral long Weierstrass
model, a nonzero torsion point has integral coordinates unless it has order exactly `2`, where the
honest bound is `4x, 8y ∈ ℤ`.

No squarefreeness hypothesis survives here. Over `ℤ` a rational prime **is** squarefree, so the
guard in the general statement discharges outright — which is why that statement carries the
hypothesis rather than a `CharZero`/unramified typeclass: the generality is free at `ℤ` and only
costs something over rings where a rational prime ramifies.

```lean
WeierstrassCurve.isInteger_or_order_two_of_torsion_rat {W : WeierstrassCurve ℤ} {x y : ℚ}
  (hns : (W.baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) :
  IsLocalization.IsInteger ℤ x ∧ IsLocalization.IsInteger ℤ y ∨
    addOrderOf (WeierstrassCurve.Affine.Point.some x y hns) = 2 ∧
      IsLocalization.IsInteger ℤ (4 * x) ∧ IsLocalization.IsInteger ℤ (8 * y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.isInteger_or_order_two_of_torsion_rat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/NagellLutz.html#WeierstrassCurve.isInteger_or_order_two_of_torsion_rat).

## Other forms

**The Nagell–Lutz theorem.** Formalized in Tau Ceti as [`WeierstrassCurve.lutz_nagell`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.lutz_nagell).

```lean
WeierstrassCurve.lutz_nagell (A B : ℤ) {x y : ℚ}
  (hns : ((WeierstrassCurve.shortCurve A B).baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) :
  ∃ x₀ y₀, ↑x₀ = x ∧ ↑y₀ = y ∧ (y₀ = 0 ∨ y₀ ^ 2 ∣ (WeierstrassCurve.shortCurve A B).Δ)
```

**Nagell–Lutz, discriminant half.** Formalized in Tau Ceti as [`WeierstrassCurve.y_eq_zero_or_sq_dvd_Δ_of_torsion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.y_eq_zero_or_sq_dvd_%CE%94_of_torsion).

```lean
WeierstrassCurve.y_eq_zero_or_sq_dvd_Δ_of_torsion {W : WeierstrassCurve ℤ} [W.IsCharNeTwoNF]
  {x y : ℚ} (hns : (W.baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) {x₀ y₀ : ℤ}
  (hx : (algebraMap ℤ ℚ) x₀ = x) (hy : (algebraMap ℤ ℚ) y₀ = y) : y₀ = 0 ∨ y₀ ^ 2 ∣ W.Δ
```

**Nagell–Lutz, integrality half.** Formalized in Tau Ceti as [`WeierstrassCurve.isInteger_of_torsion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.isInteger_of_torsion).

```lean
WeierstrassCurve.isInteger_of_torsion {W : WeierstrassCurve ℤ} [W.IsCharNeTwoNF] {x y : ℚ}
  (hns : (W.baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) :
  IsLocalization.IsInteger ℤ x ∧ IsLocalization.IsInteger ℤ y
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.isInteger_or_order_two_of_torsion_rat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/NagellLutz.html#WeierstrassCurve.isInteger_or_order_two_of_torsion_rat)
- [Source of `WeierstrassCurve.isInteger_or_order_two_of_torsion_rat` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/NagellLutz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/NagellLutz.lean#L254)
