---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.fg_point_of_numberField, WeierstrassCurve.Affine.fg_point, WeierstrassCurve.Affine.fg_point_of_variableChange, WeierstrassCurve.Affine.moduleFinite_point_of_numberField
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

## Proof depends on

- [Dirichlet's unit theorem for the field factors of the étale algebra of a curve over a number field](dirichlets-unit-theorem-for-the-field-factors-of.md)
- [The weak Mordell–Weil theorem](the-weak-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.fg_point_of_numberField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point_of_numberField).

## Other forms

**The Mordell–Weil theorem, general version.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.fg_point`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point).

```lean
WeierstrassCurve.Affine.fg_point.{u_1, u_2} {F : Type u_1} [Field F] {W : WeierstrassCurve.Affine F}
  [Height.AdmissibleAbsValues F] [Northcott Height.logHeight₁] [DecidableEq F]
  [WeierstrassCurve.IsElliptic (WeierstrassCurve.toAffine W)] (R : Type u_2) [CommRing R]
  [IsDedekindDomain R] [Algebra R F] [IsFractionRing R F] [WeierstrassCurve.IsCharNeTwoNF W]
  [∀ (p : W.f.Factors), Finite (ClassGroup (W.ringOfIntegersFactor R p))]
  [∀ (p : W.f.Factors), Monoid.FG (W.ringOfIntegersFactor R p)ˣ] : AddGroup.FG W.Point
```

**The Mordell–Weil theorem for an arbitrary Weierstrass curve.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.fg_point_of_variableChange`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point_of_variableChange).

```lean
WeierstrassCurve.Affine.fg_point_of_variableChange.{u_1, u_2} {F : Type u_1} [Field F]
  {W : WeierstrassCurve.Affine F} [Height.AdmissibleAbsValues F] [Northcott Height.logHeight₁]
  [DecidableEq F] [WeierstrassCurve.IsElliptic (WeierstrassCurve.toAffine W)] (R : Type u_2)
  [CommRing R] [IsDedekindDomain R] [Algebra R F] [IsFractionRing R F]
  (C : WeierstrassCurve.VariableChange F) [WeierstrassCurve.IsCharNeTwoNF (C • W)]
  [∀ (p : (WeierstrassCurve.toAffine (C • W)).f.Factors),
      Finite (ClassGroup ((WeierstrassCurve.toAffine (C • W)).ringOfIntegersFactor R p))]
  [∀ (p : (WeierstrassCurve.toAffine (C • W)).f.Factors),
      Monoid.FG ((WeierstrassCurve.toAffine (C • W)).ringOfIntegersFactor R p)ˣ] :
  AddGroup.FG W.Point
```

**The Mordell–Weil theorem as an instance.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.moduleFinite_point_of_numberField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.moduleFinite_point_of_numberField).

```lean
WeierstrassCurve.Affine.moduleFinite_point_of_numberField.{u_2} {F : Type u_2} [Field F]
  [NumberField F] [DecidableEq F] {W : WeierstrassCurve.Affine F}
  [WeierstrassCurve.IsElliptic (WeierstrassCurve.toAffine W)] : Module.Finite ℤ W.Point
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.fg_point_of_numberField`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.html#WeierstrassCurve.Affine.fg_point_of_numberField)
- [Source of `WeierstrassCurve.Affine.fg_point_of_numberField` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/FinitelyGenerated.lean#L139)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
