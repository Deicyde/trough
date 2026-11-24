---
declaration: lemma
origin: cited
lean: Perron.tendsto_zero_Upper
statement: formalized
proof: formalized
---

# tendsto-zero-Upper

Let $x>0$ and $\sigma',\sigma''\in\mathbb{R}$. Then

$$
\int_{\sigma'}^{\sigma''}\frac{x^{\sigma+it}}{(\sigma+it)(1+\sigma + it)}d\sigma
$$

goes to $0$ as $t\to\infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The numerator is bounded and the denominator tends to infinity.

## Lean

Formalized as [`Perron.tendsto_zero_Upper`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.tendsto_zero_Upper).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/PerronFormula.lean)
