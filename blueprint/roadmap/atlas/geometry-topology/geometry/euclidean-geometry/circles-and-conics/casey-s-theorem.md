---
declaration: section
origin: cited
lean: MetaMathlibExt.casey_theorem, MetaMathlibExt.casey_theorem_cyclic_order_core, MetaMathlibExt.casey_theorem_cyclic_order
statement: formalized
proof: formalized
---

# Casey's theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem/index.html).

## Casey's theorem

In the Euclidean plane, let a circle have center $O$ and radius $R > 0$,
and let four circles have centers $c_1, c_2, c_3, c_4$ and radii $r_1, r_2, r_3, r_4$ with
$0 < r_i < R$ and $|c_i O| + r_i = R$ for each $i$, so that each is internally tangent to the
outer circle. Assume that the four circles lie outside each other, $r_i + r_j < |c_i c_j|$ for
all $i \ne j$, and that they appear counterclockwise around $O$ with every consecutive angular
gap less than $\pi$: writing $u \times v = u_1 v_2 - u_2 v_1$ for vectors $u = (u_1, u_2)$ and
$v = (v_1, v_2)$ of the plane, $(c_i - O) \times (c_j - O) > 0$ for
$(i, j) = (1, 2), (2, 3), (3, 4), (4, 1)$. For the pairs $ij = 12, 23, 34, 41, 13, 24$ let
$t_{ij} > 0$ satisfy $t_{ij}^2 = |c_i c_j|^2 - (r_i - r_j)^2$, the length of an exterior common
tangent of the circles $i$ and $j$. Then $t_{12} t_{34} + t_{23} t_{41} = t_{13} t_{24}$.

Configurations with a consecutive angular gap of at least $\pi$ are not covered here; they are
covered by the cyclic-order form of Casey's theorem.

## Sources

- https://en.wikipedia.org/wiki/Casey%27s_theorem.

Formalized by `MetaMathlibExt.casey_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/CaseyTheorem.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/CaseyTheorem.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem/index.html#casey-theorem).

## Core identity behind Casey's theorem in cyclic order

In the Euclidean plane, write
$d(p, q)$ for the distance between points $p$ and $q$. Let $O, c_1, c_2, c_3, c_4$ be points and
$R, r_1, r_2, r_3, r_4$ real numbers with $r_i < R$ and $d(c_i, O) + r_i = R$ for each $i$.
Suppose $c_i - O = d(c_i, O)(\cos\theta_i, \sin\theta_i)$ for real numbers
$\theta_1 < \theta_2 < \theta_3 < \theta_4 < \theta_1 + 2\pi$. For each pair $(i, j)$ among
$(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)$ let $t_{ij} > 0$ satisfy
$t_{ij}^2 = d(c_i, c_j)^2 - (r_i - r_j)^2$. Then $t_{12} t_{34} + t_{23} t_{41} = t_{13} t_{24}$.

Compared with Casey's theorem for four circles in arbitrary cyclic order, neither $R$ nor the
$r_i$ need be positive and the circles need not be pairwise disjoint.

Formalized by `MetaMathlibExt.casey_theorem_cyclic_order_core`, a theorem declared in [MathlibExt/Geometry/Euclidean/CaseyTheoremCyclicOrder.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/CaseyTheoremCyclicOrder.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem/index.html#casey-theorem-cyclic-order-core).

## Casey's theorem for four circles in arbitrary cyclic order

In the Euclidean plane, write
$d(p, q)$ for the distance between points $p$ and $q$. Let $O$ be a point and $R > 0$, and let
$c_1, c_2, c_3, c_4$ be points and $r_1, r_2, r_3, r_4$ real numbers with $0 < r_i < R$ and
$d(c_i, O) + r_i = R$ for each $i$, so that the circle with center $c_i$ and radius $r_i$ is
internally tangent to the circle with center $O$ and radius $R$. Suppose any two of the four
inner circles are disjoint, that is $r_i + r_j < d(c_i, c_j)$ for $i \ne j$, and that
$c_i - O = d(c_i, O)(\cos\theta_i, \sin\theta_i)$ for real numbers
$\theta_1 < \theta_2 < \theta_3 < \theta_4 < \theta_1 + 2\pi$. For each pair $(i, j)$ among
$(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)$ let $t_{ij} > 0$ satisfy
$t_{ij}^2 = d(c_i, c_j)^2 - (r_i - r_j)^2$, so that $t_{ij}$ is the length of an outer common
tangent. Then $t_{12} t_{34} + t_{23} t_{41} = t_{13} t_{24}$.

Unlike the version of Casey's theorem that requires each consecutive pair of centers to make a
positive oriented angle at $O$, a gap between consecutive directions may be at least $\pi$.

## Sources

- https://en.wikipedia.org/wiki/Casey%27s_theorem

Formalized by `MetaMathlibExt.casey_theorem_cyclic_order`, a theorem declared in [MathlibExt/Geometry/Euclidean/CaseyTheoremCyclicOrder.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/CaseyTheoremCyclicOrder.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem/index.html#casey-theorem-cyclic-order).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Casey's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics/casey-s-theorem)
