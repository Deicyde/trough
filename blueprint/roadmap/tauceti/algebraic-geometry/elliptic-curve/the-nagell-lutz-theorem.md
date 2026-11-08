---
declaration: theorem
origin: cited
lean: WeierstrassCurve.lutz_nagell, WeierstrassCurve.isInteger_or_order_two_of_torsion_rat, WeierstrassCurve.y_eq_zero_or_sq_dvd_Δ_of_torsion, WeierstrassCurve.isInteger_of_torsion
statement: formalized
proof: formalized
---

# The Nagell–Lutz theorem

Let `A B : ℤ` and let `(x, y)` be a nonzero rational point of
finite order on `y² = x³ + Ax + B`. Then `x` and `y` are integers, and either `y = 0` or
`y² ∣ Δ`.

This is the classical statement, and the form `TauCetiRoadmap/EllipticCurves/README.md:830` names
`lutz_nagell`. It is the specialisation of the two theorems above at a short model: Mathlib's
`isCharNeTwoNF_of_isShortNF` supplies the instance, so there is nothing to discharge. No hypothesis
`Δ ≠ 0` is needed — see the module docstring.

```lean
WeierstrassCurve.lutz_nagell (A B : ℤ) {x y : ℚ}
  (hns : ((WeierstrassCurve.shortCurve A B).baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) :
  ∃ x₀ y₀, ↑x₀ = x ∧ ↑y₀ = y ∧ (y₀ = 0 ∨ y₀ ^ 2 ∣ (WeierstrassCurve.shortCurve A B).Δ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mathlib's Jacobian addition formula at `(φₘ : ωₘ : ψₘ)` and `(φₙ : ωₙ : ψₙ)` returns `(φₙ₊ₘ : ωₙ₊ₘ : ψₙ₊ₘ)`, scaled by `ψₙ₋ₘ`](mathlibs-jacobian-addition-formula-at-m-m-m-and.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.lutz_nagell`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.lutz_nagell).

## Other forms

**Nagell–Lutz over `ℚ`, the form the roadmap asks for.** Formalized in Tau Ceti as [`WeierstrassCurve.isInteger_or_order_two_of_torsion_rat`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/NagellLutz.html#WeierstrassCurve.isInteger_or_order_two_of_torsion_rat).

```lean
WeierstrassCurve.isInteger_or_order_two_of_torsion_rat {W : WeierstrassCurve ℤ} {x y : ℚ}
  (hns : (W.baseChange ℚ).toAffine.Nonsingular x y)
  (htor : IsOfFinAddOrder (WeierstrassCurve.Affine.Point.some x y hns)) :
  IsLocalization.IsInteger ℤ x ∧ IsLocalization.IsInteger ℤ y ∨
    addOrderOf (WeierstrassCurve.Affine.Point.some x y hns) = 2 ∧
      IsLocalization.IsInteger ℤ (4 * x) ∧ IsLocalization.IsInteger ℤ (8 * y)
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

- [Tau Ceti documentation: `WeierstrassCurve.lutz_nagell`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.lutz_nagell)
- [Source of `WeierstrassCurve.lutz_nagell` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.lean#L143)
