---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff
statement: formalized
proof: formalized
---

# The criterion behind the weak Mordell–Weil theorem

`2E(K)` has finite index in `E(K)`
exactly when the image of the descent map is finite.

`E(K)/2E(K)` and the image of `μ` are the same group, so finiteness of either is finiteness of
the other.

```lean
WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff.{u_1} {K : Type u_1} [Field K]
  (W : WeierstrassCurve.Affine K) [WeierstrassCurve.IsElliptic W] [WeierstrassCurve.IsCharNeTwoNF W]
  [DecidableEq K] :
  (nsmulAddMonoidHom 2).range.FiniteIndex ↔ Finite ↥WeierstrassCurve.Affine.μ.range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.html#WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.html#WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff)
- [Source of `WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.lean#L68)
