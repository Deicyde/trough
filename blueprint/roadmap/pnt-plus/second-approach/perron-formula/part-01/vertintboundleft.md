---
declaration: lemma
origin: cited
lean: Perron.vertIntBoundLeft
statement: formalized
proof: formalized
---

# vertIntBoundLeft

Let $x>1$ and $\sigma<-3/2$. Then

$$
\left|
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds\right| \leq
x^\sigma \int_\mathbb{R}\frac{1}{|(1/4+t ^ 2)(2+t ^ 2)|^{1/2}}dt.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof

Triangle inequality and pointwise estimate.

## Lean

Formalized as [`Perron.vertIntBoundLeft`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.vertIntBoundLeft).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/PerronFormula.lean)
