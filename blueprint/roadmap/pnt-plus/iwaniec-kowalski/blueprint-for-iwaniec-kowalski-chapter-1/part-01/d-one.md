---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_one
statement: formalized
proof: formalized
---

# d one

$d_1$ is $\zeta$.

## Depends on

- [d](d.md)

## Proof

By definition, $d_k$ is the $k$-fold Dirichlet convolution of $\zeta$. When $k = 1$, this means we are taking the convolution of $\zeta$ with itself once, which simply gives us $\zeta$. Therefore, $d_1 = \zeta^1 = \zeta$.

## Lean

Formalized as [`ArithmeticFunction.d_one`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_one).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
