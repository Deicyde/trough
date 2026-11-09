---
declaration: theorem
origin: cited
lean: TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt, TauCeti.enorm_sub_le_of_mem_ball_of_finrank_lt, TauCeti.holderWith_of_contDiff_of_finrank_lt
statement: formalized
proof: formalized
---

# Morrey's inequality

If `u` is `C¹` on the whole space and `p` exceeds the dimension `n`
of the space, then `‖u x - u y‖` is at most
`2 ^ (n + 1) / (n ω) * K ^ (1 - 1 / p) * (2 ‖x - y‖) ^ (1 - n / p)` times the `Lᵖ` norm of the
derivative of `u`, where `ω = μ(B(0, 1))` and `K = n ω (p - 1) / (p - n)`.

```lean
TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {p : NNReal} [CompleteSpace F] (hu : ContDiff ℝ 1 u) (x y : E)
  (hp : ↑(Module.finrank ℝ E) < p) :
  ‖u x - u y‖ₑ ≤
    ENNReal.ofReal
        (2 ^ (Module.finrank ℝ E + 1) / (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1)) *
            (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1) * (↑p - 1) /
                (↑p - ↑(Module.finrank ℝ E))) ^
              (1 - 1 / ↑p) *
          (2 * ‖x - y‖) ^ (1 - ↑(Module.finrank ℝ E) / ↑p)) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morrey potential estimate for the mean](the-morrey-potential-estimate-for-the-mean.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt).

## Other forms

**Morrey's inequality on a ball.** Formalized in Tau Ceti as [`TauCeti.enorm_sub_le_of_mem_ball_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_le_of_mem_ball_of_finrank_lt).

```lean
TauCeti.enorm_sub_le_of_mem_ball_of_finrank_lt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {p : NNReal} [CompleteSpace F] {z : E} {r : ℝ}
  (hu : ContDiffOn ℝ 1 u (Metric.ball z r)) {x y : E} (hx : x ∈ Metric.ball z r)
  (hy : y ∈ Metric.ball z r) (hp : ↑(Module.finrank ℝ E) < p) :
  ‖u x - u y‖ₑ ≤
    ENNReal.ofReal
        (2 ^ (Module.finrank ℝ E + 1) / (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1)) *
            (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1) * (↑p - 1) /
                (↑p - ↑(Module.finrank ℝ E))) ^
              (1 - 1 / ↑p) *
          (2 * r) ^ (1 - ↑(Module.finrank ℝ E) / ↑p)) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) (μ.restrict (Metric.ball z r))
```

**Morrey's inequality, Hölder form.** Formalized in Tau Ceti as [`TauCeti.holderWith_of_contDiff_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.holderWith_of_contDiff_of_finrank_lt).

```lean
TauCeti.holderWith_of_contDiff_of_finrank_lt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {p : NNReal} [CompleteSpace F] (hu : ContDiff ℝ 1 u)
  (hp : ↑(Module.finrank ℝ E) < p) (hDu : MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) μ ≠ ⊤) :
  HolderWith
    ((2 ^ (Module.finrank ℝ E + 1) / (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1)) *
            (↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1) * (↑p - 1) /
                (↑p - ↑(Module.finrank ℝ E))) ^
              (1 - 1 / ↑p) *
          2 ^ (1 - ↑(Module.finrank ℝ E) / ↑p)).toNNReal *
      (MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) μ).toNNReal)
    (1 - ↑(Module.finrank ℝ E) / p) u
```

## Sources

- [Tau Ceti documentation: `TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt)
- [Source of `TauCeti.enorm_sub_le_of_contDiff_of_finrank_lt` in TauCeti/Analysis/Sobolev/Morrey.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Morrey.lean#L244)
