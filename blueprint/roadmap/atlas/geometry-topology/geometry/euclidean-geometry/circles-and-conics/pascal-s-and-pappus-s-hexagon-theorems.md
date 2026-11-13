---
declaration: section
origin: cited
lean: MetaMathlibExt.pascal_theorem, MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.SamePoint, MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.OnConic, MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.meet, MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.Collinear3, MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.pascal
statement: formalized
---

# Pascal's and Pappus's hexagon theorems

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html).

## Pascal's theorem in an affine plane

Let $k$ be a field of characteristic different from
$2$ and let $P$ be an affine plane over $k$, that is, an affine space whose space of translations
$V$ is a $k$-vector space of dimension $2$. Fix a point $O \in P$ and a nondegenerate symmetric
bilinear form $\beta$ on $V \times k$, and call the set of points $x \in P$ with
$\beta((x - O, 1), (x - O, 1)) = 0$ the conic. Let $v_0, v_1, \dots, v_5$ be six distinct points
of the conic such that, for each of the three pairs of opposite sides $(v_0 v_1, v_3 v_4)$,
$(v_1 v_2, v_4 v_5)$ and $(v_2 v_3, v_5 v_0)$ of the hexagon $v_0 v_1 v_2 v_3 v_4 v_5$, the four
endpoints are not collinear, so that the two lines are distinct. If $q_1$ lies on the lines
$v_0 v_1$ and $v_3 v_4$, $q_2$ lies on the lines $v_1 v_2$ and $v_4 v_5$, and $q_3$ lies on the
lines $v_2 v_3$ and $v_5 v_0$, then $q_1$, $q_2$, $q_3$ are collinear.

## Sources

- https://en.wikipedia.org/wiki/Pascal%27s_theorem.

Formalized by `MetaMathlibExt.pascal_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/PascalTheorem.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/PascalTheorem.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#pascal-theorem).

## Same projective point

Two vectors $v, w \in \mathbb{R}^3$ represent the same point of the
real projective plane when $w = c v$ for some real number $c \ne 0$.

Formalized by `MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.SamePoint`, a definition declared in [WantedExt/Geometry/PascalPappusWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/PascalPappusWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#same-point).

## Points on a conic

For a real $3 \times 3$ matrix $M$, a vector $v \in \mathbb{R}^3$ lies on
the conic $x^\top M x = 0$ when $v^\top M v = 0$.

Formalized by `MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.OnConic`, a definition declared in [WantedExt/Geometry/PascalPappusWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/PascalPappusWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#on-conic).

## Meet of two lines

Writing $\times$ for the cross product on $\mathbb{R}^3$, the meet of
the line through $a$ and $b$ with the line through $c$ and $d$, for $a, b, c, d \in \mathbb{R}^3$,
is the vector $(a \times b) \times (c \times d)$.

When $a \times b$ and $c \times d$ are nonzero and not proportional, this vector represents the
intersection point of the two projective lines.

Formalized by `MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.meet`, a definition declared in [WantedExt/Geometry/PascalPappusWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/PascalPappusWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#meet).

## Collinear projective points

Writing $\cdot$ and $\times$ for the dot and cross products
on $\mathbb{R}^3$, three vectors $p, q, r \in \mathbb{R}^3$ represent collinear points of the
real projective plane when their triple product vanishes: $p \cdot (q \times r) = 0$.

Formalized by `MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.Collinear3`, a definition declared in [WantedExt/Geometry/PascalPappusWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/PascalPappusWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#collinear3).

## Pascal's theorem for real projective conics

Let $M$ be a real symmetric $3 \times 3$
matrix with $\det M \ne 0$, and let $a_1, a_2, a_3, b_1, b_2, b_3 \in \mathbb{R}^3$ be nonzero
vectors on the conic $x^\top M x = 0$, no two of which represent the same projective point.
Writing $\cdot$ and $\times$ for the dot and cross products on $\mathbb{R}^3$, let
$p = (a_1 \times b_2) \times (a_2 \times b_1)$, $q = (a_1 \times b_3) \times (a_3 \times b_1)$ and
$r = (a_2 \times b_3) \times (a_3 \times b_2)$ be the meets of the opposite sides of the hexagon
$a_1 b_2 a_3 b_1 a_2 b_3$. Then $p$, $q$ and $r$ are collinear: $p \cdot (q \times r) = 0$.

## Sources

- B. Pascal, *Essay pour les coniques* (1640). Knill, *Some fundamental theorems in mathematics*, §146. Problem `pascal` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.PascalPappusWanted.Geometry.PascalPappus.pascal` is written with `theorem_wanted` in [WantedExt/Geometry/PascalPappusWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/PascalPappusWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html#pascal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pascal's and Pappus's hexagon theorems](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics/pascal-s-and-pappus-s-hexagon-theorems)
