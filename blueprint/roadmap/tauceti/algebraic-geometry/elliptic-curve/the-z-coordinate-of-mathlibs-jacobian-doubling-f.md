---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly
statement: formalized
proof: formalized
---

# The `Z`-coordinate of Mathlib's Jacobian doubling formula at `(φₙ, ωₙ, ψₙ)` is `ψ₂ₙ` — already in the polynomial ring, with no reduction modulo the Weierstrass polynomial

```lean
WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly {n : ℤ} :
  WeierstrassCurve.Jacobian.dblZ WeierstrassCurve.Universal.curvePoly
      (WeierstrassCurve.Universal.Jacobian.smulPoly n) =
    WeierstrassCurve.ψ WeierstrassCurve.Universal.curve (2 * n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly)
- [Source of `WeierstrassCurve.Universal.Jacobian.dblZ_smulPoly` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean#L769)
