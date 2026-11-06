# Discrete spaces are 0-manifolds

A discrete space `M` is a smooth manifold over the trivial model on a trivial normed space.

```lean
IsManifold.of_discreteTopology.{u_1, u_2, u_4} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] (n : WithTop ℕ∞) {M : Type u_4}
  [TopologicalSpace M] [DiscreteTopology M] [Unique E] : IsManifold (modelWithCornersSelf 𝕜 E) n M
```

## Depends on

- [Smooth or analytic manifold (with boundary and corners)](../part-01/smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [$C^k$ function](../../../analysis/differentiability/c-k-function.md)

## Sources

- [Mathlib documentation: `IsManifold.of_discreteTopology`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/Basic.html#IsManifold.of_discreteTopology)
- [Source of `IsManifold.of_discreteTopology` in Mathlib/Geometry/Manifold/IsManifold/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/Basic.lean#L912)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L463)
