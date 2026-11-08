---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries
statement: formalized
proof: formalized
---

# Row Hodge lower bound for a row-compact operator

Let `v` be a real additive valuation
on an ultrametric normed field with `‖x‖ = b ^ (-v x)` for `x ≠ 0`, where `b > 1`. For a
row-compact endomorphism `u` of `C₀(I, K)`, the row Hodge polygon of its row norms lies below
the Newton polygon of its principal-minor series `u.matrixCoeff.charPowerSeries`. When `K` is
complete, these principal-minor sums converge and the series is the Fredholm series
`det (1 - T u)`.

```lean
ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries.{u_1, u_2}
  {I : Type u_1} {K : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I] {b : ℝ}
  [NormedField K] [IsUltrametricDist K] {v : AddValuation K (WithTop ℝ)}
  {u : ZeroAtInftyContinuousMap I K →L[K] ZeroAtInftyContinuousMap I K} (hu : u.IsRowCompact)
  (hb : 1 < b) (hv : ∀ (x : K), x ≠ 0 → ‖x‖ = b ^ (-(v x).untop₀)) :
  TauCeti.rowHodgePolygon b u.rowNorm ≤ u.matrixCoeff.charPowerSeries.newtonPolygon v
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [Row Hodge lower bound for the principal-minor series](../../part-02/matrix/row-hodge-lower-bound-for-the-principal-minor-se.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RowHodge.html#ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RowHodge.html#ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries)
- [Source of `ContinuousLinearMap.IsRowCompact.rowHodgePolygon_rowNorm_le_newtonPolygon_charPowerSeries` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/RowHodge.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RowHodge.lean#L48)
