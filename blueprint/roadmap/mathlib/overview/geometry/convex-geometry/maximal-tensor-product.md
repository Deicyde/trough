---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: PointedCone.maxTensorProduct
mathlib_file: Mathlib/Geometry/Convex/Cone/TensorProduct.lean
---

# Maximal tensor product

The maximal tensor product of two cones is the dual (pointed cone) of the minimal tensor product
of the dual cones.

```lean
PointedCone.maxTensorProduct.{u_1, u_2, u_3} {R : Type u_1} [CommRing R] [LinearOrder R]
  [IsStrictOrderedRing R] {G : Type u_2} [AddCommGroup G] [_root_.Module R G] {H : Type u_3}
  [AddCommGroup H] [_root_.Module R H] (C₁ : PointedCone R G) (C₂ : PointedCone R H) :
  PointedCone R (TensorProduct R G H)
```

## Depends on

- [Dual cone](dual-cone.md)
- [Dual vector space](../../linear-algebra/duality/dual-vector-space.md)
- [Minimal tensor product](minimal-tensor-product.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `PointedCone.maxTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Convex/Cone/TensorProduct.html#PointedCone.maxTensorProduct)
- [Source of `PointedCone.maxTensorProduct` in Mathlib/Geometry/Convex/Cone/TensorProduct.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Convex/Cone/TensorProduct.lean#L62)
- [Mathlib overview: Geometry › Convex geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L494)
