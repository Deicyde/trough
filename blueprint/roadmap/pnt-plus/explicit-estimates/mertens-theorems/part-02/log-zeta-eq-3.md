---
declaration: lemma
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_log_log_eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1584
---

# First integral identity

If $s > 1$ then $(s-1) \int_1^\infty \log \log x \cdot x^{-s}\ dx = -\log (s-1) + \Gamma'(1)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Writing $t = \log x$, the LHS is $(s-1) \int_0^\infty \log t e^{-(s-1) t}\ dt$. Now differentiate $\Gamma(z) = (s-1)^z \int_0^\infty t^{z-1} e^{-(s-1)t}\ dt$ in $z$ at $z=1$.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_log_log_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_log_log_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
