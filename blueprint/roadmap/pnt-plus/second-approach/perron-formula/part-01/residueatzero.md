---
declaration: lemma
origin: cited
lean: Perron.residueAtZero
statement: formalized
proof: formalized
---

# residueAtZero

Let $x>0$. Then for all sufficiently small $c>0$, we have that

$$
\frac1{2\pi i}
\int_{-c-i*c}^{c+ i*c}\frac{x^s}{s(s+1)}ds = 1.
$$

## Depends on

- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)

## Proof depends on

- [diffBddAtZero](diffbddatzero.md)
- [ResidueTheoremOnRectangleWithSimplePole](../../residue-calculus-on-rectangles/residuetheoremonrectanglewithsimplepole.md)
- [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md)
- [isHolomorphicOn](isholomorphicon.md)

## Proof

For $c>0$ sufficiently small,

$x^s/(s(s+1))$ is equal to $1/s$ plus a function, $g$, say, holomorphic in the whole rectangle (by Lemma [diffBddAtZero](diffbddatzero.md)).

Now apply Lemma [ResidueTheoremOnRectangleWithSimplePole](../../residue-calculus-on-rectangles/residuetheoremonrectanglewithsimplepole.md).

## Lean

Formalized as [`Perron.residueAtZero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.residueAtZero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/PerronFormula.lean)
