---
declaration: section
origin: cited
lean: WeierstrassCurve.VariableChange.mapAffineCoordinates, WeierstrassCurve.VariableChange.affineCoordinatesEquiv, WeierstrassCurve.VariableChange.equation_mapAffineCoordinates_iff, WeierstrassCurve.VariableChange.affineEquationEquiv, WeierstrassCurve.VariableChange.pointEquiv, WeierstrassCurve.VariableChange.natCard_point_eq, WeierstrassCurve.Affine.CoordinateRing.XYIdeal_ne_bot
statement: formalized
proof: formalized
---

# Weierstrass curves

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html).

## Coordinate map of a Weierstrass variable change

For a variable change $C = (u, r, s, t)$
over a field $F$, with $u \in F^\times$ and $r, s, t \in F$, the affine coordinate map of $C$
sends $(x, y) \in F^2$ to $(u^2 x + r,\ u^3 y + u^2 s x + t)$.

Formalized by `WeierstrassCurve.VariableChange.mapAffineCoordinates`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#map-affine-coordinates).

## Variable changes act bijectively on affine coordinates

For a variable change
$C = (u, r, s, t)$ over a field $F$, the map $(x, y) \mapsto (u^2 x + r,\ u^3 y + u^2 s x + t)$
is a bijection $F^2 \to F^2$, whose inverse is the corresponding map of the inverse variable
change $C^{-1}$.

Formalized by `WeierstrassCurve.VariableChange.affineCoordinatesEquiv`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#affine-coordinates-equiv).

## Variable changes transform the Weierstrass equation

Let $W$ be a Weierstrass curve over
a field $F$, let $C = (u, r, s, t)$ be a variable change and let $C \cdot W$ be the transformed
curve. A pair $(x, y) \in F^2$ satisfies the Weierstrass equation of $C \cdot W$ if and only if
$(u^2 x + r,\ u^3 y + u^2 s x + t)$ satisfies the Weierstrass equation of $W$.

Formalized by `WeierstrassCurve.VariableChange.equation_mapAffineCoordinates_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#equation-map-affine-coordinates-iff).

## Variable changes biject affine solutions

Let $W$ be a Weierstrass curve over a field $F$,
let $C = (u, r, s, t)$ be a variable change and let $C \cdot W$ be the transformed curve. The map
$(x, y) \mapsto (u^2 x + r,\ u^3 y + u^2 s x + t)$ is a bijection from the solutions
$(x, y) \in F^2$ of the Weierstrass equation of $C \cdot W$ onto the solutions in $F^2$ of the
Weierstrass equation of $W$; its inverse is the corresponding map of $C^{-1}$.

Formalized by `WeierstrassCurve.VariableChange.affineEquationEquiv`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#affine-equation-equiv).

## Variable changes biject rational points

Let $W$ be an elliptic Weierstrass curve over a
field $F$, let $C = (u, r, s, t)$ be a variable change and let $C \cdot W$ be the transformed
curve. There is a bijection from the rational points of $C \cdot W$ to the rational points of
$W$, where in both cases the point at infinity is included; it sends the point at infinity to
the point at infinity and an affine point $(x, y)$ to $(u^2 x + r,\ u^3 y + u^2 s x + t)$.

Formalized by `WeierstrassCurve.VariableChange.pointEquiv`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#point-equiv).

## Variable changes preserve the point count

Let $W$ be an elliptic Weierstrass curve over
a finite field $F$, let $C$ be a variable change and let $C \cdot W$ be the transformed curve.
Then $C \cdot W$ and $W$ have the same number of rational points.

Formalized by `WeierstrassCurve.VariableChange.natCard_point_eq`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/VariableChangePoint.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#nat-card-point-eq).

## The ideal of a point on a Weierstrass curve is nonzero

The ideal generated by `X - x` and `Y - y` is nonzero.

Formalized by `WeierstrassCurve.Affine.CoordinateRing.XYIdeal_ne_bot`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/XYIdeal.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/EllipticCurve/XYIdeal.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html#xyideal-ne-bot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weierstrass curves](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/weierstrass-curves)
