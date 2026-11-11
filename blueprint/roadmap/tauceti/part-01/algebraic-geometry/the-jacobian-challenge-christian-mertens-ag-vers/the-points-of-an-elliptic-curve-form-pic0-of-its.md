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

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.pointAddEquivPicZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.html#WeierstrassCurve.pointAddEquivPicZero).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.pointAddEquivPicZero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.html#WeierstrassCurve.pointAddEquivPicZero)
- [Source of `WeierstrassCurve.pointAddEquivPicZero` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/PicZero.lean#L115)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)
