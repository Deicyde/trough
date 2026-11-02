---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: VectorField.leibniz_identity_mlieBracket
mathlib_file: Mathlib/Geometry/Manifold/VectorField/LieBracket.lean
---

# Jacobi/Leibniz identity

The Lie bracket of vector fields in manifolds satisfies the Leibniz identity
`[U, [V, W]] = [[U, V], W] + [V, [U, W]]` (also called Jacobi identity).

```lean
VectorField.leibniz_identity_mlieBracket.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {H : Type u_2} [TopologicalSpace H] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {I : ModelWithCorners 𝕜 E H} {M : Type u_4}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (minSmoothness 𝕜 3) M] [CompleteSpace E]
  {U V W : (x : M) → TangentSpace I x}
  (hU : ContMDiff I I.tangent (minSmoothness 𝕜 2) fun x => ⟨x, U x⟩)
  (hV : ContMDiff I I.tangent (minSmoothness 𝕜 2) fun x => ⟨x, V x⟩)
  (hW : ContMDiff I I.tangent (minSmoothness 𝕜 2) fun x => ⟨x, W x⟩) :
  VectorField.mlieBracket I U (VectorField.mlieBracket I V W) =
    VectorField.mlieBracket I (VectorField.mlieBracket I U V) W +
      VectorField.mlieBracket I V (VectorField.mlieBracket I U W)
```

## Depends on

- [Lie bracket of vector field](lie-bracket-of-vector-field.md)
- [Product of vector spaces](../../../../undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Smooth map between manifolds](smooth-map-between-manifolds.md)
- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)
- [Tangent bundle](tangent-bundle.md)
- [Topological fiber bundle](../../../topology/general-topology/part-01/topological-fiber-bundle.md)

## Proof depends on

- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Cluster point](../../../topology/general-topology/part-01/cluster-point.md)
- [Generating sets](../../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)

## Sources

- [Mathlib documentation: `VectorField.leibniz_identity_mlieBracket`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/VectorField/LieBracket.html#VectorField.leibniz_identity_mlieBracket)
- [Source of `VectorField.leibniz_identity_mlieBracket` in Mathlib/Geometry/Manifold/VectorField/LieBracket.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/VectorField/LieBracket.lean#L1151)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L452)
