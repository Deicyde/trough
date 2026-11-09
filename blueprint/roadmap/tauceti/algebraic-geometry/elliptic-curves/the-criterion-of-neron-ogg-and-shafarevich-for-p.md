---
declaration: theorem
origin: cited
lean: WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation
statement: formalized
proof: formalized
---

# The criterion of Néron, Ogg and Shafarevich for potential good reduction (Silverman AEC VII.7.3)

Let `W` be an elliptic curve over a nonarchimedean local field `K`, and let `ℓ` be a
prime different from the residue characteristic of `K`. Then `W` has potential good reduction
exactly when the inertia subgroup of `Gal(K^{alg}/K)` acts on the `ℓ`-adic Tate module of `W`
through a finite quotient.

```lean
WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation.{u_1}
  {K : Type u_1} [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  {W : WeierstrassCurve K} [W.IsElliptic] [DecidableEq (AlgebraicClosure K)] {ℓ : ℕ}
  [Fact (Nat.Prime ℓ)] (hℓ : ↑ℓ ≠ 0) :
  WeierstrassCurve.HasPotentialGoodReduction (↥(ValuativeRel.valuation K).integer) W ↔
    (⇑(W.tateModuleGaloisRepresentation ℓ) '' ↑(TauCeti.inertiaSubgroup K)).Finite
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

Formalized in Tau Ceti as [`WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/PotentialGoodReduction.html#WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/PotentialGoodReduction.html#WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation)
- [Source of `WeierstrassCurve.hasPotentialGoodReduction_iff_finite_image_tateModuleGaloisRepresentation` in TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/PotentialGoodReduction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/PotentialGoodReduction.lean#L361)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
