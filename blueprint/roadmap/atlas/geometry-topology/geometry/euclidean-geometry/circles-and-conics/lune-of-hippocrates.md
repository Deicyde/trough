---
declaration: section
origin: cited
lean: MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.Plane, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.det2, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.midpoint, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.vec, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.euclideanDistSq, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.closedHalfDisk, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.A, MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.B
statement: formalized
---

# Lune of Hippocrates

14 results, 13 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html).

## Coordinate plane for Hippocrates' lunes

The coordinate plane is the set
$\mathbb{R} \times \mathbb{R}$ of ordered pairs $(x, y)$ of real numbers.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.Plane`, an abbreviation declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#plane).

## Planar determinant for Hippocrates' lunes

For vectors $u = (u_1, u_2)$ and
$v = (v_1, v_2)$ of the coordinate plane, $\det(u, v) = u_1 v_2 - u_2 v_1$, the signed area of
the parallelogram spanned by $u$ and $v$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.det2`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#det2).

## Midpoint of two points in the plane

For points $p = (p_1, p_2)$ and
$q = (q_1, q_2)$ of the coordinate plane, their midpoint is
$\left(\frac{p_1 + q_1}{2}, \frac{p_2 + q_2}{2}\right)$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.midpoint`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#midpoint).

## Displacement vector between two points of the plane

For points $p = (p_1, p_2)$ and
$q = (q_1, q_2)$ of $\mathbb{R}^2$, the displacement vector from $p$ to $q$ is
$(q_1 - p_1, q_2 - p_2)$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.vec`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#vec).

## Squared Euclidean distance in the plane

For points $p = (p_1, p_2)$ and
$q = (q_1, q_2)$ of the coordinate plane, the squared Euclidean distance between them is
$(p_1 - q_1)^2 + (p_2 - q_2)^2$.

This uses the Euclidean distance, not the sup metric of the product
$\mathbb{R} \times \mathbb{R}$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.euclideanDistSq`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#euclidean-dist-sq).

## Closed half-disk on a diameter

Given points $p$ and $q$ of the coordinate plane and a
property $S$ of real numbers, this is the set of points $x$ such that the squared Euclidean
distance from $x$ to the midpoint of $p$ and $q$ is at most one quarter of the squared Euclidean
distance from $p$ to $q$ (so $x$ lies in the closed disk with diameter $pq$), and $S$ holds of
the planar determinant $\det(q - p, x - p)$. For $p \ne q$, taking $S(t)$ to be $t \ge 0$
(respectively $t \le 0$) selects the closed half of that disk to the left (respectively right)
of the directed line from $p$ to $q$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.closedHalfDisk`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#closed-half-disk).

## Right-angle vertex of the lune triangle

The point $A = (0, 0)$, the origin of the
coordinate plane; it is the right-angle vertex of the triangle in Hippocrates' theorem on
lunes.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.A`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#a).

## Horizontal leg endpoint of the lune triangle

For a real number $a$, the point
$B = (a, 0)$ on the $x$-axis of the coordinate plane; it is the endpoint of the horizontal leg of
the right triangle in Hippocrates' theorem on lunes.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.B`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#b).

## Vertical leg endpoint of the lune triangle

For a real number $b$, the point
$C = (0, b)$ on the $y$-axis of the coordinate plane; it is the endpoint of the vertical leg of
the right triangle in Hippocrates' theorem on lunes.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.C`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#c).

## Half-disk on the hypotenuse

For real numbers $a$ and $b$, let $B = (a, 0)$ and
$C = (0, b)$. The half-disk on the hypotenuse is the set of points $x = (x_1, x_2)$ of the
closed disk with diameter $BC$ satisfying $\det(C - B, x - B) \ge 0$, that is,
$b x_1 + a x_2 \le ab$. For $a, b > 0$ this is the half of the disk on the side of the line
$BC$ containing the right-angle vertex $(0, 0)$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.hypotenuseSemidisk`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#hypotenuse-semidisk).

## Lune on the horizontal leg

For real numbers $a$ and $b$, let $A = (0, 0)$,
$B = (a, 0)$ and $C = (0, b)$. The lune on the horizontal leg is the set of points
$x = (x_1, x_2)$ of the closed disk with diameter $AB$ satisfying $a x_2 \le 0$ that do not
lie in the half-disk on the hypotenuse, the set of points of the closed disk with diameter $BC$
satisfying $b x_1 + a x_2 \le ab$. For $a, b > 0$ this is the set of points of the closed lower
half-disk on the leg $AB$ that lie outside the closed disk with diameter $BC$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.horizontalLune`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#horizontal-lune).

## Hippocrates lune on the vertical leg

For real numbers $a$ and $b$, the vertical lune is
the set of points $(x, y) \in \mathbb{R}^2$ with $x^2 + (y - b/2)^2 \le b^2/4$ and $bx \le 0$
that do not satisfy both $(x - a/2)^2 + (y - b/2)^2 \le (a^2 + b^2)/4$ and $bx + ay \le ab$.

For $a, b > 0$ this is the closed half-disk on the segment from $(0, 0)$ to $(0, b)$, on the side
away from $(a, 0)$, minus the closed half-disk on the hypotenuse from $(a, 0)$ to $(0, b)$, on
the side of the origin.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.verticalLune`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#vertical-lune).

## Right triangle with legs on the axes

For real numbers $a$ and $b$, the right triangle
$T(a, b)$ is the convex hull in the plane $\mathbb{R}^2$ of the three points $(0, 0)$, $(a, 0)$
and $(0, b)$.

Formalized by `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.rightTriangle`, a definition declared in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#right-triangle).

## Hippocrates' theorem on lunes

Let $a, b > 0$ and consider the right triangle with
vertices $A = (0, 0)$, $B = (a, 0)$ and $C = (0, b)$. The Lebesgue measure of the lune on the
horizontal leg plus the Lebesgue measure of the lune on the vertical leg equals the Lebesgue
measure of the triangle, that is, of the convex hull of $A$, $B$ and $C$.

## Sources

- Hippocrates of Chios (c. 440 BC). Knill, §166. Problem `hippocrates_lunes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.HippocratesLunesWanted.Geometry.HippocratesLunes.hippocrates_lunes` is written with `theorem_wanted` in [WantedExt/Geometry/HippocratesLunesWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/HippocratesLunesWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html#hippocrates-lunes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lune of Hippocrates](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics/lune-of-hippocrates)
