---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex
statement: formalized
proof: formalized
---

# Tate's local index is the point-group index

(Silverman, *Advanced Topics*, IV.9, Table 4.1).
Suppose that the valuation ring of `v` is Henselian with finite residue field, for instance the
ring of integers of a nonarchimedean local field, and that Tate's algorithm, run on the integral
model of `W` with a generator `ϖ` of the maximal ideal, stops with the symbol `s`. Then the local
index the algorithm reports is `[W(F) : E₀(F)]`, the index of the subgroup of points with
nonsingular reduction.

Finiteness of the residue field is used only at nonsplit multiplicative reduction of even type
`I₂ₘ`, to find a point with singular reduction; over a general perfect residue field the index can
be `1` there.

```lean
WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex.{u_1, u_2} {F : Type u_1}
  {Γ₀ : Type u_2} [Field F] [LinearOrderedCommGroupWithZero Γ₀] (v : Valuation F Γ₀)
  {W : WeierstrassCurve.Affine F} [WeierstrassCurve.IsIntegral (↥v.valuationSubring) W]
  [DecidableEq F] [HenselianLocalRing ↥v.valuationSubring]
  [Finite (IsLocalRing.ResidueField ↥v.valuationSubring)] {ϖ : ↥v.valuationSubring}
  (hϖ : IsLocalRing.maximalIdeal ↥v.valuationSubring = Ideal.span {ϖ}) {s : TauCeti.ReductionSymbol}
  (h : (WeierstrassCurve.integralModel (↥v.valuationSubring) W).IsTateTerminal ϖ s) :
  (WeierstrassCurve.Affine.nonsingularReduction v W).index =
    (WeierstrassCurve.integralModel (↥v.valuationSubring) W).tateLocalIndex ϖ s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Point/Index/TateAlgorithm.html#WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Point/Index/TateAlgorithm.html#WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex)
- [Source of `WeierstrassCurve.Affine.index_nonsingularReduction_eq_tateLocalIndex` in TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Point/Index/TateAlgorithm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Affine/Point/Index/TateAlgorithm.lean#L413)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EllipticCurves/STATUS.md)
