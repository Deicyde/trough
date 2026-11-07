---
declaration: theorem
origin: cited
lean: TauCeti.Probability.map_coe_apply_inverseWishartMeasure
statement: formalized
proof: formalized
---

# The diagonal entries of an inverse-Wishart matrix are inverse gamma

For a
positive-definite scale `S`, the entry `(i, i)` of an inverse-Wishart matrix of degree `n` has the
inverse-gamma law of shape `(n - p + 1) / 2` and scale `S i i / 2`. For degrees at most `p - 1`
both sides are the zero measure.

```lean
TauCeti.Probability.map_coe_apply_inverseWishartMeasure {p : ℕ} {n : ℝ}
  {S : Matrix (Fin p) (Fin p) ℝ} (hS : S.PosDef) (i : Fin p) :
  MeasureTheory.Measure.map (fun B => ↑B i i) (TauCeti.Probability.inverseWishartMeasure n S) =
    TauCeti.Probability.inverseGammaMeasure ((n - ↑p + 1) / 2) (S i i / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.map_coe_apply_inverseWishartMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Wishart/Inverse/Marginal.html#TauCeti.Probability.map_coe_apply_inverseWishartMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.map_coe_apply_inverseWishartMeasure`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/Wishart/Inverse/Marginal.html#TauCeti.Probability.map_coe_apply_inverseWishartMeasure)
- [Source of `TauCeti.Probability.map_coe_apply_inverseWishartMeasure` in TauCeti/Probability/Distributions/Wishart/Inverse/Marginal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/Wishart/Inverse/Marginal.lean#L65)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
