---
declaration: def
origin: cited
lean: TauCeti.waldschmidtDeltaOperator
statement: formalized
---

# TauCeti.waldschmidtDeltaOperator

Waldschmidt's delta polynomial `δ_k(X; σ) = Δ(X; k) ^ q Δ(X; r)`, where `σ = k q + r` with
`0 ≤ r < k` and `Δ(X; k) = (X + 1) ⋯ (X + k) / k!` is Baker's binomial polynomial. For `k = 0` it
is `Δ(X; σ)`. Used as the differential operator `δ_k(∂/∂z₀; σ)`, it replaces the iterated
derivative `∂^σ/∂z₀^σ` in the columns of the interpolation matrix.

```lean
TauCeti.waldschmidtDeltaOperator (k σ : ℕ) : Polynomial ℚ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.waldschmidtDeltaOperator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Delta/Operator.html#TauCeti.waldschmidtDeltaOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.waldschmidtDeltaOperator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Delta/Operator.html#TauCeti.waldschmidtDeltaOperator)
- [Source of `TauCeti.waldschmidtDeltaOperator` in TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Delta/Operator.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Transcendental/Waldschmidt/Interpolation/Delta/Operator.lean#L76)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
