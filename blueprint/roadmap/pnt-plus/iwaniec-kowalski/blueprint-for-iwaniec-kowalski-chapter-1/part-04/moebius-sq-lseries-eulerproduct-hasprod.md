---
declaration: theorem
origin: cited
lean: ArithmeticFunction.moebius_sq_LSeries_eulerProduct_hasProd
statement: formalized
proof: formalized
---

# moebius-sq-LSeries-eulerProduct-hasProd

For $1\lt \Re(s)$ we have that

$$
\sum_{1\leq n}\mu^2(n)n^{-s}=\prod_p(1+p^{-s}).
$$

The naming convention here is designed to match

```
riemannZeta_eulerProduct_hasProd
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [LSeriesSummable-moebius-sq](../part-03/lseriessummable-moebius-sq.md)
- [moebius-sq-tsum-prime-pow](../part-03/moebius-sq-tsum-prime-pow.md)
- [moebius-sq-LSeries.term-isMultiplicative](../part-03/moebius-sq-lseries-term-ismultiplicative.md)

## Proof

Immediately follows from Lemmas moebius-sq-LSeries.term-IsMultiplicative and moebius-sq-tsum-prime-pow.

## Lean

Formalized as [`ArithmeticFunction.moebius_sq_LSeries_eulerProduct_hasProd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.moebius_sq_LSeries_eulerProduct_hasProd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
