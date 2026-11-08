---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two
statement: formalized
proof: formalized
---

# The weak Mordell–Weil theorem

`E(K)/2E(K)` is finite, for an elliptic curve in the normal
form `y² = x³ + a₂x² + a₄x + a₆` over the fraction field `K` of a Dedekind domain `R`, provided
that for each irreducible factor `p` of the cubic the ring of integers of `K[X] ⧸ (p)` has finite
class group and finitely generated unit group.

This is the input to the descent argument in the Mordell–Weil theorem proper.

```lean
WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two.{u_1, u_2} {K : Type u_1} [Field K]
  (W : WeierstrassCurve.Affine K) [WeierstrassCurve.IsElliptic W] [WeierstrassCurve.IsCharNeTwoNF W]
  (R : Type u_2) [CommRing R] [IsDedekindDomain R] [Algebra R K] [IsFractionRing R K]
  [∀ (p : W.f.Factors), Finite (ClassGroup (W.ringOfIntegersFactor R p))]
  [∀ (p : W.f.Factors), Monoid.FG (W.ringOfIntegersFactor R p)ˣ] [DecidableEq K] :
  (nsmulAddMonoidHom 2).range.FiniteIndex
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chinese Remainder Theorem for `AdjoinRoot`](../../ring-theory/part-02/other-results/part-01/chinese-remainder-theorem-for-adjoinroot.md)
- [The criterion behind the weak Mordell–Weil theorem](the-criterion-behind-the-weak-mordell-weil-theor.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.html#WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.html#WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two)
- [Source of `WeierstrassCurve.Affine.finiteIndex_range_nsmulAddMonoidHom_two` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WeakMordellWeil.lean#L88)
