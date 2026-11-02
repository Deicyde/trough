---
declaration: proposition
origin: cited
lean: Mertens.E₁.le
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1316
---

# Upper bound on $E_1$

One has $E_1 \leq \frac{5 \log 2 + 3}{4}$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [$E_1$ summable](e1-summable.md)

## Proof

We can bound $E_1 \leq \sum_{n=2}^\infty \frac{\log n}{n(n-1)} \leq \frac{\log 2}{2} + \frac{3}{2} \sum_{n=3}^\infty \frac{\log n}{n^2}$. Calculus shows that $\log x / x^2$ is decreasing for $x \geq 2 > e^{1/2}$, so we can bound $\sum_{n=3}^\infty \frac{\log n}{n^2} \leq \int_2^\infty \frac{\log t}{t^2}\ dt = \frac{\log 2+1}{2}$.

## Lean

Formalized as [`Mertens.E₁.le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₁.le).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
