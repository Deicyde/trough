---
declaration: theorem
origin: cited
lean: ArithmeticFunction.LSeriesSummable_moebius_sq
statement: formalized
proof: formalized
---

# LSeriesSummable-moebius-sq

The $L$-series with coefficients given by $\mu^2(n)$ converges on the region $1\lt \Re(s)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [LSeriesSummable-two-pow-omega](lseriessummable-two-pow-omega.md)

## Proof

This follows by comparison test against the Riemann zeta function.

## Lean

Formalized as [`ArithmeticFunction.LSeriesSummable_moebius_sq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.LSeriesSummable_moebius_sq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
