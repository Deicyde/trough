---
declaration: section
origin: cited
lean: MetaMathlibExt.volume_coordinateCrossPolytope, MetaMathlibExt.volume_coordinateCube, MeasureTheory.toReal_volume_convexHull_triangle, MeasureTheory.volume_unitSquare
statement: formalized
proof: formalized
---

# Volumes of polytopes

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html).

## Volume of the cross-polytope

For every integer $n \ge 1$, the cross-polytope
$\{x \in \mathbb{R}^n : |x_1| + \dots + |x_n| \le 1\}$ in the Euclidean space $\mathbb{R}^n$ has
volume $2^n / n!$.

## Sources

- optimizationproblems `constants/25a.md`, line 44 (the polar-volume identity).

Formalized by `MetaMathlibExt.volume_coordinateCrossPolytope`, a theorem declared in [MathlibExt/MeasureTheory/Measure/CoordinateCrossPolytope.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/CoordinateCrossPolytope.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html#volume-coordinate-cross-polytope).

## Volume of the coordinate cube

For every $n \in \mathbb{N}$, the coordinate cube
$[-1, 1]^n$ in the Euclidean space $\mathbb{R}^n$ has volume $2^n$.

## Sources

- optimizationproblems `constants/25a.md`, line 44 (the cube-volume identity).

Formalized by `MetaMathlibExt.volume_coordinateCube`, a theorem declared in [MathlibExt/MeasureTheory/Measure/CoordinateCube.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/CoordinateCube.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html#volume-coordinate-cube).

## Determinant formula for the area of a triangle

Write $x = (x_1, x_2)$ for the
coordinates of a point $x$ of the Euclidean plane $\mathbb{R}^2$. For all points $a, b, c$ in
$\mathbb{R}^2$, the Lebesgue measure (area) of the convex hull of $\{a, b, c\}$, as a real
number, equals $\frac{1}{2}\,\lvert (b_1 - a_1)(c_2 - a_2) - (b_2 - a_2)(c_1 - a_1) \rvert$.

Formalized by `MeasureTheory.toReal_volume_convexHull_triangle`, a theorem declared in [MathlibExt/MeasureTheory/Measure/Lebesgue/TriangleArea.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/Lebesgue/TriangleArea.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html#to-real-volume-convex-hull-triangle).

## Area of the unit square

The closed unit square
$\{x \in \mathbb{R}^2 : 0 \le x_1 \le 1 \text{ and } 0 \le x_2 \le 1\}$ in the Euclidean plane has
Lebesgue measure (area) $1$.

Formalized by `MeasureTheory.volume_unitSquare`, a theorem declared in [MathlibExt/MeasureTheory/Measure/Lebesgue/TriangleArea.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Measure/Lebesgue/TriangleArea.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html#volume-unit-square).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Volumes of polytopes](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/lebesgue-measure/volumes-of-polytopes)
