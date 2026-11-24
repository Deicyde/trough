---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_pow_four_eq
statement: formalized
proof: formalized
---

# zeta pow four eq

Corollary: $\zeta(s)^4 = \zeta(2s) \sum_{n=1}^{\infty} \tau(n)^2 n^{-s}$ for $\Re(s) > 1$.

```
This is IK (1.29).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [sigmaR](../part-01/sigmar.md)
- [zeta mul zeta mul zeta mul zeta eq](zeta-mul-zeta-mul-zeta-mul-zeta-eq.md)

## Proof

This is a special case of the previous theorem where we set $\alpha = \beta = 0$.

## Lean

Formalized as [`ArithmeticFunction.zeta_pow_four_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_pow_four_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
