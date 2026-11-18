# Angle

The undirected angle between two vectors. If either vector is 0,
this is π/2. See `Orientation.oangle` for the corresponding oriented angle
definition.

```lean
InnerProductGeometry.angle.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  (x y : V) : ℝ
```

## Depends on

- [Inner product space, over $R$ or $C$](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md)
- [Inverse trigonometric functions](../../analysis/special-functions/inverse-trigonometric-functions.md)

## Sources

- [Mathlib documentation: `InnerProductGeometry.angle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Euclidean/Angle/Unoriented/Basic.html#InnerProductGeometry.angle)
- [Source of `InnerProductGeometry.angle` in Mathlib/Geometry/Euclidean/Angle/Unoriented/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Geometry/Euclidean/Angle/Unoriented/Basic.lean#L37)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L437)
- [Mathlib undergraduate list: Affine and Euclidean Geometry › Euclidean affine spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L264)
