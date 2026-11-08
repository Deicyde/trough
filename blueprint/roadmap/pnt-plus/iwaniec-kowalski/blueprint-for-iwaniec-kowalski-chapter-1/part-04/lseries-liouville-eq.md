---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeries_liouville_eq
statement: formalized
---

# LSeries liouville eq

The Dirichlet series of the Liouville function is $\zeta(2s)/\zeta(s)$.

## Depends on

- [liouville](liouville.md)

## Proof

The Liouville function $\lambda(n)$ is multiplicative, and its value at prime powers is given by $\lambda(p^k) = (-1)^k$. The Dirichlet series of $\lambda$ can be expressed as an Euler product over primes:

$$
L(\lambda, s) = \prod_{p} \left(1 + \lambda(p)p^{-s} + \lambda(p^2)p^{-2s} + \ldots\right) = \prod_{p} \left(1 - p^{-s}\right) \left(1 - p^{-2s}\right)^{-1} = \frac{\zeta(2s)}{\zeta(s)}.
$$

## Lean

Stated as [`ArithmeticFunction.LSeries_liouville_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeries_liouville_eq); the blueprint marks no proof of it as formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
