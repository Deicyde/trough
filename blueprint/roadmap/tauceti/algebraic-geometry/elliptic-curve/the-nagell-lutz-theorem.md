---
declaration: theorem
origin: cited
lean: WeierstrassCurve.lutz_nagell
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
- [Mathlib's Jacobian doubling formula sends `(φₙ : ωₙ : ψₙ)` to `(φ₂ₙ : ω₂ₙ : ψ₂ₙ)`, as an equality of triples and not merely of the points they represent](mathlibs-jacobian-doubling-formula-sends-n-n-n-t.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.lutz_nagell`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.lutz_nagell).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.lutz_nagell`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.html#WeierstrassCurve.lutz_nagell)
- [Source of `WeierstrassCurve.lutz_nagell` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ShortNagellLutz.lean#L143)
