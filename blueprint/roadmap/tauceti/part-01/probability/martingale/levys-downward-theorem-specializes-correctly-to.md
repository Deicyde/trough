---
declaration: theorem
origin: cited
lean: TauCeti.Probability.tendsto_ae_condExp_of_eventually_const
statement: formalized
proof: formalized
---

# Lévy's downward theorem specializes correctly to an eventually constant filtration

Run the flagship `MeasureTheory.tendsto_ae_condExp_iInf` on an antitone filtration that is
constant from index `N` on, then collapse its limit through
`condExp_iInf_eq_of_eventually_const`. The a.e. limit it delivers is `μ[f | 𝔽 N]` — exactly the
value the sequence already reaches by the elementary
`tendsto_condExp_of_eventually_const`. The general and elementary computations agree.

```lean
TauCeti.Probability.tendsto_ae_condExp_of_eventually_const.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  {μ : MeasureTheory.Measure Ω} {𝔽 : ℕ → MeasurableSpace Ω} [MeasureTheory.IsFiniteMeasure μ]
  (h_anti : Antitone 𝔽) (h_le0 : 𝔽 0 ≤ inferInstance) {N : ℕ}
  (h_const : ∀ (n : ℕ), N ≤ n → 𝔽 n = 𝔽 N) (f : Ω → ℝ) :
  ∀ᵐ (ω : Ω) ∂μ, Filter.Tendsto (fun n => μ[f | 𝔽 n] ω) Filter.atTop (nhds (μ[f | 𝔽 N] ω))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.tendsto_ae_condExp_of_eventually_const`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/LevyDownwardEventuallyConst.html#TauCeti.Probability.tendsto_ae_condExp_of_eventually_const).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.tendsto_ae_condExp_of_eventually_const`](https://taucetiproject.org/docs/TauCeti/Probability/Martingale/LevyDownwardEventuallyConst.html#TauCeti.Probability.tendsto_ae_condExp_of_eventually_const)
- [Source of `TauCeti.Probability.tendsto_ae_condExp_of_eventually_const` in TauCeti/Probability/Martingale/LevyDownwardEventuallyConst.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Martingale/LevyDownwardEventuallyConst.lean#L88)
