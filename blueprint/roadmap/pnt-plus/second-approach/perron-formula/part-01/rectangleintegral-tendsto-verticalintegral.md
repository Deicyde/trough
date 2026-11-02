---
declaration: lemma
origin: cited
lean: RectangleIntegral_tendsTo_VerticalIntegral
statement: formalized
proof: formalized
---

# RectangleIntegral-tendsTo-VerticalIntegral

Let $\sigma,\sigma' \in \mathbb{R}$, and $f : \mathbb{C} \to \mathbb{C}$ such that the vertical integrals $\int_{(\sigma)}f(s)ds$ and $\int_{(\sigma')}f(s)ds$ exist and the horizontal integral $\int_{(\sigma)}^{\sigma'}f(x + yi)dx$ vanishes as $y \to \pm \infty$. Then the limit of rectangle integrals

$$
\lim_{T\to\infty}\int_{\sigma-iT}^{\sigma'+iT}f(s)ds =
\int_{(\sigma')}f(s)ds - \int_{(\sigma)}f(s)ds.
$$

## Depends on

- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof

Almost by definition.

## Lean

Formalized as [`RectangleIntegral_tendsTo_VerticalIntegral`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/RectangleIntegral_tendsTo_VerticalIntegral).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
