---
declaration: theorem
origin: cited
lean: ArithmeticFunction.d_succ
statement: formalized
proof: formalized
---

# d succ

Recurrence: $d_{k+1} = d_k * \zeta$.

## Depends on

- [d](d.md)

## Proof

By definition, $d_k$ is the $k$-fold Dirichlet convolution of $\zeta$. Therefore, $d_{k + 1}$ is the $(k + 1)$-fold convolution of $\zeta$, which can be expressed as the convolution of $d_k$ (the $k$-fold convolution) with $\zeta$. Thus, we have $d_{k + 1} = d_k * \zeta$.

## Lean

Formalized as [`ArithmeticFunction.d_succ`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.d_succ).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
