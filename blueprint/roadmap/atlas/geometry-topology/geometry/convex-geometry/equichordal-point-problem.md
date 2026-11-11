---
declaration: section
origin: cited
lean: MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.Plane, MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.IsEquichordalPoint, MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.equichordal_point_unique
statement: formalized
---

# Equichordal point problem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/equichordal-point-problem/index.html).

## Euclidean plane for the equichordal point problem

The Euclidean plane is the space
$\mathbb{R}^2$ of pairs of real numbers with the Euclidean inner product and norm.

Formalized by `MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.Plane`, an abbreviation declared in [WantedExt/Geometry/EquichordalWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/EquichordalWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/equichordal-point-problem/index.html#plane).

## Equichordal point

Let $K$ be a subset of the Euclidean plane. A point $P$ is an
equichordal point of $K$ if $P$ lies in the interior of $K$ and there is a real $L > 0$ such
that for every unit vector $u$ there are reals $a > 0$ and $b > 0$ for which $P + a u$ and
$P - b u$ lie in the boundary (frontier) of $K$, the open segment between $P - b u$ and
$P + a u$ lies in the interior of $K$, and the distance between $P + a u$ and $P - b u$
equals $L$.

The open segment condition makes $P + a u$ and $P - b u$ the endpoints of the chord through $P$
in direction $u$, ruling out other boundary crossings for nonconvex star-shaped domains.

Formalized by `MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.IsEquichordalPoint`, a definition declared in [WantedExt/Geometry/EquichordalWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/EquichordalWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/equichordal-point-problem/index.html#is-equichordal-point).

## Equichordal point theorem

Let $K$ be a compact convex subset of the Euclidean plane
with nonempty interior. Then $K$ does not have two distinct equichordal points: there are no
points $P \ne Q$ of the plane such that both $P$ and $Q$ are equichordal points of $K$.

## Sources

- M. R. Rychlik, A complete solution to the equichordal point problem of Fujiwara, Blaschke, Rothe and Weizenböck, Invent. Math. 129 (1997). Listed as §205 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §205. Problem `equichordal_point_unique` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.EquichordalWanted.Geometry.Equichordal.equichordal_point_unique` is written with `theorem_wanted` in [WantedExt/Geometry/EquichordalWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/EquichordalWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/equichordal-point-problem/index.html#equichordal-point-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equichordal point problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/equichordal-point-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/equichordal-point-problem)
