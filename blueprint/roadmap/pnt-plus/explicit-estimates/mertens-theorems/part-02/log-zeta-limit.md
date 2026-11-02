---
declaration: lemma
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_limit
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1586
---

# limiting behavior of log zeta

One has $\log \zeta(s) = - \log(s-1) + o(1)$ as $s \to 1^+$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Start with the asymptotic $\zeta(s) = \frac{1}{s-1} + O(1)$ and take logarithms.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_limit`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.log_zeta_limit).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
