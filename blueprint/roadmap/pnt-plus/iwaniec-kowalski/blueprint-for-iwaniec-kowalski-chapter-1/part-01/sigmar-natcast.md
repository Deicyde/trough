---
declaration: theorem
origin: cited
lean: ArithmeticFunction.sigmaR_natCast
statement: formalized
proof: formalized
---

# sigmaR-natCast

For natural exponents, $\sigma^R$ agrees with $\sigma$.

## Depends on

- [sigmaR](sigmar.md)

## Proof

The function $\sigma^R$ is defined as the sum of the $s$-th powers of the divisors of $n$. When $s$ is a natural number $k$, this definition coincides with the classical divisor power sum function $\sigma_k(n)$, which also sums the $k$-th powers of the divisors of $n$. Therefore, for natural exponents, we have $\sigma^R_k(n) = \sigma_k(n)$ when we view $\sigma_k(n)$ as a complex number. This can be shown by directly comparing the definitions and noting that both functions sum over the same set of divisors with the same exponentiation.

## Lean

Formalized as [`ArithmeticFunction.sigmaR_natCast`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.sigmaR_natCast).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
