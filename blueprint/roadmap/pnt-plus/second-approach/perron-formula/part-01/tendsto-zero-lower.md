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

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/PerronFormula.lean)
