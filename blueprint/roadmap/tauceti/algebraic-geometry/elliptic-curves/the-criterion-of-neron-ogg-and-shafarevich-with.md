---
declaration: theorem
origin: cited
lean: WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup
statement: formalized
proof: formalized
---

# The criterion of Néron, Ogg and Shafarevich with finite coefficients (Serre–Tate)

Let
`W` be an elliptic curve over a nonarchimedean local field `K`, given by a minimal equation, with
potential good reduction, and let `N ≥ 3` be an integer that is nonzero in the residue field of
`K`. Then `W` has good reduction exactly when the inertia subgroup of `Gal(K^{alg}/K)` fixes every
point of `E(K^{alg})[N]`.

```lean
WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {W : WeierstrassCurve K} [W.IsElliptic]
  [WeierstrassCurve.IsMinimal (↥(ValuativeRel.valuation K).integer) W]
  (h : WeierstrassCurve.HasPotentialGoodReduction (↥(ValuativeRel.valuation K).integer) W) {N : ℕ}
  (hN : 3 ≤ N) (hNk : ↑N ≠ 0) :
  WeierstrassCurve.HasGoodReduction (↥(ValuativeRel.valuation K).integer) W ↔
    ∀ σ ∈ TauCeti.inertiaSubgroup K,
      ∀ (P : (W.baseChange (AlgebraicClosure K)).toAffine.Point),
        N • P = 0 → (WeierstrassCurve.Affine.Point.map ↑σ) P = P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, the tame case](../../number-theory/part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../number-theory/part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma without monicity](../../ring-theory/part-02/other-results/part-01/hensels-lemma-without-monicity.md)
- [Serre's lemma for the `ℓ`-adic representation](serres-lemma-for-the-l-adic-representation.md)
- [TauCeti.algebraicExtensionNormedField](../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/part-01/vietas-formula-at-a-pair-of-parameters-cleared-o.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/TorsionCriterion.html#WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/TorsionCriterion.html#WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup)
- [Source of `WeierstrassCurve.HasPotentialGoodReduction.hasGoodReduction_iff_forall_mem_inertiaSubgroup` in TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/TorsionCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/TorsionCriterion.lean#L103)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
