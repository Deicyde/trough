---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.isSingular_iff
statement: formalized
proof: formalized
---

# The Jacobian criterion as two equalities, the form `Nonsingular` negates

```lean
WeierstrassCurve.Affine.isSingular_iff.{u_1} {R : Type u_1} [CommRing R]
  (W : WeierstrassCurve.Affine R) (x y : R) :
  W.IsSingular x y ↔
    W.Equation x y ∧ W.a₁ * y = 3 * x ^ 2 + 2 * W.a₂ * x + W.a₄ ∧ y = -y - W.a₁ * x - W.a₃
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.isSingular_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.html#WeierstrassCurve.Affine.isSingular_iff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.isSingular_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.html#WeierstrassCurve.Affine.isSingular_iff)
- [Source of `WeierstrassCurve.Affine.isSingular_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.lean#L135)
