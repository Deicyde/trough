---
declaration: lemma
origin: cited
lean: RectanglePullToNhdOfPole
statement: formalized
proof: formalized
---

# RectanglePullToNhdOfPole

If $f$ is holomorphic on a rectangle $z$ and $w$ except at a point $p$, then the integral of $f$ over the rectangle with corners $z$ and $w$ is the same as the integral of $f$ over a small square centered at $p$.

## Depends on

- [RectangleIntegral](rectangleintegral.md)

## Proof depends on

- [HolomorphicOn.vanishesOnRectangle](holomorphicon-vanishesonrectangle.md)
- [RectangleBorder](rectangleborder.md)

## Proof

Chop the big rectangle with two vertical cuts and two horizontal cuts into smaller rectangles, the middle one being the desired square. The integral over each of the outer rectangles vanishes, since $f$ is holomorphic there. (The constant $c$ being “small enough” here just means that the inner square is strictly contained in the big rectangle.)

## Lean

Formalized as [`RectanglePullToNhdOfPole`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/RectanglePullToNhdOfPole).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ResidueCalcOnRectangles.lean)
