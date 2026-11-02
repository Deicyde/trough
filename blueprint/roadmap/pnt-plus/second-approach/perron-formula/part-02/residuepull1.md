---
declaration: lemma
origin: cited
lean: Perron.residuePull1
statement: formalized
proof: formalized
---

# residuePull1

For $x>1$ (of course $x>0$ would suffice) and $\sigma>0$, we have

$$
\frac1{2\pi i}
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds =1
+
\frac 1{2\pi i}
\int_{(-1/2)}\frac{x^s}{s(s+1)}ds.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [residueAtZero](../part-01/residueatzero.md)
- [HolomorphicOn.vanishesOnRectangle](../../residue-calculus-on-rectangles/holomorphicon-vanishesonrectangle.md)
- [tendsto-zero-Lower](../part-01/tendsto-zero-lower.md)
- [isIntegrable](../part-01/isintegrable.md)
- [tendsto-zero-Upper](../part-01/perron-tendsto-zero-upper.md)
- [RectangleBorder](../../residue-calculus-on-rectangles/rectangleborder.md)
- [RectangleIntegral-tendsTo-VerticalIntegral](../part-01/rectangleintegral-tendsto-verticalintegral.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [isHolomorphicOn](../part-01/isholomorphicon.md)

## Proof

We pull to a square with corners at $-c-i*c$ and $c+i*c$ for $c>0$ sufficiently small. By Lemma [residueAtZero](../part-01/residueatzero.md), the integral over this square is equal to $1$.

## Lean

Formalized as [`Perron.residuePull1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.residuePull1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
