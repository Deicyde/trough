---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.Jacobian.addZ_smulPoly
statement: formalized
proof: formalized
---

# The `Z`-coordinate of Mathlib's Jacobian addition formula at `(φₘ, ωₘ, ψₘ)` and `(φₙ, ωₙ, ψₙ)` is `ψₙ₊ₘψₙ₋ₘ`, again already in the polynomial ring

```lean
WeierstrassCurve.Universal.Jacobian.addZ_smulPoly {m n : ℤ} :
  WeierstrassCurve.Jacobian.addZ (WeierstrassCurve.Universal.Jacobian.smulPoly m)
      (WeierstrassCurve.Universal.Jacobian.smulPoly n) =
    WeierstrassCurve.ψ WeierstrassCurve.Universal.curve (n + m) *
      WeierstrassCurve.ψ WeierstrassCurve.Universal.curve (n - m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.Jacobian.addZ_smulPoly`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.addZ_smulPoly).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.Jacobian.addZ_smulPoly`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.addZ_smulPoly)
- [Source of `WeierstrassCurve.Universal.Jacobian.addZ_smulPoly` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean#L820)
