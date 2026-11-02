---
declaration: lemma
origin: cited
lean: Perron.tendsto_zero_Lower
statement: formalized
proof: formalized
---

# tendsto-zero-Lower

Let $x>0$ and $\sigma',\sigma''\in\mathbb{R}$. Then

$$
\int_{\sigma'}^{\sigma''}\frac{x^{\sigma+it}}{(\sigma+it)(1+\sigma + it)}d\sigma
$$

goes to $0$ as $t\to-\infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The numerator is bounded and the denominator tends to infinity.

## Lean

Formalized as [`Perron.tendsto_zero_Lower`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.tendsto_zero_Lower).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
