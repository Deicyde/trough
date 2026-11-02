---
declaration: lemma
origin: cited
lean: _private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_gamma_eq
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1585
---

# Second integral identity

If $s > 1$ then $(s-1) \int_1^\infty \gamma \cdot x^{-s}\ dx = \gamma$.

## Depends on

- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)

## Proof

Apply the fundamental theorem of calculus.

## Lean

Formalized as [`_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_gamma_eq`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/_private.PrimeNumberTheoremAnd.IEANTN.Mertens.0.Mertens.mul_integ_gamma_eq).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
