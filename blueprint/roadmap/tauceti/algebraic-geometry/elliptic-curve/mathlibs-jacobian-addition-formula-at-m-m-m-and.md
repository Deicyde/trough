---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.Jacobian.addXYZ_smulField
statement: formalized
proof: formalized
---

# Mathlib's Jacobian addition formula at `(φₘ : ωₘ : ψₘ)` and `(φₙ : ωₙ : ψₙ)` returns `(φₙ₊ₘ : ωₙ₊ₘ : ψₙ₊ₘ)`, scaled by `ψₙ₋ₘ`

The scaling is genuine: `addXYZ` is homogeneous, and
the representative it produces is the canonical triple only up to that factor.

```lean
WeierstrassCurve.Universal.Jacobian.addXYZ_smulField {m n : ℤ} :
  WeierstrassCurve.Jacobian.addXYZ WeierstrassCurve.Universal.pointedCurve
      (WeierstrassCurve.Universal.Jacobian.smulField m)
      (WeierstrassCurve.Universal.Jacobian.smulField n) =
    WeierstrassCurve.Universal.polyToField
        (WeierstrassCurve.ψ WeierstrassCurve.Universal.curve (n - m)) •
      WeierstrassCurve.Universal.Jacobian.smulField (n + m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.Jacobian.addXYZ_smulField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.addXYZ_smulField).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.Jacobian.addXYZ_smulField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.addXYZ_smulField)
- [Source of `WeierstrassCurve.Universal.Jacobian.addXYZ_smulField` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean#L863)
