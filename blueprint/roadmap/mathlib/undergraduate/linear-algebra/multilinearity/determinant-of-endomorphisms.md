# Determinant of endomorphisms

The determinant of an endomorphism independent of basis.

If there is no finite basis on `M`, the result is `1` instead.

```lean
LinearMap.det.{u_2, u_5} {M : Type u_2} [AddCommGroup M] {A : Type u_5} [CommRing A]
  [_root_.Module A M] : (M →ₗ[A] M) →* A
```

## Depends on

- [Algebra of endomorphisms of a vector space](../fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Determinant](../../../overview/linear-algebra/matrices/determinant.md)
- [Matrix representation of a linear map](../../../overview/linear-algebra/matrices/matrix-representation-of-a-linear-map.md)

## Sources

- [Mathlib documentation: `LinearMap.det`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Determinant.html#LinearMap.det)
- [Source of `LinearMap.det` in Mathlib/LinearAlgebra/Determinant.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/Determinant.lean#L160)
- [Mathlib undergraduate list: Linear algebra › Multilinearity](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L38)
