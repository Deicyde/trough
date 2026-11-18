---
declaration: theorem
origin: cited
lean: ArithmeticFunction.two_pow_omega_LSeries_eulerProduct_tprod
statement: formalized
proof: formalized
---

# two-pow-omega-LSeries-eulerProduct-tprod

For $1\lt \Re(s)$ we have that

$$
\sum_{1\leq n}2^{\omega(n)}n^{-s}=\prod_p\frac{1+p^{-s}}{1-p^{-s}}.
$$

The naming convention here is designed to match

```
riemannZeta_eulerProduct_tprod
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [two-pow-omega-tsum-prime-pow](two-pow-omega-tsum-prime-pow.md)
- [two-pow-omega-LSeries.term-isMultiplicative](two-pow-omega-lseries-term-ismultiplicative.md)
- [LSeriesSummable-two-pow-omega](lseriessummable-two-pow-omega.md)
- [sumOnPrimePows-apply](sumonprimepows-apply.md)
- [sumOnPrimePows](sumonprimepows.md)

## Proof

Immediately follows from Lemmas two-pow-omega-LSeries.term-IsMultiplicative and two-pow-omega-tsum-prime-pow.

## Lean

Formalized as [`ArithmeticFunction.two_pow_omega_LSeries_eulerProduct_tprod`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.two_pow_omega_LSeries_eulerProduct_tprod).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
