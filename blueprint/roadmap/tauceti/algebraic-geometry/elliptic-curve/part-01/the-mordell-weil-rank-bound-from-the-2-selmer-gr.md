---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂, WeierstrassCurve.Affine.pow_rank_add_one_le_prod
statement: formalized
proof: formalized
---

# The Mordell–Weil rank bound from the 2-Selmer group

for an elliptic curve over a number
field `F`, `2 ^ rank W(F) * #W(F)[2] ≤ #Sel₂(W/F)`. The rank is that of the finitely generated
group `W(F)` (`fg_point_of_numberField`), and the right-hand side is finite by
`finite_selmerGroup₂`.

```lean
WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂.{u_1, u_2, u_3} {F : Type u_1} [Field F]
  [NumberField F] (W : WeierstrassCurve.Affine F) [WeierstrassCurve.IsElliptic W]
  [WeierstrassCurve.IsCharNeTwoNF W] {ι : Type u_2} (Loc : ι → Type u_3) [(i : ι) → Field (Loc i)]
  [(i : ι) → Algebra F (Loc i)] :
  2 ^ Module.finrank ℤ W.Point * Nat.card ↥(nsmulAddMonoidHom 2).ker ≤
    Nat.card ↥(W.selmerGroup₂ (NumberField.RingOfIntegers F) Loc)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chinese Remainder Theorem for `AdjoinRoot`](../../../ring-theory/part-02/other-results/part-01/chinese-remainder-theorem-for-adjoinroot.md)
- [Dirichlet's unit theorem (`WeierstrassCurve.Affine.fg_units_ringOfIntegersFactor`)](../../elliptic-curves/dirichlets-unit-theorem-weierstrasscurve-affine.md)
- [The Mordell–Weil theorem](../../elliptic-curves/the-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.html#WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup%E2%82%82).

## Other forms

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

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.html#WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup%E2%82%82)
- [Source of `WeierstrassCurve.Affine.pow_rank_le_card_selmerGroup₂` in TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/MordellWeil/RankBound.lean#L127)
