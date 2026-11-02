---
declaration: lemma
origin: cited
lean: Perron.isIntegrable
statement: formalized
proof: formalized
---

# isIntegrable

Let $x>0$ and $\sigma\in\mathbb{R}$. Then

$$
\int_{\mathbb{R}}\frac{x^{\sigma+it}}{(\sigma+it)(1+\sigma + it)}dt
$$

is integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [isHolomorphicOn](isholomorphicon.md)

## Proof

By [isHolomorphicOn](isholomorphicon.md), $f$ is continuous, so it is integrable on any interval.

Also, $|f(x)| = \Theta(x^{-2})$ as $x\to\infty$,

and $|f(-x)| = \Theta(x^{-2})$ as $x\to\infty$.

Since $g(x) = x^{-2}$ is integrable on $[a,\infty)$ for any $a>0$, we conclude.

## Lean

Formalized as [`Perron.isIntegrable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.isIntegrable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
