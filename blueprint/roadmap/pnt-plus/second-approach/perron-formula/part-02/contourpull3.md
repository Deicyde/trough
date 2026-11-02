---
declaration: lemma
origin: cited
lean: Perron.contourPull3
statement: formalized
proof: formalized
---

# contourPull3

For $x>1$ and $\sigma<-3/2$, we have

$$
\frac1{2\pi i}
\int_{(-3/2)}\frac{x^s}{s(s+1)}ds = \frac 1{2\pi i}
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [zeroTendstoDiff](../part-01/zerotendstodiff.md)
- [tendsto-zero-Lower](../part-01/tendsto-zero-lower.md)
- [isIntegrable](../part-01/isintegrable.md)
- [tendsto-zero-Upper](../part-01/perron-tendsto-zero-upper.md)
- [RectangleIntegral-tendsTo-VerticalIntegral](../part-01/rectangleintegral-tendsto-verticalintegral.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [isHolomorphicOn](../part-01/isholomorphicon.md)

## Proof

Pull contour from $(-3/2)$ to $(\sigma)$.

## Lean

Formalized as [`Perron.contourPull3`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.contourPull3).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
