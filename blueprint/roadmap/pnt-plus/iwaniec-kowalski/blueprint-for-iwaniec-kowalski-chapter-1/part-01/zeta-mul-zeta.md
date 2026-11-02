---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_mul_zeta
statement: formalized
proof: formalized
---

# zeta mul zeta

The Dirichlet convolution of $\zeta$ with itself is $\tau$ (the divisor count function).

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By definition of $\zeta$, we have $\zeta(n) = 1$ for all $n \geq 1$. Thus, the Dirichlet convolution $(\zeta * \zeta)(n)$ counts the number of ways to write $n$ as a product of two positive integers, which is exactly the number of divisors of $n$, i.e., $\tau(n)$.

## Lean

Formalized as [`ArithmeticFunction.zeta_mul_zeta`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_mul_zeta).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
