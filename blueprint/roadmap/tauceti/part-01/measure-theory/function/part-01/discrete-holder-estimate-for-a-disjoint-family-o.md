---
declaration: theorem
origin: cited
lean: TauCeti.sum_edist_ceil_div_rpow_le
statement: formalized
proof: formalized
---

# Discrete Hölder estimate for a disjoint family of intervals `(sᵢ, tᵢ]` in `[0, T]`

the
`p`-th power of the sum of the distances between the piecewise constant interpolant at times `sᵢ`
and `tᵢ` is at most `(|⋃ (sᵢ, tᵢ]| + k τ) ^ (p - 1)` times the discrete `p`-action up to time `T`,
where `k` is the number of intervals. As `τ → 0` the factor tends to the one in the Hölder
estimate `AbsolutelyContinuousOnInterval.edist_rpow_le_mul_curveAction` for curves.

```lean
TauCeti.sum_edist_ceil_div_rpow_le.{u_1} {X : Type u_1} [TopologicalSpace X]
  [WeakPseudoEMetricSpace X] {p : ℝ} {τ : NNReal} {U : ℕ → X} (hp : 1 ≤ p) (hτ : 0 < τ) {T : ℝ}
  (hT : 0 ≤ T) {E : ℕ × (ℕ → ℝ × ℝ)} (hE : E ∈ AbsolutelyContinuousOnInterval.disjWithin 0 T) :
  (∑ i ∈ Finset.range E.1, edist (U ⌈(E.2 i).1 / ↑τ⌉₊) (U ⌈(E.2 i).2 / ↑τ⌉₊)) ^ p ≤
    (MeasureTheory.volume (⋃ i ∈ Finset.range E.1, Set.uIoc (E.2 i).1 (E.2 i).2) + ↑E.1 * ↑τ) ^
        (p - 1) *
      ∑ n ∈ Finset.range ⌈T / ↑τ⌉₊, edist (U n) (U (n + 1)) ^ p / ↑τ ^ (p - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_edist_ceil_div_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/CurveAction/PiecewiseConstant.html#TauCeti.sum_edist_ceil_div_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_edist_ceil_div_rpow_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Function/CurveAction/PiecewiseConstant.html#TauCeti.sum_edist_ceil_div_rpow_le)
- [Source of `TauCeti.sum_edist_ceil_div_rpow_le` in TauCeti/MeasureTheory/Function/CurveAction/PiecewiseConstant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Function/CurveAction/PiecewiseConstant.lean#L103)
