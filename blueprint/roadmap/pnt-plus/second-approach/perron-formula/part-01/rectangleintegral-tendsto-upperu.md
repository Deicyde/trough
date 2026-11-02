---
declaration: lemma
origin: cited
lean: RectangleIntegral_tendsTo_UpperU
statement: formalized
proof: formalized
---

# RectangleIntegral-tendsTo-UpperU

Let $\sigma,\sigma' \in \mathbb{R}$, and $f : \mathbb{C} \to \mathbb{C}$ such that the vertical integrals $\int_{(\sigma)}f(s)ds$ and $\int_{(\sigma')}f(s)ds$ exist and the horizontal integral $\int_{(\sigma)}^{\sigma'}f(x + yi)dx$ vanishes as $y \to \pm \infty$. Then the limit of rectangle integrals

$$
\int_{\sigma+iT}^{\sigma'+iU}f(s)ds
$$

as $U\to\infty$ is the “UpperUIntegral” of $f$.

## Depends on

- [UpperUIntegral](../../residue-calculus-on-rectangles/upperuintegral.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)

## Proof

Almost by definition.

## Lean

Formalized as [`RectangleIntegral_tendsTo_UpperU`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/RectangleIntegral_tendsTo_UpperU).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
