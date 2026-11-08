---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField
statement: formalized
proof: formalized
---

# Mathlib's Jacobian doubling formula sends `(φₙ : ωₙ : ψₙ)` to `(φ₂ₙ : ω₂ₙ : ψ₂ₙ)`, as an equality of triples and not merely of the points they represent

```lean
WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField {n : ℤ} :
  WeierstrassCurve.Jacobian.dblXYZ WeierstrassCurve.Universal.pointedCurve
      (WeierstrassCurve.Universal.Jacobian.smulField n) =
    WeierstrassCurve.Universal.Jacobian.smulField (2 * n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `Z`-coordinate of Mathlib's Jacobian doubling formula at `(φₙ, ωₙ, ψₙ)` is `ψ₂ₙ` — already in the polynomial ring, with no reduction modulo the Weierstrass polynomial](the-z-coordinate-of-mathlibs-jacobian-doubling-f.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.html#WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField)
- [Source of `WeierstrassCurve.Universal.Jacobian.dblXYZ_smulField` in TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/DivisionPolynomial/ZSMul.lean#L788)
