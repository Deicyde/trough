---
declaration: lemma
origin: cited
lean: Perron.residuePull2
statement: formalized
proof: formalized
---

# residuePull2

For $x>1$, we have

$$
\frac1{2\pi i}
\int_{(-1/2)}\frac{x^s}{s(s+1)}ds = -1/x +
\frac 1{2\pi i}
\int_{(-3/2)}\frac{x^s}{s(s+1)}ds.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [HolomorphicOn.vanishesOnRectangle](../../residue-calculus-on-rectangles/holomorphicon-vanishesonrectangle.md)
- [tendsto-zero-Lower](../part-01/tendsto-zero-lower.md)
- [isIntegrable](../part-01/isintegrable.md)
- [tendsto-zero-Upper](../part-01/perron-tendsto-zero-upper.md)
- [RectangleBorder](../../residue-calculus-on-rectangles/rectangleborder.md)
- [residueAtNegOne](residueatnegone.md)
- [RectangleIntegral-tendsTo-VerticalIntegral](../part-01/rectangleintegral-tendsto-verticalintegral.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [isHolomorphicOn](../part-01/isholomorphicon.md)

## Proof

Pull contour from $(-1/2)$ to $(-3/2)$.

## Lean

Formalized as [`Perron.residuePull2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.residuePull2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
