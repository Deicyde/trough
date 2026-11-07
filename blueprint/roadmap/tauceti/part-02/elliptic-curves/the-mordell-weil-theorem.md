---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.fg_point_of_numberField
statement: formalized
proof: formalized
---

# The Mordell–Weil theorem

the group `E(K)` of `K`-rational points of an elliptic curve `E`
over a number field `K` is finitely generated.

The square on the left-hand side is completed by an admissible change of variables, possible since
`K` has characteristic zero, and the finiteness hypotheses of `fg_point` for the resulting model
are the class number theorem and Dirichlet's unit theorem.

```lean
WeierstrassCurve.Affine.fg_point_of_numberField.{u_2} {F : Type u_2} [Field F] [NumberField F]
  [DecidableEq F] {W : WeierstrassCurve.Affine F}
  [WeierstrassCurve.IsElliptic (WeierstrassCurve.toAffine W)] : AddGroup.FG W.Point
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.fg_point_of_numberField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point_of_numberField).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.fg_point_of_numberField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point_of_numberField)
- [Source of `WeierstrassCurve.Affine.fg_point_of_numberField` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean#L139)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
