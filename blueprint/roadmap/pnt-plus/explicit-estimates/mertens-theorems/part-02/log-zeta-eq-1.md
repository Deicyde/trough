---
declaration: lemma
origin: cited
lean: Mertens.log_zeta_eq_sum
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1582
---

# Dirichlet series for $\log \zeta(s)$

If $s > 1$ then $\log\zeta(s) = - \log (s-1) + \Gamma'(1) + \gamma + (s-1) \int_1^\infty E_{2,\Lambda}(x) x^{-s}\ ds$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

First use the fundamental theorem of calculus and decay of $\log \zeta(s)$ to write

$$
\log \zeta(s) = \int_s^\infty -\frac{\zeta'(u)}{\zeta(u)}\ du.
$$

Then substitute in the known identity $-\frac{\zeta'(u)}{\zeta(u)} = \sum_n \frac{\Lambda(n)}{n^u}$ and integrate term by term.

## Lean

Formalized as [`Mertens.log_zeta_eq_sum`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.log_zeta_eq_sum).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
