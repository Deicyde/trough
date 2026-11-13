---
declaration: section
origin: cited
lean: isometry_apply_eq_linear_apply_add_map_zero, isometry_isLinearMap_of_map_zero
statement: formalized
proof: formalized
---

# Isometries of Euclidean space

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/isometries-of-euclidean-space/index.html).

## Isometries of Euclidean space are affine

For every natural number $n$, every
isometry $f$ of the Euclidean space $\mathbb{R}^n$ is affine: there is a linear map
$A : \mathbb{R}^n \to \mathbb{R}^n$, the linear part of $f$, such that $f(x) = A x + f(0)$
for every $x \in \mathbb{R}^n$.

Formalized by `isometry_apply_eq_linear_apply_add_map_zero`, a theorem declared in [MathlibExt/Geometry/Euclidean/IsometryLinear.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/IsometryLinear.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/isometries-of-euclidean-space/index.html#isometry-apply-eq-linear-apply-add-map-z).

## Isometries of Euclidean space fixing the origin are linear

For every natural
number $n$, if $f$ is an isometry of the Euclidean space $\mathbb{R}^n$ with $f(0) = 0$, then
$f$ is $\mathbb{R}$-linear: $f(x + y) = f(x) + f(y)$ and $f(c x) = c f(x)$ for all
$x, y \in \mathbb{R}^n$ and $c \in \mathbb{R}$.

Formalized by `isometry_isLinearMap_of_map_zero`, a theorem declared in [MathlibExt/Geometry/Euclidean/IsometryLinear.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/IsometryLinear.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/isometries-of-euclidean-space/index.html#isometry-is-linear-map-of-map-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isometries of Euclidean space](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/isometries-of-euclidean-space/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/isometries-of-euclidean-space)
