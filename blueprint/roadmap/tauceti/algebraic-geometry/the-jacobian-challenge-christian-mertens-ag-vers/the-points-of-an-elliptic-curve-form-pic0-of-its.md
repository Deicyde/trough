---
declaration: def
origin: cited
lean: WeierstrassCurve.pointAddEquivPicZero
statement: formalized
---

# The points of an elliptic curve form `Pic⁰` of its projective model

For an elliptic
curve `W` over a field `K`, the group `W.toAffine.Point` of Mathlib, with its chord-and-tangent
group law, is isomorphic to the group `Pic⁰ (projModel W)` of degree-zero line bundles on the
projective model. The point at infinity goes to the trivial bundle, and an affine point `P` to the
class of `𝒪(x_P - x_O)` (`coe_pointAddEquivPicZero_some`).

```lean
WeierstrassCurve.pointAddEquivPicZero.{u} {K : Type u} [Field K] (W : WeierstrassCurve K)
  [W.IsElliptic] [DecidableEq K] :
  W.toAffine.Point ≃+ ↥(TauCeti.AlgebraicGeometry.LineBundleClass.picZero K W.projModel)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobian criterion for étaleness](../../ring-theory/other-results/part-01/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.pointAddEquivPicZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.html#WeierstrassCurve.pointAddEquivPicZero).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.pointAddEquivPicZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.html#WeierstrassCurve.pointAddEquivPicZero)
- [Source of `WeierstrassCurve.pointAddEquivPicZero` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.lean#L115)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
