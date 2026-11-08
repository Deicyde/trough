---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.isSingular_iff, WeierstrassCurve.Affine.isSingular_iff_equation_and_not_nonsingular
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

## Other forms

**The Jacobian criterion is Mathlib's singularity condition, `Nonsingular` being the conjunction of the equation with the negation of both partials vanishing.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.isSingular_iff_equation_and_not_nonsingular`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.html#WeierstrassCurve.Affine.isSingular_iff_equation_and_not_nonsingular).

```lean
WeierstrassCurve.Affine.isSingular_iff_equation_and_not_nonsingular.{u_1} {R : Type u_1}
  [CommRing R] {W : WeierstrassCurve.Affine R} {x y : R} :
  W.IsSingular x y ↔ W.Equation x y ∧ ¬W.Nonsingular x y
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.isSingular_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.html#WeierstrassCurve.Affine.isSingular_iff)
- [Source of `WeierstrassCurve.Affine.isSingular_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Singular.lean#L135)
