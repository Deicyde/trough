---
declaration: proposition
origin: cited
lean: Mertens.E₁.summable
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1352
---

# $E_1$ summable

The series $E_1 := \sum_p \frac{\log p}{p(p-1)}$ converges.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have $\sum_{n=2}^\infty \frac{\log n}{n(n-1)}$ converges by comparison with $\sum_{n=2}^\infty \frac{2\log n}{n^2}$, which converges by the integral test. By a further application of comparison test we can conclude that $E_1$ converges as well. Alternatively bound $\log n$ by $2\sqrt n$ and use the existing Mathlib API for $\sum n^{-3/2}$.

## Lean

Formalized as [`Mertens.E₁.summable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁.summable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
