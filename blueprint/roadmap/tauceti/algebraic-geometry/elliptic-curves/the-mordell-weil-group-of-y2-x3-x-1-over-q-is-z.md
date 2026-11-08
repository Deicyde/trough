---
declaration: theorem
origin: cited
lean: TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne, WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂, WeierstrassCurve.Affine.pow_rank_add_one_le_prod, WeierstrassCurve.Affine.fg_point, WeierstrassCurve.Affine.fg_point_of_variableChange, WeierstrassCurve.Affine.moduleFinite_point_of_numberField
statement: formalized
proof: formalized
---

# The Mordell–Weil group of `y² = x³ - x + 1` over `ℚ` is `ℤ`

It is finitely generated,
torsion-free and of rank one.

```lean
TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne :
  Nonempty ((TauCeti.WorkedExamples.curveX3SubXAddOne.baseChange ℚ).toAffine.Point ≃+ ℤ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brill's theorem, parity form](../../number-theory/part-02/number-field/brills-theorem-parity-form.md)
- [Chinese Remainder Theorem for `AdjoinRoot`](../../ring-theory/part-02/other-results/part-01/chinese-remainder-theorem-for-adjoinroot.md)
- [Dirichlet's unit theorem (`WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor`)](dirichlets-unit-theorem-weierstrasscurve-affine.md)
- [The Mordell–Weil theorem](the-mordell-weil-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak Mordell–Weil theorem](../elliptic-curve/the-weak-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne).

## Other forms

**The Mordell–Weil rank bound from the 2-Selmer group.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.html#WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup%E2%82%82).

```lean
WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂.{u_1, u_2, u_3} {F : Type u_1} [Field F]
  [NumberField F] (W : WeierstrassCurve.Affine F) [WeierstrassCurve.IsElliptic W]
  [WeierstrassCurve.IsCharNeTwoNF W] {ι : Type u_2} (Loc : ι → Type u_3) [(i : ι) → Field (Loc i)]
  [(i : ι) → Algebra F (Loc i)] :
  2 ^ Module.finrank ℤ W.Point * Nat.card ↥(nsmulAddMonoidHom 2).ker ≤
    Nat.card ↥(W.selmerGroup₂ (NumberField.RingOfIntegers F) Loc)
```

**The Mordell–Weil rank bound from the units and class groups of the field factors.** Formalized in Tau Ceti as [`WeierstrassCurve.Affine.pow_rank_add_one_le_prod`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.html#WeierstrassCurve.Affine.pow_rank_add_one_le_prod).

```lean
WeierstrassCurve.Affine.pow_rank_add_one_le_prod.{u_1} {F : Type u_1} [Field F] [NumberField F]
  (W : WeierstrassCurve.Affine F) [WeierstrassCurve.IsElliptic W] [WeierstrassCurve.IsCharNeTwoNF W]
  [Fintype W.f.Factors]
  (ha₂ :
    ∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers F)),
      (IsDedekindDomain.HeightOneSpectrum.valuation F v) W.a₂ ≤ 1)
  (ha₄ :
    ∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers F)),
      (IsDedekindDomain.HeightOneSpectrum.valuation F v) W.a₄ ≤ 1)
  (ha₆ :
    ∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers F)),
      (IsDedekindDomain.HeightOneSpectrum.valuation F v) W.a₆ ≤ 1)
  (hd :
    ∀ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers F)),
      WithZero.exp (-1) ≤ (IsDedekindDomain.HeightOneSpectrum.valuation F v) W.f.discr)
  (h : ¬IsSquare (-1)) :
  2 ^ (Module.finrank ℤ W.Point + 1) * Nat.card ↥(nsmulAddMonoidHom 2).ker ≤
    ∏ p,
      2 ^
          (Module.finrank ℤ (Additive (W.ringOfIntegersFactor (NumberField.RingOfIntegers F) p)ˣ) +
            1) *
        Nat.card ↥(powMonoidHom 2).ker
```

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

- [Tau Ceti documentation: `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.html#TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne)
- [Source of `TauCeti.WorkedExamples.nonempty_addEquiv_int_point_curveX3SubXAddOne` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/WorkedExamples/X3SubXAddOne/Rank.lean#L181)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
