---
declaration: theorem
origin: cited
lean: SmoothedChebyshevPull1
statement: formalized
proof: formalized
---

# SmoothedChebyshevPull1

We have that

$$
\psi_{\epsilon}(X) =
\mathcal{M}(\widetilde{1_{\epsilon}})(1)
X^{1} +
I_1 - I_2 +I_{37} + I_8 + I_9
.
$$

## Depends on

- [I₁](../part-01/i1.md)
- [SmoothedChebyshev](../part-01/smoothedchebyshev.md)
- [I₃₇](../part-01/i37.md)
- [I₉](../part-01/i9.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [I₂](../part-01/i2.md)
- [I₈](../part-01/i8.md)

## Proof depends on

- [Smooth1Nonneg](../../mellin-transforms/part-01/smooth1nonneg.md)
- [ResidueMult](../../zeta-bounds/part-01/residuemult.md)
- [SmoothedChebyshevPull1-aux-integrable](../part-01/smoothedchebyshevpull1-aux-integrable.md)
- [ResidueTheoremOnRectangleWithSimplePole](../../residue-calculus-on-rectangles/residuetheoremonrectanglewithsimplepole.md)
- [BddAbove-to-IsBigO](../../zeta-bounds/part-01/bddabove-to-isbigo.md)
- [riemannZetaLogDerivResidue](../../zeta-bounds/part-01/riemannzetalogderivresidue.md)
- [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md)
- [existsDifferentiableOn-of-bddAbove](../../residue-calculus-on-rectangles/existsdifferentiableon-of-bddabove.md)
- [Smooth1ContinuousAt](../../mellin-transforms/part-01/smooth1continuousat.md)
- [Smooth1LeOne](../../mellin-transforms/part-01/smooth1leone.md)
- [RectangleIntegral](../../residue-calculus-on-rectangles/rectangleintegral.md)
- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof

Pull rectangle contours and evaluate the pole at $s=1$.

## Lean

Formalized as [`SmoothedChebyshevPull1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevPull1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
