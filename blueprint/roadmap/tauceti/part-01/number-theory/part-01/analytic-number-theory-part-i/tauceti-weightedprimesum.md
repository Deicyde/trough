---
declaration: def
origin: cited
lean: TauCeti.weightedPrimeSum
statement: formalized
---

# TauCeti.weightedPrimeSum

The weighted prime sum `Σ_{p ≤ x} (log p / p) • a p`, as a finite sum over the primes in
`Nat.primesLE ⌊x⌋₊`.

```lean
TauCeti.weightedPrimeSum.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] (a : ℕ → E)
  (x : ℝ) : E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.weightedPrimeSum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.html#TauCeti.weightedPrimeSum).

## Sources

- [Tau Ceti documentation: `TauCeti.weightedPrimeSum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.html#TauCeti.weightedPrimeSum)
- [Source of `TauCeti.weightedPrimeSum` in TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/WeightedPrimeMellin.lean#L69)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
