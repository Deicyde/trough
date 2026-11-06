# Cross product

The cross product of two vectors in $R^3$ for $R$ a commutative ring.

```lean
crossProduct.{u_1} {R : Type u_1} [CommRing R] : (Fin 3 → R) →ₗ[R] (Fin 3 → R) →ₗ[R] Fin 3 → R
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Integer](../../../overview/general-algebra/numbers/integer.md)
- [Linear map](../../../overview/linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `crossProduct`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CrossProduct.html#crossProduct)
- [Source of `crossProduct` in Mathlib/LinearAlgebra/CrossProduct.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/CrossProduct.lean#L46)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Low dimensions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L236)
