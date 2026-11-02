---
declaration: theorem
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1319
---

# An identity for $\log \zeta(s)$

If $s > 1$ then $\log\zeta(s) = - \log (s-1) + \Gamma'(1) + \gamma + (s-1) \int_1^\infty E_{2,\Lambda}(x) x^{-s}\ ds$.

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)

## Proof depends on

- [First integral identity](log-zeta-eq-3.md)
- [Integration by parts identity for $\log \zeta(s)$](log-zeta-eq-2.md)
- [Second integral identity](log-zeta-eq-4.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Bound for second Mertens error (von Mangoldt form)](mertens-second-error-mangoldt-bound.md)

## Proof

Combine the previous four sublemmas.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
