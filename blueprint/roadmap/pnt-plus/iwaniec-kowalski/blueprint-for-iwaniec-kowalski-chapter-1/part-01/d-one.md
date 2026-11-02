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

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
