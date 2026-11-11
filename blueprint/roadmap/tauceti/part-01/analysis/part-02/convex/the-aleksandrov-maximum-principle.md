---
declaration: theorem
origin: cited
lean: TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure
statement: formalized
proof: formalized
---

# The Aleksandrov maximum principle

Let `Ω` be a bounded open convex subset of a real inner
product space `E` of finite dimension `n ≥ 1`, and let `u` be convex on `Ω`, continuous on its
closure, and nonnegative on its frontier. Then at every `x₀ ∈ Ω`,

  `max (-u x₀) 0 ^ n * μ (ball 0 1) ≤ 2 ^ (n + 1) * diam Ω ^ (n - 1) * dist(x₀, ∂Ω) * MA_u(Ω)`,

where `dist(x₀, ∂Ω)` is the distance from `x₀` to the complement of `Ω` and `MA_u` is the
Aleksandrov Monge–Ampère measure of `u` (extended by `⊤` off `Ω`) with respect to the additive
Haar measure `μ`. When `MA_u(Ω)` is finite, this bounds the negative part `max (-u x₀) 0` above
on `Ω` and shows that `max (-u x₀) 0 = O(dist(x₀, ∂Ω) ^ (1 / n))` as `x₀` approaches the
boundary.

```lean
TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : Set E} {u : E → ℝ} [Nontrivial E] (μ : MeasureTheory.Measure E)
  [μ.IsAddHaarMeasure] [DecidablePred fun x => x ∈ Ω] (hΩo : IsOpen Ω) (hΩ : Bornology.IsBounded Ω)
  (hu : ConvexOn ℝ Ω u) (hc : ContinuousOn u (closure Ω)) (hfr : ∀ x ∈ frontier Ω, 0 ≤ u x) {x₀ : E}
  (hx₀ : x₀ ∈ Ω) :
  ENNReal.ofReal (-u x₀) ^ Module.finrank ℝ E * μ (Metric.ball 0 1) ≤
    2 ^ (Module.finrank ℝ E + 1) *
        ENNReal.ofReal (Metric.diam Ω ^ (Module.finrank ℝ E - 1) * Metric.infDist x₀ Ωᶜ) *
      (TauCeti.mongeAmpereMeasure μ fun x => if x ∈ Ω then ↑(u x) else ⊤) Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality](the-fenchel-young-inequality.md)
- [Rademacher's theorem for extended-real convex functions](rademachers-theorem-for-extended-real-convex-fun.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Basic.html#TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Basic.html#TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure)
- [Source of `TauCeti.ofReal_neg_pow_mul_addHaar_ball_le_mul_mongeAmpereMeasure` in TauCeti/Analysis/Convex/MongeAmpere/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/MongeAmpere/Basic.lean#L609)
