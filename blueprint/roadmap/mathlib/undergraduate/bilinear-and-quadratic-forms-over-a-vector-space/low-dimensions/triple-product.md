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
- [Source of `triple_product_eq_det` in Mathlib/LinearAlgebra/CrossProduct.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/LinearAlgebra/CrossProduct.lean#L101)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Low dimensions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L237)
