---
declaration: theorem
origin: cited
lean: MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq
statement: formalized
proof: formalized
---

# MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq

A predictable holding with almost surely finite weighted time mass and square energy
admits bounded, left-measurable finite-grid approximations whose pathwise weighted
square-energy errors tend to zero almost surely. The sample measure need only be s-finite;
the time measure need only be s-finite and have no initial atom. The weight need only be
almost everywhere measurable on the product; no expected-energy bound, Brownian motion,
or usual filtration conditions are assumed.

```lean
MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq.{u_1}
  {Ω : Type u_1} {mΩ : MeasurableSpace Ω} {ℱ : MeasureTheory.Filtration NNReal mΩ}
  {P : MeasureTheory.Measure Ω} [MeasureTheory.SFinite P] {ν : MeasureTheory.Measure NNReal}
  [MeasureTheory.SFinite ν] {H : NNReal → Ω → ℝ} (hH : MeasureTheory.IsStronglyPredictable ℱ H)
  (hν : ν {0} = 0) {w : NNReal × Ω → ENNReal} (hw : AEMeasurable w (ν.prod P))
  (hfin : ∀ᵐ (ω : Ω) ∂P, ∫⁻ (t : NNReal), w (t, ω) * (1 + ‖H t ω‖ₑ ^ 2) ∂ν < ⊤) :
  ∃ n τ a C,
    (∀ (k : ℕ), τ k 0 = 0) ∧
      (∀ (k : ℕ), StrictMonoOn (τ k) (Set.Iic (n k))) ∧
        (∀ (k j : ℕ), j < n k → MeasureTheory.StronglyMeasurable (a k j)) ∧
          (∀ (k j : ℕ), j < n k → ∀ (ω : Ω), ‖a k j ω‖ ≤ C k) ∧
            ∀ᵐ (ω : Ω) ∂P,
              Filter.Tendsto
                (fun k =>
                  ∫⁻ (t : NNReal),
                    w (t, ω) *
                      ‖TauCeti.Finance.simpleHolding (τ k) (n k) (a k) t ω - H t ω‖ₑ ^ 2 ∂ν)
                Filter.atTop (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/SimpleStrategy/WeightedApproximation.html#MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq).

## Sources

- [Tau Ceti documentation: `MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/SimpleStrategy/WeightedApproximation.html#MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq)
- [Source of `MeasureTheory.IsStronglyPredictable.exists_seq_simpleHolding_ae_tendsto_lintegral_mul_enorm_sub_sq` in TauCeti/Probability/Finance/SimpleStrategy/WeightedApproximation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/SimpleStrategy/WeightedApproximation.lean#L48)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
