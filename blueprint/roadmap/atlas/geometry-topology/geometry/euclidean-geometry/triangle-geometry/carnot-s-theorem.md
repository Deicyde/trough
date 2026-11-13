---
declaration: section
origin: cited
lean: MetaMathlibExt.carnot_inradius_circumradius_general, MetaMathlibExt.carnot_inradius_circumradius
statement: formalized
proof: formalized
---

# Carnot's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/carnot-s-theorem/index.html).

## Carnot's theorem (inradius and circumradius), general form

Let $A, B, C$ be non-collinear
points of a Euclidean affine plane lying on the circle with center $O$ and radius $R > 0$. Take
unit vectors $n_a$, $n_b$, $n_c$ normal to the sides and pointing toward the opposite vertices:
$n_a \perp C - B$ with $\langle A - B, n_a \rangle > 0$, $n_b \perp A - C$ with
$\langle B - C, n_b \rangle > 0$, and $n_c \perp B - A$ with $\langle C - A, n_c \rangle > 0$.
Let $x = \langle O - B, n_a \rangle$, $y = \langle O - C, n_b \rangle$ and
$z = \langle O - A, n_c \rangle$ be the signed distances from $O$ to the lines $BC$, $CA$, $AB$.
If a point $I$ and a real number $r$ satisfy
$\langle I - B, n_a \rangle = \langle I - C, n_b \rangle = \langle I - A, n_c \rangle = r$
(so $I$ is the incenter and $r$ the inradius), then $x + y + z = R + r$.

This form does not assume $r > 0$ or that $O$ lies in the affine span of $A, B, C$.

## Sources

- https://en.wikipedia.org/wiki/Carnot%27s_theorem_(inradius,_circumradius). Statement ID: carnot-inradius-s1.

Formalized by `MetaMathlibExt.carnot_inradius_circumradius_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/CarnotInradius.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/CarnotInradius.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/carnot-s-theorem/index.html#carnot-inradius-circumradius-general).

## Carnot's theorem (inradius and circumradius)

Let $A, B, C$ be non-collinear points of a
Euclidean affine plane lying on the circle with center $O$ and radius $R > 0$, and suppose $O$
lies in the affine span of $A, B, C$. Take unit vectors $n_a$, $n_b$, $n_c$ normal to the sides
and pointing toward the opposite vertices: $n_a \perp C - B$ with $\langle A - B, n_a \rangle > 0$,
$n_b \perp A - C$ with $\langle B - C, n_b \rangle > 0$, and $n_c \perp B - A$ with
$\langle C - A, n_c \rangle > 0$. Let $x = \langle O - B, n_a \rangle$,
$y = \langle O - C, n_b \rangle$ and $z = \langle O - A, n_c \rangle$ be the signed distances
from $O$ to the lines $BC$, $CA$, $AB$. If a point $I$ and a real number $r > 0$ satisfy
$\langle I - B, n_a \rangle = \langle I - C, n_b \rangle = \langle I - A, n_c \rangle = r$
(so $I$ is the incenter and $r$ the inradius), then $x + y + z = R + r$.

The hypotheses $r > 0$ and that $O$ lies in the affine span of $A, B, C$ are not used; the
general form of the theorem drops them.

## Sources

- https://en.wikipedia.org/wiki/Carnot%27s_theorem_(inradius,_circumradius). Statement ID: carnot-inradius-s1.

Formalized by `MetaMathlibExt.carnot_inradius_circumradius`, a theorem declared in [MathlibExt/Geometry/Euclidean/CarnotInradius.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/CarnotInradius.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/carnot-s-theorem/index.html#carnot-inradius-circumradius).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Carnot's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/carnot-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/carnot-s-theorem)
