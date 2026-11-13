---
declaration: section
origin: cited
lean: MetaMathlibExt.descartes_circle_theorem, MetaMathlibExt.IsLensCurvatureRecurrence, MetaMathlibExt.miquel_theorem, MetaMathlibExt.pizza_theorem
statement: formalized
proof: formalized
---

# Circles and conics: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html).

Configurations of circles and conics, tangency, chains of circles, lunes, and mathematical billiards in elliptic and polygonal tables.

## Descartes' circle theorem

Let four circles in the Euclidean plane have centers $c_i$ and
radii $r_i > 0$ for $i = 1, 2, 3, 4$, let $d$ be the Euclidean distance, and let
$k_1, k_2, k_3, k_4$ be real numbers. Suppose that either
(a) any two of the circles are externally tangent, $d(c_i, c_j) = r_i + r_j$ for $i \ne j$, and
$k_i = 1/r_i$ for every $i$; or
(b) for some index $e$, each other circle is internally tangent to circle $e$, that is,
$d(c_e, c_j) = r_e - r_j$ for $j \ne e$; any two circles other than circle $e$ are externally
tangent, $d(c_i, c_j) = r_i + r_j$ for distinct $i, j \ne e$; and $k_e = -1/r_e$ and
$k_j = 1/r_j$ for $j \ne e$.
Then $(k_1 + k_2 + k_3 + k_4)^2 = 2(k_1^2 + k_2^2 + k_3^2 + k_4^2)$.

Proof: Following the Cayley-Menger/Gram-determinant argument in Lagarias, Mallows, and Wilks,
*Beyond the Descartes circle theorem*, Section 3, and Wikipedia's proof sketch, introduce signed
radii, expand the planar Gram determinant in coordinates, and clear denominators.

## Sources

- https://en.wikipedia.org/wiki/Descartes%27_theorem.

Formalized by `MetaMathlibExt.descartes_circle_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/DescartesCircleTheorem.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/DescartesCircleTheorem.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html#descartes-circle-theorem).

## Lens curvature recurrence

For real numbers $K$ and $A$, a real sequence
$(b_n)_{n \ge 0}$ satisfies the lens curvature recurrence with parameters $K$ and $A$ when
$1 + K \neq 0$ and, for every $n \ge 0$,

$$b_{n+2} = \frac{6 - 2K}{1 + K}\, b_{n+1} - b_n + \frac{-8A}{1 + K}.$$

This is the second-order nonhomogeneous recurrence of the source for the curvatures of a chain
of circles in a symmetric lens, where $A$ is the common curvature of the two lens circles.

Formalized by `MetaMathlibExt.IsLensCurvatureRecurrence`, a definition declared in [MathlibExt/Geometry/LensCurvatureRecurrence.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/LensCurvatureRecurrence.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html#is-lens-curvature-recurrence).

## Miquel's theorem

Let $A$, $B$, $C$ be non-collinear points of the Euclidean plane
$\mathbb{R}^2$, and let $D$, $E$, $F$ be points on the lines $BC$, $CA$, $AB$ respectively with
$D \ne B$, $D \ne C$, $E \ne C$, $E \ne A$, $F \ne A$ and $F \ne B$. If $A$, $E$, $F$ lie on the
circle with center $O_1$ and radius $r_1$, $B$, $F$, $D$ lie on the circle with center $O_2$ and
radius $r_2$, and $C$, $D$, $E$ lie on the circle with center $O_3$ and radius $r_3$, then these
three circles have a common point.

## Sources

- https://en.wikipedia.org/wiki/Miquel%27s_theorem.

Formalized by `MetaMathlibExt.miquel_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/MiquelTheorem.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/MiquelTheorem.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html#miquel-theorem).

## Pizza theorem

Let $n \ge 2$ be a natural number, let $D$ be the open disk of radius
$R > 0$ centered at a point $c$ of $\mathbb{R}^2$, let $p$ be a point of $D$, and let $\theta_0$
be a real number. Put $\alpha = \pi / (2n)$ and, for $k = 0, 1, \dots, 4n - 1$, let $S_k$ be the
set of points of $D$ of the form $p + r(\cos\theta, \sin\theta)$ with $r \ge 0$ and
$\theta_0 + k\alpha \le \theta < \theta_0 + (k + 1)\alpha$. Then the sum of the Lebesgue measures
of the $S_k$ with $k$ even equals the sum of the Lebesgue measures of the $S_k$ with $k$ odd.

The $4n$ sectors $S_k$ are the slices cut from the disk by $2n$ lines through $p$ at equal
angles, so alternately shading the slices gives equal shaded and unshaded areas.

## Sources

- *Pizza theorem*, Wikipedia, https://en.wikipedia.org/wiki/Pizza_theorem.

Formalized by `MetaMathlibExt.pizza_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/PizzaTheorem.lean, line 1323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PizzaTheorem.lean#L1323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html#pizza-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Circles and conics](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics)
