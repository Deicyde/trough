# Product of manifolds

The product of two `C^n` manifolds is naturally a `C^n` manifold.

```lean
IsManifold.prod.{u_5, u_6, u_7, u_8, u_9, u_10, u_11} {n : WithTop ℕ∞} {𝕜 : Type u_5}
  [NontriviallyNormedField 𝕜] {E : Type u_6} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {E' : Type u_7} [NormedAddCommGroup E'] [NormedSpace 𝕜 E'] {H : Type u_8} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} {H' : Type u_9} [TopologicalSpace H'] {I' : ModelWithCorners 𝕜 E' H'}
  (M : Type u_10) [TopologicalSpace M] [ChartedSpace H M] [IsManifold I n M] (M' : Type u_11)
  [TopologicalSpace M'] [ChartedSpace H' M'] [IsManifold I' n M'] :
  IsManifold (I.prod I') n (M × M')
```

## Depends on

- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)

## Sources

- [Mathlib documentation: `IsManifold.prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/Basic.html#IsManifold.prod)
- [Source of `IsManifold.prod` in Mathlib/Geometry/Manifold/IsManifold/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/Basic.lean#L920)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L444)
