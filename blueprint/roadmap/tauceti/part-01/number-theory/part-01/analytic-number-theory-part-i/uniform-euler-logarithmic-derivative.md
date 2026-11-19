---
declaration: theorem
origin: cited
lean: DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le
statement: formalized
proof: formalized
---

# Uniform Euler logarithmic derivative

For `1 < re s`,
`‖L′/L(s, χ) + ∑ₚ χ(p) log p / p ^ s‖` is at most `∑ₙ (if n is prime then 0 else Λ(n)) / n`,
a constant independent of the level, the character and `s`.

```lean
DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le {N : ℕ} (χ : DirichletCharacter ℂ N)
  {s : ℂ} [NeZero N] (hs : 1 < s.re) :
  ‖logDeriv (DirichletCharacter.LFunction χ) s +
        ∑' (p : Nat.Primes), χ ↑↑p * ↑(Real.log ↑↑p) / ↑↑p ^ s‖ ≤
    ∑' (n : ℕ), (if Nat.Prime n then 0 else ArithmeticFunction.vonMangoldt n) / ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/LFunction/LogDeriv.html#DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DirichletCharacter/LFunction/LogDeriv.html#DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le)
- [Source of `DirichletCharacter.norm_logDeriv_LFunction_add_tsum_prime_le` in TauCeti/NumberTheory/DirichletCharacter/LFunction/LogDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/DirichletCharacter/LFunction/LogDeriv.lean#L122)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
