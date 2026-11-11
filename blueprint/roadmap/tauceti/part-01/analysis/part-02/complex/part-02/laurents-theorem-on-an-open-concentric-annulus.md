---
declaration: theorem
origin: cited
lean: DifferentiableOn.hasLaurentSeriesOnAnnulus, TauCeti.hasLaurentSeriesOnAnnulus_of_differentiable_off_countable
statement: formalized
proof: formalized
---

# Laurent's theorem on an open concentric annulus

Every function `f : ℂ → E` into a complex
Banach space that is complex-differentiable on `Metric.eball c R \ Metric.closedBall c r` (`0 ≤ r`,
`r < ρ`, `ENNReal.ofReal ρ < R`) expands in a convergent Laurent series with coefficients
`circleLaurentCoeff f c ρ`.

```lean
DifferentiableOn.hasLaurentSeriesOnAnnulus.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {c : ℂ} {r ρ : ℝ} {R : ENNReal}
  (hf : DifferentiableOn ℂ f (Metric.eball c R \ Metric.closedBall c r)) (hr : 0 ≤ r) (hrρ : r < ρ)
  (hρR : ENNReal.ofReal ρ < R) :
  TauCeti.HasLaurentSeriesOnAnnulus f (TauCeti.circleLaurentCoeff f c ρ) c r R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DifferentiableOn.hasLaurentSeriesOnAnnulus`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Laurent/Expansion.html#DifferentiableOn.hasLaurentSeriesOnAnnulus).

## Other forms

**Laurent's theorem on an open concentric annulus (with countable exceptional set).** Formalized in Tau Ceti as [`TauCeti.hasLaurentSeriesOnAnnulus_of_differentiable_off_countable`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Laurent/Expansion.html#TauCeti.hasLaurentSeriesOnAnnulus_of_differentiable_off_countable).

```lean
TauCeti.hasLaurentSeriesOnAnnulus_of_differentiable_off_countable.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {c : ℂ} {r ρ : ℝ}
  {R : ENNReal} {s : Set ℂ} (hr : 0 ≤ r) (hrρ : r < ρ) (hρR : ENNReal.ofReal ρ < R)
  (hs : s.Countable) (hc : ContinuousOn f (Metric.eball c R \ Metric.closedBall c r))
  (hd : ∀ z ∈ (Metric.eball c R \ Metric.closedBall c r) \ s, DifferentiableAt ℂ f z) :
  TauCeti.HasLaurentSeriesOnAnnulus f (TauCeti.circleLaurentCoeff f c ρ) c r R
```

## Sources

- [Tau Ceti documentation: `DifferentiableOn.hasLaurentSeriesOnAnnulus`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Laurent/Expansion.html#DifferentiableOn.hasLaurentSeriesOnAnnulus)
- [Source of `DifferentiableOn.hasLaurentSeriesOnAnnulus` in TauCeti/Analysis/Complex/Laurent/Expansion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Laurent/Expansion.lean#L327)
