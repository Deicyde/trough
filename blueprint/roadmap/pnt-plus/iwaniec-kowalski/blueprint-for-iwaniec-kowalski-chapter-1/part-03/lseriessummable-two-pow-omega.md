---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeriesSummable.of_norm_le_norm, ArithmeticFunction.LSeriesSummable_two_pow_omega
statement: formalized
proof: formalized
---

# LSeriesSummable-two-pow-omega

An L-series is convergent if the absolute value of each term is term wise less than a summable series.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [d](../part-01/d.md)
- [two-pow-omega-le-sigma-zero](two-pow-omega-le-sigma-zero.md)
- [d two](../part-01/d-two.md)
- [LSeries d summable](../part-01/lseries-d-summable.md)

## Proof

Apply triangle inequality and comparison test.

## Lean

Formalized as [`ArithmeticFunction.LSeriesSummable.of_norm_le_norm`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeriesSummable.of_norm_le_norm), [`ArithmeticFunction.LSeriesSummable_two_pow_omega`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeriesSummable_two_pow_omega).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
