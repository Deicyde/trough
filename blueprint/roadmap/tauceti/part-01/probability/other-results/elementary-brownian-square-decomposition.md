---
declaration: theorem
origin: cited
lean: TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub
statement: formalized
proof: formalized
---

# Elementary Brownian square decomposition

Squared elementary gains minus the
sum of squared heights times elapsed interval lengths form a true martingale. The
compensator is random pathwise energy, not its expectation. The process is defined
at all observation times, including times inside trading intervals.

```lean
TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub.{u_1} {Ω : Type u_1}
  {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω} {ℱ : MeasureTheory.Filtration NNReal mΩ}
  {W : NNReal → Ω → ℝ} (hW : TauCeti.Probability.IsFilteredPreBrownianReal ℱ W P) {τ : ℕ → NNReal}
  {n : ℕ} {a : ℕ → Ω → ℝ} (hτ : MonotoneOn τ (Set.Iic n))
  (ha : ∀ i < n, MeasureTheory.StronglyMeasurable (a i))
  (ha₂ : ∀ i < n, MeasureTheory.MemLp (a i) 2 P) :
  MeasureTheory.Martingale
    (fun t ω =>
      TauCeti.Finance.simpleGains τ n a W t ω ^ 2 -
        ∑ i ∈ Finset.range n, a i ω ^ 2 * (↑(min (τ (i + 1)) t) - ↑(min (τ i) t)))
    ℱ P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Integral/Square.html#TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub`](https://taucetiproject.org/docs/TauCeti/Probability/BrownianMotion/Integral/Square.html#TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub)
- [Source of `TauCeti.Probability.IsFilteredPreBrownianReal.martingale_sq_simpleGains_sub` in TauCeti/Probability/BrownianMotion/Integral/Square.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/BrownianMotion/Integral/Square.lean#L110)
