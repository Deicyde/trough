---
declaration: lemma
origin: cited
lean: Perron.formulaGtOne
statement: formalized
proof: formalized
---

# formulaGtOne

For $x>1$ and $\sigma>0$, we have

$$
\frac1{2\pi i}
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds =1-1/x.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [vertIntBoundLeft](../part-01/vertintboundleft.md)
- [residuePull1](residuepull1.md)
- [tendsto-rpow-atTop-nhds-zero-of-norm-gt-one](../part-01/tendsto-rpow-attop-nhds-zero-of-norm-gt-one.md)
- [residuePull2](residuepull2.md)
- [limitOfConstantLeft](../part-01/limitofconstantleft.md)
- [contourPull3](contourpull3.md)

## Proof

Let $f(s) = x^s/(s(s+1))$. Then $f$ is holomorphic on $\mathbb{C} \setminus {0,-1}$.

First pull the contour from $(\sigma)$ to $(-1/2)$, picking up a residue $1$ at $s=0$.

Next pull the contour from $(-1/2)$ to $(-3/2)$, picking up a residue $-1/x$ at $s=-1$.

Then pull the contour all the way to $(\sigma')$ with $\sigma'<-3/2$.

For $\sigma' < -3/2$, the integral is bounded by $x^{\sigma'}\int_\mathbb{R}\frac{1}{|(1+t ^ 2)(2+t ^ 2)|^{1/2}}dt$.

Therefore $\int_{(\sigma')}\to 0$ as $\sigma'\to\infty$.

So pulling contours gives $\int_{(-3/2)}=0$.

## Lean

Formalized as [`Perron.formulaGtOne`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.formulaGtOne).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
