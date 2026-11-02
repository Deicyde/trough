---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_pow_three_eq_alt
statement: formalized
---

# zeta pow three eq alt

symmetric square $L$-function for $\zeta^2$:

$$
\zeta(s)^3 = \sum_{n=1}^{\infty} \left( \sum_{d^2 m = n} \tau(m^2) \right) n^{-s}
$$

for $\Re(s) > 1$.

```
Alternative expression for `ζ^3`, in IK between (1.30) and (1.31).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is an alternative expression for $\zeta(s)^3$ that can be derived from the previous results. By expressing $\zeta(s)^3$ in terms of the L-series of $\tau(n^2)$ and using the properties of Dirichlet convolutions, we can rewrite the sum in a way that involves summing over divisors $d$ and corresponding $m$ such that $d^2 m = n$. This rearrangement of the series allows us to express $\zeta(s)^3$ in the desired form.

## Lean

Formalized as [`ArithmeticFunction.zeta_pow_three_eq_alt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_pow_three_eq_alt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
