# Minimal tensor product

The minimal tensor product of two cones is given by all conical combinations of elementary
tensor products `x ⊗ₜ y` with `x ∈ C₁` and `y ∈ C₂`.

```lean
PointedCone.minTensorProduct.{u_1, u_2, u_3} {R : Type u_1} [CommRing R] [LinearOrder R]
  [IsStrictOrderedRing R] {G : Type u_2} [AddCommGroup G] [_root_.Module R G] {H : Type u_3}
  [AddCommGroup H] [_root_.Module R H] (C₁ : PointedCone R G) (C₂ : PointedCone R H) :
  PointedCone R (TensorProduct R G H)
```

## Depends on

- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Pointed cone](pointed-cone.md)
- [Tensor product](../../linear-algebra/fundamentals/tensor-product.md)

## Sources

- [Mathlib documentation: `PointedCone.minTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/TensorProduct.html#PointedCone.minTensorProduct)
- [Source of `PointedCone.minTensorProduct` in Mathlib/Geometry/Convex/Cone/TensorProduct.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/TensorProduct.lean#L56)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L493)
