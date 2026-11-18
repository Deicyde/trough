# Triple product

The triple product of `u`, `v`, and `w` is equal to the determinant of the matrix
with those vectors as its rows.

```lean
triple_product_eq_det.{u_1} {R : Type u_1} [CommRing R] (u v w : Fin 3 → R) :
  u ⬝ᵥ (crossProduct v) w = Matrix.det ![u, v, w]
```

## Depends on

- [Cross product](cross-product.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)

## Sources

- [Mathlib documentation: `triple_product_eq_det`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CrossProduct.html#triple_product_eq_det)
- [Source of `triple_product_eq_det` in Mathlib/LinearAlgebra/CrossProduct.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/LinearAlgebra/CrossProduct.lean#L101)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Low dimensions](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L237)
