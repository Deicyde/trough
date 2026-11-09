---
declaration: theorem
origin: cited
lean: TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval, TauCeti.Probability.IsFilteredPreBrownianReal.isBrownianReal_sub_mul_min_tilted_mul_eval
statement: formalized
proof: formalized
---

# Girsanov's theorem for a constant drift

If `W` is a Brownian motion relative to `ℱ`
under `P`, then `t ↦ W t - θ min(t, T)` is a Brownian motion relative to `ℱ` under the measure
`P.tilted (θ * W T ·)`, whose density with respect to `P` is `exp (θ W_T - θ² T / 2)`.

```lean
TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval.{u_1} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω} {ℱ : MeasureTheory.Filtration NNReal mΩ}
  {W : NNReal → Ω → ℝ} (hW : TauCeti.Probability.IsFilteredPreBrownianReal ℱ W P) (θ : ℝ)
  (T : NNReal) :
  TauCeti.Probability.IsFilteredPreBrownianReal ℱ (fun t ω => W t ω - θ * ↑(min t T))
    (P.tilted fun ω => θ * W T ω)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Probability.setIntegral_exp_mul_gaussianReal](../financial-mathematics-one-factor-markets-and-rep/tauceti-probability-setintegral-exp-mul-gaussian.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Girsanov.html#TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval).

## Other forms

**Girsanov's theorem for a constant drift, with continuous paths.** Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPreBrownianReal.isBrownianReal_sub_mul_min_tilted_mul_eval`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Girsanov.html#TauCeti.Probability.IsFilteredPreBrownianReal.isBrownianReal_sub_mul_min_tilted_mul_eval).

```lean
TauCeti.Probability.IsFilteredPreBrownianReal.isBrownianReal_sub_mul_min_tilted_mul_eval.{u_1}
  {Ω : Type u_1} {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω}
  {ℱ : MeasureTheory.Filtration NNReal mΩ} {W : NNReal → Ω → ℝ}
  (hW : TauCeti.Probability.IsFilteredPreBrownianReal ℱ W P)
  (hcont : ∀ᵐ (ω : Ω) ∂P, Continuous fun x => W x ω) (θ : ℝ) (T : NNReal) :
  ProbabilityTheory.IsBrownianReal (fun t ω => W t ω - θ * ↑(min t T)) (P.tilted fun ω => θ * W T ω)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Girsanov.html#TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval)
- [Source of `TauCeti.Probability.IsFilteredPreBrownianReal.sub_mul_min_tilted_mul_eval` in TauCeti/Probability/BrownianMotion/Girsanov.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/BrownianMotion/Girsanov.lean#L120)
