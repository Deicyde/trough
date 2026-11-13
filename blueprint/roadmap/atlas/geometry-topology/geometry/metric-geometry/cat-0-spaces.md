---
declaration: section
origin: cited
lean: IsCAT0FourPoint, isCAT0FourPoint_iff, IsCAT0FourPoint.of_isometry, IsCAT0FourPoint.iff_of_isometryEquiv, IsCAT0FourPoint.of_subsingleton
statement: formalized
proof: formalized
---

# CAT(0) spaces

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html).

## CAT(0) four-point condition

A metric space $X$ satisfies the CAT(0) four-point
comparison condition if for all points $x, y, z, w \in X$ (not necessarily distinct),

$$d(x, z)^2 + d(y, w)^2 \le d(x, y)^2 + d(y, z)^2 + d(z, w)^2 + d(w, x)^2,$$

that is, the sum of the squares of the diagonals of every quadrilateral $xyzw$ is at most the
sum of the squares of its sides.

For geodesic metric spaces this is equivalent to the usual Euclidean comparison-triangle
definition of a CAT(0) space.

Formalized by `IsCAT0FourPoint`, a definition declared in [MathlibExt/Geometry/CAT0.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/CAT0.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html#is-cat0-four-point).

## Unfolding the CAT(0) four-point condition

A metric space $X$ satisfies the CAT(0)
four-point condition if and only if for all points $x, y, z, w \in X$,

$$d(x, z)^2 + d(y, w)^2 \le d(x, y)^2 + d(y, z)^2 + d(z, w)^2 + d(w, x)^2.$$

Formalized by `isCAT0FourPoint_iff`, a theorem declared in [MathlibExt/Geometry/CAT0.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/CAT0.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html#is-cat0-four-point-iff).

## The CAT(0) four-point condition passes to isometrically embedded spaces

Let $X$ and $Y$
be metric spaces and let $f : X \to Y$ be an isometry, that is, $d(f(a), f(b)) = d(a, b)$ for
all $a, b \in X$. If $Y$ satisfies the CAT(0) four-point condition, then so does $X$.

Formalized by `IsCAT0FourPoint.of_isometry`, a theorem declared in [MathlibExt/Geometry/CAT0.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/CAT0.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html#of-isometry).

## Isometry invariance of the CAT(0) four-point condition

If $X$ and $Y$ are metric spaces
and there is an isometric bijection from $X$ onto $Y$, then $X$ satisfies the CAT(0) four-point
condition if and only if $Y$ does.

Formalized by `IsCAT0FourPoint.iff_of_isometryEquiv`, a theorem declared in [MathlibExt/Geometry/CAT0.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/CAT0.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html#iff-of-isometry-equiv).

## Spaces with at most one point satisfy the CAT(0) four-point condition

Every metric
space with at most one point (including the empty space) satisfies the CAT(0) four-point
condition.

Formalized by `IsCAT0FourPoint.of_subsingleton`, a theorem declared in [MathlibExt/Geometry/CAT0.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/CAT0.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html#of-subsingleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: CAT(0) spaces](https://deicyde.github.io/atlas-lean/roadmap/Geometry/metric-geometry/cat-0-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/metric-geometry/cat-0-spaces)
