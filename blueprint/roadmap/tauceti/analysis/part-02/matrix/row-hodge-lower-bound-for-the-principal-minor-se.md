---
declaration: theorem
origin: cited
lean: Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries
statement: formalized
proof: formalized
---

# Row Hodge lower bound for the principal-minor series

Let `v` be a real additive
valuation with `‖x‖ = b ^ (-v x)` for `x ≠ 0`, where `b > 1`. For a bounded row majorant
`‖A i j‖ ≤ r i`, the row Hodge polygon of `r` lies below the Newton polygon of the principal-minor
series `A.charPowerSeries`, which is the Fredholm determinant `det (1 - T A)` when its
principal-minor families are summable.

```lean
Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries.{u_1, u_2} {ι : Type u_1} {K : Type u_2}
  [DecidableEq ι] [NormedField K] [IsUltrametricDist K] {v : AddValuation K (WithTop ℝ)} {b : ℝ}
  {A : Matrix ι ι K} {r : ι → ℝ} (hb : 1 < b) (hv : ∀ (x : K), x ≠ 0 → ‖x‖ = b ^ (-(v x).untop₀))
  (hr : BddAbove (Set.range r)) (hA : ∀ (i j : ι), ‖A i j‖ ≤ r i) :
  TauCeti.rowHodgePolygon b r ≤ A.charPowerSeries.newtonPolygon v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/CharPowerSeries/RowHodge.html#Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries).

## Sources

- [Tau Ceti documentation: `Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/CharPowerSeries/RowHodge.html#Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries)
- [Source of `Matrix.rowHodgePolygon_le_newtonPolygon_charPowerSeries` in TauCeti/Analysis/Matrix/CharPowerSeries/RowHodge.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/CharPowerSeries/RowHodge.lean#L213)
