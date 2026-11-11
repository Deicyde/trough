---
declaration: section
origin: cited
lean: MetaMathlibExt.brahmagupta_area, MetaMathlibExt.euler_quadrilateral, MetaMathlibExt.japanese_theorem_concyclic_quadrilaterals, MetaMathlibExt.varignon
statement: formalized
proof: formalized
---

# Polygons and quadrilaterals: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html).

Theorems about quadrilaterals, cyclic polygons and squares erected on polygon sides.

## Brahmagupta's formula

Let $P, Q, R, S$ be points of the Euclidean plane with side
lengths $|PQ| = a$, $|QR| = b$, $|RS| = c$, $|SP| = d$ and diagonal $|PR| = e$, and let
$s = (a + b + c + d)/2$. Suppose that some point $O$ is equidistant from $P, Q, R, S$ (so the
quadrilateral $PQRS$ is cyclic) and that some point $T$ satisfies $|PT| + |TR| = |PR|$ and
$|QT| + |TS| = |QS|$ with $|PT|, |TR|, |QT|, |TS| > 0$ (so $T$ lies strictly inside both
diagonals and $PQRS$ is convex). Let $p = (a + b + e)/2$ and $q = (c + d + e)/2$, and let $A$ be
the sum of the Heron areas of the triangles $PQR$ and $RSP$:

$$A = \sqrt{p(p - a)(p - b)(p - e)} + \sqrt{q(q - c)(q - d)(q - e)}.$$

Then $A = \sqrt{(s - a)(s - b)(s - c)(s - d)}$.

## Sources

- https://en.wikipedia.org/wiki/Brahmagupta%27s_formula

Formalized by `MetaMathlibExt.brahmagupta_area`, a theorem declared in [MathlibExt/Geometry/Euclidean/BrahmaguptaArea.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/BrahmaguptaArea.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html#brahmagupta-area).

## Euler's quadrilateral theorem

For any four points $A, B, C, D$ of the Euclidean plane,
write $XY$ for the distance between points $X$ and $Y$, and let $M$ and $N$ be the midpoints of
$AC$ and $BD$. Then

$$AB^2 + BC^2 + CD^2 + DA^2 = AC^2 + BD^2 + 4 MN^2.$$

## Sources

- https://en.wikipedia.org/wiki/Euler%27s_quadrilateral_theorem

Formalized by `MetaMathlibExt.euler_quadrilateral`, a theorem declared in [MathlibExt/Geometry/Euclidean/EulerQuadrilateral.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/EulerQuadrilateral.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html#euler-quadrilateral).

## Japanese theorem for concyclic quadrilaterals

Let $A, B, C, D$ be pairwise distinct
points of the Euclidean plane $\mathbb{R}^2$ lying on a circle of positive radius, such that the
diagonals $AC$ and $BD$, as closed segments, intersect; so $ABCD$ is a convex cyclic
quadrilateral. Let $r_1, r_2, r_3, r_4 > 0$, and suppose that for each of the triangles $ABC$,
$CDA$, $BCD$ and $DAB$ there is a closed disc of radius $r_1$, $r_2$, $r_3$ and $r_4$
respectively that is contained in the closed triangle and whose boundary circle meets each of
the three closed sides of the triangle; so $r_1, r_2$ are the inradii of the triangles $ABC$,
$CDA$ of one triangulation and $r_3, r_4$ those of the triangles $BCD$, $DAB$ of the other.
Then $r_1 + r_2 = r_3 + r_4$.

## Sources

- https://en.wikipedia.org/wiki/Japanese_theorem_for_concyclic_quadrilaterals.

Formalized by `MetaMathlibExt.japanese_theorem_concyclic_quadrilaterals`, a theorem declared in [MathlibExt/Geometry/Euclidean/JapaneseQuads.lean, line 944](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/JapaneseQuads.lean#L944). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html#japanese-theorem-concyclic-quadrilateral).

## Varignon's theorem

Let $A$, $B$, $C$, $D$ be any four points of the Euclidean plane
$\mathbb{R}^2$, degenerate and self-crossing configurations included, and let $P$, $Q$, $R$,
$S$ be the midpoints of $AB$, $BC$, $CD$, $DA$, that is $2P = A + B$, $2Q = B + C$,
$2R = C + D$ and $2S = D + A$. Write $[XYZ]$ for the oriented area of the triangle $XYZ$,
positive when $X$, $Y$, $Z$ are listed counterclockwise. Then $P + R = Q + S$, so the diagonals
of $PQRS$ bisect each other and $PQRS$ is a possibly degenerate parallelogram, and

$$2([PQR] + [PRS]) = [ABC] + [ACD],$$

that is, the signed area of $PQRS$ is half the signed area of $ABCD$.

## Sources

- https://en.wikipedia.org/wiki/Varignon%27s_theorem. `A B C D` are arbitrary points in the Euclidean plane, including degenerate or self-crossing configurations. `P Q R S` are the midpoints of sides AB, BC, CD, DA (`2 • P = A + B`, etc.). Conclusion: `P + R = Q + S` (the diagonals of PQRS bisect each other, i.e. PQRS is a parallelogram via parallel opposite sides / bisecting diagonals), and twice the signed area of PQRS, expressed through `EuclideanGeometry.orientedTriangleArea`, equals the signed area of ABCD.

Formalized by `MetaMathlibExt.varignon`, a theorem declared in [MathlibExt/Geometry/Euclidean/Varignon.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Varignon.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html#varignon).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polygons and quadrilaterals](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/polygons/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/polygons)
