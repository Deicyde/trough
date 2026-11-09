---
declaration: theorem
origin: cited
lean: TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt, TauCeti.enorm_sub_setAverage_le_of_convex_of_finrank_lt
statement: formalized
proof: formalized
---

# The Morrey potential estimate for the mean

If `u` is `C¹` on an open set `Ω` which is
star-convex about `x` and contained in `closedBall x D`, and `p` exceeds the dimension `n` of the
space, then for every `S ⊆ Ω` of positive measure the deviation of `u x` from the mean of `u`
over `S` is at most `D ^ n / (n μ(S)) * K ^ (1 - 1 / p) * D ^ (1 - n / p)` times the `Lᵖ(Ω)`
norm of the derivative of `u`, where `K = n μ(B(0, 1)) (p - 1) / (p - n)`.

```lean
TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} {x : E} {D : ℝ} {p : NNReal} [CompleteSpace F]
  (hΩ : IsOpen Ω) (hu : ContDiffOn ℝ 1 u Ω) (hx : StarConvex ℝ x Ω) (hD : Ω ⊆ Metric.closedBall x D)
  (hS : S ⊆ Ω) (hS₀ : μ S ≠ 0) (hp : ↑(Module.finrank ℝ E) < p) :
  ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ≤
    ENNReal.ofReal (D ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E)) / μ S *
        ENNReal.ofReal
          ((↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1) * (↑p - 1) /
                (↑p - ↑(Module.finrank ℝ E))) ^
              (1 - 1 / ↑p) *
            D ^ (1 - ↑(Module.finrank ℝ E) / ↑p)) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) (μ.restrict Ω)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt).

## Other forms

**The Morrey potential estimate on a convex domain.** Formalized in Tau Ceti as [`TauCeti.enorm_sub_setAverage_le_of_convex_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_setAverage_le_of_convex_of_finrank_lt).

```lean
TauCeti.enorm_sub_setAverage_le_of_convex_of_finrank_lt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℝ F] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {u : E → F} {Ω S : Set E} {x : E} {p : NNReal} [CompleteSpace F]
  (hΩ : IsOpen Ω) (hΩc : Convex ℝ Ω) (hb : Bornology.IsBounded Ω) (hu : ContDiffOn ℝ 1 u Ω)
  (hx : x ∈ Ω) (hS : S ⊆ Ω) (hS₀ : μ S ≠ 0) (hp : ↑(Module.finrank ℝ E) < p) :
  ‖u x - ⨍ (y : E) in S, u y ∂μ‖ₑ ≤
    ENNReal.ofReal (Metric.diam Ω ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E)) / μ S *
        ENNReal.ofReal
          ((↑(Module.finrank ℝ E) * μ.real (Metric.ball 0 1) * (↑p - 1) /
                (↑p - ↑(Module.finrank ℝ E))) ^
              (1 - 1 / ↑p) *
            Metric.diam Ω ^ (1 - ↑(Module.finrank ℝ E) / ↑p)) *
      MeasureTheory.eLpNorm (fderiv ℝ u) (↑p) (μ.restrict Ω)
```

## Sources

- [Tau Ceti documentation: `TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Morrey.html#TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt)
- [Source of `TauCeti.enorm_sub_setAverage_le_of_starConvex_of_finrank_lt` in TauCeti/Analysis/Sobolev/Morrey.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Morrey.lean#L140)
