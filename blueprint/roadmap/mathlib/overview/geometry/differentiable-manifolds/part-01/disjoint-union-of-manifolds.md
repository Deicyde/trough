# Disjoint union of manifolds

The disjoint union of two `C^n` manifolds modelled on `(E, H)`
is a `C^n` manifold modelled on `(E, H)`.

```lean
IsManifold.disjointUnion.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {M' : Type u_5} [TopologicalSpace M'] [ChartedSpace H M']
  [hM : IsManifold I n M] [hM' : IsManifold I n M'] : IsManifold I n (M ⊕ M')
```

## Depends on

- [Smooth or analytic manifold (with boundary and corners)](smooth-or-analytic-manifold-with-boundary-and-co.md)

## Proof depends on

- [Induced topology](../../../topology/general-topology/part-01/induced-topology.md)

## Sources

- [Mathlib documentation: `IsManifold.disjointUnion`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Geometry/Manifold/IsManifold/Basic.html#IsManifold.disjointUnion)
- [Source of `IsManifold.disjointUnion` in Mathlib/Geometry/Manifold/IsManifold/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Geometry/Manifold/IsManifold/Basic.lean#L959)
- [Mathlib overview: Geometry › Differentiable manifolds](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L445)
