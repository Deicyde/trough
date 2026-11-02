---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_pow_three_eq'
statement: formalized
proof: formalized
---

# zeta pow three eq

Zeta cubed: $\zeta(s)^3 = \zeta(2s) \sum_{n=1}^{\infty}\tau(n^2) n^{-s}$.

```
This is IK (1.30).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [zeta mul tau square eq](../part-02/zeta-mul-tau-square-eq.md)
- [zeta pow four eq](../part-02/zeta-pow-four-eq.md)

## Proof

This follows from the previous two theorems. From the corollary of Ramanujan's formula, we have $\zeta(s)^4 = \zeta(2s) \sum_{n=1}^{\infty} \tau(n)^2 n^{-s}$. From the Baby Rankin-Selberg result, we have $\zeta(s) \sum_{n=1}^{\infty} \tau(n^2) n^{-s} = \sum_{n=1}^{\infty} \tau(n)^2 n^{-s}$. Combining these two results, we can express $\zeta(s)^4$ in terms of $\zeta(s)$ and $\sum_{n=1}^{\infty} \tau(n^ 2) n^{-s}$, which leads to the conclusion that $\zeta(s)^3 = \zeta(2s) \sum_{n=1}^{\infty} \tau(n^2) n^{-s}$.

## Lean

Formalized as [`ArithmeticFunction.zeta_pow_three_eq'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_pow_three_eq').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
