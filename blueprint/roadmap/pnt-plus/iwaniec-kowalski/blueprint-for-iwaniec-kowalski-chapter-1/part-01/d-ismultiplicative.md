---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_isMultiplicative
statement: formalized
proof: formalized
---

# d isMultiplicative

$d_k$ is multiplicative for all $k$.

## Depends on

- [d](d.md)

## Proof depends on

- [d succ](d-succ.md)
- [d zero](d-zero.md)

## Proof

The function $d_k$ is defined as the $k$-fold Dirichlet convolution of $\zeta$. Since $\zeta$ is a multiplicative function, and the Dirichlet convolution of multiplicative functions is also multiplicative, it follows that $d_k$ is multiplicative for all $k$. This can be shown by induction on $k$, using the fact that the convolution of a multiplicative function with another multiplicative function remains multiplicative.

## Lean

Formalized as [`ArithmeticFunction.d_isMultiplicative`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_isMultiplicative).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
