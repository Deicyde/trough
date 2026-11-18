---
declaration: lemma
origin: cited
lean: Perron.formulaLtOne
statement: formalized
proof: formalized
---

# formulaLtOne

For $x>0$, $\sigma>0$, and $x<1$, we have

$$
\frac1{2\pi i}
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds =0.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [vertIntBound](vertintbound.md)
- [limitOfConstant](limitofconstant.md)
- [zeroTendstoDiff](zerotendstodiff.md)
- [tendsto-zero-Lower](tendsto-zero-lower.md)
- [isIntegrable](isintegrable.md)
- [tendsto-zero-Upper](perron-tendsto-zero-upper.md)
- [RectangleIntegral-tendsTo-VerticalIntegral](rectangleintegral-tendsto-verticalintegral.md)
- [tendsto-rpow-atTop-nhds-zero-of-norm-lt-one](tendsto-rpow-attop-nhds-zero-of-norm-lt-one.md)
- [integralPosAux](integralposaux.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [isHolomorphicOn](isholomorphicon.md)

## Proof

Let $f(s) = x^s/(s(s+1))$. Then $f$ is holomorphic on the half-plane $\{s\in\mathbb{C}:\Re(s)>0\}$. The rectangle integral of $f$ with corners $\sigma-iT$ and $\sigma+iT$ is zero. The limit of this rectangle integral as $T\to\infty$ is $\int_{(\sigma')}-\int_{(\sigma)}$. Therefore, $\int_{(\sigma')}=\int_{(\sigma)}$.

But we also have the bound $\int_{(\sigma')} \leq x^{\sigma'} * C$, where $C=\int_\mathbb{R}\frac{1}{|(1+t)(1+t+1)|}dt$.

Therefore $\int_{(\sigma')}\to 0$ as $\sigma'\to\infty$.

So pulling contours gives $\int_{(\sigma)}=0$.

## Lean

Formalized as [`Perron.formulaLtOne`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.formulaLtOne).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/PerronFormula.lean)
