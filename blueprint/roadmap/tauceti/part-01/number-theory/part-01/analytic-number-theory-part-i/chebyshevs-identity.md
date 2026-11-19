---
declaration: theorem
origin: cited
lean: Chebyshev.log_floor_factorial_eq_sum_vonMangoldt, Chebyshev.log_floor_factorial_eq_sum_psi
statement: formalized
proof: formalized
---

# Chebyshev's identity

`log ⌊x⌋₊! = ∑_{1 ≤ n ≤ x} Λ(n) ⌊x / n⌋₊` for every real `x`.

```lean
Chebyshev.log_floor_factorial_eq_sum_vonMangoldt (x : ℝ) :
  Real.log ↑⌊x⌋₊.factorial = ∑ n ∈ Finset.Ioc 0 ⌊x⌋₊, ArithmeticFunction.vonMangoldt n * ↑⌊x / ↑n⌋₊
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Chebyshev.log_floor_factorial_eq_sum_vonMangoldt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/LogFactorial.html#Chebyshev.log_floor_factorial_eq_sum_vonMangoldt).

## Other forms

**Chebyshev's identity in terms of `ψ`.** Formalized in Tau Ceti as [`Chebyshev.log_floor_factorial_eq_sum_psi`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/LogFactorial.html#Chebyshev.log_floor_factorial_eq_sum_psi).

```lean
Chebyshev.log_floor_factorial_eq_sum_psi (x : ℝ) :
  Real.log ↑⌊x⌋₊.factorial = ∑ m ∈ Finset.Ioc 0 ⌊x⌋₊, Chebyshev.psi (x / ↑m)
```

## Sources

- [Tau Ceti documentation: `Chebyshev.log_floor_factorial_eq_sum_vonMangoldt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/LogFactorial.html#Chebyshev.log_floor_factorial_eq_sum_vonMangoldt)
- [Source of `Chebyshev.log_floor_factorial_eq_sum_vonMangoldt` in TauCeti/NumberTheory/Chebyshev/LogFactorial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/LogFactorial.lean#L40)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)
