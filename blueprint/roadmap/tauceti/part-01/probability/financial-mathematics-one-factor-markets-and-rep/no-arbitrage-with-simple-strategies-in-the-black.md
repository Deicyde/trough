---
declaration: theorem
origin: cited
lean: TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion
statement: formalized
proof: formalized
---

# No arbitrage with simple strategies in the Black–Scholes market

Let the stock have drift
`μ` and volatility `σ ≠ 0`, let the bond be `e^{r t}`, and let `Q = P.tilted (-κ W_T ·)`,
`κ = (μ - r) / σ`, be the risk-neutral measure for the horizon `T`. No self-financing simple
strategy trading at dates `τ 0 ≤ ⋯ ≤ τ (n + 1) ≤ T`, whose stock holdings `a j` are chosen at
`τ j` and whose trades in the discounted stock have `Q`-integrable gains, is an arbitrage under
`P`.

```lean
TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion.{u_1}
  {Ω : Type u_1} {mΩ : MeasurableSpace Ω} {P : MeasureTheory.Measure Ω}
  {ℱ : MeasureTheory.Filtration NNReal mΩ} {W : NNReal → Ω → ℝ} {σ : ℝ} {T : NNReal}
  (hW : TauCeti.Probability.IsFilteredPreBrownianReal ℱ W P) (s μ r : ℝ) (hσ : σ ≠ 0)
  {τ : ℕ → NNReal} {n : ℕ} {a b : ℕ → Ω → ℝ}
  (h :
    TauCeti.Finance.IsSelfFinancing τ (n + 1) a b
      (TauCeti.Probability.geometricBrownianMotion s μ σ W) fun t x => Real.exp (r * ↑t))
  (hτ : MonotoneOn τ (Set.Iic (n + 1))) (hτT : τ (n + 1) ≤ T)
  (ha : ∀ j < n + 1, MeasureTheory.StronglyMeasurable (a j))
  (hint :
    ∀ j < n + 1,
      MeasureTheory.Integrable
        (fun ω =>
          a j ω *
            (TauCeti.Probability.geometricBrownianMotion s μ σ W (τ (j + 1)) ω /
                Real.exp (r * ↑(τ (j + 1))) -
              TauCeti.Probability.geometricBrownianMotion s μ σ W (τ j) ω / Real.exp (r * ↑(τ j))))
        (P.tilted fun ω => -((μ - r) / σ) * W T ω)) :
  ¬TauCeti.Finance.IsArbitrage P
      (fun ω =>
        a 0 ω * TauCeti.Probability.geometricBrownianMotion s μ σ W (τ 0) ω +
          b 0 ω * Real.exp (r * ↑(τ 0)))
      fun ω =>
      a n ω * TauCeti.Probability.geometricBrownianMotion s μ σ W (τ (n + 1)) ω +
        b n ω * Real.exp (r * ↑(τ (n + 1)))
```

## Depends on

- [TauCeti.Finance.IsSelfFinancing](tauceti-finance-isselffinancing.md)
- [TauCeti.Probability.geometricBrownianMotion](tauceti-probability-geometricbrownianmotion.md)

## Proof depends on

- [Girsanov's theorem for a constant drift](girsanovs-theorem-for-a-constant-drift.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/NoArbitrage.html#TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/BlackScholes/NoArbitrage.html#TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion)
- [Source of `TauCeti.Probability.IsFilteredPreBrownianReal.not_isArbitrage_geometricBrownianMotion` in TauCeti/Probability/Finance/BlackScholes/NoArbitrage.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/BlackScholes/NoArbitrage.lean#L111)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
