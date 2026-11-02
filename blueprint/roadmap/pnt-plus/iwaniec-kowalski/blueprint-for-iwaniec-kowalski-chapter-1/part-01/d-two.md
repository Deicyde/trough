---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_two
statement: formalized
proof: formalized
---

# d two

$d_2$ is the classical divisor count function $\tau$.

## Depends on

- [d](d.md)

## Proof depends on

- [zeta mul zeta](zeta-mul-zeta.md)

## Proof

By definition, $d_k$ is the $k$-fold Dirichlet convolution of $\zeta$. When $k = 2$, this means we are taking the convolution of $\zeta$ with itself twice, which gives us $\zeta * \zeta$. From the earlier theorem, we know that $\zeta * \zeta = \tau$, where $\tau$ is the divisor count function. Therefore, $d_2 = \zeta^2 = \tau$.

## Lean

Formalized as [`ArithmeticFunction.d_two`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_two).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
