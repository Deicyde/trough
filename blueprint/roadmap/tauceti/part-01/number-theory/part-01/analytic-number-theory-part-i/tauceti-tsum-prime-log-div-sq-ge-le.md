---
declaration: theorem
origin: cited
lean: TauCeti.tsum_prime_log_div_sq_ge_le
statement: formalized
proof: formalized
---

# TauCeti.tsum_prime_log_div_sq_ge_le

For `y > 0`, the sum of `log p / p²` over primes `p ≥ y` is at most
`2 log 4 / y`, including a prime at the lower endpoint.

```lean
TauCeti.tsum_prime_log_div_sq_ge_le {y : ℝ} (hy : 0 < y) :
  (∑' (n : ℕ), if Nat.Prime n ∧ y ≤ ↑n then Real.log ↑n / ↑n ^ 2 else 0) ≤ 2 * Real.log 4 / y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_prime_log_div_sq_ge_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/PrimeTail.html#TauCeti.tsum_prime_log_div_sq_ge_le).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_prime_log_div_sq_ge_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/PrimeTail.html#TauCeti.tsum_prime_log_div_sq_ge_le)
- [Source of `TauCeti.tsum_prime_log_div_sq_ge_le` in TauCeti/NumberTheory/Chebyshev/PrimeTail.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/PrimeTail.lean#L221)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
