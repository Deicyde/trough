---
declaration: theorem
origin: cited
lean: TauCeti.hasSum_weightedPrimeSeries
statement: formalized
proof: formalized
---

# The weighted-prime Mellin identity

for weights bounded by `1` on primes and `η > 0`,
`Σ_p (log p / p^(1+η)) • a p = η ∫_{t > 1} t^(-1-η) • A(t) dt`.

```lean
TauCeti.hasSum_weightedPrimeSeries.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [CompleteSpace E] {a : ℕ → E} (ha : ∀ (p : ℕ), Nat.Prime p → ‖a p‖ ≤ 1) {η : ℝ} (hη : 0 < η) :
  HasSum (fun p => (Real.log ↑↑p / ↑↑p ^ (1 + η)) • a ↑p)
    (TauCeti.mellinWeightIntegral η (TauCeti.weightedPrimeSum a))
```

## Depends on

- [TauCeti.mellinWeightIntegral](tauceti-mellinweightintegral.md)
- [TauCeti.weightedPrimeSum](tauceti-weightedprimesum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_weightedPrimeSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.html#TauCeti.hasSum_weightedPrimeSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_weightedPrimeSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.html#TauCeti.hasSum_weightedPrimeSeries)
- [Source of `TauCeti.hasSum_weightedPrimeSeries` in TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.lean#L346)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
