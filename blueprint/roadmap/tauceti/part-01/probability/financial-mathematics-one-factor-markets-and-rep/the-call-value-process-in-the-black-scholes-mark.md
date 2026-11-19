---
declaration: theorem
origin: cited
lean: TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion
statement: formalized
proof: formalized
---

# The call value process in the Black–Scholes market

For a stock with drift `μ` and
volatility `σ > 0` under `P`, and `u ≤ T`, the extended Black–Scholes call price at the spot `S_u`
and remaining maturity `T - u` is the discounted conditional expected payoff
`e^{-r (T - u)} E_Q[(S_T - K)⁺ | ℱ_u]` under the risk-neutral measure
`Q = P.tilted (-κ W_T ·)`, `κ = (μ - r) / σ`.

```lean
TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion.{u_1}
  {Ω : Type u_1} {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω}
  {ℱ : MeasureTheory.Filtration NNReal mΩ} {W : NNReal → Ω → ℝ} {σ K : ℝ} {u T : NNReal}
  (hW : TauCeti.Probability.IsFilteredPreBrownianReal ℱ W P) (s μ r : ℝ) (hσ : 0 < σ) (hK : 0 < K)
  (huT : u ≤ T) :
  (fun ω =>
      TauCeti.BlackScholes.callValue (TauCeti.Probability.geometricBrownianMotion s μ σ W u ω) r σ K
        (↑T - ↑u)) =ᵐ[P.tilted fun ω => -((μ - r) / σ) * W T ω]
    fun ω =>
    Real.exp (-r * (↑T - ↑u)) *
      (P.tilted fun ω => -((μ - r) / σ) * W T ω)[fun ω =>
          (TauCeti.Probability.geometricBrownianMotion s μ σ W T ω - K)⁺ | ↑ℱ u]
        ω
```

## Depends on

- [TauCeti.Probability.geometricBrownianMotion](tauceti-probability-geometricbrownianmotion.md)

## Proof depends on

- [The Black–Scholes call formula](the-black-scholes-call-formula.md)
- [Girsanov's theorem for a constant drift](girsanovs-theorem-for-a-constant-drift.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/ConditionalPrice.html#TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/ConditionalPrice.html#TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion)
- [Source of `TauCeti.Probability.IsFilteredPreBrownianReal.callValue_eq_condExp_tilted_geometricBrownianMotion` in TauCeti/Probability/Finance/BlackScholes/ConditionalPrice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/BlackScholes/ConditionalPrice.lean#L188)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
