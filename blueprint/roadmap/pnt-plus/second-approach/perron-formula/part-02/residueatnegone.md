---
declaration: lemma
origin: cited
lean: Perron.residueAtNegOne
statement: formalized
proof: formalized
---

# residueAtNegOne

Let $x>0$. Then for all sufficiently small $c>0$, we have that

$$
\frac1{2\pi i}
\int_{-c-i*c-1}^{c+ i*c-1}\frac{x^s}{s(s+1)}ds = -\frac1x.
$$

## Depends on

- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)

## Proof depends on

- [ResidueTheoremOnRectangleWithSimplePole](../../residue-calculus-on-rectangles/residuetheoremonrectanglewithsimplepole.md)
- [diffBddAtNegOne](../part-01/diffbddatnegone.md)
- [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md)
- [isHolomorphicOn](../part-01/isholomorphicon.md)

## Proof

Compute the integral.

## Lean

Formalized as [`Perron.residueAtNegOne`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.residueAtNegOne).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/PerronFormula.lean)
