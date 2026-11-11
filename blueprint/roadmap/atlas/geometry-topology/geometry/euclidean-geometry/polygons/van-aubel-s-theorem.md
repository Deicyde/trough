---
declaration: section
origin: cited
lean: MetaMathlibExt.vanAubel, MetaMathlibExt.vanAubel_right
statement: formalized
proof: formalized
---

# Van Aubel's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/van-aubel-s-theorem/index.html).

## Van Aubel's theorem

Let $A$, $B$, $C$, $D$ be any four points of the Euclidean plane
$\mathbb{R}^2$, and let $\rho(x, y) = (-y, x)$ be the counterclockwise rotation by $90^\circ$.
On each directed side $A \to B$, $B \to C$, $C \to D$, $D \to A$ erect the square lying to its
left; its centre is the side midpoint plus half the side vector rotated by $\rho$:
$O_{AB} = \tfrac12(A + B) + \tfrac12\rho(B - A)$,
$O_{BC} = \tfrac12(B + C) + \tfrac12\rho(C - B)$,
$O_{CD} = \tfrac12(C + D) + \tfrac12\rho(D - C)$ and
$O_{DA} = \tfrac12(D + A) + \tfrac12\rho(A - D)$.
Then $\lVert O_{AB} - O_{CD} \rVert = \lVert O_{BC} - O_{DA} \rVert$ and
$\langle O_{AB} - O_{CD}, O_{BC} - O_{DA} \rangle = 0$: the segments joining the centres of
opposite squares have equal length and are perpendicular.

No orientation hypothesis is needed. When the vertices are listed clockwise these are the
outward squares; when they are listed counterclockwise they are the inward squares, and the
outward version is Van Aubel's theorem with squares on the right.

## Sources

- https://en.wikipedia.org/wiki/Van_Aubel%27s_theorem.

Formalized by `MetaMathlibExt.vanAubel`, a theorem declared in [MathlibExt/Geometry/Euclidean/VanAubel.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/VanAubel.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/van-aubel-s-theorem/index.html#van-aubel).

## Van Aubel's theorem with squares on the right

Let $A$, $B$, $C$, $D$ be any four
points of the Euclidean plane $\mathbb{R}^2$, and let $\rho(x, y) = (y, -x)$ be the clockwise
rotation by $90^\circ$. On each directed side $A \to B$, $B \to C$, $C \to D$, $D \to A$
erect the square lying to its right; its centre is the side midpoint plus half the side vector
rotated by $\rho$:
$O_{AB} = \tfrac12(A + B) + \tfrac12\rho(B - A)$,
$O_{BC} = \tfrac12(B + C) + \tfrac12\rho(C - B)$,
$O_{CD} = \tfrac12(C + D) + \tfrac12\rho(D - C)$ and
$O_{DA} = \tfrac12(D + A) + \tfrac12\rho(A - D)$.
Then $\lVert O_{AB} - O_{CD} \rVert = \lVert O_{BC} - O_{DA} \rVert$ and
$\langle O_{AB} - O_{CD}, O_{BC} - O_{DA} \rangle = 0$: the segments joining the centres of
opposite squares have equal length and are perpendicular.

When $A$, $B$, $C$, $D$ are listed counterclockwise these are the outward squares; together
with Van Aubel's theorem for squares on the left this covers the outward construction for both
orientations.

Formalized by `MetaMathlibExt.vanAubel_right`, a theorem declared in [MathlibExt/Geometry/Euclidean/VanAubel.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/VanAubel.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/van-aubel-s-theorem/index.html#van-aubel-right).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van Aubel's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/van-aubel-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/polygons/van-aubel-s-theorem)
