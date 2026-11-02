---
declaration: lemma
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq_integ
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1583
---

# Integration by parts identity for $\log \zeta(s)$

If $s > 1$ then $\log\zeta(s) = (s-1) \int_1^\infty (\log \log x + \gamma + E_{2,\Lambda}(x)) x^{-s})\ dx$.

## Depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)

## Proof depends on

- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Dirichlet series for $\log \zeta(s)$](log-zeta-eq-1.md)

## Proof

Apply the preceding identity then integrate by parts.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq_integ`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_eq_integ).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
