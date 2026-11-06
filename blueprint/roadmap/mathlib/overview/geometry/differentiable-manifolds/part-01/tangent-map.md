# Tangent map

`tangentMap I I' f` is the derivative of `f : M → M'` as a map between the tangent bundles
`TM` and `TM'`.

```lean
tangentMap.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type u_5} [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] {H' : Type u_6} [TopologicalSpace H']
  (I' : ModelWithCorners 𝕜 E' H') {M' : Type u_7} [TopologicalSpace M'] [ChartedSpace H' M']
  (f : M → M') : TangentBundle I M → TangentBundle I' M'
```

## Depends on

- [Continuous linear map](../../../topology/topological-algebra/continuous-linear-map.md)
- [Tangent bundle](tangent-bundle.md)

## Sources

- [Mathlib documentation: `tangentMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/MFDeriv/Defs.html#tangentMap)
- [Source of `tangentMap` in Mathlib/Geometry/Manifold/MFDeriv/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/MFDeriv/Defs.lean#L350)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L449)
