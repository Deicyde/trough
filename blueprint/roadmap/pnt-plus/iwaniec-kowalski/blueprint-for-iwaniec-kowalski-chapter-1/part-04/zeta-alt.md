---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_alt
statement: formalized
proof: formalized
---

# zeta alt

$$
\zeta(s) =\zeta(2s) \sum_{n=1}^{\infty}\mu^2(n)n^{-s}.
$$

```
An expression for `ζ`, in IK (1.32).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [moebius-sq-LSeries-eulerProduct-tprod](moebius-sq-lseries-eulerproduct-tprod.md)
- [moebius-sq-LSeries-eulerProduct-hasProd](moebius-sq-lseries-eulerproduct-hasprod.md)
- [Complex.one-add-prime-cpow-ne-zero](../part-03/complex-one-add-prime-cpow-ne-zero.md)

## Proof

The series $\sum_{n=1}^{\infty}\mu^2(n)n^{-s}$ has Euler product $\prod_{p} (1 + p^{-s})$. On the other hand, $\zeta(2s)=\prod_p (1 - p^{-2s})^{-1}$. The product of these two Euler products is $\prod_p (1 - p^{-s})^{-1} = \zeta(s)$, which gives the desired formula.

## Lean

Formalized as [`ArithmeticFunction.zeta_alt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_alt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
