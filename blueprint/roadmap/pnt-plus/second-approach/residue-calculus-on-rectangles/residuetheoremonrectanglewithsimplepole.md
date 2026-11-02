---
declaration: lemma
origin: cited
lean: ResidueTheoremOnRectangleWithSimplePole
statement: formalized
proof: formalized
---

# ResidueTheoremOnRectangleWithSimplePole

Suppose that $f$ is a holomorphic function on a rectangle, except for a simple pole at $p$. By the latter, we mean that there is a function $g$ holomorphic on the rectangle such that, $f = g + A/(s-p)$ for some $A\in\mathbb{C}$. Then the integral of $f$ over the rectangle is $A$.

## Depends on

- [RectangleIntegral](rectangleintegral.md)

## Proof depends on

- [HolomorphicOn.vanishesOnRectangle](holomorphicon-vanishesonrectangle.md)
- [RectangleBorder](rectangleborder.md)

## Proof

Replace $f$ with $g + A/(s-p)$ in the integral. The integral of $g$ vanishes by Lemma [HolomorphicOn.vanishesOnRectangle](holomorphicon-vanishesonrectangle.md). To evaluate the integral of $1/(s-p)$, pull everything to a square about the origin using Lemma [RectanglePullToNhdOfPole](rectanglepulltonhdofpole.md), and rescale by $c$; what remains is handled by Lemma [ResidueTheoremAtOrigin](residuetheorematorigin.md).

## Lean

Formalized as [`ResidueTheoremOnRectangleWithSimplePole`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ResidueTheoremOnRectangleWithSimplePole).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean)
