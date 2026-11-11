---
declaration: section
origin: cited
lean: MetaMathlibExt.conway_circle_theorem, MetaMathlibExt.euler_oi, MetaMathlibExt.Feuerbach_theorem, MetaMathlibExt.intercept_theorem, MetaMathlibExt.marden, MetaMathlibExt.routh
statement: formalized
proof: formalized
---

# Triangle geometry: its own results

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html).

Theorems about triangles, their centers, cevians, inscribed and circumscribed circles, and triangle inequalities.

## Conway circle theorem

Let $A$, $B$, $C$ be affinely independent points of the Euclidean
plane, and write $a = d(B, C)$, $b = d(A, C)$, $c = d(A, B)$ for the side lengths, where $d$ is
the Euclidean distance. Extend each side beyond each of its endpoints by the length of the side
opposite that endpoint; this gives the six points

$$A + \tfrac{a}{c}(A - B),\quad B + \tfrac{b}{c}(B - A),\quad B + \tfrac{b}{a}(B - C),$$



$$C + \tfrac{c}{a}(C - B),\quad C + \tfrac{c}{b}(C - A),\quad A + \tfrac{a}{b}(A - C).$$

Then there are a point $O$ and a real number $r$ such that all six points are at distance $r$
from $O$.

## Sources

- https://en.wikipedia.org/wiki/Conway_circle_theorem

Formalized by `MetaMathlibExt.conway_circle_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/ConwayCircle.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/ConwayCircle.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#conway-circle-theorem).

## Euler's theorem on the circumcenter–incenter distance

Let $P_0, P_1, P_2$ be affinely
independent points of the Euclidean plane, $d$ the Euclidean distance and $\langle x, y \rangle$
the inner product. Let $O$ be a point and $R \ge 0$ with $d(O, P_i) = R$ for each $i$, so that
$O$ is the circumcenter and $R$ the circumradius. Let $I = w_0 P_0 + w_1 P_1 + w_2 P_2$ with
$w_0, w_1, w_2 > 0$ and $w_0 + w_1 + w_2 = 1$, and let $r \ge 0$. Suppose there are points $F_0$
on the line $P_0 P_1$, $F_1$ on the line $P_1 P_2$ and $F_2$ on the line $P_2 P_0$ with
$d(I, F_k) = r$ for each $k$ and
$\langle F_0 - I, P_1 - P_0 \rangle = \langle F_1 - I, P_2 - P_1 \rangle =
\langle F_2 - I, P_0 - P_2 \rangle = 0$, so that $I$ is an interior point at distance $r$ from
all three side lines, that is, the incenter, and $r$ is the inradius. Then
$d(O, I)^2 = R(R - 2r)$ and $R \ge 2r$.

## Sources

- https://en.wikipedia.org/wiki/Euler%27s_theorem_in_geometry

Formalized by `MetaMathlibExt.euler_oi`, a theorem declared in [MathlibExt/Geometry/Euclidean/EulerOI.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/EulerOI.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#euler-oi).

## Feuerbach's theorem

Let $T$ be a triangle in a two-dimensional Euclidean affine space,
with incircle $\omega$, nine-point circle $N$, and excircle $\omega_i$ opposite its $i$-th vertex
for each $i$. If $T$ is not equilateral, then there is a point $F$ at which $\omega$ is internally
tangent to $N$ (that is, $F$ lies on both circles and the center of $\omega$ lies on the segment
from the center of $N$ to $F$), and $F$ is the only common point of $\omega$ and $N$. For every
triangle $T$ and every $i$, the nine-point circle $N$ is externally tangent to $\omega_i$.

## Sources

- K. W. Feuerbach, 1822; https://en.wikipedia.org/wiki/Feuerbach_point

Formalized by `MetaMathlibExt.Feuerbach_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/FeuerbachTheorem.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/FeuerbachTheorem.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#feuerbach-theorem).

## Intercept theorem

Let $A, B, C, D, E$ be points of the Euclidean plane $\mathbb{R}^2$,
and write $XY$ for the distance between points $X$ and $Y$. Suppose that $C - A$ is not a real
multiple of $B - A$; that $AD + DB = AB$ with $AD > 0$ and $DB > 0$, so $D$ lies strictly
between $A$ and $B$; that $AE + EC = AC$ with $AE > 0$ and $EC > 0$, so $E$ lies strictly
between $A$ and $C$; and that $E - D = r(C - B)$ for some real $r \ne 0$, so $DE$ is parallel
to $BC$. Then $AD / DB = AE / EC$.

## Sources

- https://en.wikipedia.org/wiki/Intercept_theorem.

Formalized by `MetaMathlibExt.intercept_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/InterceptTheorem.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/InterceptTheorem.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#intercept-theorem).

## Marden's theorem

Let $a, b, c$ be complex numbers such that $(b - a)/(c - a)$ has
nonzero imaginary part, so that they are the vertices of a nondegenerate triangle, and let
$p(z) = (z - a)(z - b)(z - c)$. Then there are complex numbers $f_1, f_2$ and a real number $L$
such that the roots of $p'$, counted with multiplicity, are exactly $f_1$ and $f_2$, and such
that the function $\sigma(z) = |z - f_1| + |z - f_2|$ satisfies
$\sigma((a + b)/2) = \sigma((b + c)/2) = \sigma((c + a)/2) = L$ and, for every real $t \ne 0$,
$\sigma((a + b)/2 + t(b - a)) > L$, $\sigma((b + c)/2 + t(c - b)) > L$ and
$\sigma((c + a)/2 + t(a - c)) > L$.

Thus the ellipse $\sigma(z) = L$ with foci $f_1$ and $f_2$ (a circle when $f_1 = f_2$) passes
through the midpoints of the three sides and touches each side line only at its midpoint: it is
the Steiner inellipse, and its foci are the roots of $p'$.

Proof: The statement is Marden's theorem (M. Marden, *Geometry of Polynomials*, 2nd ed.,
Math. Surveys No. 3, AMS, 1966; D. Kalman, *An Elementary Proof of Marden's Theorem*,
Amer. Math. Monthly 115(4) (2008), 330-338, <https://doi.org/10.1080/00029890.2008.11920532>).
Following [Wikipedia, *Marden's theorem*](https://en.wikipedia.org/wiki/Marden%27s_theorem),
we use Vieta's relations, the midpoint identity for the derivative, and the ellipse reflection
property expressed by a strict triangle inequality.

## Sources

- https://en.wikipedia.org/wiki/Marden%27s_theorem.

Formalized by `MetaMathlibExt.marden`, a theorem declared in [MathlibExt/Geometry/Euclidean/Marden.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Marden.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#marden).

## Routh's theorem

Let $A, B, C$ be points of the Euclidean plane $\mathbb{R}^2$ whose
triangle (the convex hull of $\{A, B, C\}$) has nonzero area, and let $x, y, z$ be positive
reals with $xyz \ne 1$. Let $D = \frac{x}{x+1} B + \frac{1}{x+1} C$,
$E = \frac{1}{y+1} A + \frac{y}{y+1} C$ and $F = \frac{z}{z+1} A + \frac{1}{z+1} B$, the
points of the sides $BC$, $CA$, $AB$ with $DC/DB = x$, $EA/EC = y$ and $FB/FA = z$. If $P$
lies on the segments $BE$ and $CF$, $Q$ lies on the segments $CF$ and $AD$, and $R$ lies on
the segments $AD$ and $BE$, then the area of the triangle $PQR$ (the convex hull of
$\{P, Q, R\}$) is

$$\frac{(xyz - 1)^2}{(xy + y + 1)(yz + z + 1)(zx + x + 1)}$$

times the area of $ABC$. Areas are Lebesgue measures.

## Sources

- https://en.wikipedia.org/wiki/Routh%27s_theorem

Formalized by `MetaMathlibExt.routh`, a theorem declared in [MathlibExt/Geometry/Euclidean/Routh.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Routh.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html#routh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Triangle geometry](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry)
