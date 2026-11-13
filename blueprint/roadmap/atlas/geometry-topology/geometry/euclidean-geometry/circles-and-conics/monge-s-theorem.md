---
declaration: section
origin: cited
lean: MetaMathlibExt.monge_three_circles_general, MetaMathlibExt.monge_three_circles
statement: formalized
proof: formalized
---

# Monge's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/monge-s-theorem/index.html).

## Monge's three-circle theorem, algebraic form

Let $V$ be a real vector space, let
$c_1, c_2, c_3 \in V$, and let $r_1, r_2, r_3$ be pairwise distinct real numbers. Then the three
points $(r_1 - r_2)^{-1}(r_1 c_2 - r_2 c_1)$, $(r_2 - r_3)^{-1}(r_2 c_3 - r_3 c_2)$ and
$(r_1 - r_3)^{-1}(r_1 c_3 - r_3 c_1)$ of $V$ are collinear.

For positive $r_i$, read as the radii of circles centered at the $c_i$, these points are the
external homothety centers of the pairs of circles. If $r_i$ and $r_j$ have opposite signs, the
point $(r_i - r_j)^{-1}(r_i c_j - r_j c_i)$ is instead the internal homothety center of the
circles of radii $|r_i|$ and $|r_j|$ centered at $c_i$ and $c_j$; for example $r_1 = -1$ and
$r_2 = 2$ give $\frac{1}{3}(c_2 + 2 c_1)$.

Formalized by `MetaMathlibExt.monge_three_circles_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/MongeCircles.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/MongeCircles.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/monge-s-theorem/index.html#monge-three-circles-general).

## Monge's three-circle theorem

Let $c_1, c_2, c_3$ be points of the Euclidean plane
$\mathbb{R}^2$ and let $r_1, r_2, r_3$ be pairwise distinct positive real numbers such that the
closed disks of radius $r_i$ centered at $c_i$ are pairwise disjoint. Then the external homothety
centers $(r_1 - r_2)^{-1}(r_1 c_2 - r_2 c_1)$, $(r_2 - r_3)^{-1}(r_2 c_3 - r_3 c_2)$ and
$(r_1 - r_3)^{-1}(r_1 c_3 - r_3 c_1)$ of the three pairs of circles are collinear.

## Sources

- https://en.wikipedia.org/wiki/Monge%27s_theorem. The source's hypothesis is that no circle lies inside another; the pairwise disjointness of the closed disks (`hd12`, `hd23`, `hd13`) is stronger. Omitted source case: the source also treats two circles of equal radius, whose external tangents are parallel and meet at a point at infinity. The distinct-radii hypotheses `h12`, `h23`, `h13` exclude it, and the affine formula for the centers cannot express it. It follows from `monge_three_circles_general`; the positivity hypotheses `hr₁`, `hr₂`, `hr₃` and the disjointness hypotheses are unused and keep the `Wanted` statement's shape.

Formalized by `MetaMathlibExt.monge_three_circles`, a theorem declared in [MathlibExt/Geometry/Euclidean/MongeCircles.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/MongeCircles.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/monge-s-theorem/index.html#monge-three-circles).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monge's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/monge-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics/monge-s-theorem)
