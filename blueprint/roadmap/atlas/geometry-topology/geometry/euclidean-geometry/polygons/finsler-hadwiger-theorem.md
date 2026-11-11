---
declaration: section
origin: cited
lean: MetaMathlibExt.finsler_hadwiger, MetaMathlibExt.finsler_hadwiger_of_ne
statement: formalized
proof: formalized
---

# Finsler–Hadwiger theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/finsler-hadwiger-theorem/index.html).

## Finsler–Hadwiger theorem

Let $A, B, C, D, E, F, G$ be points of the Euclidean plane
$\mathbb{R}^2$ with $B \ne A$ and $E \ne A$, and let $\rho(x, y) = (-y, x)$ be the
counterclockwise rotation by $90^\circ$. Suppose that $ABCD$ and $AEFG$ are squares sharing the
vertex $A$, in the sense that $D - A = \rho(B - A)$, $C = B + D - A$, $G - A = \rho(E - A)$ and
$F = E + G - A$. Let $O_1 = (A + C)/2$ and $O_2 = (A + F)/2$ be their centers, and let
$P = (B + G)/2$ and $Q = (D + E)/2$. Then $\|P - Q\| = \|O_1 - O_2\|$, the vectors $P - Q$ and
$O_1 - O_2$ are orthogonal, and $O_1 + O_2 = P + Q$; that is, the segments $O_1O_2$ and $PQ$
have equal length, are perpendicular and share their midpoint.

The hypotheses $B \ne A$ and $E \ne A$ are not used. When $B = E$ both segments are zero; with
$B \ne E$ one also gets $O_1 \ne O_2$, so that $O_1 P O_2 Q$ is a square as in the source.

## Sources

- https://en.wikipedia.org/wiki/Finsler%E2%80%93Hadwiger_theorem.

Formalized by `MetaMathlibExt.finsler_hadwiger`, a theorem declared in [MathlibExt/Geometry/Euclidean/FinslerHadwiger.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/FinslerHadwiger.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/finsler-hadwiger-theorem/index.html#finsler-hadwiger).

## Finsler–Hadwiger theorem for distinct squares

Let $A, B, C, D, E, F, G$ be points of
the Euclidean plane $\mathbb{R}^2$ with $B \ne E$, and let $\rho(x, y) = (-y, x)$ be the
counterclockwise rotation by $90^\circ$. Suppose that $ABCD$ and $AEFG$ are squares sharing the
vertex $A$, in the sense that $D - A = \rho(B - A)$, $C = B + D - A$, $G - A = \rho(E - A)$ and
$F = E + G - A$. Let $O_1 = (A + C)/2$ and $O_2 = (A + F)/2$ be their centers, and let
$P = (B + G)/2$ and $Q = (D + E)/2$. Then $\|P - Q\| = \|O_1 - O_2\|$, the vectors $P - Q$ and
$O_1 - O_2$ are orthogonal, $O_1 + O_2 = P + Q$ and $O_1 \ne O_2$; so the segments $O_1O_2$ and
$PQ$ are nonzero, equal, perpendicular and share their midpoint, and $O_1 P O_2 Q$ is a square.

The points $B$ and $E$ may equal $A$: if, say, $E = A$, then $AEFG$ is the single point $A$
and $O_1 P O_2 Q$ is a quarter of $ABCD$.

Formalized by `MetaMathlibExt.finsler_hadwiger_of_ne`, a theorem declared in [MathlibExt/Geometry/Euclidean/FinslerHadwiger.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/FinslerHadwiger.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/finsler-hadwiger-theorem/index.html#finsler-hadwiger-of-ne).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finsler–Hadwiger theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/finsler-hadwiger-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/polygons/finsler-hadwiger-theorem)
